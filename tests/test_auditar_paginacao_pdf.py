import importlib.util
import tempfile
import unittest
from pathlib import Path
import fitz

ROOT=Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location('audit_pag', ROOT/'tools/editorial/auditar_paginacao_pdf.py')
mod=importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(mod)

class TestPaginasCurtas(unittest.TestCase):
    def criar(self, textos):
        temp=tempfile.TemporaryDirectory()
        dest=Path(temp.name)/'livro.pdf'
        d=fitz.open()
        for t in textos:
            p=d.new_page();p.insert_text((60,75),t)
        d.save(dest);d.close()
        self.addCleanup(temp.cleanup)
        return dest

    def test_reconhece_fim_curto_seguido_de_novo_capitulo(self):
        p=self.criar(['Capitulo 1\nConteudo', 'Restaram apenas duas linhas', 'Capitulo 2\nComeco'])
        r=mod.auditar(p)
        self.assertEqual(r['total_candidatos'],1)
        self.assertEqual(r['candidatos'][0]['pagina_fisica'],2)

    def test_nunca_trata_capa_curta_como_orfa(self):
        p=self.criar(['Titulo da obra', 'Capitulo 1\nComeco'])
        r=mod.auditar(p)
        self.assertEqual(r['total_candidatos'],1) # capa curta também é candidata: requer contexto humano
        self.assertEqual(r['candidatos'][0]['estado'],'SUSPEITA_REQUER_INSPECAO_VISUAL')

    def test_sem_abertura_na_seguinte_nao_sinaliza(self):
        p=self.criar(['Algumas palavras','Outro paragrafo'])
        self.assertEqual(mod.auditar(p)['total_candidatos'],0)

    def test_parametro_invalido(self):
        p=self.criar(['Texto'])
        with self.assertRaises(ValueError):mod.auditar(p,0)

if __name__=='__main__':unittest.main()
