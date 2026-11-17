# Arquitetura de um pipeline RAG — dois fluxos

Complemento técnico visual do livro **IA fazendo IA — ou quase**, de José Albuquerque.

[Diagrama vetorial original](arquitetura-rag-duas-trilhas.svg) · [Página ilustrada](index.html) · [Galeria de complementos](../index.html)

## O que é RAG?

*Retrieval-Augmented Generation* (geração aumentada por recuperação) é um arranjo em que informações recuperadas de fontes externas são fornecidas ao modelo para apoiar a geração de uma resposta. A qualidade depende não só do LLM, mas da recuperação, atualidade, controle de acesso, construção do contexto e avaliação.

## Duas trilhas diferentes

**A — Preparação do conhecimento (ingestão/indexação):**
1. Coletar conteúdo de documentos, páginas e fontes autorizadas.
2. Extrair, normalizar e limpar o conteúdo.
3. Organizar trechos (*chunks*) e metadados; a fragmentação é frequente, mas depende da natureza da fonte.
4. Criar um índice de recuperação lexical (por exemplo, BM25), vetorial (com embeddings), ou híbrido.
5. Atualizar e controlar o índice, mantendo origem, permissões e informações sobre versões.

**B — Pergunta e geração (tempo de consulta):**
1. Receber a pergunta do usuário.
2. Opcionalmente reformular/expandir a consulta ou empregar HyDE; calcular embedding da consulta se a recuperação exigir.
3. Recuperar candidatos relevantes no índice construído na trilha A.
4. Filtrar e, opcionalmente, reranquear candidatos.
5. Montar o prompt com pergunta, instruções e trechos recuperados, preservando fontes.
6. Solicitar a geração ao LLM.
7. Entregar resposta fundamentada, com referências verificáveis quando disponíveis, e indicar insuficiência de evidência quando necessário.

### Diferenças importantes

- **BM25:** técnica de busca lexical. Não exige embeddings.
- **Embeddings:** representações vetoriais úteis à recuperação semântica; são uma possibilidade, não uma obrigação de todo RAG.
- **Reranker:** reordena ou filtra resultados já recuperados.
- **HyDE (*Hypothetical Document Embeddings*):** formula informação hipotética para apoiar a recuperação; não é, por definição, reranqueamento.
- **Banco vetorial:** uma opção de infraestrutura para buscas vetoriais; não é sinônimo de RAG.
- **Avaliação e guardrails:** controles aplicáveis ao processo inteiro, não simplesmente uma etapa posterior à geração.
- **Fontes:** citar documentos não garante, por si só, que a interpretação esteja correta; é preciso conferir os trechos e as permissões.

## Fontes de apoio técnico

- [Microsoft — conceitos de RAG e recuperação](https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview)
- [LlamaIndex — conceitos de ingestão e consulta](https://docs.llamaindex.ai/en/stable/understanding/)
- [Haystack — pipelines de recuperação](https://docs.haystack.deepset.ai/docs/pipelines)
- [HyDE — pesquisa original](https://arxiv.org/abs/2212.10496)
- [BM25 — referência técnica do método](https://en.wikipedia.org/wiki/Okapi_BM25)

Diagramas didáticos explicam relações conceituais e não substituem testes de desempenho, segurança e qualidade.
