# Auditoria editorial — segunda passada, rodada inicial

**Obra:** *IA fazendo IA — ou quase*  
**Base imutável avaliada:** prévia integral v1.4, 21 capítulos, PDF 265 páginas, gerada em 13/11/2026.  
**Estado:** **PARTIAL / FAIL_LAYOUT / REVISÃO AUTORAL PENDENTE.** O PASS das ferramentas não autoriza publicação.

## O que fizemos nesta rodada

1. Conferimos a integridade da referência PDF por SHA-256 e preservamos o original.
2. Reexecutamos os testes Python: **101/101 PASS** (os 94 anteriores, quatro novos testes da auditoria de paginação e três testes da definição dos blocos DOCX).
3. Conferimos a estrutura dos 21 capítulos e os dois tipos de atividade didática: **PASS estrutural**, sem validar sua qualidade de conteúdo.
4. Leitura geométrica das **265 páginas** para identificar finais de capítulo anormalmente curtos; inspeção visual dos cinco candidatos.
5. Reaproveitamos a auditoria de código já executada na v1.4: nove ocorrências de transbordamento.
6. Preparamos um **Bloco A editável em DOCX**, com Apresentação e capítulos 1 a 4 (39 páginas na renderização local de revisão). O Word é interface de leitura e revisão; o Quarto continua canônico. As citações permanecem no texto; a bibliografia será revisada no bloco próprio, sem repetição desnecessária em cada bloco.

## Ocorrências novas — finais de capítulo curtos

| Página física no PDF v1.4 | Conteúdo aproximado | Observação visual | Prioridade |
|---:|---:|---|---|
| **113** | 190 caracteres | Somente poucas linhas no alto da página, final do capítulo anterior | Revisar paginação |
| **186** | 360 caracteres | Dois parágrafos curtos no alto | Revisar paginação |
| **198** | 196 caracteres | Fechamento muito curto no alto | Revisar paginação |
| **211** | 379 caracteres | Um parágrafo curto no alto | Revisar paginação |
| **233** | 145 caracteres | Apenas duas linhas e muito espaço em branco | **Prioridade maior** |

**Nota técnica:** o identificador `PAGINA_FINAL_CURTA` é uma *suspeita mensurável*; nem toda página curta é um erro. Uma pessoa deve decidir se a distribuição é intencional e se há solução editorial que não sacrifique a leitura.

## Ocorrências anteriores mantidas

| Classe | Local | Estado |
|---|---|---|
| Trechos monoespaçados saindo do quadro | PDF v1.4 p. **65** (6), **119** (2) e **129** (1) | **FAIL de layout**, nove ocorrências |
| Glifo de seta `→` ausente em variante Noto Serif ExtraBold | Avisos na compilação v1.4 | **PENDENTE**; conferir aplicação e substituição tipográfica correta |
| Linhas longas em fontes Quarto | Relatório QA de fontes v1.4 | Avisos, não prova de corte no PDF |
| Pequenas falhas não especificadas pelo autor | Localização desconhecida | **ABERTAS**; não presumir correção |

A auditoria geométrica não detecta todas as situações: legendas órfãs, alteração de sentido, fontes inconsistentes, citações incorretas, hierarquia editorial indevida, reescrita fria, erros técnicos e material gráfico fraco exigem verificadores adicionais ou leitura humana.

## Protocolo para cada bloco DOCX

1. Preservar a v1.4 como referência; não usar o DOCX como fonte canônica direta.
2. Conferir os critérios de edição (voz, português brasileiro, clareza, fidelidade técnica, progressão didática, caixas independentes, notas, citações e ilustrações).
3. Fazer revisão do autor no DOCX, de preferência com alterações controladas.
4. Comparar o bloco alterado com o original; categorizar alterações aprovadas, dúvidas e regressões.
5. Integrar apenas as alterações aprovadas nos `.qmd`; renderizar novamente e verificar HTML, EPUB e PDF.
6. Reexecutar a auditoria. A diminuição de falhas só será PASS se não forem introduzidas novas falhas.

### Blocos previstos

- **A:** Apresentação e capítulos 1–4 — **DOCX preliminar gerado e renderizado**.
- **B:** capítulos 5–8 — preparar.
- **C:** capítulos 9–12 — preparar.
- **D:** capítulos 13–16 — preparar.
- **E:** capítulos 17–21 — preparar.
- **F:** anexos, glossário, bibliografia e elementos pré-textuais — preparar.

## Limites da prova

- A versão PDF avaliada foi produzida com Pandoc/XeLaTeX, não por PDF nativo do Quarto. O site Quarto HTML permanece uma prova distinta.
- O DOCX do Bloco A foi gerado por Pandoc a partir dos mesmos `.qmd`, com estilos editáveis específicos para `NA PRÁTICA COM A IA` e `EXPERIMENTO DO LEITOR`, renderizado e revisado por contato de páginas. Não é a diagramação final de impressão.
- A inspeção visual realizada foi dirigida aos achados e ao Bloco A; **não** constitui revisão humana detalhada de todas as 265 páginas.
- **Nenhum defeito da referência PDF v1.4 foi corrigido nesta rodada.** O objetivo é primeiro encontrar, classificar e preparar a revisão sob aprovação humana.

## Evidências e comandos

- PDF SHA-256: `c758421dac37a4815f84170ebabb72c4f26595b72eceeca72c5a80bfe365660f`
- DOCX Bloco A SHA-256: `970c2ca60618840d38056b40e47e5bdae0a2ed74ee7aa808d0dd90c65ad2f7a5` (Bloco A definitivo de 39 páginas).
- `python tools/editorial/auditar_paginacao_pdf.py PREVIA.pdf --json docs/AUDITORIA_PAGINACAO_v1.4.json`
- `python tools/editorial/verificar_pdf_boxes.py PREVIA.pdf`
- `python -m unittest discover -s tests -p 'test_*.py'`
- `python scripts/verificar_boxes.py .`
- `python scripts/verificar_estrutura.py .`
- `python scripts/gerar_blocos_docx.py A --out Bloco_A.docx --apply`

**Próximo gate:** revisão editorial do primeiro bloco pelo autor; os problemas globais permanecerão na matriz até comprovação de correção, sem mascarar o FAIL conhecido.
