# Relatório da rodada v1.0 — capítulos 11 e 12, ciclo supervisionado e avaliação

**Contexto:** primeira passada do livro. Nenhum conteúdo anterior deve ser considerado aprovado sem leitura do autor.

| Verificação | Estado observado | Escopo e ressalva |
| --- | --- | --- |
| Testes unitários | **PASS — 34/34** | `python -m unittest discover -s tests -p 'test_*.py' -q` |
| Boxes de prática | **PASS estrutural — 12 capítulos** | Presença dos seis marcadores exigidos; não julga utilidade |
| Experimentos do leitor | **PASS estrutural — 12 capítulos** | Marcadores presentes, exercícios independentes de prompts |
| Numeração | **PASS estrutural** | Capítulos 1–12; anexos e apresentação sem números |
| Ciclo supervisionado de leitura | **PASS_LIMITED** | Três operações observadas, sem LLM ou edição |
| Tentativa supervisionada de publicação | **HALTED_POLICY, comportamento esperado** | Bloqueio em `PUBLISH`; etapa seguinte não executada |
| Verificador numérico | **PASS_LIMITED / FAIL_GUARDRAIL** | Preservação didática de +5V / detecção de troca +5V→+12V |
| Preservação de conteúdo antigo | **PASS — 11 arquivos idênticos byte a byte** | Apresentação e capítulos 1–10 não modificados |
| Prévia PDF | **GERADA — 161 páginas** | Pandoc+XeLaTeX, formato 160×230mm; não renderização Quarto nativa |
| Prévia HTML/EPUB | **GERADAS** | Pandoc; o GitHub Actions executará Quarto HTML após commit |
| Verificador completo de transbordamento PDF | **FAIL — 9 ocorrências** | Páginas 62 (6), 116 (2), 126 (1). As ocorrências pertencem a capítulos anteriores; foram preservadas e ainda não corrigidas. |
| Layout completo, qualidade técnica e aprovação autoral | **NÃO APROVADOS** | Inspeção de algumas páginas novas não cobre a obra inteira |

## Observações de engenharia editorial

A linha de base anterior já continha o defeito observado pelo autor e registrado na v0.6. Na v1.0, nosso detector encontrou **nove ocorrências em quadros claros** ao percorrer todas as 161 páginas; isso não significa que capturou todos os erros de layout. O detector tem falsos negativos possíveis. O autor identificou outras falhas sem descrevê-las, intencionalmente, para testar a capacidade de descoberta; **não podemos reivindicar que essas falhas foram encontradas ou corrigidas**.

O relatório de uma política que bloqueou publicação **não representa falha operacional do controle**; representa o comportamento exigido para aquele caso. O resultado global da obra continua **PARTIAL / FAIL_LAYOUT_KNOWN**.

O ciclo não possui planejador LLM conectado, não cria aprovações e não publica. Uma decisão humana autenticada exige infraestrutura não implementada. A integridade de números não prova interpretação técnica.

## Evidências

- `docs/EXECUCAO_CICLO_LEITURA_v1.0.json`
- `docs/EXECUCAO_CICLO_BLOQUEIO_v1.0.json`
- `docs/QA_DETECTOR_v1.0.json`
- Código e testes versionados junto com esta revisão.
