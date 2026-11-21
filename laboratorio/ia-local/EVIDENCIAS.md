# Evidências — LAB-LOCAL-01

Reexecução em 21/11/2026, Python 3.13.5, dados fictícios.
- `python lab.py`: prazo conferido 45 dias [POL-003], modo offline.
- `python -m unittest discover -s tests -v`: 7/7 aprovados. Ver saida-testes.txt (tempo omitido).
- Quatro verificações estáticas via PyYAML: conjunto de três serviços; portas publicadas apenas em loopback; OLLAMA_NO_CLOUD igual a 1; ENABLE_OPENAI_API false e OLLAMA_BASE_URL apontando para o serviço interno.
- O teste de API usa mock, não um servidor. O teste de redirecionamento chama o método isoladamente. Não comprovam segurança de rede nem resposta de LLM.
- Docker não disponível no ambiente do ensaio. Não executados: Compose, Ollama/modelo, Open WebUI, embeddings, Docling, n8n, SSH, isolamento/egress, carga e restauração.
- As tags de imagens são móveis; versões e digests precisam ser fixados após a validação de cada instalação. Nenhum dado real, segredo ou log de máquina foi incluído.

## Gates
G0 Python offline: PASS limitado (7/7).
G1 YAML estático: PASS limitado (4/4).
G2 Docker e inferência: PENDENTE.
G3 WebUI, RAG e Docling: PENDENTE.
G4 rede, acesso remoto e privacidade efetiva: PENDENTE.
G5 automação n8n: PENDENTE.

Não confundir instruções propostas com execuções realizadas. O filtro de metadados é recuperação estruturada, não um RAG vetorial completo. Nenhuma validação de produção é alegada.
