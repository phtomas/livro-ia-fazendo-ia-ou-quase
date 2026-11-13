#!/usr/bin/env python3
"""Laboratório: fluxo editorial determinístico com checkpoints e retomada.

Sem LLM, sem edição do manuscrito, sem publicação e sem aprovação automática.
Estados: NEW -> INVENTORIED -> STRUCTURE_OK -> WAITING_HUMAN.
Interrupção injetada: INTERRUPTED; alterações na fonte após o checkpoint: BLOCKED.
Não é controle transacional ou de concorrência distribuída.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys


def sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(65536), b''):
            h.update(chunk)
    return h.hexdigest()


def snapshot(root: Path) -> dict[str, str]:
    files = [root / '_quarto.yml', root / 'index.qmd'] + sorted((root / 'chapters').glob('*.qmd'))
    if any(not p.is_file() or p.is_symlink() for p in files):
        raise ValueError('Fontes obrigatórias ausentes ou symbolic links não aceitos')
    return {p.relative_to(root).as_posix(): sha(p) for p in files}


def write_atomic(file: Path, data: dict) -> None:
    file.parent.mkdir(parents=True, exist_ok=True)
    temporary = file.with_name(file.name + '.tmp')
    with temporary.open('w', encoding='utf-8', newline='\n') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')
        f.flush()
        os.fsync(f.fileno())
    os.replace(temporary, file)


def event(report: dict, state: str, reason: str) -> None:
    report['state'] = state
    report.setdefault('events', []).append({
        'time_utc': datetime.now(timezone.utc).isoformat(), 'state': state, 'reason': reason})


def validate(root: Path) -> list[dict]:
    results = []
    for name in ['scripts/verificar_boxes.py', 'scripts/verificar_estrutura.py']:
        cmd = [sys.executable, str(root / name), str(root)]
        p = subprocess.run(cmd, capture_output=True, text=True, check=False, timeout=60)
        results.append({'checker': name, 'exit_code': p.returncode,
                        'output_tail': p.stdout[-1200:], 'error_tail': p.stderr[-800:]})
    return results


def run(root: Path, work: Path, fail_at: str | None = None) -> int:
    root, work = root.resolve(), work.resolve()
    if not (root / '_quarto.yml').is_file():
        raise ValueError('Não é uma raiz Quarto: falta _quarto.yml')
    # Local de estado não pode ficar dentro da árvore de fontes: elimina ciclos de snapshot.
    if work == root or root in work.parents:
        raise ValueError('Escolha --work fora do projeto para manter estado separado do manuscrito')
    state_file = work / 'state.json'
    current = snapshot(root)
    if state_file.exists():
        saved = json.loads(state_file.read_text(encoding='utf-8'))
        if saved.get('schema_version') != 1 or saved.get('source_root') != str(root):
            raise ValueError('Checkpoint incompatível ou de outro projeto; preserve e use outro diretório')
        if saved['source_sha256'] != current:
            event(saved, 'BLOCKED', 'Fonte alterada desde o checkpoint; requer novo fluxo, sem reutilizar PASS antigo')
            write_atomic(state_file, saved)
            return 3
        if saved['state'] in {'WAITING_HUMAN', 'STRUCTURE_FAILED', 'BLOCKED'}:
            return 0 if saved['state'] == 'WAITING_HUMAN' else 3
    else:
        saved = {'schema_version': 1, 'source_root': str(root), 'source_sha256': current,
                 'uses_llm': False, 'changes_sources': False, 'publishes': False,
                 'approval_status': 'NOT_GRANTED', 'checks': [], 'events': []}
        event(saved, 'INVENTORIED', 'Manifesto SHA-256 dos fontes gravado')
        write_atomic(state_file, saved)
    if fail_at == 'after-inventory':
        event(saved, 'INTERRUPTED', 'Falha didática injetada antes da validação; ainda não é PASS')
        write_atomic(state_file, saved)
        return 4
    saved['checks'] = validate(root)
    if any(c['exit_code'] != 0 for c in saved['checks']):
        event(saved, 'STRUCTURE_FAILED', 'Uma verificação estrutural falhou; não avançar')
        write_atomic(state_file, saved)
        return 2
    event(saved, 'STRUCTURE_OK', 'Duas verificações estruturais aprovadas, sem revisão de voz')
    event(saved, 'WAITING_HUMAN', 'Somente o autor pode aprovar o manuscrito; fluxo encerra sem publicar')
    write_atomic(state_file, saved)
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('root', type=Path)
    p.add_argument('--work', type=Path, required=True, help='pasta externa à árvore do manuscrito')
    p.add_argument('--fail-at', choices=['after-inventory'], help='simular falha e testar retomada')
    args = p.parse_args()
    try:
        result = run(args.root, args.work, args.fail_at)
    except (ValueError, OSError, KeyError, json.JSONDecodeError, subprocess.TimeoutExpired) as ex:
        print('ERROR:', ex, file=sys.stderr)
        return 5
    print('Código:', result, 'Estado:', (args.work / 'state.json'))
    return result


if __name__ == '__main__':
    raise SystemExit(main())
