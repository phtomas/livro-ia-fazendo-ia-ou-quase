# laboratório de IA — Cinco Sistemas de IA (protótipo documental)

Projeto de estudo **original, didático, reproduzível e sem uso de rede** inspirado nas cinco categorias mostradas no vídeo enviado em 20/11/2026.

**Atenção:** o projeto foi criado nesta sessão de trabalho e **não foi instalado em equipamento real**. O protótipo Python foi testado aqui com 10 testes locais; não existe certificação de hardware, GPU, Ollama, RAG de produção ou integrações externas.

## Cinco módulos em uma só oficina

| Módulo | Código de demonstração | Próxima integração |
|---|---|---|
| 1. Assistente documental | `python3 lab.py documentos "Qual é o prazo de reembolso?"` | Reutilizar [LAB-RAG-01](https://github.com/phtomas/livro-ia-fazendo-ia-ou-quase/tree/main/laboratorio/rag-pratico), sem duplicar |
| 2. Recepcionista por voz | `python3 lab.py voz "Quero agendar um atendimento"` | STT com faster-whisper, agenda opcional e TTS, com autorização |
| 3. Leitor de faturas | `python3 lab.py fatura` | Extração PDF/OCR, JSON com esquema rígido e revisão humana |
| 4. Assistente de pesquisa | `python3 lab.py pesquisa` | Recuperação de fontes externas, autoria, data e contrapontos |
| 5. Plataforma de avaliação | `python3 lab.py avaliar --saida saida/avaliacao.json` | Testes de regressão do RAG e dos demais módulos |

## Execução em ambiente próprio (Python 3)

Usar um terminal **na pasta extraída**. Não requer instalar nenhum pacote Python, CUDA ou Ollama:

```bash
python3 --version
python3 -m unittest discover -s testes -v
python3 lab.py diagnostico
python3 lab.py avaliar --saida saida/avaliacao.json
python3 lab.py documentos "Qual é o prazo de reembolso?"
python3 lab.py fatura
python3 lab.py pesquisa
python3 lab.py voz "Quero agendar um atendimento amanhã"
```

Este projeto não ativa serviços de rede nem exige acesso remoto. Não divulgue logs ou inventários do ambiente em repositórios públicos.

## O que os testes provam (e o que não provam)

- **Validado nesta sessão:** 10 testes `unittest`; demonstrações sintéticas de busca lexical, extração de campos, sinalização de divergências, simulação sem efeitos externos e avaliação `hit@k`.
- **Não validado:** desempenho em equipamento real, NVIDIA, VRAM, áudio real, PDFs escaneados, qualidade de um LLM, rede, segurança multiusuário e conexão com serviços reais.
- **Limitação intencional:** o localizador de documentos aqui é uma busca simples por palavras; o sistema existente LAB-RAG-01 é a base correta para o RAG da oficina.
- **Sem ações externas:** `voz` nunca agenda realmente; `fatura` nunca paga nem registra despesa; `pesquisa` só compara fontes de exemplo.
- **Dados:** todos os exemplos são fictícios. Nunca colocar dados pessoais, receitas ou chaves de API no repositório.

## Planejamento de integração

1. **G0 / Sistema:** verificar Ubuntu, CPU, RAM, discos, SMART, `nvidia-smi`, segurança de acesso. Nada de instalar grandes modelos até a linha de base ficar estável.
2. **G1 / Dados + avaliação:** importar uma cópia do LAB-RAG-01 e medir recuperação em dados sintéticos. Uma única suíte de regressão para os cinco sistemas.
3. **G2 / Assistente documental:** trazer manuais técnicos autorizados, indexação com versões, autorização por fonte, abstenção e auditoria de citações.
4. **G3 / Pesquisa:** fontes múltiplas, conflito explícito, data da fonte e parecer revisável.
5. **G4 / Faturas:** extração e validação com conferência humana; não automatizar movimentação financeira.
6. **G5 / Voz:** reconhecimento local, intenção, confirmação do usuário e integração controlada com agenda; gravações dependem de autorização.
7. **G6 / Operação:** observabilidade, regressão, backup, política de retenção e limites de CPU/GPU.

## Estrutura para GitHub, preservando convenções do livro

- `complementos/cinco-sistemas-ia-laboratório de IA/` — caderno e figuras vetoriais para o leitor;
- `laboratorio/laboratório de IA-cinco-sistemas/` — este código com dados fictícios e testes;
- `videos/index.html` — adicionar o episódio **somente após a publicação no YouTube**.

Não subir vídeo MP4 diretamente ao GitHub. O complemento pode ser publicado separadamente da videoteca, mantendo o padrão do acervo.

## Referências técnicas oficiais (consultadas em novembro de 2026)

- LAB-RAG-01 já publicado: https://github.com/phtomas/livro-ia-fazendo-ia-ou-quase/tree/main/laboratorio/rag-pratico
- Ollama Linux: https://ollama.com/download/linux
- Docling: https://docling-project.github.io/docling/getting_started/installation/
- Faster-Whisper: https://github.com/SYSTRAN/faster-whisper
- Promptfoo: https://www.promptfoo.dev/docs/getting-started/

**Lema:** Nada é “funcionou” sem prova. Simplicidade é força. Isole e meça antes de adivinhar. Não reinvente a roda. E cresçam juntos.
