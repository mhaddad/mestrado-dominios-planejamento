# Registro de experimento — EXP-14: X3, LLM como seletor (condição anônima)

| Campo | Valor |
|---|---|
| ID | EXP-14 |
| Data | 26/09/2026 |
| Fase | 4 |
| Pergunta | Q3: o LLM como seletor de planejador (`llm/x3-seletor/protocolo.md`, aprovado pelo autor) |
| Autor da execução | Claude Code (claude-opus-5-5), a pedido do autor |

## Configuração

- **Código:** `llm/x3-seletor/x3_seletor.py`.
- ***Prompt*:** `llm/prompts/x3-anonimo-v1.md`, em inglês.
- **Dados:** os 41 domínios e a cobertura publicada do EXP-12. O modelo recebe o domínio PDDL e a instância p01 do Autoscale.
  - Três arquivos passam de 40 KB e foram truncados: o domínio do Airport, o do Organic Synthesis e a instância do NoMystery.
- **Catálogo:** os 29 planejadores anônimos (P01–P29), em ordem sorteada com semente 2026, descritos só pelas técnicas da taxonomia 4D (EXP-13, aprovada).
  - Descrições idênticas: quando o modelo escolhe uma, vale a cobertura média do grupo (regra fixada antes da primeira chamada). Há três grupos: seis planejadores "busca progressiva + relaxação + STRIPS + único" (HSP, HSP2, FF, C3, YAHSP3, FFSA); três portfólios do Fast Downward (FDSS11, FDRemix, FDSS23); os dois LAMA.
- **Modelos, via OpenRouter:**
  - `anthropic/claude-sonnet-5`, atendido pela Claude Platform on AWS;
  - `openai/gpt-6-sol`;
  - `google/gemini-3.1-pro-preview`;
  - `deepseek/deepseek-v4-pro-0813`.

  O provedor de cada chamada está no registro bruto.
- **Parâmetros:** raciocínio no nível *medium*; `max_tokens` de 16.000. No teste era 8.000; o DeepSeek o esgotou só raciocinando, e o limite foi dobrado para todos antes da rodada principal. Uma repetição por par domínio × modelo. A temperatura é o padrão de cada modelo, porque parte deles não aceita ajuste com raciocínio ligado.
- **Custo:** US$ 2,69 no total, contra o teto de US$ 10: teste (12 chamadas) US$ 0,10; rodada principal (164 chamadas) US$ 2,59.
  - Por modelo, na rodada principal: Sonnet 5, US$ 0,71; GPT-6 Sol, US$ 0,66; Gemini 3.1 Pro, US$ 0,83; DeepSeek, US$ 0,39.
- **Datas:** chamadas em 26/09/2026. Cada registro traz a data UTC.

## Como reproduzir

```
uv run --no-project --with scikit-learn --with scipy python llm/x3-seletor/x3_seletor.py rodar --rodada principal
uv run --no-project --with scikit-learn --with scipy python llm/x3-seletor/x3_seletor.py avaliar --rodada principal
```

Rodar de novo não reproduz as respostas, porque os modelos mudam. As respostas desta rodada estão versionadas em `llm/registros/x3/`.

## Resultado

**Onde estão os resultados:**
- `llm/x3-seletor/resultados/principal/` (`resumo.csv`, `escolhas.csv`);
- as respostas brutas em `llm/registros/x3/principal/`.

| Seletor | Perda total (41 domínios) | Domínios com perda 0 | Wilcoxon vs. SBS | Escolha mais frequente |
|---|---|---|---|---|
| SBS (Levitron) | 143 | 14 | — | Levitron (41) |
| GPT-6 Sol | 146 | 14 | p = 0,18 | Levitron (32), Maidu (7) |
| DeepSeek V4 Pro | 188,5 (1 resposta inválida) | 14 | p = 0,011 (pior) | Levitron (26), FDSS23 (8) |
| Gemini 3.1 Pro | 253,7 | 12 | p < 0,001 (pior) | Maidu (23), FDSS23 (8) |
| Claude Sonnet 5 | 259 | 11 | p = 0,003 (pior) | FDSS23 (20), Mercury (10) |
| Melhor seletor por características (EXP-12, *random forest*, pddl+sas) | 148 | 15 | p = 0,57 | — |

- **Portfólios em quase todas as escolhas:** 158 das 163 respostas válidas apontam para um portfólio. As exceções são o Mercury (10 vezes, Sonnet) e o LAPKT-BFWS (4 vezes, Gemini).
- **Nos quatro domínios em que uma técnica antiga é a melhor** (System R no Blocks World e no TPP, SAT no Floortile, ANS no Pipesworld sem tanques), nenhum modelo escolhe o planejador vencedor nem a sua técnica.

## Interpretação

- **Nenhum LLM escolhe melhor que o *single best*.** O GPT-6 Sol empata na prática (146 contra 143, sem diferença significativa). Os outros três ficam significativamente piores. `[FATO]`
- **O comportamento dominante parece ser "escolher o mais completo".** `[HIPÓTESE]` A descrição que o GPT-6 Sol e o DeepSeek preferem, a do P07 (Levitron), é a que lista mais técnicas: duas buscas, três heurísticas, duas representações e portfólio. O resultado bom do GPT-6 Sol vem mais dessa regra geral do que de ler a estrutura de cada domínio: ele raramente troca de escolha entre domínios.
- **Parte da perda do Sonnet e do Gemini vem da regra das descrições iguais.** O FDSS23, escolha frequente do Sonnet, divide a descrição com o FDSS11 e o FDRemix, e a média do grupo rebaixa a cobertura. É o custo esperado de uma descrição que não distingue os planejadores; a regra foi fixada antes da rodada. `[FATO]`
- **Para a Q3:** nesta condição, o LLM como seletor fica no mesmo patamar do melhor seletor por características (EXP-12), ou abaixo. Nenhum dos dois captura o ajuste fino entre técnica e domínio que o mapa do EXP-13 mostra. `[HIPÓTESE]` Os LLMs trazem um viés a favor da técnica "mais sofisticada", o mesmo tipo de regra geral que o *single best* já codifica.

## Limites

- Uma repetição por par domínio × modelo. A variação entre repetições não foi medida.
- Condição anônima só: a condição com nomes (contaminação) não foi rodada.
- As descrições 4D são grossas: 29 planejadores caem em 20 descrições distintas.
- O desempenho vem da cobertura publicada (só por domínio), como no EXP-12.
