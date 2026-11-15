# Estudo de caso do capítulo 21 — O método diante de um manual técnico

**Material complementar de _IA fazendo IA — ou quase_ · José Albuquerque · 15/11/2026**

**Resultado geral: `PARTIAL`.** Esta página apresenta resultados agregados, metodologia e limites. Não distribui o manual utilizado, relatórios privados, dados pessoais, credenciais ou caminhos de trabalho.

## O que foi investigado

Uma cópia autorizada de um bloco do Manual Técnico do TK2000 foi submetida a duas abordagens: um workflow com sequência pré-determinada e um agente supervisionado que selecionou verificações conforme os resultados intermediários. Uma política independente impediu publicação não autorizada. O original foi preservado.

## O que foi observado

| Verificação | Resultado do ensaio |
| --- | --- |
| Títulos reais dos capítulos presentes na cópia | 4 |
| Cabeçalhos candidatos, incluindo índice e subseções | 74 |
| Figuras e legendas estruturais | 9 figuras, 9 legendas |
| Tabelas | 7 |
| Estado da auditoria estrutural | `PASS_LIMITED` |
| Decisões de escolha de ferramenta registradas | 6 |
| Propostas textuais, sujeitas à revisão | 3 |
| Sinalizações editoriais adicionais | 2 |
| Tentativa de publicação | `BLOCKED` |
| Alteração no original | Não |

As contagens estruturais não demonstram, por si, que a diagramação esteja correta. A análise visual de uma prova de 47 páginas identificou: uma legenda de estilo diferente, uma figura separada de sua legenda e duas tabelas com continuação sem cabeçalhos repetidos.

O relatório preliminar da etapa visual ainda registrava aprovação humana pendente. O relato posterior de encerramento informa autorização e correções **somente numa cópia candidata**. Esses registros correspondem a momentos diferentes; não constituem autorização para modificar o documento original.

A campanha foi encerrada para esta edição, sem promover o resultado `PARTIAL` a `PASS`. A identidade nativa do modelo, os tokens, custos, a verificação editorial independente completa e a correção dos circuitos eletrônicos **não foram comprovados por este ensaio**.

## Experimento para reproduzir com seus próprios arquivos

1. Crie um ambiente descartável chamado `laboratorio-ia`, com as subpastas `entrada`, `saida` e `evidencias`.
2. Use uma cópia de um documento fictício, sem informações privadas. Registre sua versão e um hash SHA-256 antes da avaliação.
3. Defina uma auditoria determinística: contagem de títulos, figuras, legendas e tabelas. Guarde a saída bruta.
4. Repita com um agente autorizado somente a ler, escolher verificadores e **propor** diferenças. Grave qual ferramenta foi escolhida e por quê, antes de executá-la.
5. Execute uma prova visual em PDF ou imagem. Compare os achados estruturais e os visuais.
6. Peça ao autor que classifique as propostas como aceitas, rejeitadas ou não verificadas. Não aplique nenhuma alteração sem autorização.
7. Compare os hashes de antes e depois e publique apenas um relatório sanitizado, sem o documento analisado.

O [laboratório do capítulo 21](../laboratorio/capitulo-21.html) reúne exercícios complementares. Para praticar uma comparação determinística de arquivos, consulte também o [script público do capítulo 13](../scripts/comparar_arquivos.py).

## O que este caso ensina

O workflow é uma boa escolha para verificações repetíveis. Um agente pode acrescentar interpretação e seleção adaptativa de ferramentas, mas suas decisões ainda precisam de evidência e revisão. Uma auditoria estrutural não substitui a prova visual; uma proposta aprovada em cópia não é permissão para modificar o original.

**A conclusão vale além da retrocomputação:** o mesmo cuidado se aplica a manuais, relatórios, documentos profissionais, software e projetos de pesquisa.
