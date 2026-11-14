import hashlib, importlib.util, json, tempfile, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
s=importlib.util.spec_from_file_location('verificar_evidencias',ROOT/'tools/hardware/verificar_evidencias.py')
m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
class EvidenceTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.dir=Path(self.tmp.name)
        (self.dir/'f.txt').write_text('Fonte hipotética',encoding='utf8')
        self.ev={'arquivo':'f.txt','tipo':'documento','revisao':'SIM-1','sha256':m.digest(self.dir/'f.txt')}
        self.item={'id':'E1','texto':'Uma hipótese','nivel':'documental','revisao':'SIM-1','evidencias':[self.ev]}
    def run_case(self,items):
        p=self.dir/'manifesto.json';p.write_text(json.dumps({'afirmacoes':items}),encoding='utf8');return m.validate(p)
    def test_valid_documentary_source(self):self.assertEqual(self.run_case([self.item])['status'],'PASS_RASTREABILIDADE')
    def test_no_measured_evidence_cannot_claim_physical(self):
        x={**self.item,'nivel':'fisico'};r=self.run_case([x]);self.assertIn('falta_prova_fisica',r['afirmacoes'][0]['erros'])
    def test_revision_mismatch(self):
        x={**self.item,'revisao':'SIM-2'};self.assertIn('revisao_divergente',self.run_case([x])['afirmacoes'][0]['erros'])
    def test_wrong_hash(self):
        x={**self.item,'evidencias':[{**self.ev,'sha256':'0'*64}]};self.assertIn('hash_divergente',self.run_case([x])['afirmacoes'][0]['erros'])
    def test_traversal_denied(self):
        x={**self.item,'evidencias':[{**self.ev,'arquivo':'../secret.txt'}]};self.assertIn('caminho_inseguro',self.run_case([x])['afirmacoes'][0]['erros'])
    def test_duplicate_id(self):self.assertIn('id_ausente_ou_repetido',self.run_case([self.item,self.item])['afirmacoes'][1]['erros'])
    def test_missing_file(self):
        x={**self.item,'evidencias':[{**self.ev,'arquivo':'nada.txt'}]};self.assertIn('arquivo_ausente_ou_inseguro',self.run_case([x])['afirmacoes'][0]['erros'])
    def test_physical_evidence_traceable_not_true(self):
        x={**self.item,'nivel':'fisico','evidencias':[{**self.ev,'tipo':'medicao'}]};r=self.run_case([x]);self.assertEqual(r['status'],'PASS_RASTREABILIDADE');self.assertIn('NÃO valida',r['aviso'])
if __name__=='__main__':unittest.main()
