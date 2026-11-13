# Estado editorial — 2026-11-13

- Apresentação: rascunho v0.2 revisado para revisão do autor.
- Capítulo 1: rascunho v0.2 revisado para revisão do autor.
- **Estado atual:** Capítulos 1–8 redigidos em primeira passada; capítulos 9–21 ainda previstos no projeto editorial. Revisão autoral integral pendente.
- As notas abaixo documentam estados históricos sucessivos e não substituem o estado atual.
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

## Emenda v0.7.1 — TK2000 contextualizado e revisão por blocos

- Acrescentada uma passagem narrativa à Apresentação situando o Manual Técnico do TK2000 como livro independente que será a prova externa do método.
- Criado `docs/PLANO_REVISAO_POR_BLOCOS.md`. O autor examinará blocos editáveis depois de concluída a primeira passada; esta emenda não iniciou a revisão.

## Rodada v0.8 — capítulos 7–8 e transporte local de skills

- Capítulos 7 `Três portas para a mesma oficina` e 8 `Uma skill que pode viajar sem perder o endereço` incluídos na fonte; cada capítulo possui box NA PRÁTICA COM A IA e EXPERIMENTO DO LEITOR autônomo.
- Comparação entre ChatGPT, Claude e Gemini feita por tipos de ambiente, contexto e permissões; não há benchmark nem ranking de modelos. Informações operacionais dependem de produto e versão.
- Ferramenta `tools/skills/instalar_skill_local.py`: empacotamento e instalação local com simulação, validação mínima de frontmatter, hash, prevenção de sobrescrita e backup. A execução em diretório temporário foi testada; **não foi provado carregamento ou comportamento em nenhum dos aplicativos externos**.
- 13 testes unitários locais PASS. Verificação estrutural dos oito capítulos PASS. Essas evidências não aprovam voz, segurança total, paginação ou publicação.
- Capítulos 1–6 não foram reescritos. A Apresentação segue a emenda v0.7.1. A falha `EDITORIAL-PDF-059` permanece registrada como defeito conhecido da prova v0.6, sem correção.
- Quarto nativo no GitHub Pages deverá ser verificado depois do commit; prévia Pandoc local não é publicação final.


## Rodada v0.9 — Capítulos 9–10 e coordenação com estado

- Capítulos 9 e 10 redigidos em primeira passada: workflow com checkpoints, retomada, idempotência, política de permissões e papel do agente. Cada capítulo possui os dois recursos didáticos distintos e comparação livro/jogo/hardware; aprovação autoral ainda pendente.
- Novo `workflows/fluxo_com_checkpoints.py`: só lê fontes e executa verificadores existentes; grava estado externo à árvore do projeto e bloqueia reutilização de checkpoints de fontes modificadas. **Não é processamento transacional concorrente ou execução de LLM.**
- Novo `agents/politica_orquestrador.py`: avaliação determinística de nomes de ações; nega operações desconhecidas e exige aprovação humana para publicar ou modificar. **Não executa a ação nem constitui agente autônomo.**
- Testes cobrem interrupção induzida, retomada, mudança de fonte, reprovação estrutural e políticas. Os capítulos 1–8 e a Apresentação foram preservados byte a byte em comparação com a v0.8.
- Defeito `EDITORIAL-PDF-059` da prova v0.6 preservado intencionalmente; nenhuma afirmação de PASS gráfico global. Quarto PDF final, aprovação autoral e ensaios em serviços externos continuam pendentes.


## Rodada v1.0 — um ciclo supervisionado e a avaliação mecânica de revisões

- Capítulos 11 e 12 redigidos, com boxes de prática e experimentos autônomos, ambos sujeitos à leitura e aprovação do autor depois da primeira passada.
- O ciclo supervisionado recebe plano externo e chama adaptadores locais permitidos. **Não é prova de que um modelo escolheu ferramenta, nem um agente LLM autônomo instalado**.
- A avaliação de propostas numéricas cobre apenas os tokens e trechos protegidos; `PASS_LIMITED` não confirma fatos nem voz.
- Os erros não descritos que o autor identificou foram deliberadamente mantidos fora do conhecimento do processo para a revisão final; não presumir ausência de erros pelo PASS dos verificadores.
- O PDF histórico com problema na página 59 não foi modificado.
