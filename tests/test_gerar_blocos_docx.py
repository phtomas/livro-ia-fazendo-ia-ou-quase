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
 def test_numeracao_global_dos_blocos(self):
  self.assertEqual([mod.NUMBER_OFFSETS[x] for x in 'ABCDE'],[0,4,8,12,16])
  for key in 'BCDE':
   sources=mod.fontes(ROOT,key)
   first=int(sources[0].stem[:2])
   self.assertEqual(first,mod.NUMBER_OFFSETS[key]+1)
 def test_patch_offset_word(self):
  from tempfile import TemporaryDirectory
  from docx import Document
  from docx.enum.style import WD_STYLE_TYPE
  with TemporaryDirectory() as temp:
   f=Path(temp)/'bloco.docx';d=Document()
   if 'Section Number' not in d.styles:d.styles.add_style('Section Number',WD_STYLE_TYPE.CHARACTER)
   from docx.oxml.ns import qn
   a=d.add_paragraph(style='Heading 1');a.add_run('1').style='Section Number';a.runs[0]._r.rPr.rStyle.val='SectionNumber';a.add_run('\tTítulo')
   b=d.add_paragraph(style='Heading 2');b.add_run('1.2').style='Section Number';b.runs[0]._r.rPr.rStyle.val='SectionNumber';b.add_run('\tSubseção')
   d.save(f)
   mod.ajustar_numeracao_word(f,'B')
   result=Document(f)
   self.assertEqual(result.paragraphs[0].text,'5\tTítulo')
   self.assertEqual(result.paragraphs[1].text,'5.2\tSubseção')
 def test_anexos_separados(self):
  self.assertEqual(len(mod.fontes(ROOT,'F')),3)
if __name__=='__main__':unittest.main()
