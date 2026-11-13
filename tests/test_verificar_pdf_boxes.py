"""Testes unitários sem LLM e sem rede.

Uso: python -m unittest discover -s tests -p 'test_*.py' -v
"""
from pathlib import Path
import importlib.util
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('verificar_pdf_boxes',ROOT/'tools/editorial/verificar_pdf_boxes.py')
mod=importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

class TestPageBoxes(unittest.TestCase):
    def test_clean_page(self):
        import fitz
        with tempfile.TemporaryDirectory() as td:
            path=Path(td)/'good.pdf'
            doc=fitz.open();page=doc.new_page(width=453.54,height=651.97)
            page.draw_rect(fitz.Rect(65,75,393,300),color=(.9,.9,.9),fill=(.95,.97,.98))
            page.insert_text((100,115),'print("PASS")',fontname='cour',fontsize=10)
            doc.save(path);doc.close()
            r=mod.inspect(path)
            self.assertEqual(r['issue_count'],0)
            self.assertGreater(r['light_boxes_inspected'],0)
            self.assertEqual(r['status'],'PASS_LIMITED')

    def test_overflow_page(self):
        import fitz
        with tempfile.TemporaryDirectory() as td:
            path=Path(td)/'bad.pdf'
            doc=fitz.open();page=doc.new_page(width=453.54,height=651.97)
            page.draw_rect(fitz.Rect(65,75,393,300),color=(.9,.9,.9),fill=(.95,.97,.98))
            page.insert_text((100,115),'print("' + 'x'*80 + '")',fontname='cour',fontsize=10)
            doc.save(path);doc.close()
            r=mod.inspect(path)
            self.assertGreater(r['issue_count'],0)
            self.assertEqual(r['status'],'FAIL')

if __name__ == '__main__':unittest.main()
