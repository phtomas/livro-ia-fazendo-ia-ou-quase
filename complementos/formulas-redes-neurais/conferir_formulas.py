"""Exemplos numéricos das nove fórmulas — apenas biblioteca padrão Python.
Execute: python conferir_formulas.py
"""
import math

def proximo(a, b, tol=1e-9):
    assert math.isclose(a, b, rel_tol=tol, abs_tol=tol), f"{a} != {b}"

# 1. Neurônio
x, w, b = 2.0, 0.5, 0.0
z = w * x + b
proximo(z, 1.0)

# 2. Ativações
relu = lambda t: max(0.0, t)
sigmoid = lambda t: 1.0 / (1.0 + math.exp(-t))
proximo(relu(-2), 0)
proximo(relu(3), 3)
proximo(sigmoid(0), 0.5)
proximo(math.tanh(0), 0.0)

# 3. Camada com duas entradas e duas saídas (W: 2x2, b: 2)
entrada = [2.0, 1.0]
matriz = [[0.5, 0.2], [-0.5, 1.0]]
vieses = [0.0, 0.1]
saida = [relu(sum(a * v for a, v in zip(linha, entrada)) + bias)
         for linha, bias in zip(matriz, vieses)]
proximo(saida[0], 1.2)
proximo(saida[1], 0.1)

# 4. Perda MSE e entropia cruzada categórica
reais = [1.0, 2.0]
previstos = [1.5, 1.0]
mse = sum((p - y) ** 2 for p, y in zip(previstos, reais)) / len(reais)
proximo(mse, 0.625)
scores = [2.0, 1.0, 0.0]
deslocamento = max(scores)
expo = [math.exp(v - deslocamento) for v in scores]
prob = [v / sum(expo) for v in expo]
ce = -math.log(prob[0])
proximo(ce, math.log(1 + math.exp(-1) + math.exp(-2)))

# 5. Retropropagação: L = 1/2*(a-y)^2, ativação identidade
alvo = 0.0
a = z
dL_da = a - alvo
da_dz = 1.0
dL_dz = dL_da * da_dz
dL_dw = dL_dz * x
dL_db = dL_dz
proximo(dL_dw, 2.0)
proximo(dL_db, 1.0)

# 6. Atualização
eta = 0.1
novo_w, novo_b = w - eta * dL_dw, b - eta * dL_db
proximo(novo_w, 0.3)
proximo(novo_b, -0.1)
l_inicial = 0.5 * (a - alvo)**2
l_nova = 0.5 * ((novo_w * x + novo_b) - alvo)**2
proximo(l_inicial, 0.5)
proximo(l_nova, 0.125)
assert l_nova < l_inicial

# 7. Regularização: L_total = L_dados + lambda * w**2
lam = 0.01
proximo(l_inicial + lam*w*w, 0.5025)

# 8. Softmax
proximo(sum(prob), 1.0)
assert prob[0] > prob[1] > prob[2]

# 9. Fluxo: um passo reduziu a perda no exemplo
print("PASS — 9 conceitos ilustrados; contas verificadas.")
print(f"Exemplo de gradiente: w {w:.1f} -> {novo_w:.1f}, b {b:.1f} -> {novo_b:.1f}")
print(f"Perda (meio erro quadrático): {l_inicial:.3f} -> {l_nova:.3f}")
print("Softmax para [2,1,0]:", [round(v, 3) for v in prob])
print("MSE de [1.5,1] frente a [1,2]:", mse)
