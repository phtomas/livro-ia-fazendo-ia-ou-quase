import json
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch
import lab

DADOS = json.loads((Path(lab.__file__).parent / 'dados/politicas.json').read_text())


class TestOficina(unittest.TestCase):
    def test_vigente(self):
        self.assertEqual(lab.recuperar(DADOS)['id'], 'POL-003')
        self.assertEqual(lab.recuperar(DADOS)['prazo_dias'], 45)

    def test_sem_vigente(self):
        with self.assertRaises(ValueError):
            lab.recuperar([DADOS[0]])

    def test_conflito(self):
        with self.assertRaises(ValueError):
            lab.recuperar([DADOS[1], DADOS[1]])

    def test_prazo_invalido(self):
        with self.assertRaises(ValueError):
            lab.recuperar([dict(DADOS[1], prazo_dias=True)])

    def test_payload(self):
        p = lab.montar_payload(lab.recuperar(DADOS))
        self.assertEqual(p['model'], lab.MODELO)
        self.assertFalse(p['stream'])
        self.assertIn('POL-003', p['messages'][1]['content'])
        self.assertNotIn('POL-002', p['messages'][1]['content'])

    def test_api_simulada(self):
        resp = MagicMock()
        resp.__enter__.return_value.read.return_value = json.dumps({
            'done': True, 'message': {'content': '45 dias [POL-003]'}
        }).encode()
        with patch.object(lab, 'build_opener') as build:
            build.return_value.open.return_value = resp
            saida = lab.consultar(lab.montar_payload(DADOS[1]))
            req = build.return_value.open.call_args.args[0]
            self.assertEqual(req.full_url, 'http://127.0.0.1:11434/api/chat')
            self.assertEqual(req.get_method(), 'POST')
            self.assertEqual(build.call_args.args[0].proxies, {})
            self.assertEqual(saida, '45 dias [POL-003]')

    def test_redirecionamento_bloqueado(self):
        self.assertIsNone(lab.SemRedirecionamento().redirect_request(
            None, None, 302, '', {}, 'https://example.invalid/'))


if __name__ == '__main__':
    unittest.main()
