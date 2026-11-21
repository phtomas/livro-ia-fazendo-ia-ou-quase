# LAB-AGENTE-01 — Crie seu primeiro agente de IA

Complemento de *IA fazendo IA — ou quase*. [Abrir videoaula e oficina guiada](index.html) · [YouTube](https://youtu.be/wYtrOdUyZvU) · [Evidências](EVIDENCIAS.md).

Requisitos: Python 3.11+ recomendado, terminal; nenhuma biblioteca externa. Baixe o ZIP do repositório em Code → Download ZIP, extraia e abra esta pasta (laboratorio/agente-matinal). No Windows use `py -3` se necessário; no Linux/macOS use `python3`. Nunca use dados reais.

```bash
python briefing.py --data 2026-11-23
python -m unittest discover -s tests -v
```

O código é um workflow determinístico: lê três JSONs, valida o contrato local, filtra tarefas e mensagens por prazo e compromissos por data. A saída rastreável está em saida-referencia.txt. O modelo de IA, quando conectado pelo leitor, pode usar a ferramenta e interpretar os resultados; essa etapa ainda requer comprovação. Os arquivos AGENTS.md, CLAUDE.md e GEMINI.md instruem cada ambiente. O Codex utiliza .agents/skills/; o Claude Code, .claude/skills/; o Gemini CLI aceita .agents/skills/ como alias de .gemini/skills/. Não é necessário duplicar a skill nesse último.

As instruções não são uma sandbox. Use uma cópia isolada, somente leitura onde possível, sem conectores pessoais; aprove apenas o comando conhecido. A data é fixa para reproduzir o exemplo. Agendamento de produção e extração dinâmica de prazos estão fora deste ensaio. Veja a oficina HTML para a construção em etapas, exemplos completos, exercícios e precauções.
