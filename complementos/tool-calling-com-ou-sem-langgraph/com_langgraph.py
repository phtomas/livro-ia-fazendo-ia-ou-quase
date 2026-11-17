"""Mesmo exemplo com LangGraph: ToolNode + tools_condition.

Requer langgraph, langchain-core, langchain-openai,
OPENAI_API_KEY e OPENAI_MODEL (compatível com tool calling).
"""
import os

from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, MessagesState, START
from langgraph.prebuilt import ToolNode, tools_condition
from ferramenta import somar


def montar_grafo():
    nome = os.environ.get("OPENAI_MODEL")
    if not nome:
        raise RuntimeError("Defina OPENAI_MODEL para um modelo com tool calling.")
    llm = ChatOpenAI(model=nome, temperature=0).bind_tools([somar])

    def consultar_llm(state: MessagesState):
        return {"messages": [llm.invoke(state["messages"])]}

    grafo = StateGraph(MessagesState)
    grafo.add_node("llm", consultar_llm)
    grafo.add_node("tools", ToolNode([somar]))
    grafo.add_edge(START, "llm")
    # Roteia para 'tools' quando o LLM solicitar ferramenta; caso contrário, encerra.
    grafo.add_conditional_edges("llm", tools_condition)
    grafo.add_edge("tools", "llm")
    return grafo.compile()


if __name__ == "__main__":
    resultado = montar_grafo().invoke(
        {"messages": [("user", "Quanto é 10 + 20? Use a ferramenta se necessário.")]},
        config={"recursion_limit": 10},
    )
    for mensagem in resultado["messages"]:
        if getattr(mensagem, "type", None) == "tool":
            print("Resultado da ferramenta:", mensagem.content)
    print("Resposta final:", resultado["messages"][-1].content)
