# Registro de experimento — EXP-24: R-29 por instância (escolha de planejador com dados das IPCs 2011 e 2018)

| Campo | Valor |
|---|---|
| ID | EXP-24 |
| Data | 27/09/2026 |
| Fase | 4B (R-29 por instância, transferido da Fase 3 por decisão do autor) |
| Pergunta | Q1, por instância: escolher o planejador pelas características da tarefa ganha da escolha fixa do melhor planejador (SBS)? |
| Autor da execução | Claude Code (claude-opus-5-5), por delegação do autor |

## Configuração

- **Continuação** do R-28 e do R-29 por domínio (EXP-12 e EXP-13, Planner Museum). Os seletores são os mesmos de `experimentos/analise/nivel4_publicados.py`, adaptados à instância.
- **Dados:** os mesmos do EXP-21 (`data/ipc-2011-2023/`):
  - 2018: ótima, *satisficing* e *agile*, com os 10 domínios do placar e as formulações normal e *split* de caldera e organic-synthesis;
  - 2011: ótima e *satisficing*.
  - Entram as instâncias com *features* SAS+ que algum planejador do recorte resolve.
- **Tarefa:** escolher um planejador por instância. Perda = 1 quando o escolhido não resolve. A validação deixa um domínio de fora por vez: o seletor é treinado nas instâncias dos outros domínios.
- **Seletores, fixados antes de rodar:**
  - referências: VBS, escolha ao acaso e SBS (maior cobertura no treino);
  - método de 2010 com o planejador como técnica (tercis do treino);
  - método de 2010 por técnica (EXP-13), com a taxonomia 4D de `planejadores_4d.csv`: todas as dimensões, só a D1 e só a D2;
  - kNN (5 vizinhos) e *random forest* multi-saída (300 árvores, semente 2010).
- **Features:** as 16 SAS+ (log1p nas contagens). As 11 métricas de 2010 não entram: saem do arquivo de domínio e são constantes dentro de cada domínio.
- **Teste:** Wilcoxon pareado da perda por domínio contra o SBS e correção de Holm entre os seletores de cada edição × trilha × recorte (função de `correcao_multipla.py`).
- **Recortes:** todos os planejadores; sem portfólios (regra D1 de `docs/fase4b-desenho.md`).

## Como reproduzir

```
uv run --no-project --with scikit-learn --with scipy --with numpy python experimentos/analise/r29_instancias.py
```

Saídas em `experimentos/analise/r29-instancias/`: `resumo.csv` (perda total, fração da lacuna do SBS fechada, p do Wilcoxon e p de Holm) e `perdas_por_dominio.csv`.

## Resultado

**Perda total** (instâncias que o seletor perde e o VBS resolve). O asterisco marca p de Holm < 0,05 contra o SBS.

| Edição e trilha | Recorte | Instâncias | SBS | Método 2010 (planejador) | 4D todas | 4D só D1 | 4D só D2 | kNN | *Random forest* | Acaso |
|---|---|---|---|---|---|---|---|---|---|---|
| 2011 ótima | todos | 203 | 18 | 18 | 34 | 68* | 55* | 45 | 23 | 50 |
| 2011 ótima | sem portfólios | 202 | 40 | 41 | 52 | 74 | 36 | 49 | 40 | 58 |
| 2011 *satisficing* | todos | 267 | 17 | 17 | 35 | 77 | 117* | 82 | 50 | 124 |
| 2011 *satisficing* | sem portfólios | 267 | 17 | 17 | 57 | 77 | 117* | 82 | 35 | 132 |
| 2018 ótima | todos | 174 | 36 | 50 | 46 | 70 | 49 | 43 | 62 | 66 |
| 2018 ótima | sem portfólios | 174 | 64 | 57 | 43 | 61 | 41 | 43 | 64 | 69 |
| 2018 *satisficing* | todos | 188 | 52 | 49 | 35 | 44 | 63 | 53 | 51 | 94 |
| 2018 *satisficing* | sem portfólios | 187 | 44 | 48 | 43 | 43 | 59 | 50 | 62 | 102 |
| 2018 *agile* | todos | 170 | 40 | 42 | 40 | 57 | 79* | 54 | 62 | 101 |
| 2018 *agile* | sem portfólios | 166 | 91 | 82 | **53*** | **53*** | 57 | 51 | 65 | 99 |

- Nas células com asterisco, o seletor é **pior** que o SBS, exceto nas duas em negrito (2018 *agile* sem portfólios), onde é **melhor**.
- **SBS geral de cada unidade**, calculado em todas as instâncias; dentro da validação, o SBS de cada dobra pode ser outro (em `perdas_por_dominio.csv`, coluna `sbs_escolhido`):
  - 2011: FDSS-1 (ótima) e LAMA-2011 (*satisficing*); sem portfólios, Selective Max na ótima;
  - 2018: Delfi1 (ótima) e Saarplan (*satisficing* e *agile*); sem portfólios, Complementary1 (ótima), LAPKT-DUAL-BFWS (*satisficing*) e a linha de base LAMA 2011 (*agile*).

## Interpretação

- **Com todos os planejadores, nenhum seletor ganha do SBS em nenhuma unidade.** `[FATO]`
  - O método de 2010 com o planejador no lugar da técnica empata com o SBS em 2011, onde escolhe o mesmo planejador, e perde em 2018.
  - As versões por técnica só com D1 ou só com D2 são significativamente piores em 4 casos.
  - O melhor caso sem significância é o 4D completo na *satisficing* de 2018: 35 contra 52, fechando 33% da lacuna, com p de Holm 0,375.
  - É a mesma conclusão do EXP-12 e do EXP-13 por domínio, agora por instância e com dados de competição.
- **Sem portfólios, na *agile* de 2018, a escolha por técnica ganha do SBS.** `[FATO]` O 4D completo e o 4D só com a D1 perdem 53 instâncias, contra 91 da linha de base LAMA 2011. Fecham 42% da lacuna, com p de Holm 0,047 dentro da unidade; com Holm sobre as 60 comparações, 0,43. É um indício, não um resultado firme.
  - Na mesma unidade, o kNN (51) e o 4D só com a D2 (57) também ficam abaixo do SBS, mas sem significância depois de Holm.
  - Na ótima de 2018 sem portfólios, vários seletores ficam abaixo do SBS (43 e 41 contra 64), sem significância.
- `[HIPÓTESE]` **O que isso sugere:**
  - A escolha por instância só ajuda quando o melhor planejador único é fraco. É o caso da *agile* sem portfólios, em que o SBS perde 91 de 166 instâncias.
  - Quando os portfólios estão na disputa, o SBS já é um portfólio (Saarplan, Delfi1), que absorve a complementaridade que um seletor tentaria explorar.
  - O ganho, onde aparece, vem do método por técnica (4D), e não do método de 2010 com o planejador no lugar da técnica. É o oposto do EXP-13 por domínio, em que o 4D piorava a escolha.

## Limites

- **Uma unidade com ganho significativo** (a *agile* de 2018 sem portfólios) em 10 unidades × 6 seletores testados. A correção de Holm é por unidade. Com Holm sobre as 60 comparações juntas, nenhum resultado fica abaixo de 0,05: o ganho do 4D na *agile* sem portfólios vai a 0,43, e a menor correção global é 0,12 (4D só com a D2, na *agile* com todos os planejadores, que é uma piora).
- **12 a 14 domínios por unidade:** o Wilcoxon por domínio tem pouco poder.
- **Só cobertura.** Qualidade e tempo, que definem os placares da *satisficing* e da *agile*, ficam fora.
- **Features:** só as 16 SAS+. As 32 tarefas de 2018 sem *features* ficam fora (regra 3 do recorte).
