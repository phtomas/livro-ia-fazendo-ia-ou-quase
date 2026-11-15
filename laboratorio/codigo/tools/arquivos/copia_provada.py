#!/usr/bin/env python3
"""Copia arquivos REGULARES de uma pasta plana, confere SHA-256 e não usa LLM.

Segurança: modo padrão é prévia (dry-run). Executar exige --execute.
Destino deve não existir ou estar vazio. Links simbólicos e subpastas são recusados.
Não remove nem sobrescreve arquivos. Projetado para demonstração em dados próprios.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
from shutil import copy2
import sys


def digest(file:Path)->str:
    h=hashlib.sha256()
    with file.open('rb') as inp:
        for data in iter(lambda:inp.read(131072),b''):h.update(data)
    return h.hexdigest()


def run(source:Path,dest:Path,execute:bool=False)->dict:
    source=source.expanduser().absolute()
    dest=dest.expanduser().absolute()
    if not source.is_dir() or source.is_symlink():
        raise ValueError('origem deve existir, ser pasta regular e não ser symlink')
    if dest.is_symlink():
        raise ValueError('destino não pode ser symlink')
    if dest==source or dest.is_relative_to(source) or source.is_relative_to(dest):
        raise ValueError('origem/destino não podem ser iguais ou estar aninhados')
    if dest.exists() and (not dest.is_dir() or any(dest.iterdir())):
        raise ValueError('destino deve estar vazio ou não existir; nunca sobrescrever')
    items=sorted(source.iterdir())
    if not items:
        raise ValueError('origem vazia: nenhuma operação para comprovar')
    if any(p.is_symlink() or not p.is_file() for p in items):
        raise ValueError('origem deve conter só arquivos regulares; recursão/symlinks não permitidos')
    plan=[{'nome':p.name,'sha256_origem':digest(p)} for p in items]
    if not execute:
        return {'status':'DRY_RUN','usa_llm':False,'origem':str(source),'destino':str(dest),
                'qtd':len(plan),'arquivos':plan}
    dest.mkdir(parents=True,exist_ok=True)
    for p in items:
        copy2(p,dest/p.name)
        if digest(p)!=digest(dest/p.name):
            raise RuntimeError('cópia divergente: '+p.name)
    return {'status':'PASS_COPY','usa_llm':False,'origem':str(source),'destino':str(dest),
            'qtd':len(plan),'arquivos':plan}


def main()->int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('origem',type=Path)
    parser.add_argument('destino',type=Path)
    parser.add_argument('--execute',action='store_true',help='sem esta opção só faz dry-run')
    args=parser.parse_args()
    try:
        print(json.dumps(run(args.origem,args.destino,args.execute),ensure_ascii=False,indent=2))
    except Exception as exc:
        print('FAIL:',exc,file=sys.stderr)
        return 2
    return 0

if __name__ == '__main__':raise SystemExit(main())
