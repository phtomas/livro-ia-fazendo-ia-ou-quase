import importlib.util
import unittest
from pathlib import Path
R=Path(__file__).resolve().parents[1]
S=importlib.util.spec_from_file_location('aval',R/'tools/editorial/avaliar_proposta.py')
mod=importlib.util.module_from_spec(S);S.loader.exec_module(mod)

class EvaluateTests(unittest.TestCase):
    def test_simple_rewrite(self):
        r=mod.evaluate('A tensão foi 5V.','Medimos uma tensão de 5V.')
        self.assertEqual(r['status'],'PASS_LIMITED')
        self.assertTrue(r['changed'])
    def test_numeric_change(self):
        r=mod.evaluate('Medimos 5V e 12V.','Medimos 6V e 12V.')
        self.assertEqual(r['status'],'FAIL_GUARDRAIL')
        self.assertIn('5V',r['removed_numeric_tokens'])
    def test_locked_phrase_missing(self):
        r=mod.evaluate('Não alterar uma hipótese pendente.','Hipótese comprovada.', ['hipótese pendente'])
        self.assertEqual(r['status'],'FAIL_GUARDRAIL')
    def test_invalid_guard(self):
        r=mod.evaluate('Olhe o vídeo.','Veja o vídeo.', ['inexistente'])
        self.assertEqual(r['status'],'FAIL_GUARDRAIL')
    def test_equal_does_not_mean_approved(self):
        r=mod.evaluate('12V','12V')
        self.assertEqual(r['status'],'PASS_LIMITED')
        self.assertFalse(r['can_publish'])
if __name__=='__main__':unittest.main()
