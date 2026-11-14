# Relatório da rodada v1.4 — primeira passada completa

**Data:** 13/11/2026. **Escopo:** capítulos 19–21, três ferramentas locais, contratos didáticos, inventário de versão, reprodução da prévia PDF/HTML/EPUB.

## Resultados que foram executados

| Verificação | Resultado | Limitação |
| --- | --- | --- |
| 21 fontes `.qmd` e numeração automática | PASS estrutural | Não avalia linguagem nem veracidade |
| Boxes de prática e experimentos autônomos dos 21 capítulos | PASS estrutural | Não aprova qualidade didática |
| Testes Python locais | **94/94 PASS** | Programas não testam compreensão do leitor |
| Fiscal de hardware (dados sintéticos) | `PASS_RASTREABILIDADE` / `FAIL_EVIDENCIA` esperado | Nenhuma placa física, nenhuma execução de KiCad |
| Pré-voo dos adaptadores (dados fictícios) | `COMPATIVEL_DECLARADO`, `BLOQUEADO_POR_CAPACIDADE`, `INDETERMINADO` | Não executou ChatGPT/Claude/Gemini |
| Inventário Quarto | `FONTE_INVENTARIADA`: **21 capítulos**, autoria pendente | Não aprova layout nem impressão |
| Auditoria das fontes | `PASS_LIMITED`, 1 WARNING | Uma linha de código longa no Capítulo 9; não prova corte |
| Pandoc + XeLaTeX, PDF leitura 16 × 23cm | Gerado, **265 páginas** | Não é renderização Quarto nativa ou miolo homologado |
| Detector geométrico do PDF inteiro | **FAIL: 9 transbordamentos** | Busca apenas código em determinados boxes; não avalia todo o livro |
| Avisos de compilação | 4 mensagens de glifo seta ausente | Necessário inspeção/correção na fase tipográfica |
| Amostras visuais das páginas 224–260 | Inspecionadas | Não equivale à conferência visual das 265 páginas |
| Comparação da Apresentação e Capítulos 1–18 com v1.3 | **Idênticos byte a byte** | Novos capítulos e arquivos de controle são mudanças previstas |

**Regressão importante:** o primeiro PDF desta rodada revelou dez transbordamentos: os nove históricos e um novo no Capítulo 20, decorrente de um caminho de arquivo longo em código inline. Alteramos apenas a redação daquele trecho do Capítulo 20 e recompilamos. O novo detector retornou nove ocorrências, sem o novo transbordamento. Este histórico não deve ser apagado.

## Achados ainda não resolvidos

- PDF com nove cortes: página 65 (6), 119 (2), 129 (1). As páginas mudaram em relação à v1.3 pela paginação; os fragmentos correspondem aos casos já documentados.
- Glifo seta com ausência reportada pelo XeLaTeX/Noto Serif ExtraBold. Nenhum acerto cosmético foi feito nesta passada.
- Outras pequenas falhas editoriais foram comunicadas pelo autor mas intencionalmente não descritas. **Não sabemos quais são**; não declarar sucesso na detecção.
- A primeira passada ainda não contém todas as ilustrações previstas. Fase gráfica posterior; sem dados quantitativos inventados.
- A autoria do texto e o fechamento editorial dependem de revisão por blocos. A prova externa TK2000 não foi executada.

## Gates para continuar

- **PASS_SOURCE_DRAFT:** 21 capítulos redigidos e presentes na fonte.
- **PASS_CODE:** 94 testes locais aprovados; repetir em GitHub Actions após commit.
- **FAIL_LAYOUT_KNOWN:** cortes de código não resolvidos, aviso tipográfico pendente.
- **PENDENTE_AUTOR:** voz, precisão, referências, figuras e versão definitiva.
- **PENDENTE_QUARTO_PDF:** o PDF local foi feito com Pandoc, não Quarto nativo.

A publicação GitHub Pages é uma prévia. A ocorrência de PASS no workflow HTML, quando confirmada após o commit, não alterará as pendências acima.
