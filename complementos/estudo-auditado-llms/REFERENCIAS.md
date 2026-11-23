# Fontes e referências — estudo auditado de LLMs

**Data da verificação documental:** 22/11/2026.  
**Escopo:** conferir afirmações técnicas e orientar o estudo; não validar execução de código ou desempenho de modelo.

## Documento que motivou a revisão

- **[F0]** *LLMs Explained — Complete Practical Guide*, 18 páginas numeradas mais capa, recebido pelo usuário como fotografias. Nas imagens disponíveis não há identificação verificável de autor, editora, URL de origem ou licença de republicação. A tradução feita para estudo privado não é redistribuída neste repositório. A ausência de metadados **não** significa obra em domínio público.

## Referências técnicas efetivamente consultadas

| ID | Referência | Sustenta | Limite |
|---|---|---|---|
| F1 | Vaswani, Ashish et al. (2017). [*Attention Is All You Need*](https://arxiv.org/abs/1706.03762) (arXiv 1706.03762; NeurIPS 2017). | Transformer original; atenção escalonada; Q/K/V e múltiplas cabeças | Não define todas as variantes e modelos publicados depois |
| F2 | Hugging Face. [*Tokenizer — Transformers Documentation*](https://huggingface.co/docs/transformers/main_classes/tokenizer). | Conversão de texto em tokens e IDs; tokenizadores específicos | A segmentação é dependente do tokenizador e modelo |
| F3 | Hugging Face. [*Generation — Transformers Documentation*](https://huggingface.co/docs/transformers/main_classes/text_generation). | Estratégias greedy/amostragem, temperatura, top-k, top-p | Argumentos e valores-padrão podem variar com a versão |
| F4 | NIST (2024). [*AI Risk Management Framework: Generative AI Profile*, NIST AI 600-1](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence). | Risco de confabulação, validade, avaliação e confiabilidade | Estrutura de gestão de risco, não certificação de uma aplicação |
| F5 | Es, Shahul et al. (2024). [*RAGAs: Automated Evaluation of Retrieval Augmented Generation*](https://aclanthology.org/2024.eacl-demo.16/), EACL 2024. | Dimensões independentes de avaliação em RAG | As métricas automáticas não substituem todas as verificações humanas |
| F6 | Python jsonschema. [*Schema Validation*](https://python-jsonschema.readthedocs.io/en/stable/validate/). | Validação de estrutura e tipos; comportamento de 'format' | Validação de esquema não comprova que campos extraídos sejam verdadeiros |
| F7 | PostgreSQL 18. [*SET TRANSACTION*](https://www.postgresql.org/docs/18/sql-set-transaction.html). | Transações READ ONLY e comandos proibidos | Não dispensa controles de autorização, custo, esquema e exposição de dados |
| F8 | OWASP (2025). [*LLM01 — Prompt Injection*](https://genai.owasp.org/llmrisk/llm01-prompt-injection/). | Riscos de instruções adversariais vindas de entradas externas | Defesa deve ser implementada e testada no sistema como um todo |
| F9 | Hugging Face Hub. [*Licenses*](https://huggingface.co/docs/hub/repositories-licenses). | Licenças e condições de acesso a repositórios de modelos | A licença concreta de cada modelo deve ser lida no respectivo repositório |

As fontes acima são independentes do PDF recebido. Links para documentações que mudam com o tempo devem ter sua versão registrada em reproduções futuras.

## Materiais já existentes no próprio portal (para evitar duplicação)

- [40 perguntas essenciais sobre LLMs](../llm-40-perguntas/index.html): conceitos e notas técnicas.
- [120 conceitos de LLMs](../llm-120-conceitos/index.html): glossário visual.
- [Fundamentos de Machine Learning](../fundamentos-machine-learning-para-llms/index.html): ponte entre ML clássico e LLMs.
- [Caderno visual de IA/ML](../caderno-visual-fundamentos-ia-ml/index.html): diagramas e PDF próprios.
- [Nove fórmulas de redes neurais](../formulas-redes-neurais/index.html): fundamentos matemáticos.
- [RAG e arquitetura](../rag-pipeline/index.html) e [LAB-RAG-01](../../laboratorio/rag-pratico/index.html).
- [Cinco sistemas de IA](../cinco-sistemas-ia/index.html): faturas, consultas documentais e avaliação.

## Precisões editoriais importantes

1. A frase “LLMs apenas predizem o próximo token” simplifica demais: aplica-se bem a modelos generativos autorregressivos, não a todas as tarefas e arquiteturas.
2. A analogia Query/Key/Value é didática, não define a operação matemática.
3. Contexto maior não implica melhor recuperação de detalhes; memória persistente é uma camada do produto, não o próprio contexto.
4. O parâmetro de temperatura não substitui checagem factual; seu efeito depende do modo de decodificação.
5. RAG precisa avaliar recuperação, fundamento da resposta e citações separadamente.
6. Validar JSON exige mais do que sintaxe. Para datas de calendário, regras de domínio devem ser verificadas; o validador de esquema depende de configurações.
7. Exemplos de SDK não executados e placeholders não devem ser descritos como código testado.
8. Open weights não equivale automaticamente a licença comercial irrestrita, transparência total ou open source.
9. SQL read-only é camada de defesa: ainda pode haver leitura de conteúdo não autorizado e consultas excessivamente custosas.
10. Um conjunto pequeno de exemplos pode detectar falhas, mas não comprova desempenho geral.

## Próxima rodada

- Identificar autoria e licença do PDF original antes de qualquer publicação integral.
- Executar os exercícios com ferramentas e versões registradas.
- Guardar resultados e falhas antes de marcar quaisquer gates como PASS.
