# Relatório da rodada v1.3 — laboratórios livro e jogo

**Data:** 13/11/2026. **Estado:** PARTIAL — primeira passada. Os resultados demonstram capacidades delimitadas; não autorizam publicação editorial final.

## Entregas

- Capítulo 17 — `chapters/17-a-editora-que-aprende-a-conferir.qmd` (primeira redação).
- Capítulo 18 — `chapters/18-um-jogo-nao-e-jogavel-so-porque-compila.qmd` (primeira redação).
- `tools/editorial/auditar_fontes_quarto.py`: recursos locais, duplicatas `fig-/sec-/tbl-/lst-`, descrição de imagem e aviso de linhas longas de código.
- `tools/jogos/replay_minijogo.py`: simulador de regras e replay, sem emulator de TK90X/MSX.
- Cenários JSON positivo e negativo em `examples/jogos/`.
- Novos testes unitários, mais dois passos na CI que preservam a falha negativa esperada.

## Verificações executadas

| Prova | Resultado | Alcance |
| --- | --- | --- |
| Preservação de index e capítulos 1–16 | PASS byte a byte | Não alterados nesta rodada |
| `verificar_estrutura.py` | PASS (18 capítulos) | Numeração automática e lista de fontes |
| `verificar_boxes.py` | PASS (18 + 18) | Um box IA e um experimento do leitor em cada capítulo |
| `unittest discover` | PASS 72/72 | Testes das ferramentas e do controlador, não do conteúdo |
| Auditor de fontes Quarto | PASS_LIMITED; 1 WARNING | Linha longa: capítulo 9, linha 57, 97 caracteres (limiar 94); não prova corte da página |
| Replay positivo | PASS_SIMULATION, código 0 | Pontuação 100, 3 vidas, estado preservado, sem emulador |
| Replay negativo | FAIL_REPLAY esperado, código 2 | Expectativa de score 200 rejeitada, mantendo score real 100 |
| PDF de leitura via Pandoc/XeLaTeX | GERADO, 234 páginas | Prévia, NÃO PDF nativo Quarto nem miolo pronto |
| Quadro de código em PDF (234 págs.) | FAIL (9 ocorrências) | 6 na pág. 64, 2 na pág. 118 e 1 na pág. 128; checagem geométrica limitada |
| Fonte tipográfica na compilação PDF | WARNING | Glifo de seta `→` indisponível em variante `Noto Serif ExtraBold`; requer conferência visual na passada gráfica |
| Páginas novas | INSPEÇÃO AMOSTRAL | Págs. 198–202 e 211–218, amostras sem corte visível nessas capturas |
| Teste de jogo no openMSX/TK90X | NÃO TESTADO | Não há ROM/arquivo de jogo para emulação neste laboratório |
| Revisão humana dos capítulos | PENDENTE | Primeira passada; revisão por blocos depois da conclusão |

A existência de falhas editoriais adicionais **não reveladas pelo autor** está registrada. Este relatório não declara que elas foram encontradas, nem que não existem outras falhas.

## Próximas provas

- Confirmar que o workflow de GitHub Actions compila a versão Quarto HTML e executa a nova bateria Python no servidor.
- Desenvolver o laboratório de hardware (cap. 19), sem inventar netlists ou medidas de bancada.
- Aplicar a mesma matriz de evidências aos três domínios (cap. 20) e à publicação viva (cap. 21).
- Ao completar a primeira passada, fatiar o livro em blocos DOCX e auditar toda a diagramação, inclusive os casos ainda não identificados e os avisos de glifos.
- Testar a oficina no Manual Técnico do TK2000, com linha de base própria e aprovação do autor.
