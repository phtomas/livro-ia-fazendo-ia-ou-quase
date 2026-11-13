#!/usr/bin/env python3
"""Avaliação mecânica limitada de uma revisão proposta, sem julgar voz nem fatos.

Compara tokens numéricos/unidades e trechos protegidos. Nunca altera os textos.
Um PASS_LIMITED só cobre estes invariantes e não aprova publicação.
"""
from __future__ import annotations
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re

# Deliberadamente conservador: números decimais, hexadecimais e unidades comuns.
NUMBERS = re.compile(r'(?<![\w])(?:0x[0-9a-fA-F]+|\$[0-9a-fA-F]+|\d+(?:[.,]\d+)?)(?:\s?(?:mV|kV|V|mA|A|MHz|kHz|Hz|ns|µs|ms|KB|MB|GB|mm|cm|Ω|ohms))?(?![\w])')
MAX_BYTES = 250_000


def sha(s:str)->str:
    return hashlib.sha256(s.encode('utf-8')).hexdigest()


def evaluate(original: str, candidate: str, protected: list[str] | None=None) -> dict:
    protected=protected or []
    old=Counter(NUMBERS.findall(original))
    new=Counter(NUMBERS.findall(candidate))
    removed=list((old-new).elements())
    added=list((new-old).elements())
    missing=[p for p in protected if p in original and p not in candidate]
    # If protected source text is absent at baseline, raise a warning.
    invalid=[p for p in protected if p not in original]
    problems=bool(removed or added or missing or invalid)
    return {'status':'FAIL_GUARDRAIL' if problems else 'PASS_LIMITED',
            'original_sha256':sha(original),'candidate_sha256':sha(candidate),
            'changed':original!=candidate,'removed_numeric_tokens':removed,
            'added_numeric_tokens':added,'missing_protected':missing,
            'invalid_protected_baseline':invalid,
            'automated_checks':['numeric_unit_token_multiset','protected_literal_presence'],
            'not_checked':['voice','technical_correctness','citations','paragraph_fidelity','layout','human_approval'],
            'can_publish':False}


def main()->int:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('original',type=Path)
    p.add_argument('candidate',type=Path)
    p.add_argument('--protect',action='append',default=[])
    p.add_argument('--report',type=Path)
    args=p.parse_args()
    for f in (args.original,args.candidate):
        if not f.is_file() or f.stat().st_size>MAX_BYTES:
            p.error('arquivo inexistente ou acima do limite de tamanho')
    output=evaluate(args.original.read_text(encoding='utf-8'),args.candidate.read_text(encoding='utf-8'),args.protect)
    if args.report:
        args.report.parent.mkdir(parents=True,exist_ok=True)
        args.report.write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(output,ensure_ascii=False))
    return 0 if output['status']=='PASS_LIMITED' else 2

if __name__=='__main__':
    raise SystemExit(main())
