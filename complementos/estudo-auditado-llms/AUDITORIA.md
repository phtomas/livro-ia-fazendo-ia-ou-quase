# Auditoria editorial — LLMs explicados, estudo e exercícios

**Data:** 22/11/2026  
**Estado:** revisão de escopo e documentação **PASS**; execução de exemplos **NOT RUN**; licença do documento motivador **NÃO DETERMINADA**.

## Decisão editorial

Não duplicar o conteúdo de [40 perguntas](../llm-40-perguntas/index.html), [120 conceitos](../llm-120-conceitos/index.html), [fundamentos ML](../fundamentos-machine-learning-para-llms/index.html), [RAG](../rag-pipeline/index.html) nem [cinco sistemas de IA](../cinco-sistemas-ia/index.html).

**Conteúdo novo publicado:** roteiro de navegação entre os materiais; tabela de precisão conceitual; oito exercícios com critérios de aceitação; bibliografia ligada às ressalvas; status sem alegação de testes inexistentes.

## Critérios de auditoria

| Critério | Resultado | Evidência / limite |
|---|---|---|
| Conteúdo duplicado | PASS (revisão temática) | Os tópicos já abordados estão ligados aos complementos existentes; a nova publicação privilegia notas de precisão e práticas de teste |
| Fonte motivadora identificada | PARTIAL | Título e 18 páginas mais capa reconhecidos; autoria e licença ainda desconhecidas |
| Reprodução integral autorizada | NOT RUN / não determinada | Por prudência, PDF traduzido e imagens originais não foram enviados ao GitHub |
| Sustentação de afirmações | PASS (documental) | Fontes oficiais ou artigos primários em [REFERENCIAS.md](REFERENCIAS.md) |
| Execução de código / SQL / testes de modelo | NOT RUN | Os exercícios são propostos, não resultados medidos |
| Proteção de dados | PASS (revisão editorial) | Só exemplos fictícios; nenhum detalhe de máquinas, endereços, usuários, credenciais ou topologia privada |
| Links externos | PASS (consulta documental) | Verificados durante a preparação; requerem nova checagem em revisões futuras |

## Itens que exigem ressalva em vez de correção silenciosa

- Predição de tokens, Transformer e arquiteturas diferentes: [F1], [F2].
- Temperatura, top-k, top-p, decodificação: [F3].
- RAG, alucinação, métricas e segurança: [F4], [F5], [F8].
- Saídas estruturadas e JSON: [F6].
- Consultas SQL e autorizações: [F7], [F8].
- Licenciamento de pesos abertos: [F9].

## Fontes

Referências por afirmação, URLs, datas e ressalvas em [REFERENCIAS.md](REFERENCIAS.md).

## Conclusão

O conjunto das 18 páginas numeradas serve como bom guia introdutório, mas não é prova de funcionamento de APIs, ferramentas ou pipelines. A contribuição útil para o repositório é transformar conceitos em tarefas com critérios verificáveis, reaproveitando o material já existente e indicando a proveniência das afirmações.
