---
name: briefing-matinal
description: Preparar e conferir briefing diário a partir de mensagens, agenda e tarefas fictícias; sem ações externas.
---
# Skill: briefing matinal seguro

1. Ler `PROTOCOLO.md` e `politica.json`.
2. Confirmar que os três JSONs em `dados/` são fictícios.
3. Ler a data indicada pelo usuário, sem presumir a data corrente.
4. Usar `python briefing.py --data 2026-11-23` como referência determinística.
5. Conferir os IDs das 5 prioridades e dos 2 eventos.
6. Redigir recomendações; não enviar, apagar, modificar nem pagar.
7. Se o resultado divergir, identificar a causa e propor mudança de código ou skill; testar outra vez.
8. Reportar explicitamente o que não foi executado e as limitações.
