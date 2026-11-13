# Portabilidade de uma skill — matriz de engenharia v0.8

**Fonte canônica:** `skills/revisao-autoral/` no GitHub. **Estado da skill:** candidata; conteúdo escrito e transporte local testado, comportamento em agentes de produção **NÃO VERIFICADO**.

## Compatibilidade não é identidade

| Ambiente | Ponto de entrada documentado em 13/11/2026 | Nosso status |
| --- | --- | --- |
| Codex (CLI/IDE) | `.agents/skills/<nome>/SKILL.md` no repositório; verificar configuração da versão | Caminho de cópia testado em diretório temporário; descoberta no Codex **NÃO TESTADA** |
| Gemini CLI | `.agents/skills/<nome>/SKILL.md` ou `.gemini/skills/<nome>/SKILL.md`; confirmação de ativação no próprio CLI | Caminho `.agents` copiado e comparado; ativação no Gemini **NÃO TESTADA** |
| Claude Code | `.claude/skills/<nome>/SKILL.md` no projeto; reconhecimento depende do ambiente | Caminho de cópia testado; descoberta no Claude Code **NÃO TESTADA** |
| ChatGPT (web/Work/plugins) | Skills podem integrar plugins e outras modalidades, conforme produto; não se presume leitura automática da pasta do Drive | Pacote não distribuído como plugin; ativação **NÃO TESTADA** |
| claude.ai (web) | Pode exigir upload de skill ZIP e configuração própria | Não realizado |

Documentação primária: https://learn.chatgpt.com/docs/build-skills; https://developers.openai.com/plugins/concepts/skills; https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview; https://geminicli.com/docs/cli/skills/; https://agentskills.io/specification.

## Como testar o transporte sem alterar sua estação

No terminal, na raiz do projeto Quarto (é preciso Python 3.10+):

```powershell
python tools/skills/instalar_skill_local.py --workspace . --targets both --json
```

É um **dry-run**. Apenas informa o que mudaria. Para executar de verdade, é preferível primeiro apontar `--workspace` a uma pasta de testes **vazia e já criada**. O comando com `--apply` modifica os diretórios `.agents/skills` e `.claude/skills` abaixo do workspace indicado. Não use `--replace` sem revisar diferenças: quando solicitado, ele guarda a versão anterior em pasta de backup adjacente.

## Gates separados

1. `PACKAGED`: `SKILL.md`, `name`, `description`, referências locais e hashes presentes.
2. `TRANSPORTED`: cópia local de mesmo conteúdo; sem conflito ou com backup explícito.
3. `DISCOVERED`: aplicação real lista a skill (requer teste por produto).
4. `ACTIVATED`: skill acionada em uma tarefa compatível, sem permissões inesperadas (requer teste por produto).
5. `EFFECTIVE`: revisão do texto preserva fatos e voz com julgamento humano e diff (não realizado).

**Não promover automaticamente os estados 3–5 a partir de 1–2.** O transporte não chama LLM nem confere contas online. Resultados de modelos devem documentar ambiente, versão, contrato, permissão, evidência e incerteza.
