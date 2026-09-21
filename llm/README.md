# Fase 4 — Camada LLM

**Objetivo:** responder Q3: onde os LLMs entram no mapa das técnicas de planejamento.
**Critério de conclusão:** os quatro experimentos executados e registrados.

| Pasta | Experimento | Pergunta |
|---|---|---|
| `x1-planejador/` | LLM como planejador | Desempenho em relação aos planejadores clássicos num subconjunto de domínios |
| `x2-tradutor/` | LLM como tradutor | O LLM gera PDDL correto a partir de linguagem natural? Com que taxa de erro? |
| `x3-seletor/` | LLM como seletor | Dada a descrição do domínio, o LLM escolhe bem o planejador? Comparar com o seletor da Fase 3 |
| `x4-verificador/` | LLM + verificador | Um validador formal (ex.: VAL) melhora X1? |
| `prompts/` | *Prompts* versionados | |
| `registros/` | Registro de cada rodada: modelo, versão, data, custo | |

## Regras

- **Congelar a versão do modelo** e registrar a data de cada rodada. Resultados mudam com novas versões.
- Registrar custo e *prompts* de cada rodada.
- Usar [templates/registro-experimento.md](../templates/registro-experimento.md).
