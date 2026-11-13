# Relatório de validação v0.9 — capítulos 9–10 e componentes de controle

**Data:** 13/11/2026. **Escopo:** primeira passada dos capítulos 9 e 10, rotina de checkpoint local, política demonstrativa e referências. Não houve alteração da Apresentação nem dos capítulos 1–8.

| Teste / critério | Resultado | Evidência e limite |
|---|---|---|
| Identidade da v0.8 | PASS | Apresentação e capítulos 1–8 com SHA-256 idênticos à pasta de referência v0.8 |
| Estrutura Quarto e numeração | PASS | `python scripts/verificar_estrutura.py` identificou dez capítulos |
| Dois recursos didáticos | PASS estrutural | `python scripts/verificar_boxes.py`: prática e experimento separados em todos os dez capítulos |
| Unitários | PASS — 23 testes | `python -m unittest discover -s tests -p 'test_*.py' -q` |
| Interrupção e retomada da fonte real | PASS limitado | `--fail-at after-inventory`: saída 4; repetição no mesmo snapshot: saída 0 e `WAITING_HUMAN` |
| Política de ação real | PASS limitado | `PUBLISH` exige revisão humana, `CHECK_STRUCTURE` permite apenas leitura; `is_executed=false` |
| PDF de leitura via Pandoc | GERADO | 142 páginas no formato de prova 16 × 23 cm; amostras dos capítulos 9–10 a inspecionar |
| Renderização nativa Quarto HTML | PENDENTE de GitHub Actions | Rodará após commit; não alegar PASS antes de leitura do run |
| Agente com modelo e executor integrado | NÃO EXECUTADO | Existe apenas a política determinística; conexão externa não foi feita |
| PDF v0.6 página 59 | FAIL conhecido | Não foi corrigido; preservado segundo decisão do autor |
| Aprovação autoral e miolo de impressão | NÃO APROVADOS | A primeira passada continua em andamento |

**Limitações conhecidas:** checkpoint local não resolve concorrência, transações distribuídas, alteração de dependências nem prova de autoria; política não executa nem impõe restrições a serviços externos. A integração Drive ↔ GitHub é mantida por atualização explícita nesta rodada, não por sincronização nativa.
