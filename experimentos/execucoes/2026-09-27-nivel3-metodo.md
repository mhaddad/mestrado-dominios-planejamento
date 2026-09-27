# Registro de experimento — EXP-19: método de 2010 com as notas do Nível 3

| Campo | Valor |
|---|---|
| ID | EXP-19 |
| Data | 27/09/2026 |
| Fase | 3 |
| Pergunta | Q1 e F3: o resultado de 2010 se mantém quando as notas de treino vêm de uma só fonte? (G9, G21) |
| Autor da execução | Claude Code (claude-opus-5-5), a pedido do autor |

## Configuração

- **Código:** `experimentos/analise/nivel3_metodo.py`, que reusa o método e as medidas de `experimentos/analise/nivel2.py`.
- **Notas de treino:** do Nível 3 (EXP-05, `experimentos/analise/nivel3/resolvidos.csv`), pela regra de 2010 (G6): nota = porcentagem de problemas resolvidos ÷ 10, arredondada com o meio para cima. A regra reproduz 99 das 100 notas publicadas. LPG-TD: mediana das 3 sementes. **R × Pathways** não rodou (G26): mantém a nota de 2010 (0), marcada em `notas.csv`.
- **Validação:** ranking real de 2010 (`data/2010/validacao_ranking.csv`), por decisão do autor (27/09/2026). Os domínios de validação não foram reexecutados.
- **Classes das métricas:** as publicadas (referência do Nível 2). **Taxonomia:** a de 2010, com o G24 como na referência, salvo nos cenários indicados.
- **Medidas:** as do Nível 2: perda em relação ao *virtual best* (medida principal, decisão do autor de 26/09/2026), acerto por posição exata (G19), correlação de postos (Spearman).

## Como reproduzir

```
python3 experimentos/analise/nivel3_resumo.py
python3 experimentos/analise/nivel3_metodo.py
```

## Resultado

**Onde estão os resultados:** `experimentos/analise/nivel3/notas.csv` (notas de 2010 × Nível 3 por par), `cenarios.csv` e `rankings.csv`.

**Notas de treino** `[FATO]`: 23 das 100 notas mudam. Pelo rótulo de origem de `data/2010/eficiencia_planejadores.csv` (38 de competição e 62 de execução própria; pelo G21 seriam 34 e 66), mudam 18 das 38 de competição (diferença média de 1,58 ponto) e 5 das 62 de execução própria (0,16 ponto). As maiores mudanças são todas em pares de competição, exceto o Blackbox no Satellite (G25):

| Planejador | Domínio | 2010 | Nível 3 |
|---|---|---|---|
| Blackbox | Logistics | 10 (competição) | 0 |
| Fast Downward | Pathways | 10 (competição) | 2 |
| Blackbox | Satellite | 10 (execução própria) | 4 |
| SATPlan | Satellite | 3 (competição) | 9 |
| Blackbox | Blocks World | 3 (competição) | 8 |
| IPP | Blocks World | 3 (competição) | 8 |
| SGPlan | Pipesworld | 7 (competição) | 2 |
| Fast Downward | Pipesworld | 4 (competição) | 8 |

**Método** `[FATO]` (Storage / Zeno-travel / Elevator):

| Cenário | Perda × *virtual best* | Acerto por posição | Spearman |
|---|---|---|---|
| Notas de 2010 (referência do Nível 2) | 3 / 0 / 0 | 50% / 30% / 40% | 0,81 / 0,86 / 0,61 |
| **Notas do Nível 3** | **3 / 0 / 0** | **30% / 40% / 70%** | **0,85 / 0,86 / 0,84** |
| Nível 3, Satellite com notas de 2010 (G25) | 3 / 0 / 0 | 40% / 30% / 70% | 0,81 / 0,86 / 0,84 |
| Nível 3, Tabela 4 sem G24 | 3 / 0 / 0 | 30% / 40% / 50% | 0,86 / 0,86 / 0,84 |
| Nível 3, taxonomia em 4 dimensões | 0 / 0 / 0 | 10% / 20% / 20% | 0,74 / 0,72 / 0,80 |
| Linha de base (sem características), notas de 2010 | 1 / 0 / 0 | 0% / 0% / 10% | 0,75 / 0,68 / 0,65 |
| Linha de base, notas do Nível 3 | 1 / 0 / 0 | 10% / 10% / 10% | 0,84 / 0,69 / 0,67 |

## Interpretação

- `[FATO]` As notas de execução própria de 2010 se reproduzem quase inteiras (5 de 62 mudam, quase sempre em 1 ponto). As de competição, não (18 de 38 mudam, algumas em 5 a 10 pontos). A mistura de fontes (G9) afetava sobretudo esses pares.
- `[FATO]` Com as notas homogêneas, o planejador que o método põe em 1.º lugar tem a mesma nota observada que em 2010 nos três domínios (perda 3 / 0 / 0). A correlação de postos sobe no Elevator (0,61 → 0,84) e fica igual ou quase igual nos outros dois. O acerto por posição exata muda em direções opostas (Storage cai, Elevator sobe), o que reforça que essa medida é instável (G19).
- `[FATO]` A linha de base sem características continua próxima do método na correlação de postos em Storage (0,84 × 0,85). No Zeno-travel e no Elevator o método fica acima (0,86 × 0,69; 0,84 × 0,67), mas ela põe em 1.º lugar um planejador de perda menor no Storage (1 × 3).
- `[HIPÓTESE]` Com 3 domínios de validação e 10 planejadores, essas diferenças não permitem afirmar que o método com notas homogêneas é melhor ou pior que o de 2010. Não foi feito teste estatístico.
- `[HIPÓTESE]` Parte das notas do Nível 3 mede limitações das versões dos binários de 2010, não da técnica. Exemplo: o Blackbox declara insolúveis todos os problemas do Logistics e do Depots, os dois domínios com hierarquia de tipos de três níveis; na IPC, o Logistics dele teve 100%. Não foi testado.
- Os pares de competição usavam o conjunto completo de instâncias da IPC; o Nível 3 usa os subconjuntos do acervo (G14, G16). Parte das mudanças pode vir disso.

## Problemas e desvios

- O ranking real da validação é o de 2010, com as condições de 2010 (execução própria e competição misturadas). Treino e validação não estão nas mesmas condições.
- Satellite: o Nível 3 usa a versão da IPC, diferente da de 2010 (G25); o cenário com as notas de 2010 no Satellite mostra o efeito isolado.
