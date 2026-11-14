import importlib.util
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('gera',ROOT/'scripts/gerar_blocos_docx.py')
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
class TestDefinicaoDeBlocos(unittest.TestCase):
 def test_cobertura_de_todos_os_21_capitulos(self):
  fs=[str(f.relative_to(ROOT)) for key in 'ABCDE' for f in mod.fontes(ROOT,key)]
  chapters=[p for p in fs if p.startswith('chapters/')]
  self.assertEqual(len(chapters),21)
  self.assertEqual(len(set(chapters)),21)
 def test_apresentacao_apenas_no_bloco_a(self):
  self.assertEqual(str(mod.fontes(ROOT,'A')[0].relative_to(ROOT)),'index.qmd')
  self.assertNotIn(ROOT/'index.qmd',[f for key in 'BCDE' for f in mod.fontes(ROOT,key)])
 def test_anexos_separados(self):
  self.assertEqual(len(mod.fontes(ROOT,'F')),3)
if __name__=='__main__':unittest.main()
