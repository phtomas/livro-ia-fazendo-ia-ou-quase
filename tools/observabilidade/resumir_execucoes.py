#!/usr/bin/env python3
"""Resume registros declarados (JSONL) e estima custos, sem APIs nem inferências.

Entrada sintética/didática. Não é auditoria de cobrança ou verificação de
identidade do modelo. Todos os custos são estimativas condicionais às tarifas.
"""
from __future__ import annotations
import argparse
from decimal import Decimal, InvalidOperation
import hashlib
import json
from pathlib import Path


def decimal_no_negative(value, field):
    if isinstance(value, bool) or value is None:
        raise ValueError(f'{field}: precisa ser número explícito')
    try:
        n = Decimal(str(value))
    except InvalidOperation as exc:
        raise ValueError(f'{field}: inválido') from exc
    if not n.is_finite() or n < 0:
        raise ValueError(f'{field}: negativo ou infinito')
    return n


def token_count(value, field):
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f'{field}: inteiro >= 0 obrigatório')
    return value


def load_runs(path: Path):
    runs = []
    ids = set()
    for line_no, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
        if not line.strip():
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f'linha {line_no}: JSON inválido') from exc
        if not isinstance(obj, dict) or not isinstance(obj.get('run_id'), str) or not obj['run_id'].strip():
            raise ValueError(f'linha {line_no}: run_id obrigatório')
        if obj['run_id'] in ids:
            raise ValueError(f'linha {line_no}: run_id duplicado')
        ids.add(obj['run_id'])
        runs.append(obj)
    if not runs:
        raise ValueError('nenhuma execução')
    return runs


def summary(runs, rates, source_sha256):
    if not isinstance(rates, dict) or rates.get('unit') != 'USD_per_1M_tokens':
        raise ValueError('tarifas: unit deve ser USD_per_1M_tokens')
    if not rates.get('synthetic') is True:
        raise ValueError('este laboratório somente admite tabelas explicitamente sintéticas')
    models = rates.get('models', {})
    if not isinstance(models, dict):
        raise ValueError('tarifas: models deve ser objeto')
    output = []
    for run in runs:
        kind = run.get('kind')
        if kind not in {'deterministic', 'model_call'}:
            raise ValueError(f"{run['run_id']}: kind inválido")
        usage = run.get('reported_usage')
        requested = run.get('model_requested')
        reported = run.get('model_effective_reported')
        if reported is not None and (not isinstance(reported, str) or not reported.strip()):
            raise ValueError('model_effective_reported vazio/inválido')
        if kind == 'deterministic':
            if usage is not None or reported is not None:
                raise ValueError('etapa determinística não admite relato de tokens/modelo')
        if usage is not None:
            if kind != 'model_call' or not isinstance(usage, dict):
                raise ValueError('reported_usage deve ser objeto para model_call')
            inp = token_count(usage.get('input_tokens'), 'input_tokens')
            cached = token_count(usage.get('cached_input_tokens'), 'cached_input_tokens')
            out = token_count(usage.get('output_tokens'), 'output_tokens')
            if cached > inp:
                raise ValueError('cached_input_tokens maior que input_tokens')
        else:
            inp = cached = out = None
        evidence = run.get('model_id_source')
        model_verified_in_log = bool(reported and evidence == 'provider_response')
        effective = reported if model_verified_in_log else None
        if reported and evidence != 'provider_response':
            raise ValueError('modelo efetivo só pode ser marcado como relatado por provider_response')
        model_cost = None
        if usage is not None and effective in models:
            tariff = models[effective]
            for key in ('uncached_input', 'cached_input', 'output'):
                if key not in tariff:
                    raise ValueError(f'tarifa incompleta: {effective}.{key}')
            uncache_price = decimal_no_negative(tariff['uncached_input'], 'uncached_input')
            cache_price = decimal_no_negative(tariff['cached_input'], 'cached_input')
            out_price = decimal_no_negative(tariff['output'], 'output')
            model_cost = ((Decimal(inp - cached) * uncache_price) + (Decimal(cached) * cache_price) + (Decimal(out) * out_price)) / Decimal(1000000)
        tool_price = run.get('tool_cost_usd')
        tool_cost = decimal_no_negative(tool_price, 'tool_cost_usd') if tool_price is not None else None
        total = model_cost + tool_cost if model_cost is not None and tool_cost is not None else None
        output.append({
            'run_id': run['run_id'], 'kind': kind, 'domain': run.get('domain', 'unknown'),
            'model_requested': requested, 'model_effective_observed': effective,
            'model_identification': 'REPORTED_BY_PROVIDER' if effective else 'UNKNOWN',
            'usage_reported_in_record': usage is not None,
            'input_tokens': inp, 'cached_input_tokens': cached, 'output_tokens': out,
            'model_estimate_usd': str(model_cost) if model_cost is not None else None,
            'tool_cost_declared_usd': str(tool_cost) if tool_cost is not None else None,
            'total_estimate_usd': str(total) if total is not None else None,
            'result_claim': run.get('result_claim', 'NOT_EVALUATED'),
            'evidence_ref_claim': run.get('evidence_ref'),
        })
    return {'schema_version': '1.0', 'synthetic': True,
            'origin': 'LOCAL_DECLARED_RECORDS_NOT_PROVIDER_AUDIT',
            'rates_unit': rates['unit'], 'rate_card_label': rates.get('label'),
            'input_sha256': source_sha256, 'records': output,
            'warnings': [
                'Esta ferramenta não confirma se chamadas de IA ocorreram, nem autentica logs.',
                'Modelo efetivo só aparece se reportado por provider_response no registro declarado.',
                'Tarifas fictícias: estimativas não representam fatura real.',
                'Campos null significam desconhecido, jamais custo zero.',
                'Claims de qualidade e evidência não são verificados independentemente.',
            ]}


def run_cli():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--runs', type=Path, required=True)
    p.add_argument('--rates', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    args = p.parse_args()
    if args.output.resolve() in (args.runs.resolve(), args.rates.resolve()):
        p.error('saída não pode sobrescrever a fonte ou as tarifas')
    data = args.runs.read_bytes()
    report = summary(load_runs(args.runs), json.loads(args.rates.read_text(encoding='utf-8')), hashlib.sha256(data).hexdigest())
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(f"PASS_LIMITED: {len(report['records'])} registros declarados, {args.output}")
    return 0


if __name__ == '__main__':
    raise SystemExit(run_cli())
