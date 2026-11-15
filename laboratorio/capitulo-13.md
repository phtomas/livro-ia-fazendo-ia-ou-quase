# Capítulo 13 — A ferramenta que não precisa de opinião

## LAB-13A: comparação de dois arquivos sem IA

**Status:** roteiro publicado; comprovação em seu próprio ambiente é parte do exercício. Atualizado em 14/11/2026.

**Objetivo:** comparar dois arquivos reais utilizando uma operação determinística, em vez de pedir que um modelo de linguagem adivinhe se são iguais.

**Requisitos:** Python 3.9+ instalado (sem bibliotecas externas); Windows, Linux ou macOS; arquivos descartáveis.

**Prepare:** na pasta `laboratorio-ia`, crie `entrada/original.txt` e `entrada/copia.txt` contendo a mesma frase. Baixe [comparar_arquivos.py](../scripts/comparar_arquivos.py) para a raiz de `laboratorio-ia`.

**Windows / PowerShell:**

```powershell
py comparar_arquivos.py entrada/original.txt entrada/copia.txt
```

**Linux / macOS:**

```bash
python3 comparar_arquivos.py entrada/original.txt entrada/copia.txt
```

**Teste:** arquivos iguais produzem `PASS: arquivos identicos` e código de saída 0. Altere um arquivo: o resultado deve ser `FAIL: arquivos diferentes`, código 1. Remova um arquivo: `ERRO`, código 2. Registre comandos e saídas em `evidencias`.

**Limites:** comparar hashes SHA-256 reduz enormemente o risco de colisão acidental, mas para uma garantia de igualdade byte a byte em contextos adversariais pode-se fazer a comparação direta do conteúdo. Não compartilhe arquivos pessoais.

**Limpeza:** remova a pasta fictícia ao terminar. Se Python não for encontrado, confira instalação e variável de ambiente. Nenhuma chamada de IA ou API é necessária.
