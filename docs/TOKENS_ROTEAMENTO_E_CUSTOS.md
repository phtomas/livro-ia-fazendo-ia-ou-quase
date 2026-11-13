# Economia de tokens e escolha verificável de modelos — pauta editorial v0.1

**Estado:** requisito aprovado como pauta; capítulo e laboratório ainda não escritos nem executados. Registrado em 13/11/2026 para a obra *IA fazendo IA (ou quase)*.

## Ideia central

O objetivo não é gastar o menor número de tokens em qualquer circunstância. É **realizar a tarefa corretamente, com custo total justificável**: tokens, preço, latência, uso de ferramentas, intervenções humanas e retrabalho. Não empregar um modelo se um algoritmo determinístico resolver o problema com igual ou maior segurança.

### Exemplo de progressão

- **Sem chamada a IA:** copiar arquivos de uma pasta para outra por um programa Python, `shutil.copy2()` ou uma ferramenta de cópia. A operação usa CPU e I/O, mas não precisa consumir tokens de inferência.
- **Modelo pequeno / barato:** classificar documentos em categorias conhecidas, extrair campos simples e sugerir etiquetas. Medir taxa de acerto com amostra rotulada. Quando possível, começar por regras determinísticas antes do modelo.
- **Modelo maior / de raciocínio:** desenhar uma arquitetura com restrições, resolver conflitos complexos ou revisar hipóteses de falha. O modelo caro só deve ser escolhido se a melhora de qualidade compensar custo, risco e tempo.
- **Escalonamento:** um modelo simples resolve a maior parte; casos incertos ou críticos são revisados por modelo mais capaz ou por uma pessoa. O roteador também tem custo e falhas; comparar com baseline de modelo único.

## O que medir

1. `provider`, `requested_model`, `reported_model` (se disponível) e data de execução.
2. `input_tokens`, `cached_input_tokens` quando informados e `output_tokens` **reais**, coletados do metadado de uso da resposta; não confundir estimativa antes da execução com consumo faturado.
3. Chamadas adicionais: embeddings, ferramenta de busca, execução remota, síntese de voz, chamadas de raciocínio, armazenamento, integrações e repetições. Nem todos são cobrados em tokens.
4. Preços **datados**, identificados pela unidade oficial e modalidade (API, assinatura, lote). Não inferir custo de API a partir de mensalidade de um chat.
5. Qualidade: taxa de sucesso, correções necessárias, validação de saída e tempo fim-a-fim.

Custo aproximado em uma API com cobrança por tokens:

`custo = entrada_nao_cacheada/1_000_000 * preco_entrada + entrada_cacheada/1_000_000 * preco_cache + saida/1_000_000 * preco_saida + custos_extras`

Valores reais dependem dos detalhes da tabela do provedor e do plano. Se algum componente não for exposto, marcar **DESCONHECIDO** em vez de imputar zero.

## Contagem prévia versus medição posterior

**Contagem prévia:** a API de contagem do provedor ou o tokenizador apropriado pode estimar os tokens de uma solicitação antes da geração. O número de tokens de **saída** não pode ser conhecido com exatidão antes de executar a tarefa; pode-se fixar um limite superior quando a plataforma permitir.

**Medição posterior:** usar o objeto de `usage` retornado pela API, quando disponível. No chat de uma interface comercial, contagens exatas e custos por mensagem podem não estar expostos; não inventar precisão. Uma ferramenta de contagem local não precisa consultar modelo de linguagem: tokenização é uma operação algorítmica.

## Como verificar o modelo efetivo

- Registrar o ID do modelo solicitado na chamada da API.
- Registrar o campo de modelo retornado pelo provedor, se existir, e demais metadados oficiais pertinentes.
- Em uma cadeia com orquestrador, gateway ou roteador, registrar também o evento de roteamento e o modelo de cada subchamada, não apenas o modelo anunciado ao usuário.
- Se a plataforma **não expõe o modelo real** ou troca dinamicamente por política interna, declarar a limitação. Não usar o texto produzido pelo modelo como prova da identidade do modelo.
- Não expor chaves, tokens de autenticação ou conteúdo sigiloso nos logs.

## Laboratório proposto (a executar)

Tarefa A: copiar dez arquivos — solução Python sem IA; medir operação, integridade (hashes) e tokens de modelo consumidos: zero **somente se nenhuma chamada a um LLM tiver sido feita nessa execução**.

Tarefa B: categorizar 30 nomes/descrições — primeiro com regras simples; depois modelo econômico e modelo mais capaz; comparar acurácia e custo real.

Tarefa C: análise textual complexa — comparar modelos com mesmos critérios de qualidade e controle de versão; medir quando o escalonamento compensa.

Entrega do leitor: tabela contendo tarefa, método, modelo solicitado, modelo comprovado/indisponível, tokens de entrada/saída, preços consultados, custo, tempo, taxa de acerto e observações.

## Boxes didáticos (dois recursos distintos)

**NA PRÁTICA COM A IA:** solicitar a uma IA a proposta de roteamento por complexidade, com limites, exemplos, custo e política de aprovação; verificar que o roteamento sugerido não afirma acesso a preços ou telemetria que não possua.

**EXPERIMENTO DO LEITOR:** escolher três tarefas reais; prever qual delas pode ser executada sem IA; executar uma baseline determinística; observar quais tarefas realmente exigiram inferência; só então comparar com uso de modelo. Registrar resultados próprios e revisar a hipótese inicial.

## Fontes técnicas para consultar antes da redação final

- OpenAI — guia de contagem de tokens e `usage`: https://platform.openai.com/docs/guides/text-generation ; https://platform.openai.com/docs/api-reference/responses
- Anthropic — token counting: https://docs.anthropic.com/en/docs/build-with-claude/token-counting
- Google Gemini — token counting: https://ai.google.dev/gemini-api/docs/tokens
- Preços oficiais: verificar páginas oficiais **na data do experimento**, e registrar edição e modelo.

**P1:** nenhum PASS sem prova; **P5:** simplicidade é força; **P7:** assertividade antes da velocidade; **P9:** não reinventar a roda; **P10:** simbiose e cuidado. O laboratório deve distinguir **MÉTODO MAIS BARATO** de **MÉTODO QUE MAIS BARATEOU COM QUALIDADE COMPROVADA**.
