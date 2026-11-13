# Estado editorial — 2026-11-13

- Apresentação: rascunho v0.2 revisado para revisão do autor.
- Capítulo 1: rascunho v0.2 revisado para revisão do autor.
- Capítulos 2–21: apenas esboçados no documento editorial v0.3, não incluídos neste pacote.
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
