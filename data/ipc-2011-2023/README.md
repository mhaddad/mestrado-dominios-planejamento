# Resultados das IPCs 2011–2023 (Fase 4B)

Dataset da Fase 4B, em construção. Por enquanto contém só o levantamento das fontes; o levantamento completo, com o que cada edição publicou e o que ainda está acessível, está em [`docs/resultados-ipc-2011-2023.md`](../../docs/resultados-ipc-2011-2023.md).

## Arquivos

| Arquivo | Conteúdo | Gerado por |
|---|---|---|
| `resumo_fontes.csv` | Uma linha por edição e trilha: granularidade, execuções, planejadores, linhas de base, domínios, tarefas por domínio, limites e execuções resolvidas | `scripts/levantar_fontes.py` |
| `suporte_pddl_2023.csv` | Uma linha por receita Apptainer da IPC 2023 (65): repositório, entrada, nome, trilhas e os nove rótulos de suporte a PDDL (`sim`, `não`, `parcial`), como declarados pelos autores | `scripts/suporte_pddl_2023.py` |
| `ipc2011_problemas.csv` | Problemas das trilhas *satisficing* e ótima da IPC 2011: trilha, domínio, problema (hash do conteúdo no WebPlan) e número, quando o *dump* o registra. 560 linhas (2 × 14 × 20) | `scripts/webplan_2011.py` |
| `ipc2011_resultados.csv` | Um plano válido por linha: trilha, domínio, problema, planejador (nome oficial e nome no WebPlan), custo, melhor custo da trilha e nota da IPC 2011 recalculada | `scripts/webplan_2011.py` |
| `ipc2011_arquivos.csv` | Liga cada problema de 2011 no WebPlan ao arquivo PDDL do `downward-benchmarks` (pasta `<domínio>-opt11-strips` ou `-sat11-strips`): trilha, domínio, problema, número, arquivo e tipo de ligação (`sha1` conferido; `texto` igual depois de normalizar; `numero` ainda não conferido) | `scripts/webplan_2011_arquivos.py` |
| `ipc2018_resultados.csv` | Uma execução por linha, IPC 2018, trilhas ótima, *satisficing* e *agile* (17.640): trilha, domínio, domínio original, `oficial` (domínio do placar oficial da trilha), problema, algoritmo, equipe, planejador, linha de base, cobertura, custo, tempo total (s), memória (KiB), erro, nota da trilha (cobertura na ótima, `sat_score`, `agl_score`) e expansões | `scripts/ipc2018.py` |
| `features_sas_ipc.csv` | *Features* SAS+ por tarefa (1.856): edição, trilha, domínio, problema, `ajuste`, `status` e as 16 *features* de tamanho, grafo causal e DTG do extrator da Fase 3 (`experimentos/extratores/features_sas.py`). 2011, 2018 e 2023: pastas `*-opt*`/`*-sat*` do `downward-benchmarks` do Planner Museum (a *agile* usou as tarefas da *satisficing*); 2014: *seq-opt*, *seq-sat* e *seq-agl* do ZIP oficial | `scripts/features_ipc.py` |
| `planejadores_4d.csv` | Planejadores de 2011 e 2018 na taxonomia em 4 dimensões, uma linha por valor: edição, planejador, trilhas, dimensão, valor, tipo de portfólio, fonte (página do *booklet* de 2011 ou URL do resumo de 2018) e observação. Regras em `docs/fase4b-desenho.md` | `scripts/taxonomia_4d.py` |
| `topologia_ipc.csv` | Propriedades de topologia de busca por tarefa (1.824 tarefas de 2011, 2014 e 2018): resultado básico de Hoffmann (2011), fração de transições inversíveis, hFF(s₀) e custo do plano relaxado, e, em 10 estados amostrados, taxa de becos sem saída, taxa de sucesso da sondagem e profundidade média da saída. Extrator validado contra a Tabela 3 de `hoffmann2011analyzing` (`experimentos/extratores/topologia-validacao/`) | `scripts/topologia_ipc.py` |
| `brutos/` | Arquivos baixados das fontes (fora do Git) | os scripts |

## Origem

- **IPC 2018:** `https://ipc2018-classical.bitbucket.io/results/{optimal,satisficing,agile}-results.tar.bz2` (JSON do *downward lab*), baixados em 27/09/2026. Sem licença declarada.
- **IPC 2023:** `index.md` do repositório `ipc2023-classical/ipc2023-classical.github.io` (tabelas por domínio). Limites de tempo e memória transcritos do mesmo arquivo (seção *Tracks*).
- **IPC 2023, suporte a PDDL:** receitas `Apptainer.*` da branch `ipc2023-classical` dos 24 repositórios `ipc2023-classical/plannerN`, lidas em 27/09/2026. É o que os autores declararam, sem verificação independente.
- **IPC 2011:** *dump* `ipc.json` do WebPlan (`bitbucket.org/lohre/webplan_ipc_data`, repositório Mercurial apagado em 2020), baixado do Software Heritage. Proveniência em `brutos/2011/webplan/PROVENIENCIA.txt`. Sem tempo de execução; ausência de registro = não resolveu. Validação no próprio script (ordem oficial dos *slides* e `coles2012survey`). Licença não declarada `[A CONFIRMAR]`.
- **IPC 2014, PDDL:** `benchmarksV1.1.zip` fornecido pelo autor em 27/09/2026, idêntico à cópia arquivada do site oficial (SHA-256 `477c2b7c…172635`). Guardado em `brutos/2014/` (fora do Git). Só PDDL, sem resultados.
- **IBM/IPC-graph-data** (`ferber2019ipc`, ainda não citável): `problems/problem-names-{train,valid,test}.txt`, licença Apache-2.0.

## Como reproduzir

```sh
.venv/bin/python data/ipc-2011-2023/scripts/levantar_fontes.py
.venv/bin/python data/ipc-2011-2023/scripts/suporte_pddl_2023.py
.venv/bin/python data/ipc-2011-2023/scripts/webplan_2011.py
.venv/bin/python data/ipc-2011-2023/scripts/ipc2018.py
uv run --no-project --with networkx python data/ipc-2011-2023/scripts/features_ipc.py --limite 300 --processos 6   # ~75 min
uv run --no-project --with numpy --with networkx python data/ipc-2011-2023/scripts/topologia_ipc.py --edicoes 2011,2014,2018   # ~2 h
.venv/bin/python data/ipc-2011-2023/scripts/webplan_2011_arquivos.py   # 120 consultas/h ao Software Heritage; rodar até não restar `numero`
```

Os scripts baixam os arquivos para `brutos/` só se ainda não estiverem lá.

## Observações

- `execucoes_resolvidas` de 2018 conta as execuções com `coverage` = 1, incluindo linhas de base e formulações alternativas (`-split`, `-combined`). Não é o placar oficial.
- `planejadores` exclui as linhas de base (nomes com `baseline`).
- `ipc2018_resultados.csv`: o placar oficial usa 10 domínios por trilha; as linhas com `oficial` = `não` são as formulações alternativas (`caldera`, `caldera-split`, `organic-synthesis`, `organic-synthesis-split`) e, na ótima, o flashfill. O script confere, para cada algoritmo, cobertura, nota e contagens de erro contra a tabela *Summary* do relatório final e falha se algo não bater.
- `erro` = `whitelisted-error` (2.314 execuções) é uma categoria do relatório de 2018 cujo critério não está documentado nos arquivos baixados `[A CONFIRMAR]`. Não tratar como "não suporta" sem confirmar.
- `ipc2011_arquivos.csv` (27/09/2026): liga os problemas do WebPlan aos arquivos das pastas `*-opt11-*`/`*-sat11-*` do `downward-benchmarks`, pelo SHA-1 do `problem.pddl` que a API do Software Heritage informa (120 consultas por hora; o *vault*, que empacotaria a pasta inteira, falhou por falta de espaço no servidor deles). Os problemas ainda não consultados ficam ligados pelo número final do nome do arquivo (`ligacao` = `numero`); no visitall o número não serve e só vale o SHA-1. Até a troca de fonte, 150 problemas conferidos por SHA-1, sem divergência.
- `features_sas_ipc.csv` (27/09/2026; 300 s por tradução e, para as falhas de 2018, 1.800 s, o limite da competição): 2.026 de 2.136 tarefas traduzidas. 2011 e 2014: todas. 2018: 229/240 na ótima e 219/240 na *satisficing*; sem *features* ficam 28 do organic-synthesis normal e 4 do flashfill (a formulação `split` do organic-synthesis traduziu todas). 2023 (só 300 s até agora): 107/140 e 95/140; as falhas estão em labyrinth, slitherlink, recharging-robots e folding.
- **Fonte do PDDL (27/09/2026):** a primeira versão usou o `pddl-instances` (`experimentos/benchmarks/ipc/`) para 2011 e 2014. Lá, a pasta do floortile ótimo de 2011 é cópia da *satisficing*, o que a ligação com o WebPlan revelou. Por isso 2011 passou para o `downward-benchmarks`, cujos arquivos casam por SHA-1 com os do WebPlan, e 2014 para o ZIP oficial.
- `brutos/2011/resumos/` e `brutos/2018/resumos/`: *booklet* de 2011 (Internet Archive, cópia de 16/04/2024 de `www.plg.inf.uc3m.es/ipc2011-deterministic/attachments/ParticipatingPlanners/ipc2011-booklet.pdf`) e resumos de 2018 (`ipc2018-classical.bitbucket.io/planner-abstracts/`), fontes da codificação 4D.
- `topologia_ipc.csv` (27/09/2026): 1.793 de 1.824 tarefas com as 10 amostras; 26 parciais (medidas acima de 120 s; transport de 2014 e caldera, organic-synthesis e agricola de 2018) e 5 com tradução acima de 300 s. A coluna `hff_custo_s0` não deve ser dividida pelo melhor custo conhecido da instância numa análise de desempenho: o melhor custo vem dos planos dos competidores (vazamento; ver o EXP-25).
