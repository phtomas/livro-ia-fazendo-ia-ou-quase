# Contrato didático da série — v0.4 (revisão de 13/11/2026)

## Fonte e proveniência

A exigência do box **NA PRÁTICA COM A IA** foi confirmada pela leitura de trechos reais das três obras existentes no Google Drive: *IA fazendo jogos — TK90X & MSX*, *IA fazendo Hardware — A saga da FabULA* e *Manual Técnico do TK90X — Circuitos, Revisões, Diagnóstico e Reparos*. Cada obra aplica o recurso à sua maneira, mas preserva um convite prático ao leitor, um prompt ou procedimento e explicação de limites e evidências.

## Regra permanente de capítulos didáticos

Todo capítulo didático novo deve oferecer, quando houver uma prática pertinente, ao menos **um** box marcado `NA PRÁTICA COM A IA`, contendo:

1. **O que testar:** objetivo claro e acessível, sem obrigar uso de ferramenta paga.
2. **Como proceder:** entradas, cuidados, passos e permissões.
3. **Prompt que usaríamos hoje:** texto copiável quando for adequada uma interação com IA; se for tarefa determinística, fornecer comando equivalente.
4. **Por que funciona:** relação entre a estrutura do pedido, o mecanismo da ferramenta e o comportamento esperado. Não apresentar hipótese como prova.
5. **Como verificar:** resultado observável, possíveis falhas e critério de sucesso/limite da experiência.

A presença de um box não basta: a revisão humana determina clareza, adequação, originalidade e segurança. Não despejar boxes como decoração nem repetir instruções mecânicas inúteis.

## Duas marcas didáticas distintas (confirmadas em *IA fazendo jogos*)

**NA PRÁTICA COM A IA** é um box de utilização da ferramenta: explica um problema, ensina como estruturar um pedido ou operação, mostra por que o procedimento faz sentido e como conferir o retorno. É um roteiro orientado e reproduzível, normalmente com um prompt copiável. A IA é parte explícita da atividade.

**EXPERIMENTO DO LEITOR** é um convite à investigação independente: parte de uma curiosidade ou problema, propõe que o leitor escolha um caso, varie uma condição, observe, compare e construa seu próprio julgamento. A IA pode participar ou não. O exercício não deve antecipar a resposta nem reduzir o leitor a executor de um prompt pronto.

Em *IA fazendo jogos*, os experimentos do leitor aparecem de modo autônomo: a proposta de comparar duas conversas sobre a criação de um jogo; a comparação entre duas máquinas Z80 com recursos diferentes; a investigação de uma build que parece pronta, mas falha diante de provas distintas; e a escolha entre produzir um recurso isolado ou construir o processo que permite repeti-lo. Há hipótese, escolha, observação e reflexão. Essas experiências **não são o mesmo artefato** que os boxes de prompts reutilizáveis.

### Orientação para capítulos futuros

- Quando o assunto permitir uma aplicação de IA, planejar um box NA PRÁTICA COM A IA.
- Quando o assunto permitir descoberta pessoal, planejar um EXPERIMENTO DO LEITOR separado, com liberdade de escolher exemplos e registrar conclusões; não exigir ferramentas pagas sem alternativas.
- Cada experiência começa com convite narrativo: por que vale tentar, o que observar e como interpretar o resultado. O texto deve provocar a curiosidade, não entregar a conclusão antes da experiência.
- Um capítulo pode ter ambos, um só, ou uma ausência justificada. A contagem automática é indício estrutural, não garantia pedagógica. Não duplicar a mesma tarefa simplesmente com dois títulos.
- Em boxes: enfatizar uso correto da IA e verificação. Em experimentos: enfatizar descoberta, autonomia e aprendizado do leitor.
- Registrar ambos como **dois componentes semânticos diferentes**, com diagramação distinta no HTML, EPUB e PDF.

### Estudo de caso editorial do próprio livro

Na v0.2, faltava o box da série; na v0.3, a primeira correção promoveu um exercício de comparação de respostas ao box e acrescentou outro box sobre a ausência de regras. O autor fez uma segunda observação, mais profunda: não basta ensinar prompts, é preciso cultivar a investigação autônoma do leitor. A v0.4 mantém os boxes e acrescenta o primeiro EXPERIMENTO DO LEITOR independente, com possibilidade de ser feito sem IA. O novo critério será verificado em capítulos seguintes.

## Regra de escopo e não regressão

- Toda solicitação de revisão deve enumerar o que pode mudar e o que deve permanecer intacto.
- Não reescrever seções não solicitadas, nem alterar voz, fatos, figuras, tabelas, anexos ou referências sem motivo explícito.
- Comparar o estado anterior com o posterior e apresentar o **diff**.
- Executar verificação mecânica de presença dos boxes e inspeção visual de PDF/EPUB/HTML.
- Guardar a versão anterior. Uma prova de diagramação não é uma aprovação editorial.

## O caso que nos ensinou a regra

Na revisão v0.2 de *IA fazendo IA — ou quase*, o capítulo passou a conter exercícios e explicações, mas a convenção histórica dos boxes **NA PRÁTICA COM A IA** não foi aplicada. O autor percebeu a ausência. O caso demonstra que melhorar partes visíveis do texto pode causar uma regressão quando uma regra consolidada não está explicitada no contrato de revisão. Não houve teste automatizado desse requisito na v0.2. A v0.3 insere os boxes e acrescenta uma checagem local. Evitar chamar isso de autonomia comprovada: foi a revisão humana que encontrou a falha.

## Gate mínimo

- **PASS de estrutura:** verificador encontra o box e as cinco partes necessárias em cada capítulo didático presente no pacote.
- **PASS editorial:** autor confere coerência com texto, qualidade da prática e preservação da voz.
- **PASS de publicação:** HTML, EPUB e PDF são renderizados e inspecionados nas condições reais de publicação.

Esses gates são diferentes e devem ser informados separadamente.
