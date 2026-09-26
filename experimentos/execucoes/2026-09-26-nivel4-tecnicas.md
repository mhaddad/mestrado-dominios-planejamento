# Registro de experimento — EXP-13: Nível 4 por técnica (29 planejadores na taxonomia 4D)

| Campo | Valor |
|---|---|
| ID | EXP-13 |
| Data | 26/09/2026 |
| Fase | 3 |
| Pergunta | Q1: a pergunta de 2010, por técnica, com dados publicados (continuação do EXP-12) |
| Autor da execução | Claude Code (claude-opus-5-5), a pedido do autor |

## Configuração

- **Codificação:** os 29 planejadores do Planner Museum na taxonomia 4D, em `auditoria/taxonomia/planejadores_museu_4d.csv`, com a mesma estrutura do `planejadores_4d.csv` de 2010 e duas colunas a mais: `tipo_fonte` e `codificacao`.
- **Fontes:**
  - **22 planejadores com fonte primária lida:**
    - 15 por nota de leitura já existente, em 4 deles somada ao resumo da IPC, ao código ou à descrição secundária;
    - 7 só pelos resumos das IPCs de 2018 e 2023, baixados das páginas oficiais em 26/09/2026.
  - **7 planejadores só com fonte secundária:** a descrição de `lequen2026planner`, em 5 casos somada à documentação ou ao código do artefato. São eles MIPS, SimPlanner, MIPS-XXL, C3, FFSA, Probe e Mercury (**M1**).
  - Cada linha do CSV diz qual fonte sustenta a classificação.
- **Decisões de codificação (pendentes de revisão do autor):**
  - **P1, portfólios:** D4 = Portfólio; D1 a D3 recebem a união dos valores dos componentes descritos na fonte. É a leitura da taxonomia, §6. São portfólios: FDSS11, FDSS23, FDRemix, Saarplan, Maidu e Levitron.
  - **M2, componentes de portfólio não listados na fonte lida:** a D2 do FDSS11, do Maidu e do Levitron segue a composição usual dos portfólios do Fast Downward (relaxação, grafo causal, *landmarks*). Precisa de confirmação.
  - **Valores novos:**
    - **N1:** "Busca por largura/novidade" na D1, já previsto na taxonomia, §6;
    - **N2:** "Relaxação parcial (red-black)" na D2 (Mercury, Saarplan);
    - **N3:** "Heurística de SAT para planejamento" na D2 (Madagascar);
    - **N4:** "Contagem de metas" na D2 (BFWS, ANS);
    - **N5:** "Busca desacoplada (topologia em estrela)" na D1 (DecStar, Saarplan);
    - **N6:** "*Lifted* (sem aterramento)" na D3 (Levitron, pelo Powerlifted).
  - **Dimensões não determinadas pela fonte:** a D2 do MIPS e do MIPS-XXL e a D3 do SimPlanner e do MIPS-XXL ficam sem valor.
- **Análise:** `experimentos/analise/nivel4_publicados.py`, com o método de 2010 **por técnica** (a mesma regra do Nível 1, com tercis no lugar dos extremos), com as quatro dimensões juntas ou uma de cada vez. Rodado em dois recortes:
  - **todos** os 29 planejadores;
  - **sem portfólios** (23 planejadores).

  Os demais seletores (EXP-12) também foram rodados de novo em cada recorte. Saída descritiva nova: `mapa-tecnicas.csv`, a melhor cobertura que algum planejador de cada técnica alcança em cada domínio.

## Como reproduzir

```
uv run --no-project --with scikit-learn --with scipy python experimentos/analise/nivel4_publicados.py
```

## Resultado

**Onde estão os resultados:** `experimentos/analise/nivel4-publicados/` (`resumo.csv`, `escolhas.csv`, `mapa-tecnicas.csv`).

**Linhas de base por recorte** (41 domínios):

| Recorte | Planejadores | SBS | Cobertura do SBS | Cobertura do VBS | Lacuna |
|---|---|---|---|---|---|
| Todos | 29 | Levitron | 953 | 1.096 | 143 |
| Sem portfólios | 23 | Mercury | 819 | 1.050 | 231 |

**Perda total** (instâncias perdidas em relação ao VBS; entre parênteses, o p do Wilcoxon contra o SBS):

| Seletor | Todos (pddl / sas / pddl+sas) | Sem portfólios (pddl / sas / pddl+sas) |
|---|---|---|
| SBS | 143 | 231 |
| Método de 2010, planejador como técnica | 160 / 143 / 143 | **228** (0,24) / 251 / 241 |
| Método de 2010, 4D (todas as dimensões) | 170 / 170 / 170 | 341 / 308 / 338 |
| Método de 2010, só D1 | 387 (p < 0,001) nos três | 327 / 318 / 348 |
| Método de 2010, só D2 | 277 (p = 0,002) nos três | 231 nos três (= SBS) |
| Método de 2010, só D3 | 143 nos três (= SBS) | 671 (p < 0,001) nos três |
| *Random forest* | 151 / 189 / 148 | 243 / 256 / 254 |
| kNN | 228 / 231 / 220 | 356 / 303 / 347 |

**Mapa das técnicas** (em quantos dos 41 domínios algum planejador da técnica empata com o melhor geral):
- **D1:** busca progressiva no espaço de estados, 37; busca desacoplada, 21; busca por largura/novidade, 18; decomposição recursiva por metas (System R), 8; compilação para SAT, 5; grafo de planejamento, busca local, planos parciais e busca simbólica, 0.
- **Onde a busca progressiva não empata com o melhor:**
  - Blocks World e TPP: vence o System R (30 de 30 nos dois);
  - Floortile: vence o Madagascar, SAT (15);
  - Pipesworld sem tanques: vence o ANS, busca por largura (30).

## Interpretação

- **Agrupar os planejadores por técnica piora a escolha.** `[FATO]`
  - Com todos os planejadores, o método de 2010 por técnica perde de 170 a 387 instâncias, contra 143 do SBS.
  - A versão só com a D1 é a pior: perde mais que o dobro.
  - Sem portfólios, só a versão com o planejador no lugar da técnica fica, por pouco, abaixo do SBS (228 contra 231). A diferença não é significativa (p = 0,24).
- **Por quê** `[HIPÓTESE]`: um mesmo valor de técnica reúne planejadores de gerações muito diferentes. "Busca progressiva com relaxação" vai do HSP (1998) ao Levitron (2023). A média da técnica mistura desempenhos que diferem mais pela engenharia do que pela família de técnica. A técnica, nas categorias da taxonomia, não determina o desempenho: a implementação e a época pesam mais.
- **O fenômeno de 2010 aparece no mapa, não no seletor.** `[FATO]` Há domínios em que uma técnica "antiga" é a melhor: a decomposição recursiva por metas do System R no Blocks World e no TPP, com cobertura total, e o SAT no Floortile. `[HIPÓTESE]` Esses casos indicam que existe, sim, ajuste entre técnica e domínio, mas em poucos domínios e sem que as características extraídas do PDDL o antecipem.
- **Para a Q1:** com a taxonomia sustentada por fontes primárias, 29 planejadores e 41 domínios, o método de 2010 não ganha da escolha fixa do melhor planejador. É a mesma conclusão do Nível 2 (EXP-09), agora numa amostra quatro vezes maior em domínios e três vezes maior em planejadores.

## Limites

- 7 dos 29 planejadores foram classificados só com fonte secundária (M1). Há decisões de codificação pendentes (P1, M2, N1–N6).
- Os mesmos limites do EXP-12: só cobertura, só por domínio, *features* SAS+ de uma amostra de 10 instâncias.
- O recorte "sem portfólios" depende da classificação P1.
