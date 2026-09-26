# Extratores de características de domínio (Fase 3)

| Script | Item | O que faz | Saída |
|---|---|---|---|
| `metricas_2010_pddl.py` | R-25 | Extrai do PDDL as métricas de 2010 que têm correspondente no PDDL (11 de 17), por regras fixas descritas no próprio script, e compara com os valores publicados | `metricas-2010-pddl/` |
| `features_sas.py` | R-26 | *Features* modernas por instância, a partir da tradução SAS+ do Fast Downward: tamanho, grafo causal (densidade, ciclos, componentes, *treewidth*) e DTG (conectividade, arcos invertíveis); mediana por domínio | `features-sas/` |

## Benchmarks

Os scripts leem os domínios do repositório `potassco/pddl-instances` no commit `cf19edf` (o mesmo de `data/2010/benchmarks_ipc_mapa_final.csv`). O repositório não é versionado aqui (`.gitignore`); para obtê-lo:

```bash
git clone https://github.com/potassco/pddl-instances.git experimentos/benchmarks/ipc/pddl-instances
git -C experimentos/benchmarks/ipc/pddl-instances checkout cf19edf
```

## Fast Downward (tradutor)

O `features_sas.py` usa o tradutor do Fast Downward, release-26.6.0 (commit `7ea275526`), fora do git:

```bash
git clone https://github.com/aibasel/downward.git experimentos/ferramentas/downward
git -C experimentos/ferramentas/downward checkout release-26.6.0
```

## Como rodar

```bash
uv run --no-project python experimentos/extratores/metricas_2010_pddl.py
uv run --no-project --with networkx python experimentos/extratores/features_sas.py --limite 300 --processos 8
```

Saídas em `metricas-2010-pddl/`:
- `metricas.csv`: valor extraído por domínio e métrica, com o arquivo PDDL usado;
- `comparacao.csv`: valor e classe (Baixo/Médio/Alto) de 2010 × extraídos, por domínio;
- `resumo.csv`: por métrica, valores iguais, correlação de postos e classes iguais.

A classe do valor extraído usa a regra de discretização que 2010 aplicou de fato (extremos do treino, achado G23). Os valores de 2010 comparados já incluem as correções aprovadas (`data/2010/correcoes_2010.csv`).
