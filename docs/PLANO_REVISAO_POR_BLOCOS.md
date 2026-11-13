# Revisão final por blocos editáveis — Livro IA fazendo IA (ou quase)

**Estado:** plano editorial; ainda não iniciado. O autor decidiu ler a obra completa após a primeira passada de redação e só então revisar fragmentos editáveis, conforme o método aplicado ao *Manual Técnico do TK90X*.

## Por que dividiremos o livro

A revisão humana de um texto longo fica mais precisa quando cada entrega tem limites claros. Não queremos substituir a obra inteira quando o autor estiver corrigindo apenas uma página; tampouco queremos perder referências cruzadas ou impedir que o conjunto seja reconstituído.

## Fluxo de revisão pactuado

1. **Congelar a primeira passada:** registrar um commit e um pacote DOCX/PDF/Quarto de referência, com lista de capítulos, tamanho do livro, versão e hash dos arquivos.
2. **Fatiar em blocos editáveis:** agrupar capítulos segundo a extensão e a unidade temática (como no TK90X, blocos de aproximadamente 3–4 capítulos, ajustáveis); conservar uma versão íntegra única como baseline. O bloco é artefato de revisão, não novo livro.
3. **Entregar DOCX editável e prova PDF do bloco:** preservar textos, imagens, boxes, legendas, bibliografia e numeração; manter identificação do capítulo no documento e prova.
4. **Revisão do autor:** receber correções de voz, tom, precisão, didática e apresentação, registrando decisões. Não alterar capítulos fora do bloco por iniciativa própria.
5. **Comparar antes e depois:** diff textual, relatório de alterações, testes de presença dos boxes NA PRÁTICA COM A IA e EXPERIMENTO DO LEITOR, verificação de imagens e tabelas, e lista de pendências.
6. **Reintegrar na fonte Quarto:** aplicar somente correções aprovadas; preservar a identidade de cada trecho e as referências; recriar a prova completa e verificar a transição entre blocos.
7. **Segunda passada visual e fechamento:** introduzir diagramas e figuras quando forem pedagogicamente úteis, confirmar legibilidade e proveniência e executar os testes de publicação para cada formato.
8. **Gate final:** autor confere e aprova a versão identificada; sem aprovação, o livro permanece manuscrito em revisão.

## Regras de segurança editorial

- Propostas da IA não representam aprovação do autor; PASS estrutural não equivale a PASS editorial.
- Não reescrever páginas não solicitadas, não mudar fatos técnicos sem origem, não substituir desenhos comprovados por ilustrações apenas plausíveis.
- Manter versões e backups; permitir rollback sem destruir a última edição aprovada.
- A presença de um box correto não deve esconder um texto didaticamente ruim, e a ausência de uma figura não autoriza gerar imagem decorativa.
- A lista de pendências acompanha o bloco até a decisão explícita; não desaparece na consolidação.

## Prova final TK2000

O Manual Técnico do TK2000 será o caso externo de integração da metodologia, não uma obra que surgiu para servir ao teste. Já existia antes deste livro, com conteúdo, limitações e decisões próprias. A revisão desse manual exigirá linha de base independente, propriedade intelectual respeitada e pendências técnicas explícitas. A apresentação desta motivação integra **index.qmd**; o protocolo técnico permanece em **docs/PROVA_FINAL_TK2000.md**.

## Critério de pronto deste plano

**PLANEJADO, não executado.** O trabalho começa depois de concluída a primeira passada editorial e de selecionada a versão-base pelo autor.
