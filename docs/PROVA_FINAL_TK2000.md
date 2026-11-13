# Prova final — O Manual Técnico do TK2000

**Projeto:** IA fazendo IA — ou quase  
**Data de inclusão:** 13/11/2026  
**Situação:** compromisso editorial e plano inicial. **A execução do laboratório ainda não começou.**

## Por que este será o teste final

Uma IA pode revisar uma página, criar um box ou montar uma figura e parecer impressionante. O teste verdadeiro do método será lidar com uma **obra técnica inteira**, preservando sua história, os fatos, a voz do autor, as limitações das fontes e o controle editorial. O livro escolhido pelo autor é o **Manual Técnico do TK2000 — Circuitos, Revisões, Diagnóstico e Reparos** (título definitivo sujeito à revisão editorial), atualmente desenvolvido em trabalho independente.

Ele já tem manuscrito candidato, blocos editáveis, auditorias do TK2000 histórico, esquemas e registro de pendências. Não começaremos reescrevendo tudo. Primeiro **congelaremos uma linha de base**, inventariaremos conteúdo e lacunas e separaremos trabalho editorial de novas investigações elétricas ou lógicas.

## Fontes identificadas no Drive (sem importar conteúdo protegido ao Git público)

- Pasta do projeto: `Projetosia/Projeto TK2000`.
- `TK2000_Manual_Tecnico_COMPLETO_REV0_1_CANDIDATO.pdf` — prova candidata; conferir estrutura e paginação quando iniciar o teste.
- Blocos `TK2000_REV0_1_BLOCO_*` — fontes editáveis de capítulos e anexos.
- `TK2000_REV0_1_BLOCO_08_PENDENCIAS_PARA_REVISAO.docx` — 28 itens editoriais e técnicos em aberto segundo o documento de 12/11/2026.
- `TK2000_PENDENCIAS_TECNICAS_LIVRO_REV0_5.md` — separação de fatos, hipóteses e ensaios ainda não executados.
- `AUDITORIA_TK2000_2026-11-11.md` e `ARQUITETURA_TK2000_V0_1.md` — inventário e ressalvas de fontes. Não equivalem a medições físicas.
- `tk2000_manual_tecnico.pdf`, `esquema-tk2000.pdf` e projetos de referência com autoria própria e de terceiros, a conferir licença e proveniência antes de qualquer reprodução.

**Aviso:** materiais do Drive e esquemas de terceiros não serão copiados para este repositório público automaticamente. O laboratório poderá ter pasta privada de trabalho, com apenas scripts originais, relatórios e exemplos autorizados publicados.

## O que precisa melhorar

1. **Ilustrações:** auditar a presença, pertinência, legibilidade e fidelidade das figuras; redesenhar a partir de conexões confirmadas em esquemáticos, fotografias próprias e fontes com licença adequada. Não usar imagem gerada plausível como representação técnica comprovada. Figuras de circuitos devem ser reconciliadas com esquema, revisão e legenda.
2. **Voz e tom por capítulo:** retirar rupturas de estilo, repetição e prosa de relatório; preservar a voz aprovada da série sem uniformizar artificialmente capítulos que têm objetivos diferentes.
3. **Didática:** incorporar, quando couber, os boxes **NA PRÁTICA COM A IA** e os **EXPERIMENTOS DO LEITOR**, com funções diferentes. Um ensina a usar a ferramenta; o outro convida à investigação pessoal.
4. **Rigor técnico:** distinguir documentação original, esquema recriado, implementação HDL/emulador, medição física e hipótese. Manter pendências com ID e a decisão de publicação do autor. Não inventar provas para fechá-las.
5. **Produção gráfica:** formato de impressão a confirmar; verificar margens, resolução de imagens, hierarquia de títulos, tipografia, tabelas, legendas, referências cruzadas, glossário, bibliografia e páginas órfãs.
6. **Custo e execução:** usar verificadores determinísticos para tamanho de arquivos, estilos, dimensões, links, hashes e pré-voo; escolher IA apenas onde interpretação agrega valor, registrar modelo efetivo e consumo de tokens quando expostos.

## Processo de teste proposto

**T0 — Congelar a referência.** Selecionar a versão aprovada para edição; guardar SHA-256 dos fontes e PDFs e inventário das imagens/legendas; manter cópia imutável. Resultado: baseline inequívoca.

**T1 — Auditoria sem alteração.** Ler todos os capítulos, mapear divergências de voz, fonte, hierarquia, figuras, tabelas e referências; relacionar cada falha a uma regra editorial e uma localização. Resultado: plano de correções delimitadas.

**T2 — Ferramentas antes de agentes.** Automatizar tarefas mecânicas (inventário, comparação, validação de links e tamanhos, checagem de paginação e figuras) com scripts. Medir tempo, custo e falsos positivos.

**T3 — Skills e revisão assistida.** Aplicar guia de voz, contrato editorial e revisão de fontes; gerar propostas e diffs, nunca sobrescrever silenciosamente. Resultado: alterações autorizadas com justificativas.

**T4 — Figuras técnicas.** Reconciliar cada artefato com a referência, identificar autor/licença, inspecionar legibilidade a 16 × 23 cm ou formato aprovado, e encaminhar divergências a uma fila técnica. Uma ilustração atraente mas eletricamente errada é **NO-GO**.

**T5 — Orquestração e checkpoints.** Um workflow controla a sequência de edições e revisões. Agentes só recebem autonomia limitada onde uma comparação medida mostrar vantagem. Publicação, alteração de tese, retirada de ressalva técnica e decisão de fonte continuam com aprovação humana.

**T6 — Publicação e regressão.** Renderizar DOCX e PDF de impressão, e formatos digitais escolhidos; inspecionar todas as páginas e links, comparar com baseline, registrar custos e provas. Decidir com o autor o que publicar, com que limitações e créditos.

## Critérios para considerar o teste concluído

- **PASS estrutural:** nenhum capítulo, figura, tabela, legenda ou referência aprovada desapareceu sem registro; boxes e experimentos atendem ao contrato, quando cabíveis.
- **PASS técnico/editorial:** os fatos são rastreáveis à fonte correta; pendências permanecem visíveis ou são resolvidas com evidências. Não confundir “publicável com ressalvas” com “testado em placa”.
- **PASS autoral:** revisão de voz aprovada por comparação entre amostras e versão candidata; mudanças não solicitadas são rejeitadas.
- **PASS gráfico:** prova visual e preflight completos em cada formato de entrega, sem cortes, órfãos, baixa resolução ou figuras tecnicamente inventadas.
- **PASS operacional:** existem logs, diffs, versões, hashes, custos/tokens quando mensuráveis, permissões controladas e caminho de rollback.
- **PASS final:** o autor aprova conscientemente uma versão identificada. Sem aprovação humana, o laboratório pode estar tecnicamente adiantado, mas a obra **não está publicada**.

## Onde isto entra no livro

Propor uma **Prova Final** após os laboratórios de edição, jogos e hardware, com a história inteira do TK2000 como estudo de integração e não como mais uma coleção de promessas de IA. Cada capítulo preparatório deverá ensinar uma competência aplicável ao caso: prompts e contratos; agente; skill; ferramenta; controle de versão; verificação de figuras; voz; custo; publicação. Ao final, o leitor poderá adaptar o mesmo método a seu próprio livro, sem precisar possuir um TK2000.

**Não são entregas desta revisão:** alterar os arquivos originais do TK2000, fechar pendências de engenharia, inventar novas imagens ou publicar qualquer manuscrito final. O plano documenta a meta e o método.
