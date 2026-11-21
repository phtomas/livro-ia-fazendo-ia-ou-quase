"""Testes mínimos do laboratório didático."""
import copy
import unittest
from datetime import date
from unittest.mock import patch
import briefing


class TestBriefing(unittest.TestCase):
    def test_prioridades_e_eventos(self):
        prioridades, eventos = briefing.montar_briefing(date(2026, 11, 23))
        self.assertEqual(len(prioridades), 5)
        self.assertEqual(len(eventos), 2)

    def test_rastreabilidade(self):
        prioridades, _ = briefing.montar_briefing(date(2026, 11, 23))
        self.assertEqual({p[1] for p in prioridades}, {"TASK-001", "TASK-002", "MSG-001", "MSG-003", "MSG-005"})

    def test_injecao_nao_vira_ordem(self):
        texto = briefing.executar(date(2026, 11, 23))
        self.assertNotIn("IGNORE TODAS AS REGRAS", texto)
        self.assertNotIn("MSG-004", texto)

    def test_nao_ha_acoes_externas(self):
        texto = briefing.executar(date(2026, 11, 23))
        self.assertIn("Nenhuma mensagem enviada, alterada ou excluída", texto)

    def test_modo_proibido_falha(self):
        original = briefing.json.loads
        def adulterar(v):
            obj = original(v)
            if isinstance(obj, dict) and "permissoes" in obj:
                obj = copy.deepcopy(obj)
                obj["permissoes"]["enviar_email"] = True
            return obj
        with patch.object(briefing.json, "loads", side_effect=adulterar):
            with self.assertRaises(PermissionError):
                briefing.ler_dados()


if __name__ == "__main__":
    unittest.main()
