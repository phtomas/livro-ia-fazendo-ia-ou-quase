#!/usr/bin/env python3
"""Módulo determinístico que avalia propostas de ação. Não é agente com LLM.

Apenas avalia política de uma lista fechada; NÃO executa ações propostas.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path

ACTIONS = {
    'READ_SOURCE': 'ALLOW_READ_ONLY',
    'CHECK_STRUCTURE': 'ALLOW_READ_ONLY',
    'GENERATE_REPORT': 'ALLOW_READ_ONLY',
    'PROPOSE_TEXT_DIFF': 'ALLOW_PROPOSAL_ONLY',
    'MODIFY_MANUSCRIPT': 'REQUIRE_HUMAN_APPROVAL',
    'CHANGE_TECHNICAL_FACT': 'REQUIRE_HUMAN_APPROVAL',
    'PUBLISH': 'REQUIRE_HUMAN_APPROVAL',
    'ACCESS_SECRET': 'DENY',
    'RUN_UNTRUSTED_COMMAND': 'DENY',
}


def decide(action: str) -> dict:
    decision = ACTIONS.get(action, 'DENY_UNKNOWN_ACTION')
    return {'action': action, 'decision': decision,
            'is_executed': False, 'model_used': None,
            'note': 'Decisão de política: não comprova origem, autorização ou execução'}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--action', required=True, help='código de ação, ex.: PUBLISH')
    parser.add_argument('--out', type=Path, help='opcional: relatório JSON')
    args = parser.parse_args()
    result = decide(args.action)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(result, ensure_ascii=False))


if __name__ == '__main__':
    main()
