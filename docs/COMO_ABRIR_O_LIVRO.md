# Abrir o manuscrito no Drive e ver a prévia no GitHub

**Fonte de versionamento:** https://github.com/phtomas/livro-ia-fazendo-ia-ou-quase (branch `main`).  
**Espelho de trabalho do autor:** `Meu Drive/Projetosia/Livro — IA fazendo IA (ou quase)/02_Manuscrito/Quarto_Fonte`.  
**Atenção:** Google Drive para computador sincroniza arquivos com o Google Drive, mas **não realiza commits Git automaticamente**. Alterações futuras devem ser reconciliadas com o repositório, com diff e aprovação do autor quando necessário.

## Leitura direta no GitHub

- Workflow de renderização: https://github.com/phtomas/livro-ia-fazendo-ia-ou-quase/actions/workflows/previa-quarto.yml
- Prévia HTML, depois de ativar e executar GitHub Pages: https://phtomas.github.io/livro-ia-fazendo-ia-ou-quase/
- Em cada push de `main`, o workflow executa os verificadores estruturais, gera HTML no Quarto e publica um artefato `livro-html` para download no GitHub Actions.
- Para abrir no navegador, habilite **Settings > Pages > Build and deployment > Source: GitHub Actions** uma única vez. A publicação Pages pode falhar enquanto a fonte não estiver habilitada; nesse caso o artefato do job de renderização poderá estar disponível, mas não se deve anunciar a página como publicada.
- O site é uma **prévia pública** porque o repositório também é público. Não subir manuscritos privados, imagens de terceiros sem licença nem chaves de API.

## Quarto no Windows com Google Drive para computador

1. Instale Quarto em https://quarto.org/docs/download/.
2. Abra a pasta acima na unidade sincronizada do Drive, onde ficará o arquivo `_quarto.yml` e as pastas `chapters`, `appendices`, `filters` etc.
3. No PowerShell aberto nessa pasta, execute `quarto --version`, `quarto check` e `quarto render --to html`.
4. O arquivo de leitura aparecerá em `_book/index.html`; abra-o com o navegador.
5. Para gerar PDF, após conferir a instalação, use `quarto install tinytex` e `quarto render --to pdf`.

## Estado e compromissos

- **Não há sincronização automática Google Drive ↔ GitHub.** O espelho foi inicializado com conteúdo conferido e será atualizado em cada rodada editorial pela rotina de trabalho acordada.
- Os PDFs antigos não são a fonte da edição; os arquivos `.qmd` e o repositório Git são.
- Quarto no GitHub gera saída HTML, não corrige automaticamente o defeito do PDF na página 59. Esse erro continua registrado em `docs/CASES_DE_REGRESSAO.md`.
- Renderizar HTML e publicar não significa que todos os critérios de revisão gráfica foram aprovados.
