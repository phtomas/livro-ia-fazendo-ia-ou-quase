# Rodada v1.2 — testes e limites

**Escopo:** Capítulos 15 e 16, contrato para avaliação de frameworks e ferramenta local de consolidação de execuções sintéticas. Nenhuma API de modelos é chamada. Os capítulos 1–14 e a Apresentação foram preservados no manuscrito.

## Matriz de evidências

| Verificação | Estado | Limitação |
|---|---|---|
| Estrutura de capítulos e boxes | PASS — 16 capítulos | Estrutura não mede qualidade de prosa |
| Ferramenta de custos e tokens | PASS local — 56 testes totais | Aceita registros declarados; não autentica provedor |
| Custo com tarifas sintéticas | PASS aritmético — 3 registros sintéticos | Não é preço de API real |
| Identificação de modelo efetivo | REGRA IMPLEMENTADA | Prova externa dos dados ainda não coletada |
| Benchmark LangGraph/CrewAI/Microsoft/OpenAI/Google | NÃO EXECUTADO | Apenas documentação oficial comparada |
| Análise PDF visual e transbordamentos | FAIL_LAYOUT_KNOWN — 9 ocorrências | Erros anteriores continuam pendentes |
| Quarto HTML no GitHub Actions | A conferir após commit | Não equivale à prova de PDF impresso |
| Aprovação autoral | NÃO REALIZADA | Primeira passada ainda incompleta |

Os resultados abaixo foram obtidos localmente antes do commit. PASS de ferramentas não substitui aprovação editorial.

## Resultado observado (13/11/2026)

- `python -m unittest discover -s tests -p 'test_*.py' -q`: **56/56 PASS**, incluindo 12 novos casos do laboratório de medição. Na primeira tentativa a suíte acusou uma falha porque o controlador estrutural ainda não listava os dois capítulos; após atualizar `_quarto.yml`, a segunda execução passou.
- `scripts/verificar_boxes.py`: PASS nos **16 capítulos** e presença de 16 experimentos do leitor; `scripts/verificar_estrutura.py`: PASS estrutural e capítulos numerados.
- Ferramenta de custos: entrada sintética `SINT-002` retornou **US$0,0104** de inferência estimada com tarifa **fictícia**. Em `SINT-003`, a ausência de modelo identificado e uso medido resultou em campos `null`, não zero. O caso sem modelo `SINT-001` é uma etapa determinística, não uma inferência.
- Prévia com Pandoc/XeLaTeX: **208 páginas**, capítulos 15 e 16 nas páginas 173 e 185. A renderização Quarto nativa em PDF **não** foi realizada nesta rodada. Uma amostra de 8 páginas dos dois capítulos foi renderizada e inspecionada; inspeção visual integral ainda não realizada.
- Detector geométrico do PDF: **FAIL — nove transbordamentos**: páginas 63 (6), 117 (2), 127 (1). As ocorrências são as mesmas da v1.1, com a mesma paginação até o final dos capítulos antigos. O detector não cobre todas as falhas tipográficas ou de sentido. **Nenhuma correção nos capítulos antigos** foi feita.
- Comparação de bytes: Apresentação e capítulos 1–14 **idênticos** aos arquivos contidos no ZIP v1.1.
- Prova da API de frameworks externos: **NÃO EXECUTADA**. Resumo de execuções sintéticas não prova chamadas a modelos nem faturamento.

**Resultado editorial: PARTIAL/FAIL_LAYOUT_KNOWN.** Aprovação humana, revisão por blocos, figuras da segunda passada e testes com modelos reais permanecem pendentes.
