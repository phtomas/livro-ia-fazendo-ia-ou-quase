#!/usr/bin/env python3
"""Kit do leitor — ensaios locais reproduzíveis para os 21 capítulos.

Somente dados sintéticos. Sem LLM, credenciais, rede, alterações em fontes
editoriais ou publicações. Os exercícios humanos não recebem PASS automático.
Python 3.11+. Execute --ajuda para instruções.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
CODE = ROOT / "laboratorio" / "codigo"
MANUAIS = {1, 2, 3, 5, 6, 7, 15}
TITULOS = {
    1: "Voz e revisão com critérios",
    2: "Escolher a menor solução",
    3: "Contrato e limites do agente",
    4: "Cópia íntegra sem IA",
    5: "Matriz de evidências",
    6: "Perfil de voz autoral",
    7: "Comparação entre plataformas",
    8: "Skill em modo de simulação",
    9: "Interrupção e checkpoint",
    10: "Política de ações",
    11: "Ciclo supervisionado",
    12: "Propostas de revisão",
    13: "Comparação de duas árvores",
    14: "Linha de base e conflito",
    15: "Framework ou Python simples",
    16: "Métricas e custo",
    17: "Auditoria Quarto",
    18: "Regressão de microjogo",
    19: "Rastreabilidade de hardware",
    20: "Portabilidade declarada",
    21: "Inventário de edição",
}

def gravar(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")

def projeto_sintetico(dest: Path) -> Path:
    """Mini-projeto descartável compatível com os verificadores canônicos."""
    root = dest / "quarto-ficticio"
    gravar(root / "_quarto.yml",
           "project:\n  type: book\nbook:\n  chapters:\n"
           "    - index.qmd\n    - chapters/01-exemplo.qmd\n"
           "number-sections: true\nnumber-depth: 2\n")
    gravar(root / "index.qmd", "# Apresentação {.unnumbered}\n\nProjeto fictício.\n")
    gravar(root / "chapters/01-exemplo.qmd",
           "# Exemplo fictício\n\n"
           "::: {.na-pratica-com-ia}\n"
           "**NA PRÁTICA COM A IA**\n"
           "**O que testar.** Uma regra simples.\n"
           "**Como proceder.** Usar arquivos fictícios.\n"
           "**Prompt que usaríamos hoje**\n"
           "Analisar sem modificar.\n"
           "**Por que funciona.** Permite observar.\n"
           "**Como verificar.** Conferir o resultado.\n"
           ":::\n\n::: {.experimento-do-leitor}\n"
           "**EXPERIMENTO DO LEITOR**\n"
           "Investigar uma regra sem IA.\n:::\n")
    for path, text in {
        "appendices/10-principios.qmd": "# Princípios {.unnumbered}\n",
        "appendices/glossario.qmd": "# Glossário {.unnumbered}\n",
        "references.qmd": "# Referências {.unnumbered}\n",
        "scripts/gerar_previa.sh": "#!/bin/sh\n# --number-sections --top-level-division=chapter chapters/01-exemplo.qmd\n",
        "pdf-preambulo.tex": "% chapterprefix=true\n% formatChapterTocNumber\n",
        "styles.css": "/* Exemplo sem estilos do livro */\n",
        "references.bib": "% Não contém fontes reais\n",
        "filters/boxes.lua": "-- Exemplo sem filtro de publicação\n",
    }.items():
        gravar(root / path, text)
    for name in ("verificar_boxes.py", "verificar_estrutura.py"):
        original = CODE / "scripts" / name
        if not original.is_file():
            raise FileNotFoundError(f"Verificador público ausente: {original}")
        dest_check = root / "scripts" / name
        dest_check.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(original, dest_check)
    return root

def executar_comando(label: str, args: list[str], expected: int, out: Path) -> dict:
    """Roda somente executáveis locais com argumentos explícitos; sem shell."""
    try:
        cp = subprocess.run(
            [sys.executable, *args], text=True, capture_output=True,
            timeout=40, check=False, cwd=out
        )
        code, stdout, stderr = cp.returncode, cp.stdout, cp.stderr
    except (OSError, subprocess.TimeoutExpired) as exc:
        code, stdout, stderr = None, "", repr(exc)
    gravar(out / "logs" / f"{label}.stdout.txt", stdout[-16000:])
    gravar(out / "logs" / f"{label}.stderr.txt", stderr[-16000:])
    return {
        "etapa": label,
        "comando": ["python", *args],
        "saida_esperada": expected,
        "codigo_observado": code,
        "criterio": "CODIGO_ESPERADO" if code == expected else "DIVERGENCIA",
        "falha_intencional": expected != 0,
        "aviso": "Código de saída é evidência limitada; inspecione também os relatórios gerados.",
    }

def ensaio(cap: int, out: Path) -> dict:
    if cap not in TITULOS:
        raise ValueError("Capítulo inexistente")
    if out.exists():
        raise FileExistsError("O destino já existe; escolha um diretório novo, sem sobrescrever.")
    out.mkdir(parents=True)
    gravar(out / "LEIA_PRIMEIRO.md",
           f"# Capítulo {cap:02d} — {TITULOS[cap]}\n\n"
           "Estes dados são fictícios. O relatório automático não substitui a "
           "conferência humana nem prova o funcionamento de qualquer plataforma de IA.\n\n"
           f"Roteiro: laboratorio/kit-do-leitor/capitulos/{cap:02d}.md\n")
    record = {
        "capitulo": cap, "titulo": TITULOS[cap],
        "horario_utc": datetime.now(timezone.utc).isoformat(),
        "dados": "FICTICIOS", "chamadas_llm": 0, "publicacao": False,
        "edicao_manuscrito": False, "aprovacao_autor": "PENDENTE",
        "etapas": [], "estado": "NAO_VERIFICADO",
    }
    if cap in MANUAIS:
        gravar(out / "REGISTRO_MANUAL.md",
               f"# Capítulo {cap:02d} — registro do leitor\n\n"
               "Situação escolhida (fictícia, sem dados privados):\n\n"
               "Hipótese anterior à consulta de IA:\n\n"
               "Critérios observáveis:\n\n"
               "Resposta/observação independente:\n\n"
               "Resposta do modelo, serviço e versão (se houver):\n\n"
               "Comparação e eventuais divergências:\n\n"
               "Evidência material disponível:\n\n"
               "Decisão humana e data:\n\n"
               "Estado inicial: NÃO VERIFICADO.\n")
    else:
        sandbox = out / "area-descartavel"
        sandbox.mkdir()
        root = projeto_sintetico(sandbox)
        t = lambda p: str(CODE / p)
        a = lambda p: str(sandbox / p)
        p = lambda p: str(root / p)
        steps: list[tuple[str, list[str], int]] = []
        if cap == 4:
            orig = sandbox / "origem"
            orig.mkdir()
            gravar(orig / "a.txt", "Arquivo sintético A\n")
            gravar(orig / "b.txt", "Arquivo sintético B\n")
            tool = t("tools/arquivos/copia_provada.py")
            steps = [
                ("previa", [tool, str(orig), a("destino")], 0),
                ("copia_com_hash", [tool, str(orig), a("destino"), "--execute"], 0),
            ]
        elif cap == 8:
            area = sandbox / "workspace"
            area.mkdir()
            steps = [("dry_run_skill", [
                t("tools/skills/instalar_skill_local.py"),
                "--source", t("skills/revisao-autoral"),
                "--workspace", str(area), "--targets", "both", "--json"], 0)]
        elif cap == 9:
            script = t("workflows/fluxo_com_checkpoints.py")
            steps = [
                ("interrupcao_esperada", [script, str(root),
                                          "--work", a("checkpoint"),
                                          "--fail-at", "after-inventory"], 4),
                ("retomada", [script, str(root), "--work", a("checkpoint")], 0),
            ]
        elif cap == 10:
            script = t("agents/politica_orquestrador.py")
            steps = [
                ("leitura", [script, "--action", "READ_SOURCE",
                             "--out", a("politica-leitura.json")], 0),
                ("publicacao_bloqueada", [script, "--action", "PUBLISH",
                                          "--out", a("politica-publicacao.json")], 0),
            ]
        elif cap == 11:
            gravar(sandbox / "permitido.json", json.dumps({
                "goal": "Exemplo supervisionado", "steps": [
                    {"action": "READ_SOURCE", "path": "index.qmd"},
                    {"action": "GENERATE_REPORT"}]}, ensure_ascii=False))
            gravar(sandbox / "bloqueado.json", json.dumps({
                "goal": "Bloqueio intencional", "steps": [
                    {"action": "PUBLISH"}]}, ensure_ascii=False))
            script = t("agents/ciclo_supervisionado.py")
            steps = [
                ("leitura_permitida", [script, "--root", str(root),
                                      "--plan", a("permitido.json"),
                                      "--report", a("leitura.json")], 0),
                ("publicacao_negada", [script, "--root", str(root),
                                       "--plan", a("bloqueado.json"),
                                       "--report", a("bloqueado.json.saida")], 2),
            ]
        elif cap == 12:
            script = t("tools/editorial/avaliar_proposta.py")
            base = "examples/avaliacao/"
            steps = [
                ("revisao_preservada", [
                    script, t(base + "original.txt"), t(base + "proposta_segura.txt"),
                    "--report", a("proposta-segura.json")], 0),
                ("tensao_alterada", [
                    script, t(base + "original.txt"), t(base + "proposta_tensao_errada.txt"),
                    "--report", a("proposta-reprovada.json")], 2),
            ]
        elif cap in (13, 14):
            left = sandbox / "canon"
            right = sandbox / "espelho"
            left.mkdir()
            right.mkdir()
            gravar(left / "igual.txt", "Mesmo conteúdo\n")
            gravar(left / "diferente.txt", "Valor original\n")
            shutil.copyfile(left / "igual.txt", right / "igual.txt")
            shutil.copyfile(left / "diferente.txt", right / "diferente.txt")
            script = t("tools/sync/conferir_espelhos.py")
            if cap == 13:
                steps = [
                    ("iguais", [script, "--canon", str(left), "--espelho", str(right),
                               "--report", a("iguais.json")], 0)]
                record["_mutacao"] = "divergencia"
            else:
                steps = [
                    ("linha_base", [script, "--canon", str(left),
                                   "--snapshot", a("baseline.json")], 0)]
                record["_mutacao"] = "conflito"
        elif cap == 16:
            steps = [("metricas_sinteticas", [
                t("tools/observabilidade/resumir_execucoes.py"),
                "--runs", t("examples/metricas/execucoes_sinteticas.jsonl"),
                "--rates", t("examples/metricas/tarifas_ficticias.json"),
                "--output", a("metricas.json")], 0)]
        elif cap == 17:
            steps = [("fontes_quarto", [
                t("tools/editorial/auditar_fontes_quarto.py"), str(root),
                "--output", a("auditoria-fontes.json")], 0)]
        elif cap == 18:
            script = t("tools/jogos/replay_minijogo.py")
            steps = [
                ("vitoria", [script, t("examples/jogos/cenario_vitoria.json"),
                             "--output", a("vitoria.json")], 0),
                ("regressao_proposital", [
                    script, t("examples/jogos/cenario_regressao.json"),
                    "--output", a("regressao.json")], 2),
            ]
        elif cap == 19:
            script = t("tools/hardware/verificar_evidencias.py")
            steps = [
                ("manifesto_documental", [
                    script, t("examples/hardware/manifesto_documental.json"),
                    "--output", a("documental.json")], 0),
                ("medicao_inexistente", [
                    script, t("examples/hardware/manifesto_sem_medicao.json"),
                    "--output", a("sem-medicao.json")], 1),
            ]
        elif cap == 20:
            script = t("tools/portabilidade/auditar_adaptador.py")
            base = "examples/portabilidade/"
            contrat = t(base + "contrato_revisao.json")
            steps = [
                ("compatibilidade_declarada", [
                    script, contrat, t(base + "adaptador_completo.json"),
                    "--output", a("completo.json")], 0),
                ("recurso_ausente", [
                    script, contrat, t(base + "adaptador_sem_execucao.json"),
                    "--output", a("sem-execucao.json")], 1),
                ("recurso_desconhecido", [
                    script, contrat, t(base + "adaptador_desconhecido.json"),
                    "--output", a("desconhecido.json")], 3),
            ]
        elif cap == 21:
            steps = [("manifesto_da_edicao", [
                t("tools/publicacao/inventariar_edicao.py"), str(root),
                "--expected-chapters", "1", "--output", a("manifesto.json")], 0)]
        for label, args, expected in steps:
            record["etapas"].append(executar_comando(label, args, expected, out))
        if cap in (13, 14):
            if cap == 13:
                gravar(sandbox / "espelho" / "diferente.txt", "Versão divergente\n")
                args = [t("tools/sync/conferir_espelhos.py"),
                        "--canon", a("canon"), "--espelho", a("espelho"),
                        "--report", a("divergentes.json")]
                record["etapas"].append(executar_comando("diferentes", args, 1, out))
            else:
                gravar(sandbox / "canon" / "diferente.txt", "Alteração Git\n")
                gravar(sandbox / "espelho" / "diferente.txt", "Alteração Drive\n")
                args = [t("tools/sync/conferir_espelhos.py"),
                        "--canon", a("canon"), "--espelho", a("espelho"),
                        "--baseline", a("baseline.json"),
                        "--report", a("conflitos.json")]
                record["etapas"].append(executar_comando("conflito_detectado", args, 1, out))
        if cap == 9 and all(e["criterio"] == "CODIGO_ESPERADO" for e in record["etapas"]):
            gravar(root / "chapters/01-exemplo.qmd",
                   (root / "chapters/01-exemplo.qmd").read_text(encoding="utf-8")
                   + "\nAlteração proposital posterior ao checkpoint.\n")
            record["etapas"].append(executar_comando(
                "fonte_alterada_bloqueada",
                [t("workflows/fluxo_com_checkpoints.py"), str(root),
                 "--work", a("checkpoint")], 3, out))
        record.pop("_mutacao", None)
        record["estado"] = ("PASS_LIMITED" if record["etapas"] and
                            all(e["criterio"] == "CODIGO_ESPERADO" for e in record["etapas"])
                            else "FAIL" )
    gravar(out / "resultado.json", json.dumps(record, ensure_ascii=False, indent=2) + "\n")
    return record

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--listar", action="store_true",
                        help="mostra os capítulos e o tipo de experimento")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--capitulo", type=int, choices=range(1,22))
    group.add_argument("--todos", action="store_true")
    parser.add_argument("--saida", type=Path,
                        help="pasta NOVA de evidências, preferencialmente fora do repositório")
    args = parser.parse_args()
    if args.listar:
        for n, title in TITULOS.items():
            print(f"{n:02d} | {'MANUAL' if n in MANUAIS else 'PYTHON'} | {title}")
        return 0
    if not (args.capitulo or args.todos) or args.saida is None:
        parser.error("use --listar ou --capitulo N/--todos junto com --saida")
    target = args.saida.expanduser().resolve()
    if target == ROOT or target.is_relative_to(ROOT):
        parser.error("escolha --saida fora da árvore do repositório")
    if target.exists():
        parser.error("o diretório de saída já existe; escolha outro para não sobrescrever")
    try:
        if args.todos:
            target.mkdir(parents=True)
            reports = [ensaio(n, target / f"capitulo-{n:02d}")
                       for n in TITULOS]
            gravar(target / "resumo.json", json.dumps(
                [{"capitulo":r["capitulo"], "estado":r["estado"]}
                 for r in reports], ensure_ascii=False, indent=2) + "\n")
            for r in reports:
                print(f"{r['capitulo']:02d}: {r['estado']}")
            return 1 if any(r["estado"] == "FAIL" for r in reports) else 0
        report = ensaio(args.capitulo, target)
        print(f"Capítulo {report['capitulo']:02d}: {report['estado']}")
        print(f"Evidência: {target / 'resultado.json'}")
        return 1 if report["estado"] == "FAIL" else 0
    except (OSError, ValueError, subprocess.SubprocessError) as exc:
        print("NO-GO:", exc, file=sys.stderr)
        return 2

if __name__ == "__main__":
    raise SystemExit(main())
