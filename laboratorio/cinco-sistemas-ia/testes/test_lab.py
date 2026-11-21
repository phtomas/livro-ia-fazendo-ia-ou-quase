import json
from pathlib import Path
import sys
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import lab

class Laboratorio(unittest.TestCase):
    def test_normalizacao_acentos(self): self.assertIn('reembolso',lab.palavras('REEMBOLSO, ação!'))
    def test_recuperacao_reembolso(self):self.assertEqual(lab.recuperar('prazo de reembolso')[0]['fonte'],'01-politica-reembolso.txt')
    def test_abstencao_sem_resultado(self):self.assertEqual(lab.responder_documento('quasar quarks nebula extraterrestre')['estado'],'SEM_EVIDENCIA')
    def test_fatura_campos(self):
        o=lab.extrair_fatura((lab.DADOS/'fatura-exemplo.txt').read_text(encoding='utf-8'))
        self.assertEqual(o['dados']['total_brl'],'1240.00')
        self.assertEqual(o['estado'],'VALIDADO_ESTRUTURALMENTE_PENDENTE_REVISAO_HUMANA')
    def test_fatura_incompleta(self): self.assertEqual(lab.extrair_fatura('Número: A')['estado'],'REVISAR')
    def test_fatura_imposto_invalido(self):
        t=(lab.DADOS/'fatura-exemplo.txt').read_text(encoding='utf-8').replace('R$ 99,20','R$ 9.999,20')
        self.assertEqual(lab.extrair_fatura(t)['estado'],'ERRO_VALIDACAO')
    def test_voz_nunca_efetiva_agendamento(self):
        o=lab.recepcionista_simulada('Quero marcar atendimento amanhã',True)
        self.assertFalse(o['efeito_externo'])
        self.assertEqual(o['intencao'],'agendamento')
    def test_pesquisa_detecta_diferenca(self):
        o=lab.comparar_fontes(json.loads((lab.DADOS/'fontes-pesquisa.json').read_text(encoding='utf-8')))
        self.assertEqual(o['estado'],'DIVERGENCIA_NUMERICA_PARA_REVISAO')
    def test_avaliacao_tres_casos(self):
        casos=json.loads((lab.DADOS/'casos-avaliacao.json').read_text(encoding='utf-8'))
        r=lab.avaliar_casos(casos)
        self.assertEqual(r['total'],3)
        self.assertEqual(r['aprovados'],3)
    def test_arquivo_sem_credenciais(self):
        self.assertNotIn('api_key', (lab.DADOS/'fatura-exemplo.txt').read_text(encoding='utf-8').lower())

if __name__=='__main__': unittest.main()
