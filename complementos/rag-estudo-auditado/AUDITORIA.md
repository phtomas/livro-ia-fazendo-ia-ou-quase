# Auditoria editorial e técnica — RAG, 18 páginas

**Data:** 23/11/2026  
**Documento motivador:** Ali Data Analytics, _RAG (Retrieval-Augmented Generation) – Complete Developer Study Notes_ (18 páginas fornecidas em imagens).  
**Tipo de trabalho:** análise crítica independente, não tradução integral pública.  
**Estados:** revisão documental **PASS (escopo limitado)**; cinco testes aritméticos locais **PASS**; reprodução integral do pipeline, versões de APIs e avaliação com LLM **NOT RUN**; licença de redistribuição **NÃO CONFIRMADA**.

## Matriz de revisão

| Páginas da obra de referência | Tema | Constatação e precisão necessária | Verificação ou fonte |
|---|---|---|---|
| 2 e 4 | Arquitetura | A representação vetorial é frequente, mas RAG também pode usar busca lexical BM25, híbrida ou outro mecanismo de recuperação. | [F1], [F2], projeto [pipeline RAG](../rag-pipeline/README.md) |
| 3 | Termos básicos | Contagem de tokens varia com o tokenizador. Temperatura baixa não prova correção nem impede alucinações. | [F8], [F4] |
| 5 | Ingestão | OCR e extração de tabelas exigem validação; limpar cabeçalhos sem preservar metadados pode destruir informação útil. | [F7], revisão conceitual |
| 6 | Chunking | O exemplo divide por caracteres, não por tokens ou significado; pode cortar palavras. A regra de 300–800 tokens e 10–20% de overlap é um ponto de partida, não garantia. Se overlap >= size, o laço didático não avança. | Teste [T3], [T4], [F7] |
| 7 | Embeddings | Vetores 3D são artificiais; a similaridade não valida recuperação semântica real. Os dois valores impressos no exemplo correspondem à conta. | Teste [T2] |
| 8 | Bancos vetoriais | FAISS é biblioteca de indexação e similaridade; Chroma, pgvector e serviços gerenciados têm arquiteturas/garantias distintas. Um modelo padrão de embedding pode depender de download/configuração. | [F3], [F9] |
| 9 e 13 | Recuperação avançada | Busca híbrida combina sinais; reranking opera sobre candidatos e não substitui boa recuperação. HyDE serve para obter candidatos, não é reranking. | [F1], [F6] |
| 10 e 15 | Prompts e alucinação | “Responder só com o contexto”, citar trechos e temperature=0 são defesas parciais. Citações devem ser verificadas. Trechos recuperados podem conter prompt injection. | [F4], [F5] |
| 11 | Python para RAG | O mini-exemplo é TF–IDF (busca lexical), não um pipeline vetorial; o bloco de geração usa `question` não definido nesse trecho, além do placeholder de modelo e credenciais. Não está pronto para execução ponta a ponta como impresso. | Leitura do código da pág. 11 |
| 12 | Frameworks | O exemplo LlamaIndex depende de pacotes e configurações do ambiente; API e padrões podem mudar. Não apresentar resultado como medido sem instalação/execução. | [F10] |
| 14 | Métricas | Hit@3 = 2/3 = 0,67 (arredondado), MRR = 0,5 nos dados mostrados; os cálculos batem. Para múltiplos documentos relevantes, Hit@k e Recall@k deixam de ser intercambiáveis. | Testes [T0], [T1], [F11] |
| 15 e 17 | Controle de acesso | Filtrar metadados é componente de segurança, mas autorização efetiva deve ser aplicada pelo backend/serviço antes do acesso, com provas de isolamento. | [F4], [F5] |
| 16 | RAG e fine-tuning | Custos são contextuais; fine-tuning não é exclusivamente “estilo”. RAG não garante citações corretas e fine-tuning pode coexistir com RAG. | [F1], síntese com ressalvas |
| 18 | Valores iniciais | top-k, temperatura, chunk size e overlap são parâmetros experimentais. Não chamar valores fixos de ótimos sem avaliação por corpus/perguntas. | [F11], [F2] |

## Ensaios reproduzíveis

Arquivo: [verificar_exemplos.py](verificar_exemplos.py). Os testes usam apenas a biblioteca padrão do Python.

| Ensaio | Prova local | Resultado |
|---|---|---|
| T0 | Hit@3 sobre três consultas didáticas | **PASS: 0,6666…** |
| T1 | MRR com posições 1, 2 e ausente | **PASS: 0,5** |
| T2 | Dois cossenos 3D | **PASS: 0,989 / 0,271** |
| T3 | Fragmentação por caracteres do exemplo | **PASS:** dois fragmentos com overlap |
| T4 | Rejeição de overlap >= size | **PASS:** ValueError explícito |

**Não testado:** dados reais, desempenho de recuperação, modelos de embedding, Chroma, LangChain, LlamaIndex, APIs pagas, avaliação de respostas, ACL multiusuário, latência de produção. Nenhum PASS acima deve ser extrapolado.

## Checklist para futura implantação

1. Identificar fontes, licenças, permissões, versões e proprietários dos documentos.
2. Conservar origem do trecho, página/seção, data e versão ao indexar.
3. Construir conjunto de perguntas positivas, difíceis, sem resposta e de acesso proibido.
4. Medir recuperação (Hit@k, MRR; Recall@k quando houver vários documentos relevantes) antes de medir geração.
5. Verificar fidelidade, pertinência, citações, abstenção e ataques por instruções injetadas.
6. Aplicar autorização no serviço, independentemente do texto do prompt.
7. Registrar logs mínimos, sem expor dados pessoais, segredos ou texto sensível.
8. Comparar custo, latência, versão do índice/modelo e resultados após cada modificação.

## Direitos e procedência

Os PDFs original e traduzido, incluindo figuras e tabelas do criador externo, foram mantidos fora da publicação por ausência de licença demonstrada. Este material é uma **crítica técnica e um conjunto novo de testes**, não uma republicação.

As referências efetivamente consultadas, com links e limites, estão em [REFERENCIAS.md](REFERENCIAS.md).
