# Arquitetura funcional de um agente de IA

**Complemento visual do livro _IA fazendo IA — ou quase_ — José Albuquerque.**

[Ver o diagrama SVG original](arquitetura-funcional-agente-ia.svg) · [Abrir a página de leitura](index.html) · [Voltar ao portal](../../index.html)

Esta ilustração apresenta uma **interpretação editorial independente**, organizada em cinco blocos: (1) objetivo e critérios de sucesso; (2) orquestração, LLM, planejamento, estado e políticas; (3) ciclo observar–decidir–agir–verificar; (4) recursos opcionais; (5) segurança, avaliação, implantação e acompanhamento.

## Distinções que merecem atenção

- **LLM não é sinônimo de agente.** O modelo produz texto ou propostas de ação; componentes de controle executam ferramentas e aplicam permissões.
- **MCP** é um protocolo para integrar ferramentas e outros recursos a aplicações de IA. **A2A** é um protocolo para interação entre agentes. Não são frameworks de orquestração.
- **RAG** é uma abordagem que recupera informações externas para apoiar a geração. Não depende obrigatoriamente de um banco vetorial.
- **Memória** é uma capacidade de retenção ou recuperação de estado. Redis e PostgreSQL são exemplos de infraestrutura que podem apoiá-la.
- **LangGraph, CrewAI e SDKs** são opções de implementação, não camadas obrigatórias.
- **Observabilidade, avaliações, limites de ferramentas e revisão humana** atravessam a solução; não devem ocorrer somente após o ciclo de execução.
- O fluxo ilustrado é **didático, não uma especificação universal**. Um agente pode não ter RAG, memória persistente, planejamento explícito nem ferramentas.

## Créditos e direitos

**Ilustração:** composição conceitual nova, criada para José Albuquerque, com auxílio de IA, em formato SVG vetorial editável. **Referência temática informada na imagem enviada:** Denis Panjuta (@denis-panjuta), cuja arte exibia o título “AI Agent Architecture”. Essa referência é um crédito de inspiração; não implica coautoria, autorização de reprodução, endosso ou uma licença de uso da obra alheia. O desenho anterior não foi anexado nem copiado para este diretório.

O diagrama usa apenas nomes descritivos de tecnologias, sem reproduzir seus logotipos. Marcas citadas pertencem aos respectivos titulares.

## Referências para aprofundamento

- [Model Context Protocol — documentação](https://modelcontextprotocol.io/introduction)
- [Agent2Agent (A2A) — projeto](https://a2a-protocol.org/latest/)
- [LangGraph — conceitos](https://docs.langchain.com/oss/python/langgraph/overview)
- [OWASP — riscos para aplicações LLM](https://genai.owasp.org/)

Publicado como **material complementar**, independente do manuscrito privado. Conceitos e compatibilidades devem ser reavaliados conforme versões de plataformas.
