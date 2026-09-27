# Registro de experimento — EXP-22: tempo e memória do Nível 3 (F5)

| Campo | Valor |
|---|---|
| ID | EXP-22 |
| Data | 27/09/2026 |
| Fase | 3 |
| Pergunta | F5 (eficiência reduzida a cobertura em 2010): o tempo muda a leitura do desempenho? Quanto das falhas é memória? |
| Autor da execução | Claude Code (claude-opus-5-5), por decisão do autor na avaliação das Fases 1 a 4 |

## Configuração

- **Dados:** as 3.390 execuções do Nível 3 (EXP-05), `experimentos/execucoes/nivel3-2010-gcp.csv`, sem nova execução. Mesma entrada do EXP-19 e do EXP-20.
- **Método, fixado antes de ver os resultados:**
  - **Escore de tempo** no formato do escore de qualidade do EXP-20: em cada problema, T\* ÷ T, com T\* o menor tempo de relógio entre os planejadores que resolveram; 0 se não resolveu. Somado por domínio e dividido pelo número de problemas (0 a 1). LPG-TD: média das 3 sementes.
  - **Piso de 1 s** nos tempos: 1.787 de 2.263 planos saem em menos de 1 s, e abaixo disso a diferença é de inicialização do processo.
  - **Comparação com a cobertura:** correlação de postos (Spearman) entre o escore de cobertura (fração resolvida) e o de tempo dos planejadores, em cada domínio.
  - **Memória:** memória máxima por execução; 3,5 GB ou mais conta como perto do teto dos binários de 32 bits (cerca de 4 GB).
- Os limites de tempo diferem por planejador (calibrados, de 7 a 13 min, EXP-05); o escore de tempo só compara execuções resolvidas.

## Como reproduzir

```
python3 experimentos/analise/nivel3_tempo_memoria.py
```

## Resultado

**Onde estão os resultados:** `experimentos/analise/nivel3/tempo.csv` (por planejador e domínio), `tempo-ranking.csv` (por domínio) e `memoria.csv` (por planejador).

`[FATO]` Média nos 10 domínios de treino (R em 9, sem o Pathways):

| Planejador | Escore de cobertura | Escore de tempo |
|---|---|---|
| YAHSP | 0,890 | 0,847 |
| LPG-TD | 0,869 | 0,772 |
| SGPlan | 0,848 | 0,791 |
| Fast Downward | 0,836 | 0,720 |
| FF | 0,736 | 0,682 |
| SATPlan | 0,653 | 0,466 |
| R | 0,567 | 0,533 |
| MAXPLAN | 0,478 | 0,285 |
| IPP | 0,444 | 0,359 |
| Blackbox | 0,270 | 0,212 |

`[FATO]` Correlação de postos entre cobertura e tempo, por domínio: de 0,78 a 1,00 em 9 dos 10 domínios; 0,57 no Mystery. A coluna de líderes de `tempo-ranking.csv` desfaz empates pela ordem alfabética e serve só de indicação.

`[FATO]` Memória: as 734 execuções que estouraram o limite não têm memória registrada (foram encerradas pelo executor). Entre as demais, 36 chegaram perto do teto de 32 bits e terminaram sem plano: 29 do IPP e 7 do MAXPLAN, em Pipesworld (13), Gripper (10), Blocks World (5), Pathways (5) e TPP (3). São 36 dos 393 "sem plano" do Nível 3. A mediana de memória dos planos resolvidos vai de 3 MB (YAHSP) a 110 MB (LPG-TD).

## Interpretação

- **Medir o tempo não muda a leitura de 2010.** `[FATO]` Tempo e cobertura ordenam os planejadores quase da mesma forma; nas médias, só três pares vizinhos trocam de posição (LPG-TD e SGPlan, SATPlan e R, MAXPLAN e IPP). A omissão do tempo em 2010 (F5) não distorce os *rankings*.
- **A qualidade do plano é o que 2010 perdeu.** `[FATO]` O escore de qualidade do EXP-20 muda mais a ordem que o tempo: o SGPlan passa ao 1.º lugar, o FF sobe do 5.º ao 3.º, o IPP do 9.º ao 7.º, e o R cai do 7.º ao 9.º (IPP e Blackbox fazem os planos mais curtos e resolvem pouco; o R resolve muito com planos longos).
- **Parte das falhas do IPP e do MAXPLAN é memória, não busca.** `[FATO]` para a contagem; `[HIPÓTESE]` para a causa: os binários de 2010 são de 32 bits, e um binário atual, com mais memória, poderia resolver parte desses problemas.

## Limites

- O piso de 1 s nivela a maior parte dos problemas; o escore de tempo discrimina só entre problemas que levam mais de 1 s.
- Limites de tempo diferentes por planejador (calibrados): um planejador com limite maior pode resolver problemas mais longos. O escore de tempo penaliza esses planos longos, mas a cobertura não.
- Tempo de relógio numa VM com 4 execuções em paralelo; comparável entre planejadores da mesma rodada, não com os tempos de 2010.
