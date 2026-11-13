from pathlib import Path
import importlib.util
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('copia_provada',ROOT/'tools/arquivos/copia_provada.py')
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)

class TestCopy(unittest.TestCase):
    def test_dry_run_then_copy(self):
        with tempfile.TemporaryDirectory() as tmp:
            t=Path(tmp);src=t/'src';dst=t/'dst';src.mkdir();(src/'a.txt').write_text('conteúdo','utf-8');(src/'b.bin').write_bytes(b'\x00\x01')
            a=mod.run(src,dst,False)
            self.assertEqual(a['status'],'DRY_RUN');self.assertFalse(dst.exists())
            b=mod.run(src,dst,True)
            self.assertEqual(b['status'],'PASS_COPY');self.assertEqual(b['qtd'],2)
            self.assertEqual((dst/'a.txt').read_text(),'conteúdo')
            self.assertEqual(mod.digest(src/'b.bin'),mod.digest(dst/'b.bin'))

    def test_no_overwrite(self):
        with tempfile.TemporaryDirectory() as tmp:
            t=Path(tmp);src=t/'src';dst=t/'dst';src.mkdir();dst.mkdir()
            (src/'a.txt').write_text('A');(dst/'a.txt').write_text('B')
            with self.assertRaises(ValueError):mod.run(src,dst,True)
            self.assertEqual((dst/'a.txt').read_text(),'B')

    def test_refuse_nested_destination(self):
        with tempfile.TemporaryDirectory() as tmp:
            t=Path(tmp);src=t/'src';src.mkdir();(src/'a.txt').write_text('A')
            with self.assertRaises(ValueError):mod.run(src,src/'out',True)

if __name__=='__main__': unittest.main()
