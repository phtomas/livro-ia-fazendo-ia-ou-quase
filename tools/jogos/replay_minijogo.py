#!/usr/bin/env python3
"""Máquina de estados de um microjogo didático. NÃO emula TK90X nem MSX.

Reproduz ações e compara o estado final com o resultado esperado. Não usa IA.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import sys

RULES_VERSION = '1.0'
ACTIONS = {'start', 'left', 'right', 'collect', 'hit', 'restart'}


def new_state() -> dict:
    return {'screen': 'menu', 'x': 0, 'lives': 3, 'score': 0,
            'star_collected': False, 'ticks': 0}


def step(state: dict, action: str) -> dict:
    if action not in ACTIONS:
        raise ValueError(f'ação desconhecida: {action}')
    state = dict(state)
    state['ticks'] += 1
    if action == 'restart':
        result = new_state()
        result['ticks'] = state['ticks']
        return result
    if state['screen'] == 'menu':
        if action == 'start':
            state['screen'] = 'playing'
        return state
    if state['screen'] != 'playing':
        return state
    if action == 'left':
        state['x'] = max(0, state['x'] - 1)
    elif action == 'right':
        state['x'] = min(4, state['x'] + 1)
    elif action == 'collect' and state['x'] == 2 and not state['star_collected']:
        state['star_collected'] = True
        state['score'] += 100
    elif action == 'hit':
        state['lives'] -= 1
        state['x'] = 0
        if state['lives'] == 0:
            state['screen'] = 'game_over'
    return state


def replay(data: dict, content_sha256: str = '') -> dict:
    if data.get('rules_version') != RULES_VERSION:
        raise ValueError('versão das regras não corresponde ao simulador')
    actions = data.get('actions')
    expected = data.get('expect')
    if not isinstance(actions, list) or not all(type(x) is str for x in actions):
        raise ValueError('actions deve ser lista de nomes de ações')
    if len(actions) > 10000:
        raise ValueError('roteiro excede limite de ações')
    if not isinstance(expected, dict) or not expected:
        raise ValueError('expect deve ser objeto JSON não vazio')
    state = new_state()
    history = []
    for i, action in enumerate(actions, 1):
        state = step(state, action)
        history.append({'step': i, 'action': action, 'state': dict(state)})
    bad_keys = sorted(set(expected) - set(state))
    if bad_keys:
        raise ValueError('campos esperados desconhecidos: '+', '.join(bad_keys))
    diffs = {key: {'expected': exp, 'actual': state[key]} for key, exp in expected.items() if state[key] != exp}
    return {'tool': 'replay_minijogo.py', 'rules_version': RULES_VERSION,
            'status': 'FAIL_REPLAY' if diffs else 'PASS_SIMULATION', 'input_sha256': content_sha256,
            'expected': expected, 'final_state': state, 'differences': diffs,
            'history': history, 'limits': 'Aprova somente esta máquina de estados Python; não é ROM, nem teste em emulador ou máquina física'}


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('scenario', type=Path)
    p.add_argument('--output', type=Path)
    a = p.parse_args()
    try:
        raw = a.scenario.read_bytes()
        output = replay(json.loads(raw), hashlib.sha256(raw).hexdigest())
    except (OSError, json.JSONDecodeError, TypeError, ValueError) as e:
        print('ERROR_INPUT: '+str(e), file=sys.stderr)
        return 3
    payload = json.dumps(output, indent=2, ensure_ascii=False)+'\n'
    if a.output:
        a.output.parent.mkdir(parents=True, exist_ok=True)
        a.output.write_text(payload, encoding='utf-8')
    else:
        print(payload)
    return 0 if output['status'] == 'PASS_SIMULATION' else 2

if __name__ == '__main__':
    sys.exit(main())
