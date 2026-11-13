# Relatório de verificação da rodada v1.1

**Data:** 13/11/2026. **Escopo:** dois capítulos novos, comparador de espelhos e preservação dos arquivos anteriores. O livro segue em primeira passada, ainda sem aprovação autoral.

| Gate | Resultado | Condição observada |
| --- | --- | --- |
| Testes unitários | **PASS 44/44** | Inclui 10 testes do comparador offline, sem credenciais |
| Contrato dos dois boxes | **PASS estrutural** | 14 capítulos com NA PRÁTICA COM A IA e EXPERIMENTO DO LEITOR independente |
| Numeração e sumário | **PASS estrutural** | 14 capítulos no `_quarto.yml` e no gerador Pandoc, sem números digitados |
| Preservação de texto anterior | **PASS: 13 arquivos iguais por bytes** | Apresentação e capítulos 1–12 conferidos diretamente contra a v1.0 |
| Demonstração de conflito | **RECONCILIACAO_PENDENTE** | Duas alterações incompatíveis reconhecidas e sem sobrescrita |
| Teste da ferramenta em provedores remotos | **NÃO TESTADO** | Não se afirma sincronização GitHub ↔ Google Drive por esta ferramenta |
| Prévia PDF | **GERADA — 183 páginas** | Pandoc/XeLaTeX, 160×230mm, não renderização Quarto PDF nativa |
| PDF — detector monoespaçado | **FAIL — 9 ocorrências** | Página 63 (6), 117 (2), 127 (1); casos anteriores mantidos |
| Inspeção visual das novas páginas | **AMOSTRAL** | Abertura dos caps. 13/14, um box e trechos internos conferidos; não substitui inspeção integral |
| Nova falha editorial observada pelo autor | **ABERTA, NÃO IDENTIFICADA** | O autor não descreveu a falha para permitir teste cego posterior |
| Aprovação final | **PENDENTE** | Primeira passada ainda em andamento; revisão em blocos futura |

O comparador é uma tool local. Não acessa provedores, não resolve conflitos, não altera fontes nem produz commits. O caso de conflito foi gerado em diretórios temporários e não deve ser apresentado como teste de sincronização remoto.

**Observação:** 44 testes passando não implicam livro aprovado; o estado global é **PARTIAL / FAIL_LAYOUT_KNOWN**. A nova ocorrência editorial relatada sem detalhes não pode ser chamada de encontrada ou resolvida.

## Evidências

- `tools/sync/conferir_espelhos.py`, `tests/test_conferir_espelhos.py`
- `docs/EXEMPLO_CONFLITO_ESPelhos_v1.1.json`
- `docs/QA_DETECTOR_v1.1.json`
- O commit e a execução nativa Quarto HTML no GitHub serão associados após a publicação.
