# LAB-RAG-01 — Criar, medir e testar um RAG

**Complemento prático do livro _IA fazendo IA — ou quase_ — José Albuquerque.**

[Iniciar o laboratório visual](index.html) · [Fluxograma vetorial](fluxo-lab-rag.svg) · [Código Python](rag_lab.py) · [Testes](testes/test_lab.py)

## O que você vai construir

Um RAG simples com duas fases:
- **Preparação dos documentos:** carregar arquivos de teste, extrair texto, dividir em trechos identificados e criar um índice de busca.
- **Consulta:** receber uma pergunta, recuperar trechos, montar o contexto com as fontes e, opcionalmente, gerar a resposta usando um modelo local.

A implementação principal utiliza SQLite FTS5/BM25, sem dependências externas. Opcionalmente, o Ollama permite experimentar embeddings e geração de texto. A busca vetorial deste exercício percorre os vetores em Python e é adequada a pequenas coleções.

## Requisitos

- Python 3.11 ou mais recente e SQLite compilado com FTS5 (verificado pelo comando de teste abaixo).
- Núcleo lexical: **nenhuma dependência externa**.
- PDFs **com texto selecionável**, quando utilizados: `python -m pip install pypdf` (opcional).
- Geração local opcional: Ollama instalado e iniciado, com `llama3.2:3b`.
- Embeddings locais opcionais: Ollama + `nomic-embed-text` (diferentes modelos usam convenções próprias de prefixo).

> No Windows use o Terminal ou PowerShell. Se `python` não funcionar, substitua por `py -3`. Os comandos abaixo pressupõem a pasta `laboratorio/rag-pratico` do projeto já extraído.

## Parte 1 — recuperação local, sem IA

### 1. Teste o programa (sem instalar pacotes)

```powershell
python --version
python -m unittest discover -s testes -v
```

**Esperado:** `Ran 7 tests` e `OK`. Falha na criação do índice FTS5 significa que seu Python/SQLite precisa ser verificado.

### 2. Crie o índice com dados fictícios

```powershell
python rag_lab.py index --data dados
```

**Esperado:** três arquivos/páginas e três trechos, índice `estado/rag.sqlite`. O índice é recriado a cada execução de `index`, inclusive os embeddings opcionais existentes.

### 3. Faça uma busca lexical

```powershell
python rag_lab.py search --question "Qual sensor precisa de substituição preventiva?"
```

**Esperado:** `02-inventario.txt` aparece como fonte. As pontuações BM25 do SQLite são usadas para ordenar resultados; não são probabilidades.

### 4. Meça a recuperação

```powershell
python rag_lab.py eval --gold testes/perguntas.json --top-k 2
```

**Esperado:** `hit_at_k: 1.0`, `total: 3`, `aprovados: 3`. Isso mede **apenas** essas três perguntas e não implica robustez fora delas.

### 5. Inspecione o prompt, sem chamar o LLM

```powershell
python rag_lab.py answer --question "Qual sensor foi marcado para substituição preventiva?" --dry-run
```

**Esperado:** `estado: PREVIEW`, mensagens de sistema/usuário, marcador `[F1]` e `modelo_executado: false`.

## Parte 2 — geração com IA local (opcional)

Instale e inicie o [Ollama](https://ollama.com/download), então:

```powershell
ollama pull llama3.2:3b
python rag_lab.py answer --question "Qual sensor foi marcado para substituição preventiva?"
```

**Critério de aprovação manual:** a resposta cita corretamente **S2**, faz referência ao documento de inventário e não inventa resultados adicionais. O estado `GERADO_SEM_VERIFICACAO_FACTUAL` indica apenas que houve geração, **não** que a resposta foi confirmada.

## Parte 3 — embeddings locais (opcional)

```powershell
ollama pull nomic-embed-text
python rag_lab.py embed
python rag_lab.py search --mode vector --question "Qual sensor deve ser trocado?" --top-k 3
python rag_lab.py answer --mode vector --question "Qual sensor foi marcado para substituição preventiva?"
```

**Importante:** execute `embed` após `index`; reconstruir o índice lexical apaga o índice vetorial. O modelo de embeddings usado para consultar deve ser o mesmo que indexou os documentos. A busca vetorial em Python percorre todos os vetores; é propositalmente didática.

Para usar Linux ou macOS, use os mesmos argumentos com `python3` no lugar de `python`. Os diretórios `estado/`, `saida/` e os caches não devem ser versionados.

## Arquivos de entrada

- `dados/01-metodo-de-teste.txt` — critérios fictícios de validação.
- `dados/02-inventario.txt` — sensores fictícios S1/S2/S3.
- `dados/03-seguranca.txt` — política sintética de autorização.
- `testes/perguntas.json` — respostas esperadas no índice.
- `testes/test_lab.py` — sete testes automatizados.

O leitor pode acrescentar `.txt`, `.md` ou `.pdf` textual à pasta `dados`, mas deve **começar somente com dados fictícios**. PDFs escaneados precisam de OCR, não incorporado.

## Como conferir os resultados

| Experimento | Resultado esperado |
|---|---|
| Testes automatizados | `Ran 7 tests` e `OK` |
| Preparação do índice | 3 arquivos e 3 trechos |
| Recuperação lexical | O inventário aparece na pergunta sobre o sensor S2 |
| Teste de recuperação | `hit_at_k: 1.0` nas três perguntas de exemplo |
| Prévia do prompt | `PREVIEW`, marcador `[F1]` e sem chamar o modelo |
| Geração opcional no Ollama | Conferir manualmente se a resposta identifica S2 e cita a fonte |
| Busca vetorial opcional | Comparar os trechos encontrados com a busca lexical |

### Cuidados de uso

- A busca BM25 usa união de termos, não um entendimento semântico. Correspondência de palavras pode retornar um trecho **irrelevante**. A ausência de hits provoca abstenção automática; um hit fraco não garante evidência suficiente.
- O prompt instrui a não obedecer a trechos maliciosos, mas **isso não é uma defesa infalível contra prompt injection**.
- Sem controle de permissões por documento, este é um exemplo **para dados públicos ou fictícios**, não para fontes sensíveis nem uso multiusuário.
- O texto do modelo pode citar referências erradas. **Referências geradas precisam de conferência.**
- `temperature=0` não garante determinismo completo.
- Não inclui reranker, busca híbrida, HyDE, avaliação automática do texto do LLM, interface web nem implantação em produção.
- Operações externas estão limitadas ao Ollama por URL configurável; para o ensaio utilize o endereço padrão de loopback.

## Documentação de apoio

- [SQLite FTS5 e BM25](https://www.sqlite.org/fts5.html)
- [Ollama API: embeddings](https://docs.ollama.com/api/embed)
- [Ollama API: chat](https://docs.ollama.com/api/chat)
- [PyPDF](https://pypdf.readthedocs.io/en/stable/)
- [Documentação de integração do LangChain](https://docs.langchain.com/oss/python/integrations/providers/overview)
