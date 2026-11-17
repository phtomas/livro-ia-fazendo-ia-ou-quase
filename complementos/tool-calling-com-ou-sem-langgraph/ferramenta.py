"""Ferramenta didática compartilhada pelos dois exemplos."""
from langchain_core.tools import tool


@tool
def somar(a: int, b: int) -> int:
    """Soma dois números inteiros e devolve o resultado.

    Args:
        a: Primeiro inteiro.
        b: Segundo inteiro.
    """
    return a + b
