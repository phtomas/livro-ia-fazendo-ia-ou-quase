import importlib.util,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];s=importlib.util.spec_from_file_location('adaptador',ROOT/'tools/portabilidade/auditar_adaptador.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
class AdapterTests(unittest.TestCase):
    def setUp(self):self.contract={'capacidades_obrigatorias':['ler','testar']}
    def t(self,cap):return m.evaluate(self.contract,{'nome':'sintetico','capacidades':cap})
    def test_complete_declared(self):self.assertEqual(self.t({'ler':True,'testar':True})['status'],'COMPATIVEL_DECLARADO')
    def test_missing_capability_blocks(self):self.assertEqual(self.t({'ler':True,'testar':False})['status'],'BLOQUEADO_POR_CAPACIDADE')
    def test_unknown_not_pass(self):self.assertEqual(self.t({'ler':True,'testar':None})['status'],'INDETERMINADO')
    def test_omitted_unknown(self):self.assertEqual(self.t({'ler':True})['status'],'INDETERMINADO')
    def test_false_overrides_unknown(self):
        r=self.t({'ler':False});self.assertEqual(r['status'],'BLOQUEADO_POR_CAPACIDADE');self.assertEqual(r['recursos_desconhecidos'],['testar'])
    def test_invalid_value(self):
        with self.assertRaises(ValueError):self.t({'ler':'sim','testar':True})
    def test_invalid_contract(self):
        self.contract['capacidades_obrigatorias']=['ler','ler']
        with self.assertRaises(ValueError):self.t({'ler':True})
if __name__=='__main__':unittest.main()
