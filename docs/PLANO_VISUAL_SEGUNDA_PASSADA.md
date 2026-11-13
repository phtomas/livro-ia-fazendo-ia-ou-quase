# Plano visual — segunda passada editorial

**Livro:** IA fazendo IA — ou quase  
**Estado:** pauta, não imagens aprovadas. Primeira passada prioriza narrativa e exemplos verificáveis; segunda passada produzirá apenas figuras que esclareçam decisões, relações ou resultados.

## Regra

1. Figura precisa responder a uma pergunta real do leitor. Evitar ilustrações decorativas de “robôs escrevendo código”.
2. Preferir fluxogramas, arquiteturas e diagramas vetoriais editáveis; gráficos quantitativos só com dados reais datados e fonte identificada.
3. Cada figura terá fonte técnica, legenda em português brasileiro, destino no texto e teste de legibilidade em 16 × 23 cm e eBook.
4. O próprio autor aprovará figuras relevantes; nenhuma foto ou esquema será redesenhado como se fosse fiel à placa real sem comparação com a fonte.
5. Os boxes “NA PRÁTICA COM A IA” e “EXPERIMENTO DO LEITOR” continuam com fundo diferente, como recursos didáticos independentes.

## Oportunidades priorizadas

| Ponto do livro | Figura a desenvolver | Questão que resolve | Origem / dependência |
| --- | --- | --- | --- |
| Cap. 1 | Da conversa ao contrato de revisão: texto, ferramenta, validação e aprovação | O que mudamos no processo? | Exemplo real do próprio livro |
| Cap. 2 | Camadas de arquitetura: prompt / skill / tool / workflow / agente | Que elemento faz o quê? | Contrato editorial, definições oficiais |
| Cap. 3 | Circuito operacional do agente: objetivo → ferramentas → resultado → evidência → decisão | Como o agente trabalha sem autoridade ilimitada? | Contrato, caso 403 GitHub |
| Cap. 4 | Fluxograma “precisa mesmo de um agente?” com ramificações manual, script, modelo, workflow, agente | Qual é a solução mínima? | Critérios do capítulo, não modelo comercial |
| Cap. 5 | Cadeia de provas e níveis de observabilidade | O que prova cada declaração? | Casos Git e editorial reais |
| Cap. 5 | Diagrama de cascata de modelos e ferramentas determinísticas | Quando roteamento economiza recursos? | Sem números de economia antes de medições |
| Laboratório de tokens posterior | Gráfico custo total × qualidade de modelos e fluxo determinístico | Qual opção foi mais eficiente? | SOMENTE depois de executar comparativo reproduzível |
| Prova final TK2000 | Pipeline editorial com checkpoints de texto, ilustração, publicação e revisão humana | Como os capítulos convergem para o livro real? | Manuscrito TK2000, sua matriz de pendências |
| Livro impresso | Página de exemplo com bom/ruim: legenda órfã, figura larga, fonte inconsistente | Qual problema editorial precisamos evitar? | Provas de página autorizadas dos manuscritos |

## Implementação planejada

Arquivos SVG rastreáveis em `figures/` e código-fonte em `figures/src/` (Mermaid, DOT ou SVG editável, conforme o caso). Cada imagem deve ter um identificador estável, legenda e referência no corpo. Criar uma suíte de regressão de PDFs que verifica margens e detecta quebras indesejadas na diagramação.

**Status:** nenhum gráfico de dados foi inventado ou aprovado nesta primeira passada. O roadmap deve ser revisitado antes da terceira rodada de capítulos e no início da fase visual.

## Revisão v0.7 — gráficos vinculados aos artefatos reais

- Capítulo 6: diagrama em três camadas **modelo/skill/tool**, com uma faixa de aprovação humana e três saídas específicas (livro, jogo, hardware). Ainda não desenhado.
- Capítulos 2–5: fluxograma de seleção sem IA → script → modelo pequeno → agente, com custo e provas **sem dados inventados**. Ainda não desenhado.
- A página 59 do PDF v0.6 é um caso de comparação antes/depois **reservado para uma rodada futura**, não uma licença para corrigir silenciosamente o exemplo. Há seis trechos monoespaçados fora do retângulo no diagnóstico inicial. A aprovação dependerá de inspeção visual.
