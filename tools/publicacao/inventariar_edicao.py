#!/usr/bin/env python3
"""Inventário SHA256 dos fontes Quarto. Nunca aprova conteúdo, layout ou publicação."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import re


def sha(path:Path)->str:
    h=hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda:f.read(65536),b''):
            h.update(chunk)
    return h.hexdigest()


def inspect(root:Path,expected_chapters:int|None=None)->dict:
    root=Path(root).resolve()
    config=root/'_quarto.yml'
    if not config.is_file():raise ValueError('_quarto.yml ausente')
    raw=config.read_text(encoding='utf-8')
    entries=re.findall(r'^\s+-\s+(index\.qmd|chapters/[\w-]+\.qmd|appendices/[\w-]+\.qmd|references\.qmd)\s*$',raw,re.M)
    chapters=[x for x in entries if x.startswith('chapters/')]
    errors=[]
    if not entries or 'index.qmd' not in entries:errors.append('lista_de_capitulos_invalida')
    if len(set(entries))!=len(entries):errors.append('arquivo_repetido_na_configuracao')
    if expected_chapters is not None and len(chapters)!=expected_chapters:errors.append('quantidade_inesperada_de_capitulos')
    for i,name in enumerate(chapters,1):
        if not name.startswith(f'chapters/{i:02d}-'):errors.append('ordem_capitulos_incorreta')
    required=sorted(set(entries+['_quarto.yml','references.bib','styles.css','pdf-preambulo.tex','filters/boxes.lua']))
    files={}
    for name in required:
        path=root/name
        if not path.is_file() or path.is_symlink() or not path.resolve().is_relative_to(root):
            errors.append('arquivo_ausente_ou_inseguro:'+name)
        else:files[name]=sha(path)
    payload=json.dumps(files,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode('utf-8')
    return {'status':'FONTE_INVENTARIADA' if not errors else 'FALHA_INVENTARIO',
            'capitulos':len(chapters),'arquivos':files,'fingerprint_sha256':hashlib.sha256(payload).hexdigest(),
            'erros':errors,'approval':'PENDENTE_AUTOR','layout':'NAO_APROVADO',
            'aviso':'Integridade dos arquivos não confirma voz, conteúdo, figuras nem PDF pronto para publicação.'}


def main(argv=None):
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('root',type=Path)
    p.add_argument('--expected-chapters',type=int)
    p.add_argument('--output',type=Path)
    a=p.parse_args(argv)
    try:result=inspect(a.root,a.expected_chapters)
    except (OSError,ValueError) as ex:
        print(json.dumps({'status':'ERRO_ENTRADA','erro':str(ex)},ensure_ascii=False));return 2
    content=json.dumps(result,ensure_ascii=False,indent=2)+'\n'
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True)
        a.output.write_text(content,encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='arquivos'},ensure_ascii=False,indent=2))
    return 0 if not result['erros'] else 1

if __name__=='__main__':raise SystemExit(main())
