# Inventário da oficina — v0.7 (13/11/2026)

Este arquivo distingue **conteúdo escrito**, **código executado**, **regras formalizadas** e **autonomia ainda planejada**. A existência de uma pasta não é prova de integração com uma plataforma.

| Peça | Caminho | Estado verificado | Limite |
|---|---|---|---|
| Contrato editorial histórico | `docs/CONTRATO_EDITORIAL.md` | DOCUMENTADO | Qualidade/voz dependem do autor |
| Perfil de voz | `voice/VOICE_PROFILE.md` | HIPÓTESE NÃO APROVADA | Não chamar de perfil canônico |
| Skill de revisão autoral | `skills/revisao-autoral/SKILL.md` | ESTRUTURA CRIADA, não instalada | Sem avaliação no runtime de modelos |
| Contrato por domínio | `skills/revisao-autoral/references/contratos-por-dominio.md` | DOCUMENTADO | Adaptações dependem de caso real |
| Tool PDF | `tools/editorial/verificar_pdf_boxes.py` | TESTADA com positivos/negativos; 6 trechos fora do quadro p.59 | Detecta apenas spans mono em quadros claros; não substitui inspeção visual |
| Tool cópia | `tools/arquivos/copia_provada.py` | TESTADA em diretórios temporários; hashes iguais | Apenas pasta plana, sem symlink, sem sobrescrita |
| Workflow de auditoria | `workflows/auditoria_editorial.py` | EXECUTADO; estrutura PASS e PDF FAIL conhecido | Não revisa a voz, não corrige, não publica |
| Projeto de agente | `agents/orquestrador-editorial.md` | DESENHADO | Nenhum loop de LLM ou integração externa implementados |
| Matriz de domínios | `docs/MATRIZ_LIVRO_JOGO_HARDWARE.md` | DOCUMENTADA | Adaptar na narrativa sem repetição |
| Prova final TK2000 | `docs/PROVA_FINAL_TK2000.md` | PLANEJADA | Manual real ainda não editado nesta rodada |

## Execuções reprodutíveis

```bash
python -m unittest discover -s tests -p 'test_*.py' -v
python tools/editorial/verificar_pdf_boxes.py /caminho/para/IA_fazendo_IA_Capitulos_1_a_5_v0.6.pdf --page 59
python workflows/auditoria_editorial.py . --pdf /caminho/para/IA_fazendo_IA_Capitulos_1_a_5_v0.6.pdf --pdf-page 59 --report dist/auditoria.json
python tools/arquivos/copia_provada.py /caminho/origem /caminho/destino
```

O detector de PDF **retorna código 1** quando encontra erro, e o workflow também sinaliza `PARTIAL_KNOWN_FAIL` (código 1) quando a estrutura passa e o PDF reprova. Esse é um resultado esperado para a linha de base v0.6, mas **continua sendo FAIL na dimensão de layout**. Falha estrutural resulta código 2 no workflow.

## Diferença entre construir e usar

- Uma skill com instruções bem estruturadas não foi necessariamente ativada ou usada por um agente.
- Uma tool que passou por testes locais não está automaticamente conectada a uma conversa ou serviço.
- Um workflow de scripts determinísticos não é, por si só, um agente baseado em IA.
- Um projeto de agente só passa a ser agente demonstrado depois que seu ciclo de decisão e seus limites forem implementados e testados.

## Próximas provas

1. Rever com o autor a fidelidade do texto do Capítulo 6.
2. Executar a skill em um ambiente compatível de verdade e medir a diferença entre revisão com e sem contrato.
3. Expandir detector de PDF para exemplos em boxes de outros estilos e imagens fora da margem.
4. Implementar o controlador de aprovações do agente — sem credenciais embutidas — e verificar que um erro de permissão suspende a execução.
5. Testar um bloco representativo do Manual TK2000 sem alterá-lo antes da autorização específica.
6. Reproduzir uma melhoria de layout da página 59 **apenas em versão futura e com comparação**, preservando o PDF defeituoso histórico como fixture.


## Atualização v0.8

| Peça | Local | Estado comprovado | Ainda não comprovado |
| --- | --- | --- | --- |
| Capítulos 7–8 | `chapters/07-*`, `chapters/08-*` | Texto e marcadores estruturais presentes | Voz aprovada, acabamento final, entendimento do leitor |
| Instalador local de skill | `tools/skills/instalar_skill_local.py` | Testes unitários de dry-run, cópia por hash, idempotência, conflito, backup, metadata e symlinks | Instalação na máquina do autor ou em produto remoto |
| Skill revisão autoral | `skills/revisao-autoral/` | Pacote canônico legível e integridade de cópia local | Descoberta, ativação e qualidade da revisão num host real |
| Matriz de compatibilidade | `docs/PORTABILIDADE_SKILLS.md` | Documentação de caminhos e condições consultadas em 13/11/2026 | Portabilidade futura em qualquer versão; execução cruzada |

**Regra:** não confundir integridade dos arquivos com eficácia da habilidade. `PASS` local não preenche campos de ensaio de host.


## Atualização v0.9 — orquestração com fronteiras explícitas

| Peça | Caminho | Comprovado | Não comprovado |
|---|---|---|---|
| Workflow com checkpoint | `workflows/fluxo_com_checkpoints.py` | Inventário SHA-256, injeção de falha, retomada, bloqueio por alteração e gate de estrutura em testes locais | Conexão com Drive/GitHub, transações distribuídas, concorrência |
| Política determinística | `agents/politica_orquestrador.py` | Retorno de ações permitidas / bloqueadas nos testes unitários | Enforcement em executor externo, acesso a LLM, autorização autenticada |
| Agente editorial | `agents/orquestrador-editorial.md` | Arquitetura descrita | Loop autônomo completo, uso de modelos, aprovação real |
| Capítulos 9–10 | `chapters/09-*`, `chapters/10-*` | Texto e marcadores didáticos | Revisão autoral, avaliação didática com leitores |

**Atenção:** checkpoint vinculado a hashes dos fontes `.qmd`, `index.qmd` e `_quarto.yml`; ainda não monitora alterações em versões de verificadores nem dependências externas. A política limita apenas uma decisão de demonstração, não a execução de ferramentas.
