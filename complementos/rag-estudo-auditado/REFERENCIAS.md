# Referências e proveniência — estudo RAG

**Consulta documental:** 23/11/2026.  
**Separação:** a obra [O0] motivou o estudo; [F1] a [F11] são fontes técnicas independentes. Links de documentação podem mudar após esta data.

## Obra de referência (não redistribuída)

- **[O0] Ali Data Analytics.** _RAG (Retrieval-Augmented Generation) – Complete Developer Study Notes_, **18 páginas**, sem data editorial verificável. Material recebido pelo usuário como imagens em 23/11/2026, com atribuição “Prepared by: Ali Data Analytics”. A postagem textual fornecida pelo leitor também identificava “Ali Data Analytics”. **URL original e licença de redistribuição/tradução pública não foram confirmadas.** A falta de licença identificada não torna a obra de domínio público. Nenhuma página, tradução integral ou reprodução de imagem de [O0] é servida por este GitHub.

## Documentação e pesquisas de apoio

| ID | Fonte | O que sustenta | Limite de interpretação |
|---|---|---|---|
| F1 | Lewis et al. (2020), [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) | Arquitetura RAG e uso de memória externa recuperada | Descreve modelos/ensaios específicos, não todas as implementações modernas |
| F2 | Microsoft Learn, [Retrieval-augmented generation in Azure AI Search](https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview) | Fluxos de indexação/consulta e recuperação híbrida | Documentação de produto e serviços Azure; não impõe um stack obrigatório |
| F3 | Chroma, [Collections — Cookbook](https://cookbook.chromadb.dev/core/collections/) | Configuração e uso de embedding functions nas coleções | Padrões e APIs mudam conforme versão do Chroma |
| F4 | OWASP, [LLM Prompt Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html) | Modelo de ameaça e camadas de defesa para documentos recuperados | Nenhuma medida única resolve prompt injection |
| F5 | OWASP, [LLM01:2026 Prompt Injection](https://genai.owasp.org/llm2026/llm012026-prompt-injection/) | Ataques por contexto RAG e limites de instruções no prompt | Risco exige testes próprios e medidas fora do LLM |
| F6 | Microsoft Learn, [Hybrid Search Scoring (RRF)](https://learn.microsoft.com/en-us/azure/search/hybrid-search-ranking) | Agregação de rankings lexical e vetorial | RRF é um mecanismo possível; não equivale à totalidade dos rerankers |
| F7 | SQLite, [FTS5 Extension](https://www.sqlite.org/fts5.html) | Recuperação textual e comportamento BM25 do SQLite | FTS5 não executa busca semântica vetorial |
| F8 | Hugging Face, [Tokenizer — Transformers](https://huggingface.co/docs/transformers/main_classes/tokenizer) | Tokens e dependência do tokenizador | Contagens não são transferíveis entre modelos |
| F9 | Chroma, [Frequently Asked Questions](https://cookbook.chromadb.dev/faq/) | Modelos padrão, dimensões e armadilhas práticas | Versionamento e configuração exatos devem ser registrados |
| F10 | LlamaIndex, [Using VectorStoreIndex](https://developers.llamaindex.ai/python/framework/module_guides/indexing/vector_store_index/) | Forma documentada de criar índice vetorial e usar leitores | Exemplo não foi executado na presente auditoria |
| F11 | Ragas, [List of available metrics](https://docs.ragas.io/en/latest/concepts/metrics/available_metrics/) | Métricas de recuperação e de fidelidade/pertinência | Métricas automáticas exigem dados de teste e podem ser falíveis |

## Conteúdo existente reutilizado como navegação, não copiado

- [Nosso diagrama de arquitetura RAG](../rag-pipeline/index.html).
- [LAB-RAG-01 — código e testes](../../laboratorio/rag-pratico/index.html).
- [LLMs explicados — estudo auditado](../estudo-auditado-llms/index.html).
- [Cinco sistemas de IA](../cinco-sistemas-ia/index.html).

## Política editorial

O novo texto apresenta correções contextualizadas, cálculos próprios e critérios de teste. Não substitui o original e não atribui resultados de experimentos em IA ao autor externo. A publicação original não pode ser deduzida a partir do número de contato impresso na capa.
