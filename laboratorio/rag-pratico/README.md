# LAB-RAG-01 — Criar, medir e testar um RAG

**Complemento prático do livro _IA fazendo IA — ou quase_ — José Albuquerque.**

[Iniciar o laboratório visual](index.html) · [Fluxograma vetorial](fluxo-lab-rag.svg) · [Código Python](rag_lab.py) · [Testes](testes/test_lab.py)

## Objetivo e critérios

Demonstrar **duas fases separadas** de um sistema RAG:

- **Preparar conhecimento:** carregar arquivos fictícios → extrair texto → dividir em trechos com origem → construir índice recuperável.
- **Responder:** receber pergunta → recuperar trechos → montar contexto com identificadores de fontes → gerar resposta pelo LLM local (opcional).

**PASS limitado** exige: sete testes automatizados verdes; indexação de três documentos sintéticos; 3/3 perguntas de referência recuperando a fonte esperada em `top-k=2`; e montagem do prompt verificável. **Não significa** precisão geral do sistema nem que um LLM real foi testado.

## Auditoria do exemplo de origem

O roteiro visual recebido tinha boas ideias, mas não era confiável para execução direta:
1. Misturava versões e caminhos de importação de LangChain; bibliotecas dependem de integrações e versões específicas.
2. Dependia de OpenAI, Chroma e chave de API mesmo para ensinar um índice mínimo.
3. Não separava teste de recuperação de teste de geração.
4. Não testava casos sem documentos pertinentes, identificadores de fontes nem autorização de acesso.
5. Não tinha dados sintéticos, asserts reproduzíveis ou relatório.
6. Pressupunha que RAG exige embeddings/banco vetorial. **Não exige.**

**Decisão:** SQLite FTS5 + BM25 para o núcleo sem dependências; API Ollama opcional para vetores e geração. A busca vetorial demonstrativa calcula similaridade em Python; **não foi projetada para grandes coleções**.

## Requisitos

- Python 3.11 ou mais recente e SQLite compilado com FTS5 (verificado pelo comando de teste abaixo).
- Núcleo lexical: **nenhuma dependência externa**.
- PDFs **com texto selecionável**, quando utilizados: `python -m pip install pypdf` (opcional).
- Geração local opcional: Ollama instalado e iniciado, com `llama3.2:3b`.
- Embeddings locais opcionais: Ollama + `nomic-embed-text` (diferentes modelos usam convenções próprias de prefixo).

> No Windows use o Terminal ou PowerShell. Se `python` não funcionar, substitua por `py -3`. Os comandos abaixo pressupõem a pasta `laboratorio/rag-pratico` do projeto já extraído.

## Passada 1 — recuperação local, sem IA

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

## Passada 2 — geração com IA local (opcional)

Instale e inicie o [Ollama](https://ollama.com/download), então:

```powershell
ollama pull llama3.2:3b
python rag_lab.py answer --question "Qual sensor foi marcado para substituição preventiva?"
```

**Critério de aprovação manual:** a resposta cita corretamente **S2**, faz referência ao documento de inventário e não inventa resultados adicionais. O estado `GERADO_SEM_VERIFICACAO_FACTUAL` indica apenas que houve geração, **não** que a resposta foi confirmada.

## Passada 3 — embeddings locais (opcional)

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

## Gates de verificação

| Gate | Verificação | Estado documentado |
|---|---|---|
| G1 | Importação e execução do núcleo Python | PASS — ensaio local |
| G2 | Criação do índice a partir de 3 documentos sintéticos | PASS — ensaio local |
| G3 | Hit@2 para 3 perguntas sintéticas | PASS 3/3 — ensaio local |
| G4 | 7 testes automatizados | PASS 7/7 — ensaio local |
| G5 | Montagem do prompt e fontes | PASS — ensaio local |
| G6 | Comunicação embedding/chat com resposta simulada | PASS — mock; não é prova de serviço |
| G7 | Ollama real com modelo baixado, hardware e medição | **NOT_RUN — exige execução do leitor** |
| G8 | Qualidade factual, privacidade, escalabilidade, segurança e benchmark | **NOT_RUN — fora do escopo da prova mínima** |

### Limitações explícitas

- A busca BM25 usa união de termos, não um entendimento semântico. Correspondência de palavras pode retornar um trecho **irrelevante**. A ausência de hits provoca abstenção automática; um hit fraco não garante evidência suficiente.
- O prompt instrui a não obedecer a trechos maliciosos, mas **isso não é uma defesa infalível contra prompt injection**.
- Sem controle de permissões por documento, este é um exemplo **para dados públicos ou fictícios**, não para fontes sensíveis nem uso multiusuário.
- O texto do modelo pode citar referências erradas. **Referências geradas precisam de conferência.**
- `temperature=0` não garante determinismo completo.
- Não inclui reranker, busca híbrida, HyDE, avaliação automática do texto do LLM, interface web nem implantação em produção.
- Operações externas estão limitadas ao Ollama por URL configurável; para o ensaio utilize o endereço padrão de loopback.

## Fontes técnicas

- [SQLite FTS5 e BM25](https://www.sqlite.org/fts5.html)
- [Ollama API: embeddings](https://docs.ollama.com/api/embed)
- [Ollama API: chat](https://docs.ollama.com/api/chat)
- [PyPDF](https://pypdf.readthedocs.io/en/stable/)
- [Documentação de integração do LangChain](https://docs.langchain.com/oss/python/integrations/providers/overview)

**Referência visual externa:** material com assinatura *m-softtech*. O laboratório, o fluxograma e o código foram elaborados em formato próprio, sem copiar os comandos ou a arte original. O crédito é referência temática, não declaração de licença ou endosso.
