# Registro vivo de regressões — v0.1

## EDITORIAL-PDF-059

- **Origem:** `IA_fazendo_IA_Capitulos_1_a_5_v0.6.pdf` — página física 59 de 85, Capítulo 4, box **NA PRÁTICA COM A IA**.
- **Sintoma:** linhas do exemplo Python extrapolam o retângulo e parte do código atinge a área externa, com texto cortado pela margem da página.
- **Estado de referência:** `FAIL CONHECIDO`, mantido deliberadamente a pedido do autor em 13/11/2026.
- **Mudança autorizada agora:** criar verificador e registrar o comportamento, **não corrigir a fonte nem substituir o PDF v0.6**.
- **Prova humana:** inspeção da página 59 em imagem rasterizada (captura guardada localmente e não publicada como página do livro).
- **Prova automática pretendida:** ao executar `tools/editorial/verificar_pdf_boxes.py` no PDF v0.6, obter pelo menos uma linha monoespaçada ultrapassando a margem direita de um quadro.
- **Teste negativo:** página sem texto transbordando deve retornar zero ocorrências (não confundir ausência de defeito com aprovação editorial de toda a página).
- **Critério futuro de fechamento:** alterar somente o exemplo necessário, renderizar, conferir a página afetada e páginas vizinhas e comparar com baseline; manter o caso histórico como regressão reprodutível.

## EDITORIAL-VOZ-001

- **Origem:** revisão dos boxes da série; primeira versão deste livro não preservou o padrão e foi corrigida a partir de observação humana.
- **Estado:** contrato e verificador estrutural presentes, porém fidelidade da voz ainda depende de revisão do autor.
- **Prova futura:** comparar original e proposta e registrar julgamentos autorais sobre significado, ritmo e didática.
