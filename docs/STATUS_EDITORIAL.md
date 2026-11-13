# Estado editorial — 2026-11-13

- Apresentação: rascunho v0.2 revisado para revisão do autor.
- Capítulo 1: rascunho v0.2 revisado para revisão do autor.
- Capítulos 2–5: agora redigidos em primeira passada, revisão autoral pendente. Capítulos 6–21: apenas esboçados no projeto editorial.
- Ainda sem avaliações formais de fidelidade da voz ou validação da paginação.
- Quarto não está instalado neste ambiente, logo ainda não foi possível validar renderização nativa.
- Bibliografia e créditos: fontes públicas primárias citadas no corpo; seguir auditando antes da publicação.
- A autoria formal, a licença e as políticas de distribuição ainda serão definidas pelo autor.

## Notas v0.2

- Glossário e princípios: incluídos como anexos preliminares; revisão de conteúdo e de terminologia ainda pendente.
- Distinção corrigida: P9 trata de reaproveitar com crédito; P10 é Simbiose e cuidado.
- Diagramação revista: antigos quadros apertados convertidos em fichas, com separação vertical.
- Renderização nativa Quarto ainda pendente; previews Pandoc podem ser geradas para revisão e não são provas de compatibilidade Quarto.

- Preview Pandoc v0.2: PDF de leitura 16 × 23 cm com 29 páginas inspecionado; EPUB e HTML gerados; NÃO confundir com PDF de miolo pronto para KDP ou UICLAP.

## Revisão v0.3 — boxes didáticos

- Confirmado o padrão NA PRÁTICA COM A IA em fontes das três obras técnicas já publicadas/preparadas.
- Exercício existente promovido a box na primeira atividade do capítulo 1, mais um novo box dedicado à regressão editorial e um terceiro no Anexo A; demais passagens da v0.2 preservadas.
- Novo estudo de caso sobre falha de regressão editorial e prevenção por contrato, exemplos e teste.
- Novo `docs/CONTRATO_EDITORIAL.md` e `scripts/verificar_boxes.py`.
- Testar nova renderização e registrar veredito técnico separado da aprovação do autor.

## Revisão v0.4 — autonomia do leitor como recurso distinto

- A leitura de IA fazendo jogos revelou duas estruturas didáticas complementares: o box NA PRÁTICA COM A IA e o EXPERIMENTO DO LEITOR autônomo.
- O capítulo 1 ganhou um experimento novo, independente da IA, que convida o leitor a descobrir regras autorais implícitas em textos próprios. Os dois boxes de IA e a narrativa anterior permaneceram sem alterações.
- Criada diagramação e tratamento semântico próprios para os experimentos em HTML/EPUB/PDF.
- Contrato editorial e verificador atualizados: dois recursos são identificados separadamente; ausência de experimento exige avaliação editorial, não criação automática de conteúdo irrelevante.
- Quarto nativo ainda não foi renderizado neste ambiente; provas geradas com Pandoc (não finais). Revisão de voz e aprovação autoral pendentes.


## Rodada v0.5 — 13/11/2026

- Capítulos 2 e 3 produzidos como **rascunhos para leitura do autor**.
- Cada capítulo possui um box de uso da IA e um experimento do leitor autônomo; a qualidade depende de revisão humana.
- O Capítulo 3 relata o caso GitHub 403 da redação desta obra, usando apenas fatos registrados; os registros JSON são expressamente fictícios e didáticos.
- Prova final de integração reservada ao Manual Técnico do TK2000: `docs/PROVA_FINAL_TK2000.md`. O manuscrito TK2000 não foi modificado.
- A fonte Quarto passa a incluir os novos capítulos. Bibliografia técnica adicionada com fontes primárias.
- O Quarto ainda não foi executado neste ambiente; qualquer prévia com Pandoc deve ser identificada como **prévia não nativa**.

## Revisão v0.6 — numeração e capítulos 4–5

- Contrato: capítulos e seções numerados automaticamente; prefixo `Capítulo` no sumário PDF/HTML. Capítulos em `.qmd` conservam títulos sem número manual.
- Apresentação e anexos não numerados; subtítulos internos igualmente marcados como `.unnumbered`.
- Capítulos 4 e 5 redigidos; cada um contém box NA PRÁTICA COM A IA e EXPERIMENTO DO LEITOR; revisão humana pendente.
- Plano da segunda passada visual em docs/PLANO_VISUAL_SEGUNDA_PASSADA.md; figuras e dados ainda não gerados.
- Preview com Pandoc e PDF scrreprt; fonte canônica Quarto com `number-sections`, `number-depth` e `toc-depth`; compilação Quarto nativa ainda pendente.
- Falta revisão autoral do texto; não chamar o capítulo de aprovado por teste estrutural.

## Rodada v0.7 — voz autoral e os primeiros componentes reutilizáveis

- Capítulo 6 redigido em primeira passada, com comparação concreta entre livro, jogo e hardware, um box de uso da IA e um experimento autônomo do leitor. **Ainda não revisado pelo autor**.
- Uma skill candidata foi empacotada em `skills/revisao-autoral/SKILL.md` segundo a especificação Agent Skills. **Não instalada nem avaliada num runtime de agentes**.
- A ferramenta `tools/editorial/verificar_pdf_boxes.py` executa checagem geométrica de texto monoespaçado que transborda quadros claros em PDF. Sua capacidade é limitada a esse tipo de artefato; não é um verificador de toda a diagramação.
- Dois testes unitários sintéticos (um PASS_LIMITED, um FAIL) executados. O PDF v0.6, página 59, reproduziu a condição conhecida com seis spans fora do limite; o documento fonte e o PDF v0.6 não foram corrigidos.
- `workflows/auditoria_editorial.py` encadeia validações sem LLM, sem alteração ao manuscrito, e produz relatórios; resultado da linha de base PDF esperado é PARTIAL_KNOWN_FAIL.
- Arquivo `agents/orquestrador-editorial.md` contém **apenas projeto de arquitetura**, não implementação.
- Matriz livro × jogo × hardware registrada em `docs/MATRIZ_LIVRO_JOGO_HARDWARE.md`, sem modificações retroativas nos capítulos 1 a 5.
- Documentos em `docs/` distinguem baseline conhecido e status dos componentes.
- Quarto nativo ainda não foi renderizado neste ambiente; as provas Pandoc são prévias, não miolo aprovado.

## Emenda editorial v0.7.1 — apresentação do TK2000 e plano de revisão por blocos

- Acrescentada somente uma passagem de contextualização do *Manual Técnico do TK2000* à Apresentação (`index.qmd`), em linguagem destinada ao leitor; capítulos 1–6 não foram alterados.
- Criado `docs/PLANO_REVISAO_POR_BLOCOS.md`: a revisão humana acontecerá após a primeira passada, com documentos editáveis por blocos, diffs e reintegração controlada.
- O manual TK2000 permanece intocado. O plano e o texto da Apresentação não equivalem à execução de teste final.
- Quarto nativo no Windows do autor ainda deve ser instalado e testado. PDF 0.7 não foi regenerado nesta emenda.
