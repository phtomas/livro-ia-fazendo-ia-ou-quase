#!/usr/bin/env python3
"""Pré-voo offline: compara capacidades *declaradas*, sem chamar serviços de IA."""
from __future__ import annotations
import argparse
import json
from pathlib import Path


def evaluate(contract:dict,adapter:dict)->dict:
    required=contract.get('capacidades_obrigatorias')
    features=adapter.get('capacidades')
    if not isinstance(required,list) or not required or not all(isinstance(x,str) and x.strip() for x in required) or len(set(required))!=len(required):
        raise ValueError('contrato de capacidades inválido')
    if not isinstance(features,dict):raise ValueError('perfil sem capacidades')
    if any(v not in (True,False,None) for v in features.values()):raise ValueError('capacidades devem ser true, false ou null')
    missing=[x for x in required if features.get(x,'unknown') is False]
    unknown=[x for x in required if x not in features or features[x] is None]
    status='BLOQUEADO_POR_CAPACIDADE' if missing else ('INDETERMINADO' if unknown else 'COMPATIVEL_DECLARADO')
    return {'status':status,'ambiente_declarado':adapter.get('nome','não identificado'),
            'recursos_ausentes':missing,'recursos_desconhecidos':unknown,
            'limite':'Compatibilidade declarada não demonstra instalação, execução, autorização ou qualidade real.'}


def main(argv=None)->int:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('contrato',type=Path)
    p.add_argument('perfil',type=Path)
    p.add_argument('--output',type=Path)
    a=p.parse_args(argv)
    try:
        report=evaluate(json.loads(a.contrato.read_text(encoding='utf8')),
                        json.loads(a.perfil.read_text(encoding='utf8')))
    except (OSError,ValueError,json.JSONDecodeError) as ex:
        print(json.dumps({'status':'ERRO_ENTRADA','erro':str(ex)},ensure_ascii=False));return 2
    content=json.dumps(report,ensure_ascii=False,indent=2)+'\n'
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True)
        a.output.write_text(content,encoding='utf8')
    print(content,end='')
    return {'COMPATIVEL_DECLARADO':0,'BLOQUEADO_POR_CAPACIDADE':1,'INDETERMINADO':3}[report['status']]

if __name__=='__main__':raise SystemExit(main())
