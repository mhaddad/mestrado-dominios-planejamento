# Registro de experimento — EXP-20: qualidade dos planos do Nível 3 (R-22)

| Campo | Valor |
|---|---|
| ID | EXP-20 |
| Data | 27/09/2026 |
| Fase | 3 |
| Pergunta | Q1 e F5 (eficiência reduzida a cobertura em 2010; R-22 de `auditoria/reexecucao.md`) |
| Autor da execução | Claude Code (claude-opus-5-5), a pedido do autor |

## Configuração

- **Código:** `experimentos/analise/nivel3_qualidade.py`.
- **Dados:** as 2.263 execuções resolvidas do Nível 3 (EXP-05) e os logs brutos (fora do git, `experimentos/execucoes/brutos/gcp*/`). Planos considerados corretos, sem VAL (decisão do autor, 27/09/2026).
- **Medida:** número de ações do plano, lido no formato de cada planejador (LPG-TD pelo resumo `Actions:`, que bate com a contagem de linhas nos 765 casos em que o plano aparece no log; SATPlan e MAXPLAN pelo `.soln`; R pelo terceiro campo da linha de resultado).
- **Escore de qualidade (estilo IPC):** por problema, menor plano entre todos os planejadores ÷ plano do planejador; 0 se não resolveu. Somado por domínio e dividido pelo número de problemas (0 a 1). LPG-TD: média das 3 sementes. Também a qualidade média só dos problemas resolvidos.

## Como reproduzir

```
python3 experimentos/analise/nivel3_qualidade.py
```

## Resultado

- **Onde estão os resultados:** `experimentos/analise/nivel3/planos.csv` (tamanho por execução) e `qualidade.csv` (por planejador e domínio).

`[FATO]` 2.263 de 2.263 planos lidos. Média nos 10 domínios de treino:

| Planejador | Escore de qualidade (cobertura e tamanho) | Qualidade média dos resolvidos |
|---|---|---|
| SGPlan | 0,715 | 0,850 |
| YAHSP | 0,710 | 0,796 |
| FF | 0,692 | 0,931 |
| LPG-TD | 0,672 | 0,760 |
| Fast Downward | 0,655 | 0,808 |
| SATPlan | 0,573 | 0,896 |
| IPP | 0,422 | 0,954 |
| MAXPLAN | 0,402 | 0,875 |
| R | 0,396 | 0,607 |
| Blackbox | 0,260 | 0,950 |

## Interpretação

- `[FATO]` Cobertura e qualidade não andam juntas. IPP e Blackbox fazem os planos mais curtos quando resolvem (0,95), mas resolvem pouco. O R resolve 133 de 255 problemas, mas com os planos mais longos (0,61): no DriverLog pfile1, 100 ações, contra 7 a 8 de outros planejadores.
- `[FATO]` SATPlan e MAXPLAN incluem ações sem efeito útil (ex.: carregar e descarregar o mesmo pacote no mesmo lugar); no DriverLog pfile1, 18 e 14 ações contra 7 a 8.
- A nota de 2010, só por cobertura, favorece planejadores que resolvem muito com planos longos (R, LPG-TD) e desfavorece os que resolvem pouco com planos curtos (IPP, Blackbox).

## Problemas e desvios

- O número de ações é o custo do plano nos domínios de treino, todos sem custo de ação; é a medida de qualidade da IPC clássica nesses domínios.
- O "menor plano" é o menor entre os 10 planejadores de 2010, não o ótimo.
- **Zeno-travel não medido:** os domínios de validação não foram reexecutados (decisão do autor, 27/09/2026). A afirmação de 2010 sobre a dificuldade de "plano de boa qualidade" no Zeno-travel (AF-303) continua sem medida.
