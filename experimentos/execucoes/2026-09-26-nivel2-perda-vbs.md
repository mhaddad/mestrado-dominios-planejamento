# Registro de experimento — EXP-09: Nível 2, R-14 (perda em relação ao *virtual best*)

| Campo | Valor |
|---|---|
| ID | EXP-09 |
| Data | 26/09/2026 |
| Fase | 3 |
| Pergunta | Q1 (item R-14 de `auditoria/reexecucao.md`; G19; AF-299, AF-322, AF-334) |
| Autor da execução | Claude Code (claude-opus-5-5), a pedido do autor |

## Configuração

- **Decisão do autor (26/09/2026, G19):** a medida principal passa a ser a **perda em relação ao *virtual best***. A correlação de postos é secundária, e o acerto por posição fica só para comparar com 2010. Todas as medidas são reportadas, sempre ao lado da linha de base.
- **Perda:** em cada domínio de validação, a nota observada do melhor planejador menos a nota observada do planejador que o método põe em 1º lugar. Se vários empatam em 1º na previsão (notas com duas casas), usa-se a média entre eles. Perda zero quer dizer que a indicação é tão boa quanto a melhor possível.
- **Código:** `experimentos/analise/nivel2.py`, função `avaliar`, aplicada a todos os cenários dos EXP-04, EXP-06 e EXP-08. A linha de base sem características é o *single best*: o planejador de maior nota média no treino (YAHSP).

## Como reproduzir

```
uv run --no-project python experimentos/analise/nivel2.py
```

## Resultado

**Onde estão os resultados:** `experimentos/analise/nivel2/cenarios.csv` (colunas `perda_*`) e `rankings.csv` (colunas `perda_vbs` e `empatados_no_topo_previsto`).

**Quão exigente é cada domínio** (notas observadas, Tabelas 31, 37 e 43):

| Domínio | Nota máxima | Planejadores com a nota máxima | Perda média de uma escolha ao acaso |
|---|---|---|---|
| Storage | 9 | 1 de 10 | 4,0 |
| Zeno-travel | 10 | 6 de 10 | 1,2 |
| Elevator | 10 | 5 de 10 | 1,9 |

**Perda por cenário** (Storage / Zeno-travel / Elevator):

| Cenário | Planejador indicado no Storage | Perda |
|---|---|---|
| Referência (método de 2010, aritmética corrigida) | Fast Downward | 3 / 0 / 0 |
| Regra de discretização do texto (amostral e populacional) | Fast Downward | 3 / 0 / 0 |
| Correções G17; classes com auxiliares; sem G24 | Fast Downward | 3 / 0 / 0 |
| 4D, todas as dimensões | LPG | 0 / 0 / 0 |
| 4D, só D1 | LPG | 0 / 0 / 0 |
| 4D, só D2; só D3 | Fast Downward | 3 / 0 / 0 |
| Linha de base (*single best*: YAHSP) | YAHSP | 1 / 0 / 0 |

## Interpretação

- **Só o Storage discrimina.** No Zeno-travel e no Elevator, metade ou mais dos planejadores tem a nota máxima, e todos os cenários, inclusive a linha de base, têm perda zero. Esses dois domínios não permitem avaliar a indicação do melhor planejador. `[FATO]`
- **No Storage, o método de 2010 indica pior que a linha de base.** Ele põe o Fast Downward em 1º (nota observada 6, perda 3), enquanto o *single best* sem características indica o YAHSP (nota 8, perda 1). `[FATO]` Todos os cenários com os 11 rótulos de 2010 dão o mesmo resultado.
- **Com a taxonomia 4D (todas as dimensões ou só a D1), o método indica o LPG,** o melhor observado no Storage, com perda zero. `[FATO]` `[HIPÓTESE]` É um único domínio discriminante e uma única indicação; não sustenta que a taxonomia 4D seja melhor. Como mostrou o EXP-06, na 4D o LPG tem valores de técnica só dele, e a indicação reflete em boa parte as notas de treino do próprio LPG.
- **Consequência para AF-299, AF-322 e AF-334:** pela medida principal, a validação de 2010 não mostra ganho sobre a linha de base sem características. Nos dois domínios em que a escolha importa pouco, empata; no único em que importa, perde. A pergunta de 2010 continua aberta e passa para o Nível 4, com mais domínios discriminantes.

## Problemas e desvios

- Com 3 domínios de validação, e só 1 discriminante, nenhuma diferença de perda entre cenários tem força estatística.
- A perda usa as notas inteiras publicadas (0–10), a mesma escala das tabelas de 2010.
