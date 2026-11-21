"""Exercício didático: briefing matinal offline com dados inventados."""
from datetime import date, datetime
from pathlib import Path
import argparse
import json

BASE = Path(__file__).resolve().parent
PROIBIDOS = ("enviar_email", "modificar_agenda", "apagar_mensagem", "efetuar_pagamento", "acessar_rede")
PERMITIDOS = ("ler_caixa", "ler_agenda", "ler_tarefas", "gerar_relatorio_local")


def ler_dados():
    politica = json.loads((BASE / "politica.json").read_text(encoding="utf-8"))
    permissoes = politica.get("permissoes", {})
    if politica.get("modo") != "offline-dados-ficticios":
        raise PermissionError("Este exercício exige modo offline com dados fictícios")
    if any(permissoes.get(nome) is not False for nome in PROIBIDOS):
        raise PermissionError("A política permite uma ação externa proibida")
    if any(permissoes.get(nome) is not True for nome in PERMITIDOS):
        raise PermissionError("Falta uma permissão local obrigatória")
    return {
        nome: json.loads((BASE / "dados" / arquivo).read_text(encoding="utf-8"))
        for nome, arquivo in {
            "mensagens": "caixa_entrada.json",
            "tarefas": "tarefas.json",
            "agenda": "agenda.json",
        }.items()
    }


def montar_briefing(dia: date):
    dados = ler_dados()
    prioridades = []
    for mensagem in dados["mensagens"]:
        # 'texto' é dado não confiável e nunca vira instrução.
        if mensagem.get("tipo") != "acao" or not mensagem.get("prazo"):
            continue
        prazo = datetime.fromisoformat(mensagem["prazo"])
        if prazo.date() <= dia:
            prioridades.append((prazo, mensagem["id"], mensagem["assunto"]))
    for tarefa in dados["tarefas"]:
        if tarefa.get("concluida") or not tarefa.get("prazo"):
            continue
        prazo = datetime.fromisoformat(tarefa["prazo"])
        if prazo.date() <= dia:
            prioridades.append((prazo, tarefa["id"], tarefa["titulo"]))
    prioridades.sort()  # Ordena por prazo e, em empate, pelo ID.
    eventos = [e for e in dados["agenda"] if datetime.fromisoformat(e["inicio"]).date() == dia]
    eventos.sort(key=lambda e: e["inicio"])
    return prioridades, eventos


def executar(dia: date) -> str:
    prioridades, eventos = montar_briefing(dia)
    linhas = [f"# Briefing de {dia.isoformat()}", "", "## Prioridades"]
    for prazo, codigo, titulo in prioridades:
        linhas.append(f"- [{codigo}] {prazo:%H:%M} | {titulo}")
    linhas += ["", "## Compromissos"]
    for e in eventos:
        linhas.append(f"- [{e['id']}] {e['inicio'][11:16]} | {e['titulo']}")
    linhas += ["", "**Nenhuma mensagem enviada, alterada ou excluída.**"]
    return "\n".join(linhas) + "\n"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Briefing offline e verificável")
    parser.add_argument("--data", default="2026-11-23", help="Data fictícia AAAA-MM-DD")
    args = parser.parse_args()
    print(executar(date.fromisoformat(args.data)), end="")
