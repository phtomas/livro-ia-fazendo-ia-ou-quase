import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('medidor', ROOT/'tools/observabilidade/resumir_execucoes.py')
med = importlib.util.module_from_spec(spec)
spec.loader.exec_module(med)
RATES = {'synthetic': True, 'unit': 'USD_per_1M_tokens', 'models': {'A': {'uncached_input': '1', 'cached_input': '0.2', 'output': '4'}}}
BASE = {'run_id': 'r', 'kind': 'model_call', 'model_requested': 'A', 'model_effective_reported': 'A', 'model_id_source': 'provider_response', 'reported_usage': {'input_tokens': 8000, 'cached_input_tokens': 2000, 'output_tokens': 1000}, 'tool_cost_usd': '0'}

class MetricsTests(unittest.TestCase):
    def test_correct_cost(self):
        x=med.summary([BASE],RATES,'x')['records'][0]
        self.assertEqual(x['model_estimate_usd'],'0.0104')
        self.assertEqual(x['total_estimate_usd'],'0.0104')
    def test_unknown_model_no_cost(self):
        x=med.summary([{**BASE,'model_effective_reported':None}],RATES,'x')['records'][0]
        self.assertIsNone(x['model_estimate_usd'])
        self.assertEqual(x['model_identification'],'UNKNOWN')
    def test_missing_usage_no_zero(self):
        x=med.summary([{**BASE,'reported_usage':None}],RATES,'x')['records'][0]
        self.assertIsNone(x['input_tokens'])
        self.assertIsNone(x['total_estimate_usd'])
    def test_tool_cost_unknown_total_unknown(self):
        x=med.summary([{**BASE,'tool_cost_usd':None}],RATES,'x')['records'][0]
        self.assertIsNone(x['total_estimate_usd'])
        self.assertEqual(x['model_estimate_usd'],'0.0104')
    def test_cache_too_big(self):
        with self.assertRaises(ValueError): med.summary([{**BASE,'reported_usage': {'input_tokens': 100, 'cached_input_tokens': 101, 'output_tokens': 0}}],RATES,'x')
    def test_negative_tokens(self):
        with self.assertRaises(ValueError): med.summary([{**BASE,'reported_usage': {'input_tokens': -1, 'cached_input_tokens': 0, 'output_tokens': 0}}],RATES,'x')
    def test_boolean_tokens(self):
        with self.assertRaises(ValueError): med.summary([{**BASE,'reported_usage': {'input_tokens': True, 'cached_input_tokens': 0, 'output_tokens': 0}}],RATES,'x')
    def test_untrusted_reported_model(self):
        with self.assertRaises(ValueError): med.summary([{**BASE,'model_id_source':'chat_claim'}],RATES,'x')
    def test_deterministic_cannot_claim_tokens(self):
        with self.assertRaises(ValueError): med.summary([{**BASE,'kind':'deterministic'}],RATES,'x')
    def test_synthetic_flag_required(self):
        with self.assertRaises(ValueError): med.summary([BASE],{**RATES,'synthetic':False},'x')
    def test_missing_tariff(self):
        x=med.summary([BASE],{**RATES,'models':{}},'x')['records'][0]
        self.assertIsNone(x['model_estimate_usd'])
    def test_duplicate_ids(self):
        from tempfile import TemporaryDirectory
        with TemporaryDirectory() as d:
            p=Path(d)/'runs.jsonl'
            p.write_text('{"run_id":"a"}\n{"run_id":"a"}\n',encoding='utf-8')
            with self.assertRaises(ValueError): med.load_runs(p)

if __name__=='__main__': unittest.main()
