import importlib.util,tempfile,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];spec=importlib.util.spec_from_file_location('edicao',ROOT/'tools/publicacao/inventariar_edicao.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
class ReleaseTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup);self.p=Path(self.tmp.name)
        (self.p/'chapters').mkdir();(self.p/'filters').mkdir()
        (self.p/'_quarto.yml').write_text('book:\n  chapters:\n    - index.qmd\n    - chapters/01-a.qmd\n',encoding='utf8')
        for name in ['index.qmd','chapters/01-a.qmd','references.bib','styles.css','pdf-preambulo.tex','filters/boxes.lua']:
            (self.p/name).write_text(name,encoding='utf8')
    def test_valid_source_still_waits_author(self):
        r=m.inspect(self.p,1);self.assertEqual(r['status'],'FONTE_INVENTARIADA');self.assertEqual(r['approval'],'PENDENTE_AUTOR')
    def test_count_rejected(self):self.assertIn('quantidade_inesperada_de_capitulos',m.inspect(self.p,2)['erros'])
    def test_missing_file(self):
        (self.p/'styles.css').unlink();self.assertIn('arquivo_ausente_ou_inseguro:styles.css',m.inspect(self.p)['erros'])
    def test_changed_file_changes_fingerprint(self):
        x=m.inspect(self.p)['fingerprint_sha256'];(self.p/'index.qmd').write_text('novo');self.assertNotEqual(m.inspect(self.p)['fingerprint_sha256'],x)
    def test_repeatable_fingerprint(self):self.assertEqual(m.inspect(self.p)['fingerprint_sha256'],m.inspect(self.p)['fingerprint_sha256'])
    def test_wrong_order(self):
        (self.p/'_quarto.yml').write_text('book:\n  chapters:\n    - index.qmd\n    - chapters/02-a.qmd\n')
        self.assertIn('ordem_capitulos_incorreta',m.inspect(self.p)['erros'])
    def test_duplicate_entry(self):
        (self.p/'_quarto.yml').write_text('book:\n  chapters:\n    - index.qmd\n    - index.qmd\n    - chapters/01-a.qmd\n')
        self.assertIn('arquivo_repetido_na_configuracao',m.inspect(self.p)['erros'])
if __name__=='__main__':unittest.main()
