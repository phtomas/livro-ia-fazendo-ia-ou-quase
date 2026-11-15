---
name: revisao-autoral
description: >-
  Revisa capítulos e textos técnicos preservando a voz e o método de ensino do autor,
  sem alterar fatos não verificados. Usar quando o trabalho pedir revisão editorial,
  adequação de tom, comparação de versões ou preparação de manuscritos de livros,
  jogos e documentação de hardware.
compatibility: "Markdown/Quarto ou documentos convertidos em texto; revisão humana obrigatória antes de escrita no original."
metadata:
  version: "0.1"
  status: "candidata, não homologada"
---

# Skill de revisão autoral — candidata v0.1

Esta pasta descreve uma **habilidade reutilizável**, não um agente autônomo nem uma conexão ativa com arquivos externos. A presença de `SKILL.md` não significa que algum ambiente a tenha instalado ou testado. Sua ativação depende do produto.

## Quando usar

Revisar clareza, sequência didática e consistência de um texto sem substituir a voz do autor por uma formulação genérica. Antes de agir, ler [contratos-por-dominio.md](references/contratos-por-dominio.md).

## Entradas obrigatórias

- Trecho-alvo e seu formato/versão. Usar uma cópia de trabalho.
- Pelo menos um exemplo de texto aprovado pelo autor ou a indicação explícita de que o perfil ainda é **hipótese**.
- Escopo autorizado (por exemplo, apenas pontuação; ou coesão de três parágrafos).
- Domínio: `livro`, `jogo` ou `hardware`; pode haver mais de um, mas deve ser declarado.
- Critérios de verificação e lista de elementos intocáveis.

Sem material de referência, não alegar fidelidade autoral: oferecer somente correção básica e marcar o limite.

## Procedimento

1. Abrir o trecho **original**, registrando identificação, versão e, quando possível, hash.
2. Analisar os exemplos do autor e formular até cinco observações de voz, separando fatos, hipóteses e regras aprovadas.
3. Conferir o contrato do domínio. Em hardware, valores, ligação elétrica e revisão de placa não mudam sem evidência. Em jogo, testar sensação e comportamento percebido. Em livro, preservar percurso didático, boxes e referências.
4. Propor o **menor diff** que satisfaça o escopo. Proibido modificar outro capítulo ou arquivo sem autorização.
5. Entregar texto proposto e um quadro: trecho original, trecho sugerido, motivo, impacto, prova disponível ou pendência.
6. Rodar ferramentas determinísticas pertinentes em modo de leitura quando disponíveis. Não solicitar um LLM para adivinhar margens, hashes ou contagens.
7. Classificar separadamente: estrutura, evidência técnica, diagramação e aprovação autoral. `PASS` automático não vale para julgamento de voz.
8. **Parar antes de sobrescrever**. A substituição/publicação exige aprovação humana explícita e um mecanismo de rollback.

## Saída esperada

Uma proposta de revisão e um relatório de diferenças com evidências. Os estados válidos são `PASS`, `FAIL`, `PARTIAL` e `NÃO VERIFICADO`, com observações sobre o limite de cada teste.

## Proibido

- Inventar medições, testes, citações, referências ou autores.
- Tratar os boxes `NA PRÁTICA COM A IA` e `EXPERIMENTO DO LEITOR` como equivalentes.
- Corrigir silenciosamente uma regressão conhecida que o autor decidiu preservar.
- Publicar um arquivo, alterar o repositório ou chamar ferramenta sensível sem autorização própria.
- Apresentar esta skill como compatível ou instalada em todos os serviços sem teste no ambiente de destino.

## Evidência inicial

No projeto deste livro, o caso `EDITORIAL-PDF-059` registra uma linha de código que ultrapassa o retângulo na página 59 da prévia v0.6. A ação autorizada nesta rodada é **detectar e documentar**, não corrigir. Ferramenta: `tools/editorial/verificar_pdf_boxes.py` na raiz do repositório.

## Referências

- Contrato editorial da série: `docs/CONTRATO_EDITORIAL.md`.
- Plano de uso por domínio: [contratos-por-dominio.md](references/contratos-por-dominio.md).
- Padrão Agent Skills: https://agentskills.io/specification (conferido em 13/11/2026).
