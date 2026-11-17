# Kit do leitor — os 21 capítulos

**IA fazendo IA — ou quase**, José Albuquerque. Complemento público; o texto integral do livro permanece privado.

Este pacote reúne os 21 roteiros do livro, os scripts já publicados, a skill de revisão autoral, modelos de contratos, um executor local offline e testes de regressão. Nenhum teste chama um modelo de IA. O leitor pode trabalhar em Windows, Linux ou macOS com Python 3.11 ou posterior, sem instalar Git.

> Para começar, prefira o [guia de execução corrigido](../COMPATIBILIDADE.html). Para conhecer os resultados verificados, consulte [evidências e limites](../EVIDENCIAS.html).

## Como obter

Abra o repositório público no GitHub, selecione **Code > Download ZIP**, extraia em uma pasta local e abra um terminal nessa pasta. Não é necessário criar conta, usar token nem instalar Git. Leia sempre o código antes de executá-lo.

## Início rápido

```sh
python laboratorio/kit-do-leitor/executar.py --listar
python laboratorio/kit-do-leitor/executar.py --capitulo 4 --saida ../meu-ensaio-04
python laboratorio/kit-do-leitor/executar.py --todos --saida ../minha-bancada-21
python -m unittest discover -s laboratorio/kit-do-leitor/testes -p 'test_*.py' -v
```

**Segurança:** `--saida` precisa apontar para um diretório novo **fora** do repositório. O programa se recusa a sobrescrever resultados existentes. Para repetir, escolha outra pasta. Os dados usados pelo executor são fictícios. Nunca rode os testes diretamente no manuscrito.

## Estados e fronteiras da prova

- `NAO_VERIFICADO`: ficha criada; experiência humana ou numa plataforma ainda não foi comprovada.
- `PASS_LIMITED`: comandos locais produziram os códigos esperados; o escopo é restrito ao cenário sintético.
- `FAIL`: houve divergência entre código esperado e observado; analisar os logs.
- Uma falha **intencional** (exemplo: publicação negada, conflito ou regressão) é esperada em determinados ensaios e não significa falha do kit.
- O executor nunca concede `APROVADO` ao autor e não certifica ChatGPT, Claude, Gemini, KiCad, TK90X, MSX, OpenAI API ou qualquer serviço remoto.

## Índice por capítulo

| Capítulo | Atividade | Execução |
|---:|---|---|
| 01 | [Um livro que aprende a ser escrito](capitulos/01.md) | Registro humano |
| 02 | [Dar nome às peças antes de montar a máquina](capitulos/02.md) | Registro humano |
| 03 | [Por dentro de um agente](capitulos/03.md) | Registro humano |
| 04 | [Quando criar um agente](capitulos/04.md) | Python offline |
| 05 | [Provar, medir e proteger antes de escalar](capitulos/05.md) | Registro humano |
| 06 | [A voz que a ferramenta não deve apagar](capitulos/06.md) | Registro humano |
| 07 | [Três portas para a mesma oficina](capitulos/07.md) | Registro humano |
| 08 | [Uma skill que pode viajar](capitulos/08.md) | Python offline |
| 09 | [O fluxo que sabe onde parou](capitulos/09.md) | Python offline |
| 10 | [Quem deixa o agente decidir?](capitulos/10.md) | Python offline |
| 11 | [O primeiro ciclo supervisionado](capitulos/11.md) | Python offline |
| 12 | [Quando uma skill merece confiança](capitulos/12.md) | Python offline |
| 13 | [A ferramenta que não precisa de opinião](capitulos/13.md) | Python offline |
| 14 | [Duas cópias, uma história](capitulos/14.md) | Python offline |
| 15 | [Os frameworks não decidem por nós](capitulos/15.md) | Registro humano |
| 16 | [Medir a oficina antes de colocar mais máquinas](capitulos/16.md) | Python offline |
| 17 | [A editora que aprende a conferir](capitulos/17.md) | Python offline |
| 18 | [Um jogo não é jogável só porque compila](capitulos/18.md) | Python offline |
| 19 | [A placa não leu nosso relatório](capitulos/19.md) | Python offline |
| 20 | [O mesmo método atravessa três portas?](capitulos/20.md) | Python offline |
| 21 | [O livro vivo sem perder a memória](capitulos/21.md) | Python offline |

## Materiais comuns

- [Modelo de Agent Skill](modelos/MODELO_SKILL.md) e [contrato AGENTS.md](modelos/AGENTS.md).
- [Contrato de ferramenta](modelos/CONTRATO_FERRAMENTA.json), [matriz de critérios](modelos/MATRIZ_CRITERIOS.csv) e [registro de evidências](modelos/MODELO_REGISTRO.md).
- [Skill pública de revisão autoral](../codigo/skills/revisao-autoral/SKILL.md).
- [Scripts e exemplos já existentes](../codigo/) — reaproveitados sem criar implementações paralelas.
- [Roteiros completos dos 21 capítulos](../README.html).

## Sobre teste de plataformas

Instalar uma skill em diretório temporário não prova que um modelo a reconheceu. Ensaios reais de ChatGPT, Claude e Gemini devem registrar fornecedor, modelo, data, modalidade de acesso, permissões, entradas, saídas e versões, preservando a distinção entre observado e suposto.

**Regra editorial:** nada é 'funcionou' sem prova. Este kit é complementar ao livro; o leitor conserva responsabilidade pelas próprias decisões.