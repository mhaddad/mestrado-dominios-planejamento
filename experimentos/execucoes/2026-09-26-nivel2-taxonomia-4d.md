# Registro de experimento — EXP-06: Nível 2, R-10 (taxonomia em 4 dimensões)

| Campo | Valor |
|---|---|
| ID | EXP-06 (o EXP-05 fica reservado para a rodada do Nível 3 no GCP, iniciada antes) |
| Data | 26/09/2026 |
| Fase | 3 |
| Pergunta | Q1 (item R-10 de `auditoria/reexecucao.md`; A6, F4; AF-213, AF-214, AF-285, AF-286, AF-326, AF-328) |
| Autor da execução | Claude Code (claude-opus-5-5), a pedido do autor |

## Configuração

- **Código:** `experimentos/analise/nivel2.py`, que reaproveita o método de 2010 de `reproducao_2010.py`.
- **Atribuição de técnicas:** `auditoria/taxonomia/planejadores_4d.csv`, uma linha por planejador × dimensão × valor. Foi codificada a partir de `auditoria/taxonomia-tecnicas.md` (§3 e decisões de 23/09/2026, validadas no M1). Cinco pontos exigiram uma decisão de codificação, marcada na coluna `codificacao`. **O autor revisou e aprovou as cinco sem alteração (26/09/2026):**
  - **C1:** o LPG tem dois valores na D1 (busca local e espaço de planos parciais).
  - **C2:** o LPG recebeu um valor próprio na D2 ("Avaliação heurística da vizinhança"), porque nenhum valor da D2 o cobre segundo a fonte lida.
  - **C3:** o SGPlan tem dois valores na D1 (decomposição e busca progressiva do Metric-FF interno).
  - **C4:** o SGPlan foi codificado na D3 pela representação do Metric-FF.
  - **C5:** o MaxPlan tem só "Compilação para SAT/CSP" na D1.
- **Cenários novos:**
  - `4d-todas`: as quatro dimensões juntas, 18 valores tratados como técnicas.
  - `4d-D1`, `4d-D2`, `4d-D3`: uma dimensão por vez. A D4 não entra sozinha: 9 dos 10 planejadores são "Planejador único".
  - `tabela4-sem-G24`: os 11 rótulos de 2010 com uma só atribuição, para isolar o efeito do G24.
- **Mantido igual à referência do EXP-04:** classes publicadas, aritmética corrigida (G18), notas previstas comparadas com duas casas e empates desempatados pela ordem publicada em 2010.
- **O que muda nos cenários 4D:** a mesma atribuição é usada na relação e na nota de cada planejador, o que corrige o G24.

## Como reproduzir

```
uv run --no-project python experimentos/analise/nivel2.py
```

## Resultado

**Onde estão os resultados:** `experimentos/analise/nivel2/`:
- `cenarios.csv` e `rankings.csv`;
- `taxonomia-4d-relacao.csv`, o equivalente às Tabelas 19–20;
- `taxonomia-4d-relevancia.csv`, o equivalente às Tabelas 21–23.

| Cenário | Técnicas | Acerto por posição (Storage / Zeno / Elevator) | Correlação de postos |
|---|---|---|---|
| Referência (11 rótulos de 2010, aritmética corrigida) | 11 | 50% / 30% / 40% | 0,81 / 0,86 / 0,61 |
| 11 rótulos, sem G24 | 11 | 50% / 30% / 40% | 0,81 / 0,86 / 0,61 |
| 4D, todas as dimensões | 18 | 10% / 0% / 20% | 0,78 / 0,72 / 0,74 |
| 4D, só D1 (algoritmo/espaço de busca) | 7 | 40% / 30% / 10% | 0,88 / 0,87 / 0,65 |
| 4D, só D2 (heurística) | 4 | 40% / 30% / 20% | 0,76 / 0,74 / 0,67 |
| 4D, só D3 (representação) | 5 | 30% / 20% / 10% | 0,58 / 0,51 / 0,78 |
| Linha de base sem características (G20) | — | 10% / 10% / 0% | 0,75 / 0,68 / 0,65 |

**Relevância das 49 características**, pela regra de 2010: diferença entre o maior e o menor valor nas técnicas.
- A classe se mantém em 36 das 49 características.
- 9 sobem de classe, 8 delas de "pouco" para "muito relevante".
- 4 descem, 3 delas de "muito" para "pouco relevante".
- No total, 26 ficam "muito relevantes" com a taxonomia 4D, contra 20 em 2010.

## Interpretação

- **O G24 não muda nada.** Usar a mesma atribuição de técnicas nos dois passos dá resultados idênticos à referência. `[FATO]`
- **Com a taxonomia corrigida, o método de 2010 não melhora.**
  - O acerto por posição cai com as quatro dimensões juntas.
  - A correlação de postos sobe no Elevator e cai no Storage e no Zeno-travel.
  - Nenhum cenário 4D se distingue da linha de base sem características de forma consistente nos três domínios.
  - Só a D1 fica acima da referência em dois dos três domínios na correlação. `[FATO]`
- **Dez dos 18 valores têm um só planejador.** São eles: busca local, planos parciais, decomposição recursiva, decomposição/particionamento, grafo causal, avaliação da vizinhança, grafos de ação, STRIPS/ADL estendido, variáveis multivaloradas e componente plugável. Nesses casos a "técnica" é o próprio planejador, e o método passa a prever o desempenho de cada planejador pelas suas notas de treino. `[FATO]`
  - Isso explica o aumento de características "muito relevantes": a diferença entre o maior e o menor valor cresce quando há técnicas de um único planejador, que chegam a 0 ou a 10. `[HIPÓTESE]`
  - Por isso o aumento não deve ser lido como mais poder explicativo das características.
- **Consequência para as afirmações AF-213, AF-214, AF-285, AF-286, AF-326 e AF-328:** o cruzamento característica × técnica de 2010 depende da taxonomia. Com a taxonomia sustentada pelas fontes primárias, o ranking dos planejadores muda (LPG e SGPlan sobem; R deixa o último lugar). A validação continua sem ganho claro sobre a linha de base. `[HIPÓTESE]` Com 10 planejadores e 3 domínios de validação, a amostra não permite separar o efeito da taxonomia do acaso. Essa pergunta passa para o Nível 4.

## Problemas e desvios

- As decisões de codificação C1 a C5 alteram os resultados dos cenários 4D; aprovadas pelo autor em 26/09/2026.
- O desempate pela ordem publicada em 2010 favorece a referência nas posições empatadas. Isso afeta o acerto por posição, não a correlação de postos. Mesmo critério do EXP-04, mantido para a comparação.
