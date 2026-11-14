# Primeira passada encerrada — protocolo da segunda passada

**Estado:** EM EXECUÇÃO; auditoria inicial realizada, Bloco A gerado; nenhuma revisão autoral de bloco foi ainda aprovada.

## Congelamento do texto integral

A primeira passada possui 21 capítulos. Registrar commit, inventário SHA-256 e PDF/EPUB/HTML de leitura. O manifesto da fonte não aprova impressão. Não atualizar blocos anteriores sem verificar se o autor editou os arquivos no Google Drive sincronizado.

## Blocos de revisão do autor (proposta)

- Bloco A: Apresentação + capítulos 1–4 — fundações, conceitos e problemas que um agente não precisa resolver.
- Bloco B: capítulos 5–8 — evidências, voz e ambientes/skills.
- Bloco C: capítulos 9–12 — workflows, políticas, ciclo supervisionado e avaliação.
- Bloco D: capítulos 13–16 — tools, versionamento, frameworks, tokens/custos.
- Bloco E: capítulos 17–21 — laboratórios, integração e livro vivo.
- Anexos, glossário, bibliografia e elementos pré-textuais serão revisados como bloco próprio.

Tamanhos propostos são flexíveis: blocos podem ser menores se houver muita intervenção. A versão Quarto permanece canônica; DOCX editável é interface de revisão, não nova fonte paralela. Cada retorno exige diff aprovado e reintegração controlada.

## Revisão cega das falhas editoriais

O autor relatou pequenos erros ao longo da primeira passada mas não os descreveu. Não presumir sua natureza nem sua posição. A próxima auditoria deve procurar **do zero**: páginas órfãs, títulos e legendas isolados, quadros que transbordam, trechos de código, glifos faltantes, fontes trocadas, citações, numeração, sumário, referências cruzadas, erros semânticos e qualidade de voz.

### Separação de gates

1. Estrutural: arquivos, capítulos e boxes.
2. Tipográfico: PDF/EPUB/HTML e inspeção visual de páginas, não apenas captura amostral.
3. Editorial: clareza, repetição, autenticidade da voz e progressão didática.
4. Técnico: proveniência, dados e limites dos exemplos; não confundir simulação com bancada.
5. Autoral: decisões e aprovação final dos blocos.

## Segunda passada gráfica

Somente depois das correções de texto, selecionar diagramas/figuras necessários. Cada elemento recebe ID, origem, justificativa didática e versão; não criar gráficos numéricos sem dados de ensaio. Ver `docs/PLANO_VISUAL_SEGUNDA_PASSADA.md`.

## Grande ensaio externo

O *Manual Técnico do TK2000* já estava sendo preparado antes deste livro. Sua editoração será o teste final externo, **ainda não iniciado**. Congelar revisão, respeitar direitos sobre imagens e esquemas e manter cada pendência técnica visível até evidência ou decisão consciente do autor.

**PASS de primeira redação** significa 21 fontes presentes; **não significa que a obra esteja revisada, aprovada, ilustrada ou publicada como edição final**.


## Início da segunda passada — auditoria v1.4

A auditoria automática e visual dirigida encontrou cinco páginas finais de capítulos excessivamente curtas (113, 186, 198, 211, 233); os nove transbordamentos de código já conhecidos continuam FAIL. O relatório detalhado é `docs/AUDITORIA_EDITORIAL_SEGUNDA_PASSADA_v1.4.md`, com JSON em `docs/AUDITORIA_PAGINACAO_v1.4.json`. O Bloco A foi gerado em DOCX editável para revisão humana. Nenhuma correção do manuscrito canônico foi aplicada.
