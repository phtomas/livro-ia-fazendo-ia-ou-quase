"""Testes do executor, sem contas, segredos ou IA remota."""
from pathlib import Path
import tempfile
import unittest
import sys

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
from executar import MANUAIS, TITULOS, ensaio

class KitTests(unittest.TestCase):
    def test_todos_os_capitulos_tem_modo(self):
        self.assertEqual(set(TITULOS), set(range(1,22)))
        self.assertTrue(MANUAIS.issubset(set(TITULOS)))

    def test_roteiros_sem_ia_nao_recebem_pass(self):
        with tempfile.TemporaryDirectory() as tmp:
            for n in MANUAIS:
                with self.subTest(capitulo=n):
                    result = ensaio(n, Path(tmp) / str(n))
                    self.assertEqual(result["estado"], "NAO_VERIFICADO")
                    self.assertEqual(result["chamadas_llm"], 0)
                    self.assertTrue((Path(tmp)/str(n)/"REGISTRO_MANUAL.md").is_file())

    def test_ensaios_python_e_falhas_esperadas(self):
        with tempfile.TemporaryDirectory() as tmp:
            for n in sorted(set(TITULOS)-MANUAIS):
                with self.subTest(capitulo=n):
                    result = ensaio(n, Path(tmp) / str(n))
                    self.assertEqual(result["estado"], "PASS_LIMITED",
                                     msg=str([(s["etapa"],s["codigo_observado"],
                                               s["saida_esperada"]) for s in result["etapas"]]))
                    self.assertFalse(result["publicacao"])
                    self.assertFalse(result["edicao_manuscrito"])
                    self.assertTrue((Path(tmp)/str(n)/"resultado.json").is_file())

    def test_nao_sobrescreve_relatorio_existente(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "01"
            ensaio(1, target)
            with self.assertRaises(FileExistsError):
                ensaio(1, target)

if __name__ == "__main__":
    unittest.main()
