# Fase 4B: decisões de desenho

Decisões tomadas em 27/09/2026 pelo Coordenador (Claude Code, claude-opus-5-5), **por delegação do autor** ("optando pelas decisões mais coerentes"). Registradas na seção 10 do plano. Base: o levantamento em [`resultados-ipc-2011-2023.md`](resultados-ipc-2011-2023.md) e o que o autor decidiu na mesma data:

- os dados por instância de 2023 **não** serão pedidos aos organizadores;
- as referências pendentes **não** serão aprovadas. Continuam fora do `referencias.bib`: `ferber2019ipc`, `ferber2022explainable`, `vallati2014eighth`, `cenamor2014ibacop` e `malitsky2014allpaca`.

> **Convenção:** `[FATO]` = conferido; `[HIPÓTESE]` = inferência; `[A CONFIRMAR]` = falta evidência.

## D1. Regra dos portfólios

**Decisão:** manter a regra **P1**, que o autor aprovou no EXP-13 (`experimentos/execucoes/2026-09-26-nivel4-tecnicas.md`). Ela diz que D4 = Portfólio e que D1 a D3 recebem a união dos valores dos componentes descritos na fonte. A 4B acrescenta dois pontos que a P1 não fixava.

**G1. Critério para as "áreas cinzentas".** `vallati2018what` (p. 33) registra que não há definição aceita de portfólio e dá o FF como caso ambíguo. Na 4B:

- **É portfólio** o sistema que, segundo a fonte:
  - (a) se descreve como portfólio; ou
  - (b) executa dois ou mais componentes completos (cada um um planejador ou uma configuração de busca com heurística) como **execuções separadas**: em sequência com fatias de tempo, em paralelo ou por escolha de um seletor por tarefa.
- **Não é portfólio** o sistema descrito como um único planejador que:
  - faz uma única busca com várias heurísticas (LAMA, busca multi-heurística do Fast Downward, SelMax);
  - repete o mesmo algoritmo com parâmetros diferentes (reinícios, iterações *anytime* do WA*);
  - aciona uma segunda fase quando a primeira falha ou termina (FF: EHC e depois busca pela melhor escolha; Dual-BFWS; DecStar com busca explícita quando não há fatoração; LAPKT-BFWS-Preference: BFWS e depois o WA* do LAMA).

  Nesses casos, D4 = Planejador único e D1/D2 recebem a união dos valores.
- **Por que:** mantém a codificação já aprovada. O FF de 2010, o LAMA (taxonomia, §6), o LAPKT e o DecStar (EXP-13) são "planejador único", e a P1 segue valendo para os portfólios do Planner Museum. Uma primeira versão deste critério, que chamava de portfólio qualquer sequência de buscas com D1 ou D2 diferentes, contradizia o EXP-13 e foi descartada antes do uso. Um critério pela estrutura descrita na fonte também é verificável: não depende de saber qual componente resolveu cada instância, o que os dados das competições não registram.
- **Caso limite registrado:** o Merge-and-Shrink de 2011 faz duas execuções separadas de A*, cada uma com uma estratégia de *merge-and-shrink*. Pelo item (b), é portfólio (fixo), embora os dois componentes tenham os mesmos valores nas D1–D3.

**G2. Tipo de portfólio**, numa coluna à parte (`portfolio_tipo`), sem mudar a D4:

| Tipo | Definição |
|---|---|
| `fixo` | Sequência ou divisão de tempo definida antes da competição, igual para toda tarefa |
| `selecao` | Escolha por tarefa, feita por regra ou modelo treinado sobre características da tarefa |
| `paralelo` | Componentes em execução simultânea |

O tipo `selecao` interessa diretamente à Q5: são os sistemas que já apostam que as características da tarefa predizem qual técnica funciona.

**Consequência para a análise:** todo resultado da 4B é apresentado em dois recortes, **todos os planejadores** e **sem portfólios**, como no EXP-13.

**Codificação (27/09/2026):** `data/ipc-2011-2023/planejadores_4d.csv`, gerado por `scripts/taxonomia_4d.py`. São 78 codificações de planejador × trilha em 2011 e 2018, a partir dos resumos oficiais (*booklet* de 2011 e resumos de 2018); os planejadores já codificados no EXP-13 foram copiados de lá. São 11 portfólios, 4 deles de seleção por tarefa (IBaCoP2-2018, Delfi1, Delfi2, MSP). Um valor novo foi criado: **N7**, "Programação linear (potenciais, contagem de operadores)" na D2, para o MSP. A D2 ficou "não determinada" em 5 casos em que o resumo não diz a heurística (CPT4, Sharaabi, Symple-1 e -2, freelunch-doubly-relaxed), e a D3 em 1 (alien).

**Correção encontrada:** pela fonte primária (*booklet* de 2011, Tabelas 2 e 3), o Stone Soup 2011 da *satisficing* usa hFF, hadd, hCG e hcea, **sem *landmarks***. O EXP-13 supôs *landmarks* para o FDSS11 (decisão M2, "a confirmar"). Corrigido em 28/09/2026, com aprovação do autor: o valor saiu do `planejadores_museu_4d.csv`, e o EXP-13 rodado de novo deu saídas idênticas.

## D2. Recorte do dataset

**Decisão:**

| Edição | Papel na 4B | Unidade | O que entra |
|---|---|---|---|
| **2018** | Análise principal | Instância, agregada por domínio | Ótima, *satisficing* e *agile*: cobertura, nota da trilha, tempo, custo |
| **2011** | Análise principal | Instância, agregada por domínio | Ótima e *satisficing*: cobertura e custo (sem tempo). *Multi-core* fora (não reproduz a ordem oficial) |
| 2014 | Descritiva | Trilha | Totais por trilha de `vallati2018what` e *features* por domínio. Fora da análise da Q5: não há resultado por domínio |
| 2023 | Descritiva | Domínio | Placar por domínio e *features*. Fora da análise da Q5: são só 7 domínios, sem dados por instância |
| IBM/Delfi | Fora | — | `ferber2019ipc` não é citável e não é dado de competição |

**Regras do recorte:**

1. **Comparações dentro de cada edição e trilha.** Não se juntam edições: *hardware*, limites (6 GB em 2011, 8 GiB em 2018) e métricas mudam.
2. **Caldera e organic-synthesis de 2018:** as quatro formulações que rodaram (normal e `split` de cada) entram como domínios separados, cada uma com o seu PDDL e as suas *features*. O `-combined` fica só para reproduzir o placar oficial. Ele copia, para cada planejador e instância, a melhor das duas formulações, e por isso não tem *features* próprias.
3. **Tarefas sem *features*** (o tradutor não terminou em 1.800 s, o limite da própria competição) ficam fora da análise, com contagem registrada. `[HIPÓTESE]` Excluí-las favorece os planejadores que também não conseguem aterrar essas tarefas; o efeito é pequeno e fica documentado.
4. **2011 só entra depois da ligação completa aos arquivos PDDL** (`ipc2011_arquivos.csv` sem ligação do tipo `numero`). Até lá, a análise de 2011 é provisória.
5. **Linhas de base** (LAMA 2011, *blind*, SBD em 2018) entram como planejadores, codificadas na taxonomia como os demais.
6. **Classificação dos planejadores:** as fontes primárias são os resumos oficiais de cada IPC, citados pela URL no CSV de trabalho, como no EXP-13. Só se classificam as edições da análise principal (2011 e 2018).

**Por que este recorte:**

- A Q5 pede relação entre características do domínio e desempenho de famílias de técnicas. Isso exige, no mínimo, resultados por domínio × planejador em muitos domínios.
- 2011 e 2018 têm resultados por instância validados contra o placar oficial. São 14 domínios em 2011 e 11 em 2018 (13 formulações, pela regra 2), nenhum repetido entre as duas edições. Somam 39 entradas de planejador em 2011 e 59 em 2018, mais 4 linhas de base.
- 2014 e 2023 não têm esse nível: 2014 só tem totais por trilha, e 2023 tem 7 domínios sem instâncias.
- `[HIPÓTESE]` O ganho de incluir 2023 por domínio (7 pontos por trilha) não compensa o risco de misturar granularidades.

## O que as decisões do autor mudam

- **Sem `ferber2022explainable`:** o principal trabalho de seleção interpretável fica sem confronto citável no texto. A comparação com seletores da literatura se restringe às obras do `referencias.bib`, como `cenamor2016ibacop` e as de seleção de algoritmos do eixo E1.
- **Sem o *booklet* de 2014 no `.bib`:** as descrições dos planejadores de 2014 não podem ser citadas no texto. Não afeta a análise, porque 2014 é descritiva.
- **Sem dados por instância de 2023:** a verificação fora da amostra, com domínios novos, fica só no nível de domínio e é descritiva.
