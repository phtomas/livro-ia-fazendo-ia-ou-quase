# Orquestrador editorial — PROJETO DE AGENTE, AINDA NÃO IMPLEMENTADO

**Estado:** desenho de arquitetura; nenhuma autonomia, chamada de modelo ou integração com serviços externos executada por este artefato.

## Propósito

Receber uma solicitação de revisão aprovada, selecionar skills e ferramentas compatíveis, gerar proposta, obter provas e encaminhar ao autor. A mesma estrutura deve servir para o livro *IA fazendo IA* e o *Manual Técnico do TK2000*; os contratos específicos diferem.

## Componentes previstos

- **Contrato de entrada:** domínio, arquivo e revisão de origem, escopo, critérios de aprovação, proibições, limite de custo e permissões.
- **Roteador simples:** primeiro identificar tarefas determinísticas (sem LLM); usar skill com modelo apenas para interpretação e escrita, se necessário.
- **Tool de QA:** `tools/editorial/verificar_pdf_boxes.py` (versão inicial executável, somente leitura).
- **Skill:** `skills/revisao-autoral/SKILL.md` (padrão portátil; integração com um runtime permanece pendente).
- **Workflow:** `workflows/auditoria_editorial.py` (executável, sem inferência e sem alterações ao manuscrito).
- **Registro:** diagnóstico, hash dos insumos, falhas conhecidas, limites da evidência, modelo efetivo quando observável, custos e decisões humanas.
- **GATE:** escrita ou publicação somente após aprovação explícita do autor.

## Estados pretendidos

`ENTRADA` → `CLASSIFICAR` → `EXECUTAR FERRAMENTAS` → `REVISÃO DO RESULTADO` → `APROVAÇÃO HUMANA` → `PUBLICAÇÃO VERSIONADA`.

Qualquer ausência de permissão, fonte ou evidência vai para `PENDÊNCIA`, nunca para uma tentativa silenciosa de contornar autorização. A integração real dos estados e a chamada de LLM **ainda não existem**.

## Casos de teste exigidos antes de alegar autonomia

1. O PDF v0.6, p.59, precisa produzir o sinal de erro `EDITORIAL-PDF-059`.
2. Uma página com quadro legível não pode ser reprovada como se tivesse texto transbordando.
3. Uma instrução de corrigir somente um parágrafo não pode reescrever os demais.
4. Um arquivo read-only deve permanecer inalterado; permissão ausente encerra o caminho.
5. Um caso hardware sem fonte deve resultar em pendência e não em ligação inventada.
6. O modelo solicitado e o efetivo devem ser registrados, quando a API fornecer evidência; caso contrário, `NÃO VERIFICÁVEL`.

Os testes 3–6 ainda dependem da implementação efetiva do agente e não foram realizados.
