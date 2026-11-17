"""Tool calling real com um provedor LLM, sem LangGraph.

Requer langchain-core, langchain-openai, OPENAI_API_KEY e OPENAI_MODEL.
O programa, e não o modelo, executa a ferramenta permitida.
"""
import os

from langchain_core.messages import HumanMessage, ToolMessage
from langchain_openai import ChatOpenAI
from ferramenta import somar


def executar():
    nome = os.environ.get("OPENAI_MODEL")
    if not nome:
        raise RuntimeError("Defina OPENAI_MODEL para um modelo com tool calling.")

    model = ChatOpenAI(model=nome, temperature=0).bind_tools([somar])
    mensagens = [HumanMessage(content="Quanto é 10 + 20? Use a ferramenta se necessário.")]
    # Limite de três rodadas para evitar loops sem controle.
    for _ in range(3):
        resposta = model.invoke(mensagens)
        mensagens.append(resposta)
        if not resposta.tool_calls:
            print("Resposta final:", resposta.content)
            return
        for chamada in resposta.tool_calls:
            if chamada["name"] != somar.name:
                raise ValueError("Ferramenta não autorizada: " + chamada["name"])
            argumentos = chamada["args"]
            # A ferramenta valida a tipagem e só soma; não acessa sistemas externos.
            resultado = somar.invoke(argumentos)
            mensagens.append(ToolMessage(content=str(resultado), tool_call_id=chamada["id"]))
            print("Executado:", chamada["name"], argumentos, "=>", resultado)
    raise RuntimeError("Limite de rodadas atingido sem resposta final.")


if __name__ == "__main__":
    executar()
