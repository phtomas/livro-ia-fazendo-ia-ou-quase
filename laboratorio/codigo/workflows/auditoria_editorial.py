#!/usr/bin/env python3
"""Workflow determinístico de pré-publicação (somente leitura dos manuscritos).

Não inicia modelos, não altera capítulos, não publica, não corrige layout.
Executa checagens e salva um relatório JSON em local especificado.
"""
from __future__ import annotations
import argparse
import datetime as dt
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys


def file_sha256(path:Path)->str:
    h=hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda:f.read(128*1024),b''):
            h.update(block)
    return h.hexdigest()


def call(script:Path,root:Path)->dict:
    cp=subprocess.run([sys.executable,str(script),str(root)],capture_output=True,text=True,check=False)
    return {'script':str(script.relative_to(root)), 'exit_code':cp.returncode,
            'output':cp.stdout[-6000:], 'stderr':cp.stderr[-1500:],
            'status':'PASS_STRUCTURE' if cp.returncode==0 else 'FAIL'}


def main()->int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root',type=Path,help='diretório do projeto Quarto')
    parser.add_argument('--pdf',type=Path,help='prévia PDF que será analisada, sem modificação')
    parser.add_argument('--pdf-page',type=int,action='append',help='restringir página(s) do PDF')
    parser.add_argument('--report',type=Path,required=True,help='destino do JSON de auditoria')
    args=parser.parse_args()
    root=args.root.resolve()
    if not (root/'_quarto.yml').is_file():
        parser.error('raiz do projeto não contém _quarto.yml')
    result={'workflow':'auditoria_editorial.py','versao':'0.1','timestamp_utc':dt.datetime.now(dt.timezone.utc).isoformat(),
            'root':str(root),'usa_llm':False,'modifica_manuscrito':False,
            'checks':[call(root/'scripts/verificar_boxes.py',root),call(root/'scripts/verificar_estrutura.py',root)]}
    result['sha256_qmd']={str(p.relative_to(root)):file_sha256(p) for p in sorted((root/'chapters').glob('*.qmd'))}
    if args.pdf:
        if not args.pdf.is_file(): parser.error(f'PDF não encontrado: {args.pdf}')
        loc=root/'tools/editorial/verificar_pdf_boxes.py'
        spec=importlib.util.spec_from_file_location('verificar_pdf_boxes',loc)
        if not spec or not spec.loader: raise RuntimeError('não foi possível importar verificador de PDF')
        mod=importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        result['pdf']=mod.inspect(args.pdf,args.pdf_page)
        result['pdf']['sha256']=file_sha256(args.pdf)
    else:
        result['pdf']={'status':'NÃO VERIFICADO','reason':'PDF não fornecido'}
    structural_ok=all(x['exit_code']==0 for x in result['checks'])
    layout_failed=result['pdf'].get('issue_count',0)>0
    result['status']='PARTIAL_KNOWN_FAIL' if structural_ok and layout_failed else ('PASS_LIMITED' if structural_ok else 'FAIL')
    result['requires_human_approval']=True
    result['message']='PASS de estrutura não prova voz, precisão técnica ou aprovação para publicação. Falha do PDF mantém seu próprio estado FAIL.'
    args.report.parent.mkdir(parents=True,exist_ok=True)
    args.report.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(f"{result['status']} — relatório: {args.report}")
    for item in result['checks']: print(item['status']+': '+item['script'])
    print('PDF: '+result['pdf']['status'])
    # Um histórico conhecido pode estar documentado; nunca converte o FAIL da página em PASS.
    return 2 if not structural_ok else (1 if layout_failed else 0)

if __name__=='__main__':
    raise SystemExit(main())
