# IA fazendo IA — ou quase (manuscrito de trabalho)

Este repositório local contém o **manuscrito editorial v0.6**, em primeira passada e ainda não aprovado para publicação. O arquivo `index.qmd` é a apresentação; `chapters/01-...` a `chapters/05-...` contêm os cinco primeiros capítulos. Os anexos de princípios e glossário têm texto inicial; capítulos 6–21 permanecem no sumário editorial, sem texto completo. Não extrapole o estado de avanço.

## Como gerar o livro

1. Instale Quarto (https://quarto.org/docs/get-started/).
2. Abra um terminal na raiz deste diretório.
3. Execute `quarto render --to html` para a versão web; `quarto render --to epub` para um EPUB; `quarto render --to pdf` para PDF (requer uma distribuição TeX compatível).
4. Os resultados devem aparecer em `_book/`. Confira visualmente links, acentos, tabelas, blocos e referências em cada formato.

## Estado de verificação

- Fonte Markdown/Quarto e YAML preparada: SIM.
- Fontes bibliográficas inseridas e urls examinadas: SIM, revisão adicional antes de publicação.
- Roteiro e capítulos ainda sujeitos à revisão de voz pelo autor: SIM.
- Quarto instalado no ambiente desta primeira preparação: NÃO.
- Renderização Quarto e inspeção visual de EPUB/PDF/HTML: NÃO REALIZADAS aqui.
- Repositório GitHub remoto criado: SIM; `phtomas/livro-ia-fazendo-ia-ou-quase`, público.
- Publicação KDP/UICLAP: NÃO.

## Contratos editoriais

P1: honestidade acima de tudo, sem resultados inventados.

P9: não reinventar a roda e dar crédito à origem de ideias, métodos e recursos.

P10: simbiose e cuidado, com parceria responsável e crescimento conjunto. As produções derivadas em áudio/vídeo não podem introduzir informações novas sem verificação.

O Git remoto já contém o manuscrito. Permanecem pendentes aprovação do perfil de voz, licenciamento e validação de publicação.

## Revisão v0.2 — solicitação do autor em 13/11/2026

- Apresentação: sinalização discreta de humor com :-) na brincadeira do ferro de solda.
- Capítulo 1: parágrafo de autoria destacado; tabela estreita substituída por cinco fichas com respiro vertical; exercício redistribuído em blocos separados.
- Referências: preferir a expressão brasileira **Acessado em** e não *acedido*.
- Novo glossário vivo: appendices/glossario.qmd.
- Novo anexo: appendices/10-principios.qmd, baseado nos documentos autorais Códex do Método v2 e Anexo de Princípios; o P10 canônico é **Simbiose e cuidado**, e o P9 conserva a obrigação de crédito.
- Recomendação editorial: desenvolver mais adiante capítulo específico sobre a criação do método e como o leitor constrói princípios próprios; o anexo já introduz o tema.

## Visualização e notas de compilação v0.2

O pacote inclui `styles.css` para espaçamento dos exemplos e prefixo de capítulo no HTML/EPUB, `estilo-referencias.csl` com termo pt-BR **acessado em** e `pdf-preambulo.tex` para evitar a quebra de fichas conceituais no PDF. Os arquivos `book-meta.yaml` e `pdf-preambulo.tex` servem também à prévia com Pandoc.

**Validações locais da prévia Pandoc (não Quarto):** PDF em 16 × 23 cm; sem texto cortado, destaque integral, fichas de conceitos não divididas, bibliografia usando “Acessado em” e glossário sem página órfã. EPUB validado como arquivo ZIP e presença de capítulos confirmada. Repetir a verificação após renderização nativa do Quarto.

## Box “NA PRÁTICA COM A IA” — contrato transversal

A v0.3 recupera o recurso didático das obras anteriores. Exemplos e regras estão em `docs/CONTRATO_EDITORIAL.md`. A forma é implementada em `styles.css` (HTML/EPUB) e `filters/boxes.lua` + `pdf-preambulo.tex` (PDF). Execute `python scripts/verificar_boxes.py` antes de gerar qualquer edição. Esse teste verifica **estrutura**, não a qualidade do conteúdo.

**Atenção:** somente novos trechos foram inseridos nesta revisão; não foi autorizada uma reescrita geral dos textos da v0.2.

## Revisão v0.4 — uma didática em duas frentes

O box **NA PRÁTICA COM A IA** demonstra uma operação reproduzível, normalmente com prompt e verificação. O **EXPERIMENTO DO LEITOR** é uma atividade independente de investigação pessoal, com hipótese, observação e conclusão próprias. Um não substitui o outro. A distinção nasce do método usado em *IA fazendo jogos* e está detalhada em `docs/CONTRATO_EDITORIAL.md`.

O Capítulo 1 conserva os dois boxes da v0.3 e recebeu um experimento autônomo que dispensa IA. O arquivo `scripts/verificar_boxes.py` identifica separadamente os componentes; a qualidade didática segue sujeita à revisão humana. Foi feita comparação de texto (somente inserções no Capítulo 1) e prova Pandoc em PDF/EPUB/HTML. Quarto nativo ainda não foi renderizado.

## Próximo assunto didático: tokens e roteamento de modelos

A pauta `docs/TOKENS_ROTEAMENTO_E_CUSTOS.md` foi acrescentada ao planejamento, **sem alterar a redação já aprovada para análise**. Vamos comparar algoritmos locais, modelos menores, escalonamento e medições reais de entrada/saída. O contador de tokens, quando for implementado, terá de distinguir previsão, medição e preço do provedor. Nenhum resultado de laboratório foi declarado PASS nesta etapa.

**Repositório remoto:** `phtomas/livro-ia-fazendo-ia-ou-quase` já criado e público por configuração atual. Revisar licença antes da distribuição definitiva.


## Rodada v0.5 — Capítulos 2 e 3, prova final TK2000

- O Capítulo 1 e a apresentação não foram reescritos nesta rodada.
- Novos rascunhos: `chapters/02-nomes-e-contratos.qmd` e `chapters/03-por-dentro-do-agente.qmd`, cada um com box **NA PRÁTICA COM A IA** e **EXPERIMENTO DO LEITOR** independentes.
- Requisito decisivo do autor: a **prova final do método** será editar o *Manual Técnico do TK2000*, com fidelidade de ilustrações, voz, tom, didática e publicação, sem fechar artificialmente pendências de engenharia. Plano: `docs/PROVA_FINAL_TK2000.md`.
- Pendente: aprovação autoral dos novos capítulos, ensaios reproduzíveis com agentes e renderização Quarto nativa. A prévia Pandoc não é prova final do projeto.
- Repositório remoto foi criado e recebeu commits no GitHub. Confirmar visibilidade e licença antes de publicar quaisquer arquivos de terceiros ou do livro TK2000.

## Revisão v0.6 — numeração e primeira passada de redação

- Livro com capítulos 1–5 e anexos. Os dois novos são `chapters/04-quando-criar-um-agente.qmd` e `chapters/05-provas-custos-e-seguranca.qmd`.
- Títulos e subseções numerados automaticamente; **não incluir `Capítulo N` ou `N.1` nos headings da fonte**. O CSS e o preâmbulo PDF exibem `Capítulo N` no sumário.
- `scripts/gerar_previa.sh` gera provas via Pandoc (HTML, EPUB e PDF), **não são renderizações nativas do Quarto**.
- O plano de figuras e fluxogramas está em `docs/PLANO_VISUAL_SEGUNDA_PASSADA.md`; produzir imagens úteis e auditáveis na segunda revisão, não imagens decorativas.
- Os boxes de uso da IA e os experimentos do leitor permanecem distintos. Testar scripts e revisar visualmente as páginas.
- GitHub remoto já existe e é público; substituir notas antigas sobre inexistência por este estado; a licença editorial está pendente de decisão autoral.
