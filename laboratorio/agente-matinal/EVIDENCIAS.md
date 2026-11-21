# Evidências — LAB-AGENTE-01

Ensaio local em 21/11/2026, Python 3.13.5, arquivos sintéticos.
Comando: python briefing.py --data 2026-11-23
Resultado: 5 prioridades e 2 compromissos. Ver saida-referencia.txt.

Comando: python -m unittest discover -s tests -v
Resultado observado:
    test_injecao_nao_vira_ordem ... ok
    test_modo_proibido_falha ... ok
    test_nao_ha_acoes_externas ... ok
    test_prioridades_e_eventos ... ok
    test_rastreabilidade ... ok
    Ran 5 tests
    OK

Dois experimentos adicionais em cópia isolada:
- TASK-002 com prazo às 08:00: tornou-se a primeira prioridade.
- enviar_email = true: programa encerrou com código 1 e PermissionError: A política permite uma ação externa proibida.

PASS limitado ao programa offline e aos casos acima. O teste de ausência de ações externas verifica texto de saída, não uma sandbox; o código não implementa ferramentas externas. O teste de injeção cobre somente a mensagem informativa artificial MSG-004. Não é validação de defesa contra ataques a LLMs.
PENDENTE: executar Claude Code, Codex e Gemini CLI separadamente, verificar descoberta de skill e ferramentas, permissões efetivas, fontes, latência e respostas. Gmail, Calendar e agendamento real não foram ativados.
