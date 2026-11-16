---
name: skill-exemplo
description: Exemplo didático de revisão somente leitura, sem executar ferramentas ou modificar documentos.
---

# Skill de exemplo

## Quando usar
Revisar um trecho fictício e comparar com critérios fornecidos pelo usuário.

## Quando NÃO usar
Para publicar, apagar, editar arquivos reais, analisar segredos ou assumir aprovação humana.

## Entradas
Texto original, critérios do autor e resultado esperado. Na falta deles, solicitar informação e parar.

## Processo
1. Conferir se há texto original e critérios explícitos.
2. Sugerir uma revisão em separado sem substituir o original.
3. Apontar alterações e incertezas de forma verificável.
4. Pedir aprovação humana antes de qualquer operação externa.

## Saída
Proposta, lista de diferenças, ressalvas e estado PROPOSTA_NAO_APROVADA.

## Ensaios mínimos
Caso aceito, informação insuficiente e pedido fora de escopo. Nunca declarar execução sem log real.
