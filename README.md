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

## Rodada v0.7 — produzir, não apenas descrever

O Capítulo 6 foi incluído na primeira passada editorial: voz autoral e como ela se traduz em **livro**, **jogo** e **hardware**. O capítulo contém um box `NA PRÁTICA COM A IA` e um `EXPERIMENTO DO LEITOR` autônomo. Sua aprovação editorial continua pendente.

Nesta rodada acrescentamos uma **skill candidata** em `skills/revisao-autoral/`, duas **tools determinísticas** em `tools/`, um **workflow executável** em `workflows/`, a **arquitetura (não implementação)** de um agente em `agents/` e uma matriz comparativa em `docs/MATRIZ_LIVRO_JOGO_HARDWARE.md`. O estado preciso de cada peça está no [inventário](docs/INVENTARIO_DE_ARTEFATOS.md).

**Linha de base conhecida:** a página 59 do PDF de leitura v0.6 apresenta linhas de código saindo do retângulo. Foi preservada, conforme decisão do autor. O detector identifica esse erro e registra `FAIL`, sem alterá-lo. O workflow declara `PARTIAL_KNOWN_FAIL`, não um PASS editorial. Confira `docs/CASES_DE_REGRESSAO.md`.

Para executar as verificações locais, com Python 3.11+ e PyMuPDF instalado:

```sh
python -m unittest discover -s tests -p 'test_*.py' -v
python scripts/verificar_boxes.py
python scripts/verificar_estrutura.py
python tools/editorial/verificar_pdf_boxes.py /caminho/para/a/previa_v0.6.pdf --page 59
python workflows/auditoria_editorial.py . --pdf /caminho/para/a/previa_v0.6.pdf --pdf-page 59 --report dist/auditoria.json
```

Nenhuma dessas operações chama API de IA, escreve no manuscrito ou publica no GitHub. A skill ainda precisa ser testada no ambiente do agente escolhido, e o agente descrito no diretório `agents/` não existe como programa funcional.

## Emenda v0.7.1 — o segundo livro e a revisão em blocos

A Apresentação passou a explicar ao leitor o Manual Técnico do TK2000 como obra independente já em desenvolvimento e prova final externa do método. O plano de revisão por blocos editáveis está em `docs/PLANO_REVISAO_POR_BLOCOS.md`, sem alterar capítulos previamente escritos.

## Rodada v0.8 — ambientes, portabilidade e transporte verificado

- Capítulos 7 e 8, em primeira passada: as famílias ChatGPT, Claude e Gemini; transporte de um contrato entre ambientes; escrita, empacotamento e teste de uma Agent Skill.
- O livro continua a comparar **livro, jogo e hardware** e a preservar os boxes `NA PRÁTICA COM A IA` e `EXPERIMENTO DO LEITOR` de maneira independente.
- Novo `tools/skills/instalar_skill_local.py`: copia a skill canônica para diretórios locais compatíveis em modo de simulação (padrão), com preflight, hashes SHA-256, detecção de conflito e backup em substituições autorizadas. Não instala recursos em contas online nem invoca modelos.
- `tests/test_instalar_skill_local.py` testa comportamento local de transporte. PASS nesses testes não comprova ativação ou eficácia da skill em ChatGPT, Claude Code, Gemini CLI ou Codex. Ver `docs/PORTABILIDADE_SKILLS.md` e `docs/RELATORIO_DE_TESTES_v0.8.md`.
- Fonte versionada: GitHub `main`. Espelho da pasta Quarto no Drive do autor em `Projetosia/Livro — IA fazendo IA (ou quase)/02_Manuscrito/Quarto_Fonte`. Prévia web pública renderizada pelo GitHub Actions e publicada no Pages se o build passar. **Não há sincronização automática bidirecional entre Drive e GitHub**.
- O defeito `EDITORIAL-PDF-059` da prévia PDF v0.6 continua um caso conhecido preservado, sem correção nesta rodada. Provas locais de Pandoc não substituem Quarto nativo nem aprovação de publicação.

## Rodada v0.9 — checkpoints e política de orquestração (Capítulos 9 e 10)

A primeira passada passa a incluir dez capítulos. O Capítulo 9 ensina estados, idempotência e retomada usando o programa determinístico `workflows/fluxo_com_checkpoints.py`. O Capítulo 10 introduz a separação entre propostas de um modelo e a autorização da oficina, com `agents/politica_orquestrador.py`. **Nenhum dos dois é um agente autônomo, e nenhum publica ou altera fontes.**

Os novos testes em `tests/test_fluxo_com_checkpoints.py` e `tests/test_politica_orquestrador.py` cobrem interrupção, retomada, bloqueio de fontes alteradas e política de permissão. O controlador trabalha com estado fora do projeto, sem credenciais e sem acesso a redes; a integração com GitHub/Drive permanece tarefa separada. Rodar `python -m unittest discover -s tests -p 'test_*.py' -v` e `python scripts/verificar_boxes.py`. O defeito da página 59 da baseline PDF v0.6 continua explicitamente aberto e não foi corrigido.

Para executar laboratório sem modificar o manuscrito:

```sh
python workflows/fluxo_com_checkpoints.py . --work ../ensaio-checkpoint --fail-at after-inventory
python workflows/fluxo_com_checkpoints.py . --work ../ensaio-checkpoint
python agents/politica_orquestrador.py --action PUBLISH
```

O PDF Pandoc é prova de leitura, não miolo final. A prévia Quarto HTML é gerada pelo workflow em `.github/workflows/previa-quarto.yml` a cada commit em `main`, com publicação no GitHub Pages. O projeto Quarto fonte é espelhado para o Google Drive do autor (`Projetosia/.../Quarto_Fonte`), sem ligação automática entre Git e Drive.


## Rodada v1.0 — ciclo supervisionado e avaliação da skill

- Capítulos 11 e 12 em primeira redação; Capítulos 1 a 10 e a Apresentação **sem qualquer alteração**.
- `agents/ciclo_supervisionado.py`: ciclo operacional de leitura e propostas, com política aplicada em cada passo. Lê planos externos JSON e para diante de ações bloqueadas. **Não possui integração a LLM** e não publica nada.
- `tools/editorial/avaliar_proposta.py`: fiscal limitado de números/unidades e expressões protegidas; nunca substitui revisão de conteúdo, de voz ou aprovação humana.
- Exemplos em `examples/`, testes em `tests/`; relatórios em `docs/RELATORIO_DE_TESTES_v1.0.md`.
- Defeito histórico da página 59 da v0.6 permanece como fixture conhecida. A ausência de detecção na página 59 da v0.9 não equivale a correção, porque o detector não encontrou quadro elegível nessa página.
- Leitura web: https://phtomas.github.io/livro-ia-fazendo-ia-ou-quase/ (atualizada após commit e sucesso do GitHub Actions).


## Rodada v1.1 — Capítulos 13 e 14 e auditoria de cópias

Os capítulos `13-a-ferramenta-que-nao-precisa-de-opiniao.qmd` e `14-duas-copias-uma-historia.qmd` completam o primeiro laboratório sobre tools determinísticas, revisão de cópias e responsabilidades entre GitHub, Drive e Quarto. A tool `tools/sync/conferir_espelhos.py` **não sincroniza arquivos**: compara árvores locais, calcula SHA-256 e emite JSON, impedindo automaticamente a ideia de que a cópia mais recente é a correta. Para executar: `python tools/sync/conferir_espelhos.py --canon DIR_A --espelho DIR_B --report fora_das_pastas.json`. A opção `--snapshot` cria manifesto prévio, permitindo classificar mudanças unilaterais e concorrentes.

Os novos testes são locais; nem o transporte entre provedores nem a reconciliação automática foram homologados. Preservar as falhas editoriais anteriores e a nova ocorrência não detalhada pelo autor para a revisão final em blocos. Esta rodada não corrige textos anteriores.


## Rodada v1.2 — frameworks e instrumentos de medição

A primeira passada agora inclui os Capítulos 15–16. O Capítulo 15 apresenta cinco famílias de frameworks com um **protocolo de aceitação proposto**, não um benchmark de desempenho. Consulte `docs/CONTRATO_AVALIACAO_FRAMEWORKS.md`.

O Capítulo 16 acompanha `tools/observabilidade/resumir_execucoes.py`, exemplos sintéticos de consumo de tokens e tarifas fictícias. O analisador **não faz chamadas de IA**, não autentica registros de provedor e não pode inferir o modelo realmente executado.

```sh
python -m unittest discover -s tests -p 'test_*.py' -v
python tools/observabilidade/resumir_execucoes.py --runs examples/metricas/execucoes_sinteticas.jsonl --rates examples/metricas/tarifas_ficticias.json --output dist/metricas.json
```

O Drive do autor é um espelho de trabalho e o GitHub é o histórico versionado. A publicação no Pages continua sujeita ao workflow e à confirmação de resultado. Problemas de layout e as ocorrências editoriais deliberadamente não reveladas pelo autor permanecem em aberto para a segunda passada.
