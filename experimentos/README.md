# Fase 3 — Infraestrutura e replicação experimental

**Objetivo:** responder Q1 e Q2 com amostra ampla, extração automática de *features* e método estatístico adequado.
**Critério de conclusão:** experimentos reprodutíveis a partir do repositório e resultados analisados.

| Pasta | Conteúdo | Versionado? |
|---|---|---|
| `containers/` | Definições de contêiner (Docker/Apptainer) do ambiente de execução | Sim (definições); imagens `.sif` não |
| `benchmarks/` | Scripts que baixam e organizam os benchmarks das IPCs 1998–2023 | Scripts sim; `benchmarks/ipc/` não |
| `planejadores/` | Scripts de compilação e teste de cada planejador; registro do que não compilou | Sim |
| `extratores/` | Extrator das métricas de 2010 a partir do PDDL; extrator de *features* modernas | Sim |
| `execucoes/` | Scripts de execução e resultados agregados; `brutos/` fica fora do Git | Agregados sim |
| `analise/` | Notebooks e scripts de análise, modelos de seleção, validação | Sim |

## Desenho (resumo)

- **Condições:** mesmo hardware, limite de tempo e memória para todos os planejadores.
- **Desempenho:** cobertura, tempo, qualidade do plano, escore IPC.
- **Conjuntos de *features*:** (a) métricas de 2010 extraídas do PDDL; (b) *features* modernas; (c) combinação.
- **Modelos:** *random forest*, *gradient boosting*; linha de base = ranking por médias de 2010.
- **Validação:** *leave-one-domain-out*; comparação com *single best* e *virtual best*.

Detalhes e atividades: seção 7 (Fase 3) do [plano](../plan/plano-revisao-dissertacao.md).

Todo número que vai para o texto sai daqui, com script + dados + configuração versionados.
Para cada rodada de experimento, preencha [templates/registro-experimento.md](../templates/registro-experimento.md).
