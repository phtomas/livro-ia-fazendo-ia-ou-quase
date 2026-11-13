# Relatório de verificação da rodada v0.8

**Escopo:** acréscimo dos capítulos 7 e 8, adaptação da fonte Quarto, documentação de portabilidade e instalador local de Agent Skill. Nenhum texto dos capítulos 1–6 foi reescrito.

| Gate | Resultado | Prova / ressalva |
| --- | --- | --- |
| Capítulos e boxes | PASS estrutural | `scripts/verificar_boxes.py` encontrou prática e experimento autônomo nos oito capítulos |
| Numeração | PASS estrutural | `scripts/verificar_estrutura.py` confirmou numeração automática e apresentação/anexos não numerados |
| Unitários locais | PASS — 13 testes | `python -m unittest discover -s tests -p 'test_*.py' -v` |
| Skill — simulação | PASS local | Nenhum arquivo de destino escrito sem `--apply` |
| Skill — transporte | PASS local limitado | Cópia para `.agents/skills` e `.claude/skills` em diretório temporário, com SHA-256 igual |
| Skill — proteção | PASS local limitado | Conflito bloqueado sem `--replace`, backup antes de substituição autorizada, symlink de origem recusado |
| Descoberta no Claude Code/Gemini/Codex | **NÃO TESTADO** | Exige instalação e execução no host correspondente |
| Qualidade da revisão autoral | **NÃO TESTADO** | Exige corpora de casos, comparação e aprovação autoral |
| Layout PDF página 59 baseline v0.6 | **FAIL conhecido** | Caso `EDITORIAL-PDF-059` preservado intencionalmente; sem correção nesta revisão |
| Publicação Quarto no GitHub Pages | A conferir após commit | Renderização nativa de HTML por Actions não implica PDF final aprovado |
| Publicação editorial | **NÃO APROVADA** | Primeira passada do livro ainda incompleta; revisão em blocos ocorrerá ao final |

**Cuidado:** um FAIL corrigido durante desenvolvimento deve aparecer no histórico do teste. Na primeira execução dos novos testes, o leitor de YAML confundiu a linha vazia depois do metadado `description: >-` e produziu cinco erros. Ajustamos o parser para retirar a quebra inicial; 13 testes passaram na rodada subsequente. Não considerar o primeiro erro como PASS retroativo.
