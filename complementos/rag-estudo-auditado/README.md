# RAG — estudo auditado e verificações práticas

**Complemento independente do livro _IA fazendo IA — ou quase_ · José Albuquerque.**  
**Revisão:** 23/11/2026. **Origem motivadora:** Ali Data Analytics, _RAG (Retrieval-Augmented Generation) – Complete Developer Study Notes_, 18 páginas.

[Leitura em português](index.html) · [Auditoria das afirmações](AUDITORIA.md) · [Fontes com limitações](REFERENCIAS.md) · [Código verificável](verificar_exemplos.py)

## Para que serve

O leitor recebeu um conjunto de 18 páginas sobre RAG. Em vez de republicar a obra de terceiro ou reproduzir seus diagramas e tabelas, este complemento reúne uma **avaliação editorial própria** sobre precisão técnica, riscos de generalização, testes reproduzíveis e caminhos para o conteúdo que já existe no portal.

**Não duplicamos:**
- [Arquitetura RAG — duas trilhas](../rag-pipeline/index.html): visão de indexação, consulta e fontes.
- [LAB-RAG-01](../../laboratorio/rag-pratico/index.html): código principal com SQLite FTS5/BM25, Ollama opcional e ensaio de busca.
- [Estudo auditado de LLMs](../estudo-auditado-llms/index.html): princípios gerais de linguagem, contexto e riscos.
- [Cinco sistemas de IA](../cinco-sistemas-ia/index.html): casos de uso práticos.

**Acrescentamos:** correções e nuances rastreadas por página do material motivador, critérios de avaliação por componente, cinco testes de aritmética e pré-processamento sem dependências, checklist de implantação e matriz de evidências.

## Executar a verificação numérica

Requer somente Python 3.9+:

```sh
python complementos/rag-estudo-auditado/verificar_exemplos.py
```

**Resultado registrado na preparação:** cinco testes PASS, incluindo Hit@3 = 2/3, MRR = 0,5 e similaridades de cosseno arredondadas para 0,989 e 0,271. Essas provas verificam apenas os exemplos didáticos, **não** desempenho de um RAG em produção.

## Direitos, atribuição e limites

O material externo foi enviado pelo leitor como imagens. É identificado como **Ali Data Analytics**, 18 páginas. Não foi disponibilizado um URL oficial de origem ou licença autorizando redistribuição integral ou tradução pública. Por isso, **os 18 slides, o PDF original e a tradução integral não estão neste repositório**. Créditos preservados na publicação crítica e no arquivo [REFERENCIAS.md](REFERENCIAS.md). A edição privada do usuário não se confunde com a publicação autoral disponível aqui.

Não inclui topologia, nomes de máquinas, endereços, dados internos, PDFs privados nem credenciais do usuário.
