# Registro de experimento — EXP-04: Nível 2, discretização pela regra escrita no texto de 2010

| Campo | Valor |
|---|---|
| ID | EXP-04 |
| Data | 24/09/2026 |
| Fase | 3 |
| Pergunta | Q1 (Nível 2 de `auditoria/reexecucao.md`; achado G23) |
| Autor da execução | Claude Code (Coordenador, claude-opus-5-5), a pedido do autor |

## Configuração

- **Código:** `experimentos/analise/nivel2.py` (usa `reproducao_2010.py`).
- **Decisão do autor (24/09/2026):** as classes publicadas (Tabelas 10–11) teriam erro de transcrição; a regra escrita no texto é a correta. Informado de que a regra, generalizada, deixa métricas com uma só classe e de que as Tabelas 19–25 foram calculadas com as classes publicadas, o autor escolheu aplicá-la **como cenário do Nível 2**, mantendo o Nível 1 com as classes publicadas.
- **Regra do texto generalizada:** Baixo se valor ≤ v, Médio se ≤ 2v, Alto se > 2v, com v = variância dos 10 domínios de treino (amostral e populacional, porque o texto diz "aproximada": 3,5 no exemplo, entre 3,24 e 3,60).
- **Referência:** o método de 2010 recalculado com as classes publicadas, sem os erros aritméticos de G18. Mantêm-se as duas atribuições de técnicas do G24 (IPP fora de *Forward-chaining* na relação, dentro na nota dos planejadores). Notas previstas comparadas com duas casas, como em 2010; empates desempatados pela ordem publicada em 2010, igual em todos os cenários.

## Como reproduzir

```
uv run --no-project python experimentos/analise/nivel2.py
```

## Resultado

- **Onde estão os resultados:** `experimentos/analise/nivel2/cenarios.csv` e `rankings.csv`.

| Cenário | Métricas com mais de uma classe | Acerto por posição (Storage / Zeno / Elevator) | Correlação de postos |
|---|---|---|---|
| Referência | 17 de 17 | 50% / 30% / 40% | 0,81 / 0,86 / 0,61 |
| Texto, variância amostral | 10 de 17 | 50% / 20% / 70% | 0,81 / 0,79 / 0,84 |
| Texto, variância populacional | 9 de 17 | 40% / 20% / 40% | 0,81 / 0,79 / 0,65 |

Linha de base sem características (G20): acerto por posição 10% / 10% / 0%; correlação 0,75 / 0,68 / 0,65.

## Interpretação

- **Corrigida a aritmética (G18), a taxa de acerto de 2010 cai** no Elevator de 50% para 40% (a publicada vinha de um empate que não existe nos valores exatos) e no Zeno-travel de 40% para 30%. `[FATO]`
- **A regra do texto elimina a distinção em 7 ou 8 das 17 métricas** (todos os domínios na mesma classe), entre elas "Casos de Uso por Atores", que 2010 apontou como a característica de maior impacto. `[FATO]`
- O efeito sobre a validação é instável: melhora o Elevator (70%) só com a variância amostral, piora o Zeno-travel nos dois casos e não muda o Storage. `[HIPÓTESE]` Com três domínios de validação e dez planejadores, essas diferenças estão dentro do que o acaso explica; nenhum cenário se distingue claramente da referência, e todos seguem próximos da linha de base sem características quando se olha a correlação de postos.

## Problemas e desvios

- A regra do texto só é especificada para uma métrica; a generalização (v e 2v) é inferência do exemplo e está declarada acima.
