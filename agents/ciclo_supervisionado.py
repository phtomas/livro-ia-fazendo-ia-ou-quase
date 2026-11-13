#!/usr/bin/env python3
"""Protótipo de ciclo supervisionado. SEM chamada a LLM, sem escrita no manuscrito.

Consome plano JSON externo (que pode ter sido escrito por pessoa ou modelo),
passa cada ação pela política e só executa verificações de leitura de uma
lista fechada. Produz relatório, mas nunca aplica patches nem publica.
"""
from __future__ import annotations
import argparse
import difflib
import hashlib
import json
from pathlib import Path, PurePosixPath
import subprocess
import sys
from typing import Any

from politica_orquestrador import decide

ALLOWED_READ_EXTS = {'.md', '.qmd', '.py', '.yml', '.yaml', '.bib', '.css', '.tex'}
ALLOWED_ACTIONS = {'READ_SOURCE', 'CHECK_STRUCTURE', 'PROPOSE_TEXT_DIFF', 'GENERATE_REPORT'}
MAX_STEPS = 24
MAX_TEXT = 150_000


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def safe_read(root: Path, rel: str) -> tuple[Path, str]:
    """Reject escapes, hidden paths, symlinks and non-source files."""
    if not isinstance(rel, str) or not rel or len(rel) > 255:
        raise ValueError('path inválido')
    posix = PurePosixPath(rel)
    if posix.is_absolute() or any(x in {'.', '..'} or x.startswith('.') for x in posix.parts):
        raise ValueError('path não autorizado')
    if posix.suffix.lower() not in ALLOWED_READ_EXTS:
        raise ValueError('extensão não permitida para leitura')
    file = root.joinpath(*posix.parts)
    if any(p.is_symlink() for p in (file, *file.parents) if p != root and root in p.parents):
        raise ValueError('link simbólico não autorizado')
    real = file.resolve()
    if not real.is_relative_to(root.resolve()) or not real.is_file():
        raise ValueError('arquivo não encontrado dentro do projeto')
    if real.stat().st_size > MAX_TEXT:
        raise ValueError('arquivo excede limite de leitura')
    return real, real.read_text(encoding='utf-8')


def execute_step(root: Path, step: dict[str, Any]) -> dict[str, Any]:
    action = step.get('action', '')
    policy = decide(action)
    entry: dict[str, Any] = {'action': action, 'policy': policy['decision'], 'executed': False, 'status': 'BLOCKED'}
    if policy['decision'] not in {'ALLOW_READ_ONLY','ALLOW_PROPOSAL_ONLY'}:
        entry['reason'] = 'política não permite execução; nenhuma aprovação local é aceita como prova de identidade'
        return entry
    if action not in ALLOWED_ACTIONS:
        entry['reason'] = 'não existe adaptador de ferramenta habilitado'
        return entry
    try:
        if action == 'CHECK_STRUCTURE':
            results=[]
            for name in ['verificar_boxes.py','verificar_estrutura.py']:
                cp=subprocess.run([sys.executable,str(root/'scripts'/name)],cwd=root,capture_output=True,text=True,timeout=25,check=False)
                results.append({'tool':name,'return_code':cp.returncode,'stdout_tail':cp.stdout[-350:]})
            entry.update(executed=True,status='PASS' if all(x['return_code']==0 for x in results) else 'FAIL',results=results)
        elif action == 'READ_SOURCE':
            file,txt=safe_read(root,step.get('path'))
            entry.update(executed=True,status='PASS',path=file.relative_to(root).as_posix(),sha256=sha256(txt.encode()),characters=len(txt))
        elif action == 'PROPOSE_TEXT_DIFF':
            file,txt=safe_read(root,step.get('path'))
            old=step.get('original_excerpt')
            new=step.get('replacement_excerpt')
            if not isinstance(old,str) or not old or not isinstance(new,str) or len(new)>2000 or txt.count(old)!=1:
                raise ValueError('proposta inválida: trecho original ausente, ambíguo ou alteração excessiva')
            proposed=txt.replace(old,new,1)
            diff=''.join(difflib.unified_diff(txt.splitlines(keepends=True),proposed.splitlines(keepends=True),fromfile='original',tofile='proposta'))
            entry.update(executed=True,status='PROPOSAL_ONLY',path=file.relative_to(root).as_posix(),source_sha256=sha256(txt.encode()),diff=diff[:7000],manuscript_changed=False)
        elif action == 'GENERATE_REPORT':
            entry.update(executed=True,status='PASS',note='O relatório final é escrito pelo controlador, fora do manuscrito.')
    except (OSError,ValueError,UnicodeError,subprocess.TimeoutExpired) as exc:
        entry.update(status='FAIL',reason=str(exc))
    return entry


def run_plan(root: Path, plan: dict[str,Any]) -> dict[str,Any]:
    if not isinstance(plan,dict) or not isinstance(plan.get('steps'),list) or not 0 < len(plan['steps']) <= MAX_STEPS:
        raise ValueError('plano deve ter entre 1 e 24 etapas')
    if any(not isinstance(s,dict) for s in plan['steps']):
        raise ValueError('etapas devem ser objetos')
    trace=[]
    for i,step in enumerate(plan['steps'],1):
        result=execute_step(root,step)
        result['step']=i
        trace.append(result)
        # Stop on any blocked or failed step: no implicit skip-ahead.
        if result['status'] in {'BLOCKED','FAIL'}:
            break
    statuses=[x['status'] for x in trace]
    status=('HALTED_POLICY' if statuses[-1]=='BLOCKED' else 'HALTED_FAILURE' if statuses[-1]=='FAIL' else 'PROPOSALS_PENDING_REVIEW' if 'PROPOSAL_ONLY' in statuses else 'PASS_LIMITED')
    return {'prototype':'ciclo_supervisionado','version':'0.1','goal':str(plan.get('goal',''))[:250],
            'source_of_proposal':str(plan.get('source','external_plan'))[:90],
            'model_requested':plan.get('model_requested'),
            'model_reported':None,'model_verified':False,'uses_llm':False,
            'status':status,'steps_requested':len(plan['steps']),'steps_observed':trace,
            'changed_manuscript':False,'published':False,'approval_authentication':'not_implemented',
            'warning':'Esta execução NÃO comprova decisão autônoma de um modelo nem aprovação de publicação.'}


def main()->int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=Path,required=True)
    parser.add_argument('--plan',type=Path,required=True)
    parser.add_argument('--report',type=Path,required=True)
    args=parser.parse_args()
    root=args.root.resolve()
    if not (root/'_quarto.yml').is_file():
        parser.error('raiz Quarto inválida')
    if not args.plan.is_file() or args.plan.stat().st_size>50000:
        parser.error('plano inexistente ou muito grande')
    plan=json.loads(args.plan.read_text(encoding='utf-8'))
    result=run_plan(root,plan)
    target=args.report.resolve()
    if target.is_relative_to(root):
        # report must live under a dedicated excluded output path only
        allowed=(root/'dist').resolve()
        if not target.is_relative_to(allowed):
            parser.error('relatório deve ficar fora do manuscrito ou sob dist/')
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(result['status'],str(target))
    return 0 if result['status'] in {'PASS_LIMITED','PROPOSALS_PENDING_REVIEW'} else 2

if __name__=='__main__':
    raise SystemExit(main())
