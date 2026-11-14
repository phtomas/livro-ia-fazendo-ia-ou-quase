#!/usr/bin/env bash
# Provas Pandoc, não publicação Quarto nativa. Executar no diretório do projeto.
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."
OUT="${1:-dist}"
mkdir -p "$OUT"
OUT="$(realpath "$OUT")"
FILES=(index.qmd chapters/01-um-livro-que-aprende.qmd chapters/02-nomes-e-contratos.qmd chapters/03-por-dentro-do-agente.qmd chapters/04-quando-criar-um-agente.qmd chapters/05-provas-custos-e-seguranca.qmd chapters/06-a-voz-que-a-ferramenta-nao-deve-apagar.qmd chapters/07-tres-portas-para-a-mesma-oficina.qmd chapters/08-uma-skill-que-pode-viajar.qmd chapters/09-o-fluxo-que-sabe-onde-parou.qmd chapters/10-quem-deixa-o-agente-decidir.qmd chapters/11-o-primeiro-ciclo-supervisionado.qmd chapters/12-quando-uma-skill-merece-confianca.qmd chapters/13-a-ferramenta-que-nao-precisa-de-opiniao.qmd chapters/14-duas-copias-uma-historia.qmd chapters/15-os-frameworks-nao-decidem-por-nos.qmd chapters/16-medindo-a-oficina.qmd chapters/17-a-editora-que-aprende-a-conferir.qmd chapters/18-um-jogo-nao-e-jogavel-so-porque-compila.qmd appendices/10-principios.qmd appendices/glossario.qmd references.qmd)
BASE=(pandoc -f markdown+fenced_divs+citations+smart+tex_math_dollars+tex_math_single_backslash --citeproc --lua-filter filters/boxes.lua --bibliography references.bib --csl estilo-referencias.csl --metadata-file book-meta.yaml --number-sections --top-level-division=chapter)
python scripts/verificar_boxes.py
"${BASE[@]}" "${FILES[@]}" -t html5 -s --toc --toc-depth=2 --css=styles.css --embed-resources -o "$OUT/IA_fazendo_IA_Leitura_no_navegador_v1.3.html"
"${BASE[@]}" "${FILES[@]}" -t epub3 --toc --css=styles.css -o "$OUT/IA_fazendo_IA_Leitura_preliminar_v1.3.epub"
"${BASE[@]}" "${FILES[@]}" -o "$OUT/IA_fazendo_IA_Previa_de_leitura_v1.3.pdf" --pdf-engine=xelatex --include-in-header=pdf-preambulo.tex -V documentclass=scrreprt -V papersize=a5 -V geometry:paperwidth=160mm -V geometry:paperheight=230mm -V geometry:top=22mm -V geometry:bottom=22mm -V geometry:left=22mm -V geometry:right=21mm -V mainfont='Noto Serif' -V sansfont='Noto Sans' -V fontsize=11pt -V linestretch=1.22 -V parskip=half -V colorlinks=true -V linkcolor=black -V urlcolor=black --toc --toc-depth=2
pdfinfo "$OUT/IA_fazendo_IA_Previa_de_leitura_v1.3.pdf" | grep Pages
printf 'Provas geradas em %s\n' "$OUT"
