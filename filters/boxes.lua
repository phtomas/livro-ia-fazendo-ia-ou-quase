-- Reproduz o box 'NA PRÁTICA COM A IA' em HTML/EPUB e PDF.
-- No HTML/EPUB, o CSS formata o Div; em LaTeX, tcolorbox.
function Div(el)
  local pratica = el.classes:includes('na-pratica-com-ia')
  local experimento = el.classes:includes('experimento-do-leitor')
  if not pratica and not experimento then return nil end
  if FORMAT:match('latex') then
    local blocks = pandoc.Pandoc(el.content)
    local latex = pandoc.write(blocks, 'latex')
    local boxopts = pratica and [=[\begin{tcolorbox}[enhanced,breakable,fontupper=\small,colback=praticaBg,colframe=praticaBorder,boxrule=0.55pt,leftrule=2.2pt,arc=1.8pt,left=7pt,right=7pt,top=6pt,bottom=6pt,before skip=11pt,after skip=13pt]]=] or [=[\begin{tcolorbox}[enhanced,breakable,fontupper=\small,colback=experimentoBg,colframe=experimentoBorder,boxrule=0.35pt,toprule=1.8pt,arc=0pt,left=7pt,right=7pt,top=7pt,bottom=7pt,before skip=14pt,after skip=14pt]]=]
    return {
      pandoc.RawBlock('latex', boxopts),
      pandoc.RawBlock('latex', latex),
      pandoc.RawBlock('latex', [[\end{tcolorbox}]])
    }
  end
  return el
end
