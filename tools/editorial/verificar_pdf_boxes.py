#!/usr/bin/env python3
"""Auditoria somente leitura: texto monoespaçado que excede a direita de quadros em PDF.

Dependência: PyMuPDF (pip install pymupdf).
Escopo: inspeção geométrica aproximada; não substitui renderização e revisão visual.
Não modifica o PDF nem realiza chamada de IA.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import sys


def inspect(pdf: Path, pages: list[int] | None = None, tolerance_pt: float = 1.0) -> dict:
    try:
        import fitz  # type: ignore
    except ImportError as exc:
        raise RuntimeError('PyMuPDF não instalado: pip install pymupdf') from exc
    findings = []
    n_containers = 0
    with fitz.open(str(pdf)) as document:
        tested = pages or list(range(1, len(document) + 1))
        for n in tested:
            if n < 1 or n > len(document):
                raise ValueError(f'página inexistente: {n} de {len(document)}')
            page = document[n - 1]
            # Retângulos claros de fundo são os quadros que efetivamente contêm texto.
            # Uma linha vertical colorida vizinha pode ter retângulo maior; ela não é o limite.
            candidates = []
            for drawing in page.get_drawings():
                rect = drawing.get('rect')
                fill = drawing.get('fill')
                if not rect or not fill or len(fill) < 3:
                    continue
                if (rect.width >= 100 and rect.height >= 32
                        and min(fill[:3]) >= 0.82
                        and max(fill[:3]) - min(fill[:3]) <= 0.12):
                    candidates.append(rect)
            # Remover duplicações de retângulos praticamente idênticos.
            unique = []
            for rect in candidates:
                if not any(abs(rect.x0-r.x0)<1 and abs(rect.x1-r.x1)<1 and
                           abs(rect.y0-r.y0)<1 and abs(rect.y1-r.y1)<1 for r in unique):
                    unique.append(rect)
            n_containers += len(unique)
            for block in page.get_text('dict').get('blocks', []):
                if block.get('type') != 0:
                    continue
                for line in block.get('lines', []):
                    for span in line.get('spans', []):
                        font = span.get('font', '')
                        if not any(token in font.lower() for token in ('mono', 'courier', 'code')):
                            continue
                        bbox = span.get('bbox')
                        if not bbox:
                            continue
                        x0,y0,x1,y1 = bbox
                        for box in unique:
                            # Atribuir o texto ao quadro que contém o início do trecho.
                            if not (box.x0 <= x0 <= box.x1 and box.y0-2 <= y0 and y1 <= box.y1+2):
                                continue
                            if x1 > box.x1 + tolerance_pt:
                                findings.append({
                                    'page': n,
                                    'kind': 'CODE_OVERFLOW_RIGHT',
                                    'text': span.get('text', '').strip()[:140],
                                    'right_edge_pt': round(float(x1),2),
                                    'box_right_pt': round(float(box.x1),2),
                                    'over_pt': round(float(x1-box.x1),2),
                                })
                            break
    return {
        'pdf': str(pdf), 'tool': 'verificar_pdf_boxes.py', 'pages_inspected': tested,
        'light_boxes_inspected': n_containers, 'issue_count': len(findings),
        'findings': findings,
        'status': 'FAIL' if findings else 'PASS_LIMITED',
        'scope': 'Apenas transbordamento geométrico de spans monoespaçados em quadros claros. PASS_LIMITED não garante página correta.',
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pdf', type=Path)
    parser.add_argument('--page', type=int, action='append', help='página física (1 a N); repetir para várias')
    parser.add_argument('--tolerance', type=float, default=1.0, help='margem de tolerância em pontos')
    parser.add_argument('--json', dest='json_path', type=Path, help='salvar relatório JSON neste arquivo')
    args=parser.parse_args()
    if not args.pdf.is_file():
        parser.error(f'PDF não encontrado: {args.pdf}')
    try:
        result=inspect(args.pdf,args.page,args.tolerance)
    except Exception as exc:
        print(f'ERRO: {exc}',file=sys.stderr)
        return 2
    data=json.dumps(result,ensure_ascii=False,indent=2)
    print(data)
    if args.json_path:
        args.json_path.parent.mkdir(parents=True,exist_ok=True)
        args.json_path.write_text(data+'\n',encoding='utf-8')
    return 1 if result['issue_count'] else 0


if __name__ == '__main__':
    raise SystemExit(main())
