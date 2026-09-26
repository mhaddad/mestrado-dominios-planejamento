# Registro de experimento — EXP-12: Nível 4 com dados publicados (Planner Museum × *features* do PDDL)

| Campo | Valor |
|---|---|
| ID | EXP-12 |
| Data | 26/09/2026 |
| Fase | 3 |
| Pergunta | Q1 e Q2, por domínio (itens R-24, R-27, R-28 e R-30 de `auditoria/reexecucao.md`, na versão restrita a dados publicados) |
| Autor da execução | Claude Code (claude-opus-5-5), a pedido do autor |

## Configuração

- **Decisão do autor (26/09/2026):** Nível 4 só com dados publicados, *benchmarks* Autoscale (`experimentos/nivel4-proposta.md`; plano, seção 10).
- **Desempenho:** cobertura por domínio do Planner Museum (`data/planner-museum/cobertura_por_dominio.csv`): 29 planejadores × 42 domínios Autoscale, 30 instâncias cada, 30 min e 4 GiB.
  - O Pathways fica fora: nenhum planejador resolve nenhuma instância. Restam **41 domínios**.
- **Características por domínio,** extraídas do PDDL das mesmas instâncias Autoscale (`experimentos/ferramentas/planner-museum`, commit `723a31c0`):
  - **(a) `pddl`:** as 11 métricas de 2010 extraíveis do PDDL (extrator do EXP-07). Nos domínios com um arquivo por instância, usa-se o da primeira. Airport (953 ações) e Organic Synthesis (1.020) têm domínios semiaterrados.
  - **(b) `sas`:** as 17 *features* SAS+ (extrator do EXP-11), mediana de uma **amostra fixa de 10 instâncias por domínio** (p01, p04, …, p28).
    - A primeira tentativa, com as 30 instâncias e 300 s por tradução, foi interrompida: as instâncias maiores levam minutos cada, e a estimativa no pior caso era de cerca de 17 horas.
    - Com 120 s por tradução, 391 de 420 instâncias traduziram. Os 29 tempos esgotados estão em 11 domínios; no pior caso, o Zeno-travel ficou com 5 de 10.
    - Nesses 11 domínios, a mediana vem das instâncias menores.
  - **(c) `pddl+sas`:** os dois conjuntos juntos.
- **Tarefa e medida:** escolher um planejador por domínio. A perda é a cobertura do melhor planejador no domínio menos a do escolhido (medida principal, G19). Validação *leave-one-domain-out*.
- **Seletores:**
  - *virtual best* (VBS);
  - *single best* (SBS): maior cobertura total no treino;
  - acaso;
  - **método de 2010**, com o planejador no lugar da técnica e discretização pelos tercis do treino. A regra dos extremos deixa quase tudo em Médio com 41 domínios (EXP-10). A classificação dos 29 planejadores na taxonomia 4D ainda não existe;
  - **kNN**, com 3 vizinhos;
  - ***random forest*** de regressão com várias saídas (300 árvores, semente 2010).
- **Comparação com o SBS:** teste de Wilcoxon pareado sobre a diferença de perda por domínio.

## Como reproduzir

```
uv run --no-project --with networkx python experimentos/extratores/features_sas.py --conjunto autoscale --limite 120 --processos 6
uv run --no-project --with scikit-learn --with scipy python experimentos/analise/nivel4_publicados.py
```

Requer o clone do Planner Museum (ver `experimentos/nivel4-proposta.md`) e o tradutor do Fast Downward (ver `experimentos/extratores/README.md`).

## Resultado

**Onde estão os resultados:**
- `experimentos/extratores/features-sas-autoscale/`;
- `experimentos/analise/nivel4-publicados/` (`caracteristicas.csv`, `escolhas.csv`, `resumo.csv`).

**Escala:** 41 domínios e 1.230 instâncias. O VBS resolve 1.096. O SBS é o **Levitron** (IPC 2023) em todos os 41 recortes e resolve 953. A lacuna entre os dois é de 143 instâncias.

| Seletor | Perda média por domínio | Perda total | Domínios com perda 0 | Lacuna SBS→VBS fechada | Wilcoxon (vs. SBS) |
|---|---|---|---|---|---|
| VBS | 0 | 0 | 41 | 100% | — |
| SBS (Levitron) | 3,49 | 143 | 14 | 0% | — |
| Acaso | 14,30 | 586 | 0 | −310% | — |
| Método de 2010 (pddl) | 3,90 | 160 | 15 | −12% | p = 0,13 |
| Método de 2010 (sas; pddl+sas) | 3,49 | 143 | 14 | 0% (escolhe sempre o Levitron) | — |
| kNN (pddl) | 5,56 | 228 | 16 | −59% | p = 0,06 |
| kNN (sas) | 5,63 | 231 | 13 | −62% | p = 0,009 (pior) |
| kNN (pddl+sas) | 5,37 | 220 | 15 | −54% | p = 0,049 (pior) |
| *Random forest* (pddl) | 3,68 | 151 | 15 | −6% | p = 0,53 |
| *Random forest* (sas) | 4,61 | 189 | 11 | −32% | p = 0,011 (pior) |
| *Random forest* (pddl+sas) | 3,61 | 148 | 15 | −4% | p = 0,57 |

**Planejadores de 2010 no Planner Museum** (41 domínios, cobertura total e domínios em que empatam com o melhor):
- **FF:** 537 de cobertura; melhor em 5 domínios.
- **System R:** 269; melhor em 8.
- **Fast Downward (2004):** 379; melhor em 4.
- **Blackbox, IPP e LPG:** 42, 40 e 195; em nenhum.

## Interpretação

- **Por domínio, nenhuma característica extraída do PDDL ajuda a escolher o planejador melhor do que usar sempre o *single best*.** `[FATO]`
  - Os seletores que se afastam do Levitron trocam por outros planejadores do topo (Saarplan, FDSS23), e cada troca custa cobertura.
  - Nas *features* SAS+, o kNN e o *random forest* ficam significativamente piores que o SBS.
  - O método de 2010 empata com o SBS quando escolhe sempre o Levitron e fica um pouco pior com as métricas do PDDL.
- **A lacuna a fechar é pequena.** O SBS já resolve 87% do que o VBS resolve (953 de 1.096). `[FATO]` `[HIPÓTESE]` Com planejadores recentes, vários deles portfólios, o espaço para a seleção por domínio encolheu. Isso é coerente com `cenamor2016ibacop`, em que o ganho do portfólio vem da diversidade do conjunto, não dos modelos preditivos.
- **Ainda assim, planejadores antigos são os melhores em alguns domínios:** o System R em 8 e o FF em 5, contando empates. `[FATO]` É o mesmo fenômeno que `lequen2026planner` descreve. A pergunta de 2010 (que técnica, para que domínio) se sustenta como fenômeno, mas estas características, neste nível de agregação, não o capturam. `[HIPÓTESE]`
- **Q2, por domínio:** as métricas de 2010 extraídas do PDDL não se saem pior que as *features* SAS+. Ao contrário: com o *random forest*, `pddl` perde 151 e `sas` perde 189. Nenhum conjunto supera o SBS. `[FATO]` Não há evidência, nesta amostra, de que as *features* modernas acrescentem poder de seleção por domínio.

## Limites

- Só cobertura, só por domínio, 41 domínios. Sem tempo, qualidade do plano ou resultado por instância (decisão do autor). A seleção por instância, que é onde a literatura mostra ganhos (síntese E1), não pode ser testada com esses dados.
- As *features* SAS+ vêm de uma amostra de 10 instâncias, com as maiores faltando em 11 domínios.
- O método de 2010 usa o planejador no lugar da técnica. A versão por técnica depende de classificar os 29 planejadores na taxonomia 4D a partir das fontes primárias.
- Uma única semente no *random forest*.

## Próximos passos possíveis

1. **Classificar os 29 planejadores na taxonomia 4D e repetir a análise por técnica.** É a pergunta de 2010 propriamente dita.
2. **Repetir sem os portfólios.** `[HIPÓTESE]` Entre planejadores de uma técnica só, as características do domínio podem pesar mais. Isso depende da mesma classificação.
