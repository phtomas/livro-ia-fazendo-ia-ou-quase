"""Microssemente RAG: testa apenas contas e fragmentação, sem LLM ou rede.
Material independente de apoio ao estudo. Requer Python >=3.9.
"""
from math import sqrt, isclose
import unittest

GOLD = {"q1": 0, "q2": 2, "q3": 3}
RANKED = {"q1": [0, 1, 3], "q2": [1, 2, 0], "q3": [1, 0, 2]}


def hit_at_k(gold, ranked, k):
    if k < 1 or not gold:
        raise ValueError("k deve ser positivo e gold não pode ser vazio")
    return sum(gold[q] in ranked[q][:k] for q in gold) / len(gold)


def mrr(gold, ranked):
    if not gold:
        raise ValueError("gold não pode ser vazio")
    return sum(1 / (ranked[q].index(gold[q]) + 1)
               if gold[q] in ranked[q] else 0
               for q in gold) / len(gold)


def cosine(a, b):
    if len(a) != len(b) or not a:
        raise ValueError("vetores devem ter mesmo comprimento não nulo")
    den = sqrt(sum(x*x for x in a)) * sqrt(sum(y*y for y in b))
    if den == 0:
        raise ValueError("cosseno indefinido para vetor zero")
    return sum(x*y for x, y in zip(a, b)) / den


def chunks(text, size=40, overlap=10):
    if not 0 <= overlap < size:
        raise ValueError("exige 0 <= overlap < size")
    result = []
    pos = 0
    while pos < len(text):
        result.append(text[pos:pos+size])
        pos += size-overlap
    return result


class VerificarExemplos(unittest.TestCase):
    def test_hit_at_3(self):
        self.assertTrue(isclose(hit_at_k(GOLD, RANKED, 3), 2/3))

    def test_mrr(self):
        self.assertTrue(isclose(mrr(GOLD, RANKED), 0.5))

    def test_cossenos_didaticos(self):
        q = [0.9, 0.1, 0.3]
        self.assertEqual(round(cosine(q, [0.8, 0.2, 0.35]), 3), 0.989)
        self.assertEqual(round(cosine(q, [0.1, 0.9, 0.2]), 3), 0.271)

    def test_fragmentacao_caracteres(self):
        txt = "Expense claims must be submitted within 30 days of purchase."
        self.assertEqual(chunks(txt), [
            "Expense claims must be submitted within ",
            "ed within 30 days of purchase.",
        ])

    def test_fragmentacao_invalida(self):
        with self.assertRaises(ValueError):
            chunks("texto", size=10, overlap=10)


if __name__ == "__main__":
    unittest.main(verbosity=2)
