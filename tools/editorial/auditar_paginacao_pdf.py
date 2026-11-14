#!/usr/bin/env python3
"""Audita páginas finais potencialmente órfãs em um PDF, sem modificar o documento.

Critério conservador: páginas curtas seguidas por abertura explícita de capítulo.
Retorna candidatos para REVISÃO VISUAL, jamais declara um problema editorial
comprovado apenas por contagem de caracteres.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import re
from pathlib import Path

CAPITULO = re.compile(r'^Cap[ií]tulo\s+\d+\b', re.I)


def auditar(pdf: Path, limite: int = 450) -> dict:
    import fitz
    if limite <= 0:
        raise ValueError('limite deve ser positivo')
    content = pdf.read_bytes()
    achados = []
    with fitz.open(stream=content, filetype='pdf') as doc:
        textos = [p.get_text(sort=True).strip() for p in doc]
        for i, atual in enumerate(textos[:-1]):
            proximo = textos[i+1].lstrip()
            # A linha final do número de página é ignorada para o critério de conteúdo.
            sem_rodape = re.sub(r'\s+\d+\s*$', '', atual).strip()
            if CAPITULO.match(proximo) and len(sem_rodape) <= limite and not CAPITULO.match(atual):
                achados.append({
                    'pagina_fisica': i+1,
                    'pagina_seguinte': i+2,
                    'caracteres': len(sem_rodape),
                    'amostra': ' '.join(sem_rodape.split())[:160],
                    'classe': 'PAGINA_FINAL_CURTA',
                    'estado': 'SUSPEITA_REQUER_INSPECAO_VISUAL',
                })
        return {
            'ferramenta':'auditar_paginacao_pdf.py',
            'arquivo':str(pdf),
            'sha256':hashlib.sha256(content).hexdigest(),
            'paginas':len(doc),
            'limite_caracteres':limite,
            'candidatos':achados,
            'total_candidatos':len(achados),
            'status':'REVISAR' if achados else 'SEM_CANDIDATOS_NESTE_CRITERIO',
            'restricao':'Contagem de caracteres e detecção da próxima abertura de capítulo; não identifica todas as viúvas/órfãs, legendas soltas, sobreposições ou erros de fonte.'
        }


def main() -> int:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('pdf',type=Path)
    p.add_argument('--limite',type=int,default=450)
    p.add_argument('--json',type=Path)
    args=p.parse_args()
    if not args.pdf.is_file():p.error('PDF não encontrado')
    result=auditar(args.pdf,args.limite)
    payload=json.dumps(result,ensure_ascii=False,indent=2)+'\n'
    if args.json:
        args.json.parent.mkdir(parents=True,exist_ok=True)
        args.json.write_text(payload,encoding='utf-8')
    print(payload,end='')
    return 0 # Indício de risco não interrompe o pipeline; exige revisão humana.

if __name__=='__main__':raise SystemExit(main())
