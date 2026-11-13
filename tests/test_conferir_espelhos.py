import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

SCRIPT=Path(__file__).resolve().parents[1]/'tools/sync/conferir_espelhos.py'
s=importlib.util.spec_from_file_location('espelhos',SCRIPT)
mod=importlib.util.module_from_spec(s)
s.loader.exec_module(mod)
class TestarEspelhos(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.base=Path(self.tmp.name)
        self.a=self.base/'canonical'; self.b=self.base/'drive';self.a.mkdir();self.b.mkdir()
        (self.a/'texto.qmd').write_text('capítulo',encoding='utf8')
        (self.b/'texto.qmd').write_text('capítulo',encoding='utf8')
        self.report=self.base/'comparacao.json'
        self.snapshot=self.base/'baseline.json'
    def run_cmp(self, baseline=False):
        cmd=['--canon',str(self.a),'--espelho',str(self.b),'--report',str(self.report)]
        if baseline: cmd+=['--baseline',str(self.snapshot)]
        return mod.main(cmd)
    def create_baseline(self):
        self.assertEqual(mod.main(['--canon',str(self.a),'--snapshot',str(self.snapshot)]),0)
    def test_iguais_pass(self):
        self.assertEqual(self.run_cmp(),0)
        self.assertEqual(json.loads(self.report.read_text())['pendencias'],0)
    def test_divergencia_bilateral(self):
        (self.b/'texto.qmd').write_text('novo',encoding='utf8')
        self.assertEqual(self.run_cmp(),1)
        self.assertEqual(json.loads(self.report.read_text())['itens'][0]['estado'],'DIVERGENTE')
    def test_novo_so_de_um_lado(self):
        (self.a/'outro.txt').write_text('ok')
        self.assertEqual(self.run_cmp(),1)
        self.assertIn('APENAS_CANON',[x['estado'] for x in json.loads(self.report.read_text())['itens']])
    def test_linha_base_de_direcao(self):
        self.create_baseline()
        (self.b/'texto.qmd').write_text('edição local',encoding='utf8')
        self.assertEqual(self.run_cmp(True),1)
        self.assertEqual(json.loads(self.report.read_text())['itens'][0]['estado'],'ALTERADO_ESPELHO')
    def test_conflito_nao_resolvido_automaticamente(self):
        self.create_baseline()
        (self.a/'texto.qmd').write_text('edicao github',encoding='utf8')
        (self.b/'texto.qmd').write_text('edicao drive',encoding='utf8')
        self.assertEqual(self.run_cmp(True),1)
        self.assertEqual(json.loads(self.report.read_text())['itens'][0]['estado'],'CONFLITO_OU_DUAS_MUDANCAS')
        self.assertEqual((self.b/'texto.qmd').read_text(),'edicao drive')
    def test_diretorios_ignorados(self):
        (self.a/'_book').mkdir();(self.a/'_book'/'index.html').write_text('html')
        (self.a/'__pycache__').mkdir();(self.a/'__pycache__'/'x.pyc').write_bytes(b'abc')
        self.assertEqual(self.run_cmp(),0)
    def test_symlink_recusado(self):
        try: (self.a/'link.txt').symlink_to(self.a/'texto.qmd')
        except (OSError,NotImplementedError): self.skipTest('symlink não disponível')
        self.assertEqual(self.run_cmp(),2)
    def test_nao_gravar_dentro_das_arvores(self):
        self.assertEqual(mod.main(['--canon',str(self.a),'--espelho',str(self.b),'--report',str(self.a/'x.json')]),2)
        self.assertFalse((self.a/'x.json').exists())
    def test_snapshot_proibido_de_editar_origem(self):
        self.create_baseline()
        self.assertTrue(self.snapshot.exists())
        self.assertEqual((self.a/'texto.qmd').read_text(),'capítulo')
    def test_manifesto_malicioso_recusado(self):
        self.snapshot.write_text(json.dumps({'formato':'espelhos-v1','arquivos':{'../x':'0'*64}}))
        self.assertEqual(self.run_cmp(True),2)
if __name__=='__main__': unittest.main()
