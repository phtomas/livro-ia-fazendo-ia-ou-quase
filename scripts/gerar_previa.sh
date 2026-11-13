#!/usr/bin/env bash
# Provas Pandoc, não publicação Quarto nativa. Executar no diretório do projeto.
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."
OUT="${1:-dist}"
mkdir -p "$OUT"
OUT="$(realpath "$OUT")"
FILES=(index.qmd chapters/01-um-livro-que-aprende.qmd appendices/10-principios.qmd appendices/glossario.qmd references.qmd)
BASE=(pandoc -f markdown+fenced_divs+citations+smart --citeproc --lua-filter filters/boxes.lua --bibliography references.bib --csl estilo-referencias.csl --metadata-file book-meta.yaml)
python scripts/verificar_boxes.py
"${BASE[@]}" "${FILES[@]}" -t html5 -s --toc --toc-depth=2 --css=styles.css --embed-resources -o "$OUT/IA_fazendo_IA_Leitura_no_navegador_v0.4.html"
"${BASE[@]}" "${FILES[@]}" -t epub3 --toc --css=styles.css -o "$OUT/IA_fazendo_IA_Leitura_preliminar_v0.4.epub"
"${BASE[@]}" "${FILES[@]}" -o "$OUT/IA_fazendo_IA_Previa_de_leitura_v0.4.pdf" --pdf-engine=xelatex --include-in-header=pdf-preambulo.tex -V documentclass=report -V papersize=a5 -V geometry:paperwidth=160mm -V geometry:paperheight=230mm -V geometry:top=22mm -V geometry:bottom=22mm -V geometry:left=22mm -V geometry:right=21mm -V mainfont='Noto Serif' -V sansfont='Noto Sans' -V fontsize=11pt -V linestretch=1.22 -V parskip=half -V colorlinks=true -V linkcolor=black -V urlcolor=black --toc --toc-depth=2
pdfinfo "$OUT/IA_fazendo_IA_Previa_de_leitura_v0.4.pdf" | grep Pages
printf 'Provas geradas em %s\n' "$OUT"
