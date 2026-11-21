# LAB-LOCAL-01 — IA local privada, passo a passo

[Oficina visual com comandos copiáveis](index.html) · [Videoaula](https://youtu.be/MZsT8y6JK9Y) · [Evidências](EVIDENCIAS.md).

## Primeira execução (Python 3.10+, sem dependências)
Baixe o ZIP do repositório, extraia e abra o terminal na pasta laboratorio/ia-local.
```bash
python3 lab.py
python3 -m unittest discover -s tests -v
```
No Windows, use py -3 se necessário. Esperado: 45 dias [POL-003] e 7 testes aprovados.

## Instalação opcional
Siga a oficina HTML: Docker atualizado, compose.yaml completo, chave local .env, Ollama e Open WebUI, API local, documentos fictícios, proteção de rede e n8n opcional. Não execute comandos em servidor de produção. Não publique .env, logs, configuração expandida, dados reais ou backups. Os endereços local e example são ilustrativos. O Compose usa CPU por padrão.

A seleção estruturada de versões é o ponto de partida; para busca vetorial/lexical, consulte o laboratório RAG existente. A conversão Docling pode começar com o Markdown sintético fornecido; para PDF, imprima a política fictícia em PDF localmente. A suíte offline é comprovada; integração real permanece pendente.
