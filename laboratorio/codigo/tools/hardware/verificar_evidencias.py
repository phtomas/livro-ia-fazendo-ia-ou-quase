#!/usr/bin/env python3
"""Audita a *rastreabilidade* de afirmações; não valida circuitos nem medições."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path

VALID_KIND = {'esquematico','datasheet','netlist','erc','drc','foto','medicao','ensaio','documento'}
FISICO = {'medicao','ensaio'}


def digest(path: Path) -> str:
    h=hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda:f.read(64 * 1024),b''):
            h.update(block)
    return h.hexdigest()


def validate(manifest: Path) -> dict:
    manifest=Path(manifest).resolve()
    data=json.loads(manifest.read_text(encoding='utf-8'))
    if not isinstance(data,dict) or not isinstance(data.get('afirmacoes'),list) or not data['afirmacoes']:
        raise ValueError('manifesto precisa de afirmacoes não vazias')
    base=manifest.parent
    items=[]
    seen=set()
    for entry in data['afirmacoes']:
        issues=[]
        if not isinstance(entry,dict):
            items.append({'id':'?', 'erros':['afirmacao_nao_objeto']}); continue
        ident=entry.get('id')
        revision=entry.get('revisao')
        level=entry.get('nivel')
        if not isinstance(ident,str) or not ident.strip() or ident in seen:issues.append('id_ausente_ou_repetido')
        seen.add(ident)
        if not isinstance(entry.get('texto'),str) or not entry['texto'].strip():issues.append('texto_ausente')
        if not isinstance(revision,str) or not revision.strip():issues.append('revisao_nao_identificada')
        if level not in {'documental','fisico'}:issues.append('nivel_invalido')
        evidence=entry.get('evidencias')
        if not isinstance(evidence,list) or not evidence:issues.append('sem_evidencias');evidence=[]
        found_kinds=set()
        for ev in evidence:
            if not isinstance(ev,dict):issues.append('evidencia_invalida');continue
            kind=ev.get('tipo'); path=ev.get('arquivo'); expected=ev.get('sha256')
            if kind not in VALID_KIND:issues.append('tipo_desconhecido');continue
            if ev.get('revisao')!=revision:issues.append('revisao_divergente')
            if not isinstance(path,str) or not path or Path(path).is_absolute() or '..' in Path(path).parts:
                issues.append('caminho_inseguro');continue
            actual=(base/path)
            if not actual.is_file() or actual.is_symlink() or not actual.resolve().is_relative_to(base):
                issues.append('arquivo_ausente_ou_inseguro');continue
            if not isinstance(expected,str) or len(expected)!=64 or expected.lower()!=digest(actual):
                issues.append('hash_divergente');continue
            found_kinds.add(kind)
        if level=='fisico' and not (found_kinds & FISICO):issues.append('falta_prova_fisica')
        items.append({'id':ident,'nivel':level,'erros':sorted(set(issues)),'tipos_confirmados':sorted(found_kinds)})
    errors=sum(bool(x['erros']) for x in items)
    return {'ferramenta':'verificar_evidencias','status':'PASS_RASTREABILIDADE' if errors==0 else 'FAIL_EVIDENCIA',
            'erros':errors,'afirmacoes':items,'aviso':'A validação dos arquivos e hashes NÃO valida as conclusões técnicas nem substitui medições.'}


def main(argv=None):
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('manifesto',type=Path)
    p.add_argument('--output',type=Path)
    args=p.parse_args(argv)
    try: outcome=validate(args.manifesto)
    except (OSError,ValueError,json.JSONDecodeError) as ex:
        print(json.dumps({'status':'ERRO_ENTRADA','erro':str(ex)},ensure_ascii=False));return 2
    content=json.dumps(outcome,ensure_ascii=False,indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(content,encoding='utf-8')
    print(content,end='')
    return 0 if outcome['erros']==0 else 1

if __name__=='__main__':
    raise SystemExit(main())
