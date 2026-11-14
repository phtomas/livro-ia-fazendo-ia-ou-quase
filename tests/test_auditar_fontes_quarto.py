from pathlib import Path
import importlib.util
import tempfile
import unittest
ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('auditar_fontes_quarto',ROOT/'tools/editorial/auditar_fontes_quarto.py')
MOD=importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)

class TestSourceAudit(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name)
        (self.root/'_quarto.yml').write_text('project: book\n',encoding='utf-8')
        (self.root/'chapters').mkdir()
        (self.root/'appendices').mkdir()
        (self.root/'index.qmd').write_text('# Índice\n',encoding='utf-8')

    def test_empty_project_is_limited_not_editorially_approved(self):
        result=MOD.audit(self.root)
        self.assertEqual(result['status'],'PASS_LIMITED')
        self.assertEqual(result['errors'],0)

    def test_missing_image_detected(self):
        (self.root/'chapters'/'01-x.qmd').write_text('# A\n![Esquema](nao_existe.png)\n',encoding='utf-8')
        result=MOD.audit(self.root)
        self.assertIn('MISSING_LOCAL_IMAGE',[x['code'] for x in result['issues']])
        self.assertEqual(result['status'],'FAIL')

    def test_existing_image_not_missing(self):
        (self.root/'chapters'/'x.png').write_bytes(b'png placeholder')
        (self.root/'chapters'/'01-x.qmd').write_text('# A\n![Desenho](x.png)\n',encoding='utf-8')
        self.assertEqual(MOD.audit(self.root)['errors'],0)

    def test_duplicate_id_detected(self):
        (self.root/'chapters'/'01-x.qmd').write_text('## A {#sec-abc}\n## B {#sec-abc}\n',encoding='utf-8')
        self.assertIn('DUPLICATE_REFERENCE_ID',[x['code'] for x in MOD.audit(self.root)['issues']])

    def test_long_code_is_warning_not_proof_of_pdf_cut(self):
        (self.root/'chapters'/'01-x.qmd').write_text('```python\n'+('x'*101)+'\n```\n',encoding='utf-8')
        x=MOD.audit(self.root,max_code_chars=94)
        self.assertEqual(x['status'],'PASS_LIMITED')
        self.assertIn('LONG_CODE_LINE',[y['code'] for y in x['issues']])

    def test_code_links_are_not_prose_links(self):
        (self.root/'chapters'/'01-x.qmd').write_text('```text\n![X](missing.png)\n```\n',encoding='utf-8')
        self.assertEqual(MOD.audit(self.root)['errors'],0)

    def test_outside_project_link_rejected(self):
        (self.root/'chapters'/'01-x.qmd').write_text('[segredo](../../segredo.txt)\n',encoding='utf-8')
        self.assertIn('OUTSIDE_PROJECT',[y['code'] for y in MOD.audit(self.root)['issues']])

if __name__ == '__main__':
    unittest.main()
