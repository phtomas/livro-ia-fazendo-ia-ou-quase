# Relatório de testes — versão v0.7

**Data:** 13/11/2026 · **Status:** PARCIAL com FAIL conhecido de diagramação; versão editorial **não aprovada**.

## Resultados executados

1. `python -m unittest discover -s tests -p 'test_*.py' -v` — **5 testes PASS**, incluindo cópia e hash, recusa de sobrescrita, recusa de destino aninhado, PDF limpo e PDF com transbordamento simulado.
2. `python scripts/verificar_boxes.py` — **PASS estrutural** em seis capítulos (o teste não mede voz nem legibilidade).
3. `python scripts/verificar_estrutura.py` — **PASS estrutural**, verificou que os seis capítulos constam dos destinos Quarto/Pandoc.
4. `python tools/editorial/verificar_pdf_boxes.py ... --page 59` na v0.6 — **FAIL conhecido** com 6 trechos monoespaçados além do retângulo, exatamente a falha apontada pelo autor.
5. `python workflows/auditoria_editorial.py ...` — **PARTIAL_KNOWN_FAIL**, estrutura PASS e layout FAIL (código de retorno 1); nenhum arquivo de manuscrito alterado.
6. `bash scripts/gerar_previa.sh` — **PASS de geração da prévia Pandoc** (PDF de 96 páginas, formato 16 × 23 cm, mais HTML/EPUB); **não é validação nativa Quarto**.
7. Detector executado na prévia PDF v0.7 inteira — **6 ocorrências na página 59**; defeito preservado de modo consciente, sem correção silenciosa.
8. Comparação de conteúdo — **8 arquivos anteriores preservados byte a byte** (Apresentação, Capítulos 1–5, filtro de boxes e CSS).
9. Inspeção humana de amostras — abertura do Capítulo 6 e box de prática foram rasterizados e visualmente examinados; **não equivale à inspeção integral das 96 páginas**.

## O que não foi executado

- Nenhuma skill foi ativada num ambiente real de agente.
- Nenhum agente com ciclo de decisão, API ou roteador de modelos foi implementado.
- Nenhuma medição de custo/tokens de API ocorreu.
- Nenhuma alteração foi aplicada ao Manual Técnico do TK2000.
- Nenhuma correção foi feita na página 59.
- Nenhuma compilação usando o binário Quarto ocorreu.

## Conclusão

**PASS das ferramentas e regras estruturais dentro do escopo testado. FAIL conhecido de layout. Aprovação do autor e aptidão para publicação: NÃO VERIFICADAS.**

A prova final continuará exigindo comparação de versões, inspeção técnica e revisão do autor. Nenhum PASS de ferramenta pode substituir essas etapas.
