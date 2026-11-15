#!/usr/bin/env python3
"""Auditoria limitada de fontes Quarto. Não altera arquivos nem prova diagramação.

Encontra: recursos locais ausentes, IDs repetidos e linhas longas em blocos de código.
Os avisos de comprimento são heurísticos, NÃO prova de corte no PDF.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

IMAGE = re.compile(r'!\[([^\]]*)\]\(([^)]+)\)')
LINK = re.compile(r'(?<!!)\[([^\]]+)\]\(([^)]+)\)')
ID = re.compile(r'\{#((?:fig|tbl|sec|lst)-[a-z0-9-]+)\}')


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def is_local(target: str) -> bool:
    return not (target.startswith(('#', '/', '//', 'data:', 'mailto:'))
                or re.match(r'^[a-z][a-z0-9+.-]*:', target, re.I))


def audit(root: Path, max_code_chars: int = 94) -> dict:
    root = root.resolve()
    if not (root / '_quarto.yml').is_file():
        raise ValueError('diretório sem _quarto.yml')
    files = [root / 'index.qmd', *sorted((root / 'chapters').glob('*.qmd')),
             *sorted((root / 'appendices').glob('*.qmd'))]
    issues = []
    ids = {}
    for path in files:
        if not path.is_file():
            issues.append({'code': 'MISSING_SOURCE', 'severity': 'ERROR', 'file': str(path.relative_to(root))})
            continue
        name = path.relative_to(root).as_posix()
        inside = False
        marker = None
        for number, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
            stripped = line.lstrip()
            m = re.match(r'^(`{3,}|~{3,})', stripped)
            if m:
                fence = m.group(1)
                if not inside:
                    inside, marker = True, fence
                elif fence[0] == marker[0] and len(fence) >= len(marker):
                    inside, marker = False, None
                continue
            if inside:
                if len(line) > max_code_chars:
                    issues.append({'code': 'LONG_CODE_LINE', 'severity': 'WARNING', 'file': name,
                                   'line': number, 'length': len(line), 'max_chars': max_code_chars})
                continue
            for match in ID.finditer(line):
                identifier = match.group(1)
                if identifier in ids:
                    issues.append({'code': 'DUPLICATE_REFERENCE_ID', 'severity': 'ERROR',
                                   'file': name, 'line': number, 'id': identifier, 'first': ids[identifier]})
                else:
                    ids[identifier] = f'{name}:{number}'
            for regex, kind in ((IMAGE, 'IMAGE'), (LINK, 'LINK')):
                for match in regex.finditer(line):
                    target = match.group(2).strip().split()[0].strip('<>')
                    target = target.split('#')[0].split('?')[0]
                    if kind == 'IMAGE' and not match.group(1).strip():
                        issues.append({'code': 'MISSING_IMAGE_ALT', 'severity': 'WARNING',
                                       'file': name, 'line': number})
                    if not target or not is_local(target):
                        continue
                    dest = (path.parent / target).resolve()
                    if not dest.is_relative_to(root):
                        issues.append({'code': 'OUTSIDE_PROJECT', 'severity': 'ERROR',
                                       'file': name, 'line': number, 'target': target})
                    elif not dest.is_file():
                        issues.append({'code': f'MISSING_LOCAL_{kind}', 'severity': 'ERROR',
                                       'file': name, 'line': number, 'target': target})
    errors = sum(i['severity'] == 'ERROR' for i in issues)
    warnings = sum(i['severity'] == 'WARNING' for i in issues)
    return {'tool': 'auditar_fontes_quarto.py', 'status': 'FAIL' if errors else 'PASS_LIMITED',
            'root': str(root), 'file_count': len(files), 'issues': issues,
            'errors': errors, 'warnings': warnings, 'changes_manuscript': False,
            'limits': ['Regex limitada; não interpreta toda a sintaxe Quarto/Markdown',
                       'Linha longa não comprova transbordamento na página',
                       'PASS_LIMITED não aprova voz, imagem, referências externas nem PDF']}


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('root', type=Path)
    p.add_argument('--max-code-chars', type=int, default=94)
    p.add_argument('--output', type=Path)
    a = p.parse_args()
    if a.max_code_chars < 20:
        p.error('max-code-chars deve ser >=20')
    try:
        result = audit(a.root, a.max_code_chars)
    except (OSError, ValueError) as ex:
        p.error(str(ex))
    payload = json.dumps(result, indent=2, ensure_ascii=False) + '\n'
    if a.output:
        a.output.parent.mkdir(parents=True, exist_ok=True)
        a.output.write_text(payload, encoding='utf-8')
    else:
        print(payload)
    return 2 if result['errors'] else 0


if __name__ == '__main__':
    sys.exit(main())
