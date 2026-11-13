# Relatório de regressão — revisão v0.3

Data-base: 13/11/2026

## Ocorrência

A v0.2 não tinha o box transversal **NA PRÁTICA COM A IA**, presente nas três obras técnicas anteriores da série. A revisão do autor detectou a omissão. Havia exercício prático, mas não estava tratado com a identidade didática aprovada.

## Solução mínima

- O exercício pré-existente do Capítulo 1 foi transformado no primeiro box, conservando seu conteúdo.
- Um segundo box acompanha o relato real da regressão e fornece um prompt para auditar materiais editoriais sem alterar nada.
- O Anexo A ganhou um box para o leitor formular seus próprios princípios.
- Adicionado `docs/CONTRATO_EDITORIAL.md` com regras verificáveis e `scripts/verificar_boxes.py` para identificar ausência e incompletude.
- Estilo cross-format em CSS e filtro Lua/LaTeX para PDF. A validação foi feita com Pandoc, não pelo executável Quarto.

## Testes

| Ensaio | V0.2 | V0.3 |
|---|---|---|
| Estrutura exigida nas fontes de capítulo | FAIL — box ausente | PASS — dois boxes completos |
| Preservação de apresentação e glossário | Baseline | PASS — bytes idênticos |
| Preservação de parágrafos externos aos boxes | Baseline | PASS — comparação textual literal |
| Anexo A original | Baseline | PASS — conteúdo original preservado, adição ao final |
| HTML | Não avaliado aqui | PASS — três contêineres de box detectados |
| EPUB | Não avaliado aqui | PASS — ZIP válido e textos presentes |
| PDF | Prova anterior | PASS técnico preliminar — 31 páginas, fontes legíveis e nenhum bloco fora da página detectado |
| Validação pelo Quarto | Pendente | Pendente (executável indisponível no ambiente) |
| Aprovação autoral | Pendente | Pendente |

Um dos boxes mais extensos atravessa duas páginas na prova PDF. A quebra foi preservada para manter tamanho legível e evitar áreas em branco excessivas. Essa é uma decisão de diagramação provisória, a rever no miolo final para KDP/UICLAP.

## Parecer

**PASS estrutural / PARTIAL editorial / NO-GO para publicação.** A revisão corrige a perda do recurso didático, mas não encerra a revisão de voz, a inspeção fina do miolo ou a homologação Quarto.
