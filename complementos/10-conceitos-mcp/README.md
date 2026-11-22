# 10 conceitos essenciais de MCP — mapa visual e guia técnico

Complemento original do livro **IA fazendo IA — ou quase**, elaborado para o portal **Laboratório Vivo**.

## Arquivos

- `index.html`: guia em português com os 10 conceitos, comparação de versões, segurança e roteiro didático.
- `assets/mapa-10-conceitos-mcp.svg`: mapa original vetorial, totalmente editável.
- `10-conceitos-mcp-a4.pdf`: versão A4 do mapa, vetorial e com texto pesquisável.
- `gerar_diagrama.py`: código-fonte gerador do SVG, para permitir ajustes e regeneração.

## Nota técnica

Revisão de referência: **MCP 2026-07-28**. A arquitetura distingue host, cliente e servidor; recursos, prompts e ferramentas não são sinônimos. O guia destaca a diferença entre `stdio`, Streamable HTTP e JSON-RPC, bem como as particularidades de autenticação. A revisão 2026-07-28 não usa o antigo handshake com `initialize` como fluxo-padrão.

## Origem e direitos

O ponto de partida foi uma imagem “10 MCP Concepts Every AI Builder Should Know”, identificada como de **Denis Panjuta (@denis-panjuta)**, junto de um texto em inglês encaminhado pelo leitor. O novo mapa, texto e diagrama são elaborados do zero; a imagem original não foi incluída na distribuição. A autoria/licença da postagem original não foi confirmada independentemente. Referências técnicas disponíveis no HTML.

## Verificação

- SVG: XML válido e convertido em PNG e PDF.
- HTML: títulos/links locais auditados.
- PDF: página A4 e caracteres renderizados; não substitui o guia narrativo em HTML.
- Exemplos: **conceituais**; nenhum servidor MCP real foi instalado, executado ou validado neste complemento.

> Nada é “funcionou” sem prova.
