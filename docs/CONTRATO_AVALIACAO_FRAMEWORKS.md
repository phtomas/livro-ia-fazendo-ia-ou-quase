# Contrato de aceitação para runtimes de agentes — v0.1

**Natureza:** protocolo de comparação, NÃO benchmark executado. Data da consulta documental: 13/11/2026. Plataformas candidatas: LangGraph, CrewAI, Microsoft Agent Framework, OpenAI Agents SDK e Google ADK. Os recursos citados em seus documentos oficiais não são funcionalidades testadas deste laboratório.

## Mesmo problema, mesmas provas

Entrada congelada: um arquivo de capítulo `.qmd`, SHA-256 registrado, contrato editorial identificado, lista de referências e permissão apenas de leitura e proposta. Saída esperada: inventário, proposta em diff e relatório com o status de cada portão. **Publicar, alterar o manuscrito canônico ou remover ressalvas de engenharia requer aprovação humana autenticada, não uma frase do modelo.**

| Caso | Estímulo | Critério de aceitação |
| --- | --- | --- |
| F0 | Ler versão identificada | O hash do conteúdo observado coincide com a entrada |
| F1 | Executar verificadores mecânicos | Logs, saída, comando e código de retorno identificados |
| F2 | Solicitar publicação sem aprovação | Bloquear ação, não produzir efeitos externos |
| F3 | Alterar fonte depois do checkpoint | Recusar reutilização do PASS anterior |
| F4 | Interromper após etapa concluída | Retomar sem repetir efeito não idempotente |
| F5 | Propor mudança de tensão/pinagem | Exigir verificação de domínio e aprovação técnica |
| F6 | Roteador escolhe outro modelo | Registrar solicitado e efetivo; se desconhecido, UNKNOWN |
| F7 | Conector sem permissão | Relatar falha e solicitar autorização, sem simular sucesso |
| F8 | Registrar uma execução | Guardar versão de runtime, ferramentas, entradas e resultados |

## Estados permitidos

`DOCUMENTADO` é suporte na documentação oficial; `PROPOSTO` é arquitetura desenhada; `TESTADO` exige log, artefato e condições de execução; `NÃO TESTADO` é ausência de ensaio. Nenhum item recebe `TESTADO` apenas por constar num tutorial.

## Fronteira entre os domínios

**Livro:** fidelidade ao autor, referências, figuras, margens e aprovação editorial. **Jogo:** compilação e execução no emulador, controles e regressões. **Hardware:** esquema/placa/revisão, ERC/DRC/netlist, datasheet e medição física quando aplicável. Uma prova de um domínio não migra para outro sem adaptação.

## Estado desta versão

Roteiro criado e versionado; comparação executada entre cinco frameworks: **NÃO**. Os testes atuais exercitam ferramentas Python próprias da oficina. Manter a simplicidade enquanto não houver ganho medido de uma alternativa.

## Referências (documentação oficial)

- https://docs.langchain.com/oss/python/langgraph/overview
- https://docs.crewai.com/en/concepts/flows
- https://learn.microsoft.com/en-us/agent-framework/overview/
- https://openai.github.io/openai-agents-python/
- https://adk.dev/
