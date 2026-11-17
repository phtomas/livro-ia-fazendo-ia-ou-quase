# Chamada de ferramentas: com ou sem LangGraph

Complemento de *IA fazendo IA — ou quase*.

[Guia visual](index.html) · [Fluxograma SVG](fluxo-tool-calling.svg)

## Ideia principal

**Não é necessário LangGraph para oferecer ferramentas a um LLM, nem para organizar skills.** Uma *skill* pode ser um conjunto de instruções, recursos e procedimentos; uma *tool* é uma operação executável com entradas e saídas; **tool calling** é o mecanismo pelo qual o modelo solicita operações que um aplicativo ou ambiente de execução efetivamente realiza.

O LangGraph é **opcional**: útil quando precisamos de ciclos, rotas condicionais, estado compartilhado, persistência e supervisão de processos mais complexos.

Atenção: `bind_tools()` apresenta as ferramentas ao modelo, **mas não executa as funções por conta própria**. Um executor precisa interpretar a chamada, verificar argumentos/permissões, executar e devolver o resultado como mensagem de ferramenta.

## Fluxos comparados

**Sem LangGraph:** pedido → LLM sugere a ferramenta e os argumentos → aplicação valida → ferramenta executa → aplicação devolve o resultado → LLM monta a resposta.

**Com LangGraph:** pedido → nó LLM com `bind_tools()` → `tools_condition` seleciona a rota → `ToolNode` executa a chamada → resultado retorna ao estado → nó LLM decide resposta ou nova ferramenta.

Nenhuma das abordagens exige que uma *skill* seja escrita em LangGraph. Provedores de modelos diferentes implementam ferramentas por APIs distintas; verifique o contrato do SDK adotado.

## Dois exemplos Python com a mesma ferramenta

Arquivos: [ferramenta.py](ferramenta.py), [sem_langgraph.py](sem_langgraph.py) e [com_langgraph.py](com_langgraph.py).

### Requisitos

Python 3.11+, um modelo de chat **compatível com tool calling**, credenciais e acesso de rede para o provedor escolhido. Os exemplos usam um provedor por conveniência, não por exigência técnica da arquitetura.

```bash
python -m pip install -U langchain-core langchain-openai langgraph
```

Configure as variáveis `OPENAI_API_KEY` e `OPENAI_MODEL` no ambiente de execução conforme as instruções do provedor. Nunca salve chaves no Git. O uso da API pode gerar custos.

**Opção A — sem LangGraph:**

```bash
python sem_langgraph.py
```

**Opção B — com LangGraph:**

```bash
python com_langgraph.py
```

Ambos devem demonstrar `somar(10, 20)` → **30** quando o modelo decidir executar a ferramenta. O modelo pode responder diretamente sem chamar a ferramenta; a solicitação e a execução devem ser verificadas no histórico/saída.

## O que conferir

- A ferramenta está disponível por **nome, descrição e esquema**.
- A operação foi realmente executada? O resultado foi `30`?
- O retorno recebido pelo modelo corresponde à execução? O código não executou nome de função arbitrário?
- A resposta final reflete o resultado observado e não apenas uma suposição do LLM?
- Para ferramentas com efeitos externos, implemente checagens de autorização, confirmação humana, logs e tratamento de falhas.

## Referências técnicas

- [LangChain — Tools](https://docs.langchain.com/oss/python/langchain/tools)
- [LangGraph — Quickstart e Graph API](https://docs.langchain.com/oss/python/langgraph/quickstart)
- [LangGraph — ToolNode e tools_condition](https://reference.langchain.com/python/langgraph.prebuilt/tool_node/tools_condition)

O roteiro é demonstrativo: **não há afirmação de teste com provedor remoto**. Execute localmente para confirmar as versões e o comportamento do modelo escolhido.
