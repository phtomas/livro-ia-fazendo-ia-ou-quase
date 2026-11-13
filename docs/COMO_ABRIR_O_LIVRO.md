# Abrir o manuscrito no Drive e ver a prévia no GitHub

**Fonte de versionamento:** https://github.com/phtomas/livro-ia-fazendo-ia-ou-quase (branch `main`).  
**Espelho de trabalho do autor:** `Meu Drive/Projetosia/Livro — IA fazendo IA (ou quase)/02_Manuscrito/Quarto_Fonte`.  
**Atenção:** Google Drive para computador sincroniza arquivos com o Google Drive, mas **não realiza commits Git automaticamente**. Alterações futuras devem ser reconciliadas com o repositório, com diff e aprovação do autor quando necessário.

## Leitura direta no GitHub

- Workflow de renderização: https://github.com/phtomas/livro-ia-fazendo-ia-ou-quase/actions/workflows/previa-quarto.yml
- Prévia HTML pública: https://phtomas.github.io/livro-ia-fazendo-ia-ou-quase/
- Cada push em `main` aciona a renderização Quarto e a publicação Pages, se o workflow passar.
- O site é prévia pública, não versão editorial aprovada. Não incluir manuscritos privados nem material de terceiros sem licença.

## Quarto no Windows com Google Drive para computador

1. Instale Quarto em https://quarto.org/docs/download/.
2. Abra `Quarto_Fonte` na unidade sincronizada do Drive; identifique `_quarto.yml` e as pastas `chapters`, `filters` etc.
3. Em PowerShell nessa pasta, execute `quarto --version`, `quarto check` e `quarto render --to html`.
4. Abra `_book/index.html` no navegador.
5. Para PDF, instale TinyTeX com `quarto install tinytex` e use `quarto render --to pdf`.

## Estado e compromissos

- **Não há sincronização automática Google Drive ↔ GitHub.** Nas revisões feitas aqui, atualizar os dois destinos e verificar o resultado.
- A fonte é o `.qmd` versionado, não o PDF antigo.
- O erro de código que ultrapassa o retângulo na página 59 do PDF de leitura v0.6 é caso de regressão conhecido. Publicar HTML não prova que o PDF está corrigido.
