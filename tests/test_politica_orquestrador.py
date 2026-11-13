import importlib.util
from pathlib import Path
import unittest
S=Path(__file__).resolve().parents[1]/'agents/politica_orquestrador.py'
spec=importlib.util.spec_from_file_location('politica_orquestrador',S)
mod=importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

class PolicyTest(unittest.TestCase):
    def test_read_only(self):
        self.assertEqual(mod.decide('CHECK_STRUCTURE')['decision'],'ALLOW_READ_ONLY')
    def test_publish_requires_human(self):
        self.assertEqual(mod.decide('PUBLISH')['decision'],'REQUIRE_HUMAN_APPROVAL')
    def test_unknown_denied(self):
        self.assertEqual(mod.decide('RUN_SOMETHING_WEIRD')['decision'],'DENY_UNKNOWN_ACTION')
    def test_secret_denied(self):
        self.assertEqual(mod.decide('ACCESS_SECRET')['decision'],'DENY')
    def test_no_execution(self):
        self.assertFalse(mod.decide('MODIFY_MANUSCRIPT')['is_executed'])

if __name__=='__main__':unittest.main()
