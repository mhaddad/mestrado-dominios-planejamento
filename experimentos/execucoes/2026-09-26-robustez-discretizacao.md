# Registro de experimento — EXP-10: Nível 2, R-16 (robustez da discretização com mais domínios)

| Campo | Valor |
|---|---|
| ID | EXP-10 |
| Data | 26/09/2026 |
| Fase | 3 |
| Pergunta | Q1 (item R-16 de `auditoria/reexecucao.md`; F7, G10; AF-250, AF-346) |
| Autor da execução | Claude Code (claude-opus-5-5), a pedido do autor |

## Configuração

- **Código:** `experimentos/analise/robustez_discretizacao.py`, que usa o extrator do R-25 (EXP-07).
- **Por que PDDL:** o acervo não tem modelos UML de outros domínios. O teste usa as 11 métricas extraíveis do PDDL, não as contagens de 2010. Mede, portanto, a estabilidade da regra de discretização, não a das classes publicadas.
- **Domínios adicionais:** uma variante por família das IPCs 1998–2008 que não esteja entre as 13, na edição mais antiga. Só variantes clássicas, com preferência por STRIPS e, em 2008, pela trilha sequencial *satisficing*. A lista está no script.
- **Revisão da regra depois da primeira execução:** a primeira execução aceitou variantes STRIPS que são compilações aterradas, com ações sem parâmetros (96.942 no Cyber Security, 446 no Promela Optical Telegraph). A regra passou a exigir variante *lifted*: no máximo metade das ações sem parâmetros. Quando a variante preferida é aterrada, passa-se à seguinte da família.
  - Quatro famílias trocaram para a variante ADL: Promela Dining Philosophers, Promela Optical Telegraph, Openstacks e Trucks. O Airport ficou com a variante STRIPS, que é *lifted*.
  - Cyber Security e PSR ficaram de fora, porque não têm variante *lifted* entre as candidatas.
  - Resultado: **18 domínios adicionais** e população ampliada de 28 domínios (10 de treino + 18).
  - A primeira execução, com 20 domínios, dava 29 de 143 classes alteradas pela regra dos extremos e 71 pela regra do texto. A direção da conclusão é a mesma.
- **Regras de discretização:** a aplicada em 2010 (extremos da população, G23) e a escrita no texto (variância, EXP-04).
- **Populações:** os 10 domínios de treino, como em 2010, contra os 28 da população ampliada. Compara-se a classe que cada um dos 13 domínios recebe em cada caso.

## Como reproduzir

```
uv run --no-project python experimentos/analise/robustez_discretizacao.py
```

Requer os benchmarks (ver `experimentos/extratores/README.md`).

## Resultado

**Onde estão os resultados:** `experimentos/analise/robustez-discretizacao/`:
- `dominios-adicionais.csv`: variante escolhida, variantes recusadas e valores;
- `classes.csv`: classe de cada domínio por métrica, regra e população;
- `resumo.csv`.

| Regra | Classes dos 13 domínios que mudam (11 métricas × 13 = 143) |
|---|---|
| Extremos (aplicada em 2010) | 24 (17%) |
| Texto (variância) | 64 (45%) |

- **Regra dos extremos:**
  - 22 das 24 mudanças são de Alto para Médio, e 2 de Baixo para Médio.
  - Das 11 métricas, 9 perdem distinção entre os 13 domínios: com 10 domínios todas têm 3 classes; com 28, sete ficam com 2 classes e duas, com 1 (Casos de Uso por Atores e Associações).
  - Só Hierarquias e DIT não mudam.
- **Regra do texto:** as métricas ligadas a ações (casos de uso, métodos, ações) mudam nos 13 domínios, que passam todos à mesma classe. A variância da população ampliada é dominada por domínios grandes: o Airport tem 39 ações; o Parc Printer, 23.

## Interpretação

- **A classe que um domínio recebe depende de quais outros domínios estão na amostra, e não só do próprio domínio.** `[FATO]` Pela regra de 2010, basta acrescentar domínios com valores fora da faixa dos 10 de treino para que o antigo máximo deixe de ser Alto. Pela regra do texto, a variância da população define os limites, e metade das classes muda.
- **Consequência para AF-250 e AF-346:** com mais pontos, a discretização por variância em Alto/Médio/Baixo não se sustenta como característica do domínio. `[HIPÓTESE]` Isso reforça a recomendação da auditoria (AF-346, R-30): no Nível 4, trabalhar com as métricas contínuas (regressão ou modelos baseados em árvore) em vez de discretizá-las, e tratar Alto/Médio/Baixo só como leitura descritiva de uma população fixa e declarada.
- **Limite:** o teste usa as métricas do PDDL, não as contagens UML de 2010. Para as 3 métricas que dependem da modelagem (atores, atributos, associações; EXP-07), a extração é só aproximada.

## Problemas e desvios

- A regra de seleção dos domínios foi revista depois da primeira execução (variantes aterradas). A revisão e o resultado anterior estão registrados acima e no cabeçalho do script.
- Para famílias com domínio por instância (Airport, Parc Printer), usou-se o domínio da primeira instância, como no Pathways.
