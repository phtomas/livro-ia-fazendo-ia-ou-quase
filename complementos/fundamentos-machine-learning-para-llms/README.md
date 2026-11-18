# Fundamentos de Machine Learning — das bases às LLMs

**IA fazendo IA — ou quase · Caderno documental do Laboratório Vivo**  
**Autor do complemento:** José Albuquerque e equipe editorial assistida por IA  
**Data:** 17 de novembro de 2026 · **Estado:** síntese conceitual revisada; exemplos numéricos didáticos, não ensaios executados.

## Propósito e escopo

Este guia preserva as ideias fundamentais do aprendizado de máquina e mostra como elas se relacionam com os modelos de linguagem contemporâneos. Foi motivado pelo PDF de 38 páginas *Machine Learning — Complete Beginner Notes*, recebido para leitura crítica. O PDF trata principalmente de **ML clássico** (tipos de aprendizado, algoritmos, pré-processamento, avaliação e ciclo de vida). As explicações de tokenização, Transformers, atenção e treinamento de LLMs foram **acrescentadas editorialmente**; não devem ser atribuídas ao documento original.

**Percurso recomendado:** [Panorama IA/ML/DL/LLM](../panorama-ia-ml-dl-genai-llm-rag-agentes/index.html) → este caderno → [40 perguntas essenciais sobre LLMs](../llm-40-perguntas/index.html) → [120 conceitos](../llm-120-conceitos/index.html) → [ecossistema de ferramentas](../stack-llm-ia-generativa-2026/index.html).

## 1. A árvore de conceitos — e seus limites

| Conceito | Definição operacional | Nota |
|---|---|---|
| Inteligência artificial (IA) | Campo geral de sistemas que desempenham tarefas associadas à inteligência | Nem toda IA aprende de dados |
| Machine Learning (ML) | Modelos que ajustam padrões a partir de dados | Inclui técnicas clássicas e redes neurais |
| Deep Learning (DL) | ML com redes neurais de várias camadas | Inclui muitas arquiteturas, não só Transformers |
| LLM | Modelo de linguagem de grande capacidade, hoje frequentemente baseado em Transformer | LLM não é sinônimo de todo DL |
| IA generativa | Família de métodos que geram texto, imagem, áudio e outros conteúdos | Não se limita a LLM |
| RAG / agente | Padrões para construir aplicações que usam modelos e/ou ferramentas | Não são novas subclasses obrigatórias de ML |

A relação **IA ⊃ ML ⊃ DL** é útil, mas as demais categorias **não** formam uma cadeia linear. Aplicações podem dispensar LLM, RAG, frameworks e agentes quando uma ferramenta determinística basta.

## 2. O ciclo básico de um modelo

\`\`\`text
Problema → dados autorizados → preparação → treino → validação
                                      ↓
                              modelo ajustado
                                      ↓
                           inferência em novos casos
                                      ↓
                             medição e monitoramento
\`\`\`

Em aprendizado supervisionado, o modelo estima **ŷ = fθ(X)**, onde **X** são entradas, **y** é o alvo conhecido, **θ** são parâmetros e **ŷ** é a previsão. O treinamento procura parâmetros que reduzam uma função de perda. Os dados de teste não devem participar da escolha dos parâmetros nem dos hiperparâmetros.

- **Feature:** variável de entrada, como o consumo de corrente de uma placa.
- **Target / label:** resultado esperado, como defeito presente ou ausente.
- **Parâmetro:** peso ou coeficiente ajustado no treinamento.
- **Hiperparâmetro:** configuração escolhida em projeto ou validação, como taxa de aprendizado.
- **Inferência:** uso do modelo ajustado, sem treinar novamente seus pesos.

Na passagem para uma LLM, essas noções continuam. Mudam os dados (sequências de tokens), objetivos de aprendizagem, escala e arquitetura.

## 3. Formas de aprendizagem

| Família | Como aprende | Exemplo |
|---|---|---|
| Supervisionada | Usa respostas-alvo rotuladas | Identificar defeitos com medidas e diagnósticos conhecidos |
| Não supervisionada | Descobre estrutura sem alvos rotulados | Agrupar padrões de falha semelhantes |
| Semissupervisionada | Combina poucos exemplos rotulados com muitos sem rótulo | Classificar imagens com poucos laudos |
| Reforço | Otimiza decisões a partir de recompensas ou retorno | Estratégia de controle num ambiente simulado |
| **Autossupervisionada** | Constrói um alvo a partir dos próprios dados | Prever tokens de texto a partir dos tokens anteriores |

O PDF-base apresenta explicitamente as **quatro primeiras** modalidades. A quinta foi acrescentada porque é central para compreender o pré-treinamento de muitos LLMs. O “agente” de aprendizado por reforço é um agente no sentido matemático de decisão; não é automaticamente um agente de software com ferramentas.

## 4. Algoritmos clássicos e quando usá-los

**Regressão** prevê um número; uma relação linear simples pode ser escrita como **ŷ = b₀ + b₁x**. **Classificação** prevê uma categoria; a regressão logística, apesar do nome, é um classificador probabilístico. **Clustering**, como K-Means, agrupa observações por similaridade sem alvo rotulado.

Árvores de decisão, Random Forest, KNN, SVM e Naive Bayes ilustram hipóteses indutivas diferentes. Servem para estudar generalização, comparar baselines e resolver muitos problemas tabulares, mas **não** são os blocos característicos de um Transformer.

Uma abordagem complexa só merece ser adotada se demonstrar ganho relevante sobre o baseline, em dados de avaliação legítimos e com custo aceitável.

## 5. A ponte técnica para LLMs

\`\`\`text
Texto → tokenização → IDs de tokens → vetores (embeddings)
         → blocos Transformer / atenção (conforme a arquitetura)
         → probabilidades do próximo token
         → decodificação → próximo token → repetir
\`\`\`

Esse fluxo resume **geração autorregressiva**, não todas as arquiteturas de linguagem. As peças essenciais são:

1. **Tokenizador:** converte texto em unidades que podem ser fragmentos de palavras.
2. **Embeddings:** representam unidades por vetores aprendidos.
3. **Posição e atenção:** modelam relações entre partes da sequência; nos decodificadores causais, há restrição de acesso a tokens futuros.
4. **Transformers:** combinam atenção, operações de projeção, não linearidades e outros componentes.
5. **Função de perda:** compara as probabilidades previstas aos próximos tokens corretos; entropia cruzada é comum.
6. **Backpropagation e otimização:** permitem calcular gradientes e modificar parâmetros.
7. **Decodificação:** escolhe as saídas usando regras ou amostragem.

A fluência do texto gerado não prova a correção factual de uma resposta nem a execução real de uma ação.

## 6. Pré-treinamento, pós-treinamento e consulta externa

| Processo | O que faz | O que não faz por definição |
|---|---|---|
| Pré-treinamento | Desenvolve representações e capacidades a partir de dados e objetivos de treino | Não consulta automaticamente arquivos privados em tempo real |
| Pós-treinamento | Ajusta respostas a tarefas, instruções e, às vezes, preferências | Não garante verdade |
| Fine-tuning | Continua o treinamento de um modelo | Não equivale a anexar uma fonte |
| Prompting | Fornece instruções e contexto no momento de uso | Não modifica necessariamente pesos |
| RAG | Recupera informação externa para compor o contexto | Não exige por si só um banco vetorial |
| Inferência | Produz resposta com parâmetros já ajustados | Não implica re-treinamento |

RLHF, DPO e outras abordagens podem aparecer em diferentes pipelines de pós-treinamento; não são etapas universais para todo modelo.

## 7. Otimização, regularização e generalização

Uma atualização didática por gradiente é:

\`\`\`text
θ_novo = θ_atual − taxa_de_aprendizado × ∇L(θ_atual)
\`\`\`

A taxa de aprendizado controla o tamanho da atualização. Regularização reduz certos tipos de complexidade ou instabilidade do modelo. **Overfitting** é excesso de ajuste ao conjunto de treino; **underfitting** é a incapacidade de captar os padrões relevantes. O objetivo é generalizar para casos ainda não vistos.

A separação entre **treino**, **validação** e **teste** é indispensável. Normalizar, selecionar atributos ou otimizar hiperparâmetros usando o teste antes da avaliação final contamina o resultado. Série temporal, documentos semelhantes e grupos repetidos exigem divisões apropriadas — uma separação aleatória pode vazar informação.

Em LLMs, também é preciso atentar à **contaminação de benchmarks** e à reutilização involuntária de exemplos de avaliação no treinamento.

## 8. Métricas: a armadilha da acurácia

Para regressão, use medidas como **MAE**, **MSE**, **RMSE** e **R²**, conforme o caso. Para classificação, consulte a matriz de confusão, **precisão**, **recall**, **F1** e métricas por limiar.

**Exemplo original e hipotético:** em 2.000 inspeções, ocorreram 40 falhas reais. O classificador detectou 25, deixou passar 15 e emitiu 25 falsos alertas. Portanto:

| Medida | Valor |
|---|---:|
| TP / FP / FN / TN | 25 / 25 / 15 / 1.935 |
| Acurácia | (25 + 1.935) / 2.000 = **98%** |
| Precisão | 25 / (25 + 25) = **50%** |
| Recall | 25 / (25 + 15) = **62,5%** |
| F1 | **55,6%**, aproximadamente |

A acurácia de 98% esconde que 15 das 40 falhas foram perdidas e metade dos alertas era falsa. Escolha um limiar considerando riscos e custos reais, não uma métrica isolada.

**Para LLMs:** avalie correção da tarefa, fidelidade a fontes, robustez, taxa de erro, segurança, custo, latência e efeitos externos verificados. Resposta convincente e benchmark alto não substituem evidências de execução.

## 9. Reprodutibilidade e ciclo de vida

\`\`\`text
Definição → dados → preparação → baseline → treinamento → validação
       → aprovação → implantação → monitoramento → correção/retirada
\`\`\`

Versione código, dados de referência e configurações; monitore qualidade, deriva dos dados, latência, segurança e impacto. **Data drift** muda a distribuição das entradas; **concept drift** muda a relação entrada–alvo. São fenômenos distintos.

Para sistemas que acionam ferramentas, registre entrada, versão, comando, resultado esperado, resultado observado e evidência. Use permissões mínimas e confirmação de estado em cada operação externa.

## 10. Roteiro de estudo do leitor

1. Diferencie IA, ML, DL, LLM, RAG e agentes.
2. Desenhe um fluxo simples de treinamento, validação, teste e inferência.
3. Explique por que a preparação de dados não pode olhar o conjunto de teste.
4. Compare regressão, classificação e agrupamento.
5. Explique overfitting e underfitting em um caso prático.
6. Reproduza os cálculos de precisão, recall e F1 do exemplo acima.
7. Explique por que predição de próximo token é autossupervisionada.
8. Compare prompting, RAG e fine-tuning.
9. Identifique um caso em que uma regra ou script é preferível a ML ou LLM.
10. Elabore um protocolo de avaliação que permita detectar regressões após mudanças.

**Experimento do leitor:** selecione cinco atividades reais. Para cada uma, anote problema, dados, baseline sem IA, necessidade ou não de ML/LLM, critério de aprovação, evidências, riscos e custo. Só avance quando a medição justificar o próximo passo.

## 11. Origem, atribuição e limites de direitos

**Fonte motivadora:** *Machine Learning — Complete Beginner Notes*, arquivo PDF em inglês, 38 páginas, recebido em 17/11/2026. O texto menciona um princípio atribuído a **“The Data Guy”** na página 28, mas não foi possível confirmar neste material o autor formal, uma URL canônica ou uma licença aberta para redistribuição. **Não reproduzimos nem hospedamos integralmente o PDF original** no repositório público.

**Leitura por páginas:** fundamentos e modalidades (pp. 1–6); workflow, pré-processamento e algoritmos (pp. 7–15); métricas, generalização e validação (pp. 16–21); ferramentas e exercícios (pp. 22–28); matemática, avaliação e desbalanceamento (pp. 29–33); interpretabilidade, pipeline e operação (pp. 33–38). O material sobre **Transformers e LLMs** é uma extensão analítica do complemento, não uma alegação de cobertura do PDF.

Este guia **não relata um teste de ML efetivamente executado**. Exemplos são ilustrativos, e requisitos de bibliografia acadêmica ou republicação do documento-fonte exigem verificação adicional de autoria e licença.

> **Lema da oficina:** Nada é “funcionou” sem prova. Simplicidade é força. Isole e meça antes de adivinhar. Não reinvente a roda. E cresçam juntos.
