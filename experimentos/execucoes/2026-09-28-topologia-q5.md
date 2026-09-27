# Registro de experimento — EXP-25: propriedades de topologia de busca na Q5 e no R-29 por instância

| Campo | Valor |
|---|---|
| ID | EXP-25 |
| Data | 27–28/09/2026 |
| Fase | 4B |
| Pergunta | As propriedades com fundamento teórico (Hoffmann, 2011) acrescentam, às 16 *features* SAS+, poder de explicar qual família de técnica resolve a instância (Q5, como no EXP-21) e de escolher o planejador por instância (Q1/R-29, como no EXP-24)? |
| Autor da execução | Claude Code (claude-opus-5-5), por delegação do autor |

## Configuração

- **Extrator:** `experimentos/extratores/topologia_sas.py`, validado antes do uso contra a Tabela 3 de `hoffmann2011analyzing` (`experimentos/extratores/topologia-validacao/README.md`). Resultado da validação:
  - critério básico só no Logistics;
  - Spearman 0,966 na sondagem (SP) e 0,987 nos becos sem saída (DE), em 30 domínios;
  - os três critérios foram fixados antes de rodar.
- **Propriedades por tarefa** (`data/ipc-2011-2023/topologia_ipc.csv`, 1.793 de 1.824 tarefas completas; `scripts/topologia_ipc.py`):
  - estruturais: resultado básico de Hoffmann e fração de transições inversíveis;
  - hFF no estado inicial;
  - por amostragem de 10 estados: taxa de becos sem saída, taxa de sucesso da sondagem e profundidade média da saída.
  - Todas são calculadas antes de resolver a tarefa, sem usar nenhum resultado da competição.
- **Rodada descartada.** A primeira rodada incluiu uma sétima medida, hFF(s₀) com custos dividido pelo melhor custo conhecido da instância. Foi descartada antes de qualquer registro de resultado: o melhor custo vem dos planos dos competidores (vazamento), e um seletor não o teria na hora de escolher.
- **Análise:** `experimentos/analise/topologia_q5.py`.
  - Mesmas unidades, famílias e recortes do EXP-21 e do EXP-24.
  - Quatro conjuntos de *features*, sempre nas mesmas instâncias: tamanho, SAS+ (16), topologia (6) e SAS+ com topologia.
  - Parte A (Q5): AUC da logística, deixando um domínio de fora. Dois testes de permutação: o do acréscimo embaralha só as linhas do bloco de topologia; o da topologia sozinha embaralha o rótulo. Os dois com 199 permutações, 1.999 se p < 0,05, e Holm por recorte.
  - Parte B (Q1): seletores do EXP-24 com cada conjunto; Wilcoxon por domínio contra o SBS e Holm por unidade.

## Como reproduzir

```
uv run --no-project --with numpy --with networkx --with scipy python experimentos/extratores/validar_topologia.py
uv run --no-project --with numpy --with networkx python data/ipc-2011-2023/scripts/topologia_ipc.py --edicoes 2011,2014,2018
uv run --no-project --with scikit-learn --with scipy --with numpy python experimentos/analise/topologia_q5.py
```

Saídas em `experimentos/analise/topologia-q5/`: `modelos.csv` (Parte A) e `seletores.csv` (Parte B).

## Resultado

**Parte A (Q5).** AUC mediana fora da amostra, deixando um domínio de fora:

| Recorte | Modelos | Só tamanho | SAS+ | Topologia | SAS+ e topologia | Acréscimo significativo (Holm) | Topologia sozinha significativa (Holm) | SAS+ e topologia abaixo de SAS+ |
|---|---|---|---|---|---|---|---|---|
| Todos | 39 | 0,56 | 0,58 | 0,52 | 0,61 | 14 | 4 | 20 |
| Sem portfólios | 34 | 0,51 | 0,56 | 0,52 | 0,62 | 15 | 4 | 15 |

**Famílias com vários planejadores em que o acréscimo passa no Holm** (recorte todos; AUC com SAS+ → com SAS+ e topologia):

| Edição e trilha | Família | Planejadores | SAS+ | SAS+ e topologia |
|---|---|---|---|---|
| 2011 ótima | Busca progressiva | 10 | 0,63 | 0,75 |
| 2011 ótima | *Landmarks* | 7 | 0,68 | 0,80 |
| 2011 *satisficing* | Compilação para SAT/CSP | 4 | 0,44 | 0,67 |
| 2018 *satisficing* | Busca por largura/novidade | 12 | 0,52 | 0,62 |
| 2018 *satisficing* | Contagem de metas | 6 | 0,59 | 0,70 |

- O acréscimo também passa em famílias de um ou dois planejadores: CPT4, FD-Autotune, Madagascar e outras. A lista completa está em `modelos.csv`.
- Sem portfólios, entra ainda a busca simbólica na ótima de 2018 (3 planejadores): 0,63 → 0,70.

**Decomposição exploratória, feita depois da análise principal.** Nas famílias do quadro acima, qual parte da topologia traz o ganho?

| Edição e trilha | Família | SAS+ | SAS+ e só hFF(s₀) | SAS+ e só amostragem (DE, SP, profundidade) | SAS+ e topologia |
|---|---|---|---|---|---|
| 2011 ótima | Busca progressiva | 0,63 | 0,78 | 0,65 | 0,75 |
| 2011 ótima | *Landmarks* | 0,68 | 0,82 | 0,72 | 0,80 |
| 2011 *satisficing* | Compilação para SAT/CSP | 0,44 | 0,71 | 0,43 | 0,67 |
| 2018 *satisficing* | Busca por largura/novidade | 0,52 | 0,54 | 0,60 | 0,62 |
| 2018 *satisficing* | Contagem de metas | 0,59 | 0,59 | 0,70 | 0,70 |

**Parte B (Q1).** Nenhum seletor ganha do SBS com significância (Holm por unidade) em nenhuma unidade, com nenhum conjunto de *features*. O caso mais próximo é a ótima de 2018 sem portfólios: kNN com SAS+ e topologia perde 33 instâncias, contra 63 do SBS, sem significância.

## Interpretação

- **A topologia acrescenta às SAS+, mas pouco e de forma desigual.** `[FATO]`
  - A AUC mediana sobe cerca de 0,03 a 0,06.
  - O acréscimo passa no teste de permutação com Holm em cerca de um terço das famílias, inclusive famílias amplas: busca progressiva e *landmarks* na ótima de 2011, largura/novidade e contagem de metas na *satisficing* de 2018.
  - Em metade dos modelos do recorte todos, somar a topologia **piora** a previsão fora do domínio.
  - Sozinha, a topologia fica abaixo das SAS+ (mediana 0,52).
- **Duas fontes diferentes de ganho** `[FATO, exploratório]`:
  - **Na ótima de 2011, o ganho vem do hFF(s₀),** o comprimento do plano relaxado: uma medida de profundidade e dificuldade da tarefa, mais do que de topologia. Os planejadores de busca heurística ótima falham nas tarefas com hFF(s₀) alto.
  - **Na *satisficing* de 2018, o ganho vem das medidas de amostragem** (becos sem saída, sucesso da sondagem, profundidade da saída), isto é, da topologia sob hFF. É nas famílias de largura/novidade e contagem de metas que ela ajuda.
- **Na Q1, nada muda:** nenhum seletor supera o SBS, com ou sem topologia.
- `[HIPÓTESE]` **Para a Q5:** as propriedades de topologia recuperam parte do que as *features* sintáticas não captam, e a busca por largura/novidade é a família em que isso aparece mais claramente. Mesmo assim, as AUCs ficam entre 0,6 e 0,8: a topologia ajuda a explicar, mas não a ponto de antecipar com segurança qual técnica funciona.

## Limites

- Dez estados por tarefa. O artigo de referência mostra taxas parecidas com 10 e com 1.000 amostras, mas por instância a medida é ruidosa.
- A sondagem usa hFF. Ela mede a topologia para a heurística do FF e está mais próxima das famílias de busca heurística do que das outras.
- A decomposição hFF × amostragem foi feita depois de ver o resultado. É exploratória, sem correção para comparações múltiplas.
- 31 tarefas sem topologia completa ficaram fora: 5 com tradução acima de 300 s e 26 com as medidas acima de 120 s. São no máximo 7 instâncias por unidade.
