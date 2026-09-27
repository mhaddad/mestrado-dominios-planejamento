# Registro de experimento — EXP-11: *features* modernas da representação SAS+ (R-26)

| Campo | Valor |
|---|---|
| ID | EXP-11 |
| Data | 26/09/2026 |
| Fase | 3 |
| Pergunta | Q2, conjunto de *features* (b) (item R-26 de `auditoria/reexecucao.md`; A5) |
| Autor da execução | Claude Code (claude-opus-5-5), a pedido do autor |

## Configuração

- **Código:**
  - `experimentos/extratores/features_sas.py` faz a extração;
  - `experimentos/analise/uml_x_sas.py` compara com as métricas UML de 2010.
- **Tradutor:** Fast Downward release-26.6.0 (commit `7ea275526`), só o tradutor PDDL → SAS+, fora do git (ver `experimentos/extratores/README.md`). Networkx 3.7 para os grafos.
- **Instâncias:** as 354 usadas em 2010 nos 13 domínios (faixa `instancias_usadas` de `data/2010/benchmarks_ipc_mapa_final.csv`). Limite de 300 s por tradução, 8 processos.
- **Features:** 17 por instância, fixadas antes de rodar a partir das estruturas que a literatura liga à complexidade (síntese E2: `helmert2009concise`, `hoffmann2011analyzing`, `domshlak2013complexity`). Por domínio, usa-se a mediana das instâncias.
  - **Tamanho:** variáveis, tamanho do domínio das variáveis, operadores, metas, axiomas.
  - **Grafo causal:** arestas, densidade, grau máximo, aciclicidade, componentes fortemente conexas, fração de variáveis na maior componente e limite superior do *treewidth* (heurística de grau mínimo).
  - **DTG:** arcos por variável, fração de variáveis com DTG fortemente conexo e fração de arcos invertíveis. As duas últimas aproximam a reversibilidade.
- **Ajuste no Pathways:** os 30 problemas redeclaram em `:objects` uma constante que o domínio já declara (`pcaf-p300`), e o tradutor recusa a duplicata. O problema é copiado sem esse nome, o que não muda a tarefa. A coluna `ajuste` de `instancias.csv` registra os 30 casos.
- **Comparação com 2010:** correlação de postos de Spearman entre cada métrica UML (valores publicados com as correções aprovadas) e cada *feature* SAS+, nos 13 domínios. O teste de permutação embaralha os valores de cada métrica entre os domínios (2.000 permutações, semente 2010) e mede com que frequência o acaso dá uma correlação máxima tão alta quanto a observada.

## Como reproduzir

```
uv run --no-project --with networkx python experimentos/extratores/features_sas.py --limite 300 --processos 8
uv run --no-project python experimentos/analise/uml_x_sas.py
```

## Resultado

**Onde estão os resultados:**
- `experimentos/extratores/features-sas/instancias.csv` e `dominios.csv`;
- `experimentos/analise/uml-x-sas/correlacoes.csv` e `resumo.csv`.

**Extração:** 354 de 354 instâncias traduzidas, sem esgotar o tempo. A execução completa levou cerca de 1 minuto.

**Estrutura dos 13 domínios** (medianas):
- **Grafo causal acíclico:** só o Logistics.
- **Uma única componente fortemente conexa com todas as variáveis:** Blocks World, Pipesworld e Storage.
- **DTG fortemente conexo em todas as variáveis:** Blocks World, Depots, DriverLog, Gripper, Logistics, Pipesworld, Storage e Zeno-travel.
- **Menos reversíveis pelos DTGs:** Pathways (47% das variáveis com DTG fortemente conexo; 61% dos arcos invertíveis), Mystery (55%) e Elevator (59%).
- **Maior limite de *treewidth*:** Depots (34,5) e Pipesworld (33).

**Métricas UML × *features* SAS+:**

| Métrica UML (2010) | *Feature* SAS+ mais correlacionada | Spearman | P95 do acaso | p (permutação) |
|---|---|---|---|---|
| Número de Atores | grau máximo do grafo causal | −0,63 | 0,76 | 0,21 |
| Casos de Uso por Atores | tamanho médio do domínio das variáveis | 0,63 | 0,75 | 0,23 |
| Ações de saída | densidade do grafo causal | 0,61 | 0,74 | 0,27 |
| Agregação | tamanho médio do domínio das variáveis | 0,56 | 0,75 | 0,38 |
| … (13 métricas restantes) | | 0,35 a 0,53 | 0,74 a 0,76 | 0,48 a 0,95 |

A tabela completa está em `experimentos/analise/uml-x-sas/resumo.csv`.

## Interpretação

- **Nenhuma métrica UML de 2010 se relaciona com as estruturas SAS+ acima do que o acaso daria.** A maior correlação de cada uma fica abaixo do percentil 95 do acaso (p entre 0,21 e 0,95). `[FATO]`
- **Isso inclui as métricas do diagrama de estados.** Estados, ações de entrada e de saída, e transições pareciam candidatas a aproximar os DTGs, e não se relacionam com eles. `[FATO]`
- **Leitura cautelosa:** com 13 domínios, o teste tem pouco poder. A ausência de correlação não prova que as métricas UML sejam independentes da estrutura das tarefas. `[HIPÓTESE]` O resultado é coerente com a crítica de Hoffmann (2011) às *features* sintáticas e com os EXP-07 e EXP-10: as métricas UML medem o modelo e a amostra, não a estrutura que a literatura liga à dificuldade.
- **Para a Q2:** não há evidência, nesta amostra, de que as métricas UML e as *features* SAS+ meçam a mesma coisa (com 13 domínios, isso não prova que meçam coisas diferentes). O R-27 terá de medir o que cada conjunto acrescenta ao prever desempenho, com os dados do Nível 4.

## Problemas e desvios

- Os problemas do Pathways foram ajustados para o tradutor (constante duplicada), sem mudar a tarefa.
- A primeira execução terminou com erro no resumo por domínio (índice de coluna deslocado pela coluna `ajuste`). As traduções estavam corretas; o erro foi corrigido e tudo rodou de novo.
