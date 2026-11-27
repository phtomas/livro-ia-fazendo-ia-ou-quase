# Auditoria e decisão editorial — ChatGPT Prompts (Data, Code & Clarity)

**Data:** 27/11/2026. **Fonte:** 18 fotografias, numeração de páginas 1–18, 104 prompts #01–#104.  
**Estado:** transcrição e conferência estrutural do PDF de estudo **PASS** (18 páginas; 104 números únicos em sequência; nenhuma caixa de texto fora da página). Revisão conceitual editorial **PASS documental**. Testes de desempenho dos prompts em modelos reais **NOT RUN**.

## Triagem de duplicação

O repositório contém os complementos [100 ideias de prompts](../100-ideias-de-prompts/index.html) e [30 estratégias simples de prompts](../30-estrategias-de-prompts/index.html), que já abrangem solicitações de resumo, redação, carreira, código, planilhas, dados, negócios, seleção de papéis, exemplos, formato, revisão e iteração. **Não** publicar mais um catálogo paralelo de 104 instruções.

| Páginas de origem | Tema | Relacionamento com o portal | Novo valor neste complemento |
|---|---|---|---|
| 3–4 | Anatomia e técnicas | Já tratado nas 30 estratégias | Restrições, proveniência, quando não usar técnica |
| 5–9 | Aprendizagem, carreira, entrevista, escrita, comunicação | Muitos exemplos já estão nas 100 ideias | Checar fatos do currículo, simulação ≠ pontuação certificada |
| 10–13 | Excel, SQL, Python, análise de dados | Já há vários guias e laboratórios | Critérios para validar código, consultas, números e evidências |
| 14–16 | Negócios, marketing, produtividade | Já aparecem nas 100 ideias | Evitar dados de mercado inventados e causalidade sem demonstração |
| 17–18 | Refinamento e resumo | Já aparece nas 30 estratégias | Contrato de testes negativos e abstenção |

## Ressalvas verificadas

1. **Página 4, “role prompting”, “expert-level answers”:** solicitar um papel ajusta o modo de resposta, mas não garante conhecimento especializado ou acerto. Conferir fatos em fontes independentes. [F1], [F3], [F6].
2. **Página 4, “step-by-step”:** explicar etapas pode ser útil, mas instruções genéricas para “pensar passo a passo” não são universalmente melhores; testar por modelo/tarefa. [F4].
3. **Páginas 4 e 17, “self-review” / “check it”:** o mesmo modelo pode repetir o erro ao revisar a própria resposta. Não contar como validação independente. [F3].
4. **Página 7, entrevistas e notas de 0–10:** são exercícios simulados, sem garantia de calibração, compatibilidade com perguntas reais nem aderência a recrutadores. [F3].
5. **Página 10, fórmulas e macros:** nome de função, separador de argumentos e suporte a recursos dependem da versão e da configuração regional. Testar na planilha real; executar macros apenas com autorização. [F3], [F6].
6. **Página 11, SQL:** consulta gerada pode ler dados indevidos ou causar carga excessiva; controles precisam ser impostos pelo banco/aplicação, não só descritos em prompt. [F5].
7. **Página 12, “write tests”:** geração de testes não prova execução. Exigir log, versão, casos negativos e verificação de expectativa. [F3].
8. **Página 13, KPIs e causas:** metas “boas”, causalidade e números não podem ser inferidos sem referencial, metodologia ou conjunto de dados suficiente. [F3], [F6].
9. **Páginas 14–15, clientes e concorrência:** “personas” e riscos podem ser hipóteses de trabalho; fatos sobre pessoas ou empresas exigem fonte e data. [F3].
10. **Página 18, segurança:** o próprio guia incentiva a proteção de dados; acrescentamos distinção entre privacidade, entrada não confiável e execução privilegiada. [F5].

## Adaptação cultural da tradução privada

- P. 8: “simple English” traduzido como **português simples**, por se tratar de edição para estudo em PT-BR.
- P. 10: XLOOKUP adaptado para **PROCX**; o funcionamento depende da versão/idioma do Excel. Conferir o idioma antes de copiar uma fórmula.
- P. 10: separar Excel de Google Planilhas; funções e macros não são universalmente intercambiáveis.
- Identificadores técnicos como SQL, Python, Pandas, JSON, STAR, SWOT e KPI permanecem reconhecíveis.
- Parênteses e campos [entre colchetes] são variáveis, não instruções para incluir dados confidenciais.

## Decisão de publicação

**Publicar:** comparação editorial, nota de proveniência, roteiro original de avaliação de prompts com casos negativos e referências verificáveis.

**Não publicar:** fotos, design original, tradução integral, transcrição dos 104 comandos (licença não identificada).

## Evidências e estado

- PDF para leitura privada: 18 páginas, texto selecionável, 104 prompts em ordem, conferência visual por páginas renderizadas; **PASS estrutural**.
- Testes de comportamento dos prompts em provedores/LLMs: **NOT RUN**.
- Robustez e segurança operacional: **NOT RUN** — não há aplicação ou modelo implantado nesta tarefa.
- Fontes bibliográficas com ligações por afirmação: [REFERENCIAS.md](REFERENCIAS.md).

> Não confundir revisão editorial com aprovação funcional: “funcionou” exige entradas, saída, versão, condições e evidência observável.
