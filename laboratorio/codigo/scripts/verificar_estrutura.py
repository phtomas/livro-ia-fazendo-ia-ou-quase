#!/usr/bin/env python3
"""Auditoria estrutural mínima do manuscrito e de sua numeração automática.
Não substitui renderização Quarto, revisão do autor nem inspeção visual do PDF.
"""
from pathlib import Path
import re
import sys
root = Path(__file__).resolve().parents[1]
conf = (root / '_quarto.yml').read_text(encoding='utf-8')
preview = (root / 'scripts/gerar_previa.sh').read_text(encoding='utf-8')
preamble = (root / 'pdf-preambulo.tex').read_text(encoding='utf-8')
errors = []
chapters = sorted((root / 'chapters').glob('*.qmd'))
if not re.search(r'^number-sections:\s*true', conf, re.M): errors.append('numeração global inativa')
if not re.search(r'^number-depth:\s*2', conf, re.M): errors.append('nível de número não é 2')
if '--number-sections' not in preview or '--top-level-division=chapter' not in preview:
    errors.append('prova Pandoc não replica numeração de capítulos')
if 'chapterprefix=true' not in preamble or 'formatChapterTocNumber' not in preamble:
    errors.append('prefixo Capítulo ausente na versão PDF')
for index, path in enumerate(chapters, 1):
    text = path.read_text(encoding='utf-8')
    first = re.search(r'^#\s+(.+)$', text, re.M)
    if not first: errors.append(f'{path.name}: falta título h1'); continue
    if re.match(r'^(Cap[ií]tulo\s+\d+|\d+[.\s])', first.group(1), re.I):
        errors.append(f'{path.name}: número digitado manualmente no título')
    if re.search(r'^##\s+\d+\.\d+', text, re.M):
        errors.append(f'{path.name}: seção digitada manualmente com número')
    if f'    - chapters/{path.name}' not in conf:
        errors.append(f'{path.name}: não está na lista Quarto')
    if f'chapters/{path.name}' not in preview:
        errors.append(f'{path.name}: não está no preview Pandoc')
    if path.name[:2] != f'{index:02d}':
        errors.append(f'{path.name}: capítulo fora da ordem numérica')
for name in ('index.qmd','appendices/10-principios.qmd','appendices/glossario.qmd','references.qmd'):
    txt = (root / name).read_text(encoding='utf-8')
    for head in re.findall(r'^#{1,2}\s+.*$',txt,re.M):
        if '{.unnumbered}' not in head:
            errors.append(f'{name}: heading deveria ser não numerado: {head}')
if errors:
    for x in errors: print('FAIL',x)
    sys.exit(1)
print(f'PASS: {len(chapters)} capítulos com numeração automática; apresentação, anexos e referências não numerados')
print('NOTA: checagem estrutural não substitui Quarto nem paginação.')
