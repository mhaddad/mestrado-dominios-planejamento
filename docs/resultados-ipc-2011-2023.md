# Resultados publicados das IPCs 2011–2023 (levantamento da Fase 4B)

Levantamento feito em 27/09/2026 (atividade 1 da Fase 4B): o que cada IPC posterior a 2010 publicou nas trilhas clássicas, em que granularidade, com que limites, e o que ainda está acessível. Serve para decidir o desenho do dataset da 4B.

> **Convenção:** `[FATO]` = conferido na fonte citada nesta data. `[HIPÓTESE]` = inferência. `[A CONFIRMAR]` = falta evidência.

## Resposta curta

- **Só a IPC 2018 tem resultados por instância acessíveis**, nas três trilhas que interessam (ótima, *satisficing*, *agile*), em JSON do *downward lab*, com tempo, memória, custo, cobertura e motivo de falha de cada execução. `[FATO]`
- **IPC 2011:** os organizadores publicaram resultados detalhados (`ipc2011-results.tar.bz2`, com planilhas por problema) e *snapshots* (`ipc2011-snapshots.tar.bz2`), mas **o site está fora do ar** (DNS de `www.plg.inf.uc3m.es` não resolve) e o Internet Archive não guardou os dois arquivos. Restam os *slides* de resultados, com o placar de **todos** os planejadores **por domínio**. `[FATO]`
- **IPC 2014:** havia um `results.tar` (92 KB) no repositório do site, que também saiu do ar e não foi arquivado. O relatório dos organizadores (`vallati2018what`, lido em texto integral em 27/09/2026) publica **totais por trilha para todos os planejadores** (placar, resolvidos, Borda), mas **nenhuma tabela por domínio e planejador**; por domínio, só agregados em figuras. Os *slides* mostram só os cinco primeiros; as `table_seq_*.pdf` arquivadas tratam de **suporte a recursos do PDDL**; o artigo da AI Magazine (DOI 10.1609/aimag.v36i3.2571) não traz tabelas. `[FATO]`
- **IPC 2023:** o site publica o placar de todos os planejadores **por domínio** (7 domínios, 20 tarefas cada) nas três trilhas; não há resultados por instância publicados. `[FATO]` Os logs no GitHub da competição são de compilação das imagens, não de execução.
- **Fontes derivadas:** o conjunto de dados da IBM (`ferber2019ipc`, ainda não citável) tem o **tempo por tarefa de 17 planejadores ótimos** (o portfólio do Delfi) em 2.439 tarefas das IPCs 1998–2018, com licença Apache-2.0. O Planner Museum (`lequen2026planner`) **não publicou resultados por instância**: o zip do Zenodo (CC-BY-4.0) traz *benchmarks*, receitas e scripts, e a Fase 3 já usou a tabela agregada. `[FATO]`

**Consequência para o desenho** `[HIPÓTESE]`: a análise por instância, com dados de competição, só é possível em 2018. 2011 e 2023 permitem análise **por domínio**; 2014, só por trilha, a menos que o autor obtenha os dados dos organizadores. Na IPC 2014 as instâncias foram escolhidas pelo desempenho dos próprios competidores, por um protocolo introduzido naquela edição (`vallati2018what`, p. 2 e 9–10), o que calibra a dificuldade por domínio e pode atenuar diferenças entre domínios. A IBM acrescenta instâncias de todas as edições até 2018, mas só para planejadores ótimos, rodados pela equipe do Delfi, e não pela competição.

## Quadro por edição

| Edição | Trilhas clássicas | Planejadores (sem linhas de base) | Domínios | Limites | Granularidade acessível | Onde |
|---|---|---|---|---|---|---|
| 2011 | *satisficing*, ótima, *multi-core* (e temporal) | 27 / 12 / 8 submetidos `[A CONFIRMAR]` na fonte primária | 14 por trilha, 20 tarefas cada | 30 min, 6 GB, cluster de 11 nós (*slides*, p. 13 e 15) | por domínio (*slides*) | *slides* e *booklet* no Internet Archive |
| 2014 | *satisficing*, ótima, *agile*, *multi-core* (e temporal) | 20 / 17 / 15 / 9 nas tabelas de `vallati2018what` (o texto diz 21 e 16 submetidos na *satisficing* e na *agile*) | 14 por trilha (Tidybot só na ótima, Thoughtful nas demais), 20 tarefas cada | 30 min (*agile*: 5 min), 4 GB; *multi-core*: 4 núcleos | total por trilha, todos os planejadores | `vallati2018what` (Tabelas 3–7); `benchmarksV1.1.zip` arquivado |
| 2018 | ótima, *satisficing*, *agile* (e *cost-bounded*) | 16 / 22 / 21 | 10 (14 com as formulações alternativas), 20 tarefas cada | 30 min (*agile*: 5 min), 8 GiB, 1 núcleo | **por instância** | `ipc2018-classical.bitbucket.io/results/` |
| 2023 | ótima, *satisficing*, *agile* | 22 / 22 / 22 | 7, 20 tarefas cada | 30 min (*agile*: 5 min), 8 GB, 1 núcleo | por domínio | `ipc2023-classical.github.io` (tabelas e *slides*) |

Contagens de 2018, 2023 e IBM: `data/ipc-2011-2023/scripts/levantar_fontes.py` → `data/ipc-2011-2023/resumo_fontes.csv`. As de 2011 vêm dos *slides*; as de 2014, das Tabelas 1–7 de `vallati2018what`. Nenhuma das duas foi gerada por script.

## Detalhes por fonte

### IPC 2018 (por instância)

- Arquivos `{optimal,satisficing,agile}-results.tar.bz2`, cada um com um `properties` (JSON do *downward lab*) e um relatório HTML. Execuções: 5.040 (ótima), 6.440 (*satisficing*), 6.160 (*agile*). `[FATO]`
- Campos por execução: `algorithm`, `domain`, `problem`, `coverage`, `cost`, `total_time`, `memory`, `out-of-memory`, `timeout`, `unexplained_errors`, `sat_score`/`agl_score`, `expansions`, `evaluated`, entre outros. `[FATO]`
- Os domínios `caldera`, `organic-synthesis` e `settlers` aparecem em formulações alternativas (`-split`, `-combined`). A regra de pontuação de cada variante está `[A CONFIRMAR]` no relatório HTML antes de agregar.
- Logs brutos das execuções também estão publicados (0,5 a 2,8 GB descompactados por trilha); não foram baixados.
- Os PDDL estão em `bitbucket.org/ipc2018-classical/domains` e em `downward-benchmarks`, incluído no zip do Planner Museum. `[FATO]`
- O site não declara licença para os resultados. `[FATO]`

### IPC 2011 (por domínio)

- A página de resultados arquivada descreve o que havia: PDFs por trilha com quatro métricas (qualidade, tempo, soluções, qualidade-tempo) e planilhas com problemas resolvidos, falhas por tempo e memória, e diagnóstico, **por problema**. Nenhum dos arquivos está acessível hoje. `[FATO]`
- Os *slides* (`ipc2011-talk.pdf`, 106 p.) trazem a tabela de placar por domínio de todos os planejadores de cada trilha. A extração por texto do PDF está `[A CONFIRMAR]` (as tabelas são reveladas aos poucos ao longo dos *slides*; vale a última de cada trilha).
- Relatórios publicados: `coles2012survey` (citável) e **López, Jiménez Celorrio e García Olaya (2015)**, *The deterministic part of the seventh International Planning Competition*, Artificial Intelligence, v. 223, p. 82–119, DOI 10.1016/j.artint.2015.01.004 (metadados conferidos no Crossref em 27/09/2026; **fora dos `.bib`**, não citável). É o relatório completo da IPC 2011 e pode ter tabelas por domínio `[A CONFIRMAR]`: precisa do texto integral.

### IPC 2014 (total por trilha)

- Relatórios publicados: `vallati2018what` (KER, citável, lido em texto integral; ver a nota de leitura) e o artigo da AI Magazine (Vallati et al., 2015), **fora dos `.bib`**.
- `vallati2018what` tem os totais por trilha de todos os planejadores (Tabelas 3–7), a complementaridade por portfólio-oráculo (Tabela 8) e agregados por domínio em figuras. **Não tem resultados por domínio e planejador.** Há inconsistências internas (Tabela 8 × Tabela 3), registradas na nota.
- Os PDFs `table_seq_*.pdf` informam que recursos do PDDL cada planejador suporta. É útil para separar "não resolveu" de "não suporta" (cuidado listado no plano).

### IPC 2023 (por domínio)

- Tabelas de cobertura (ótima) e de placar (*satisficing*, *agile*) por domínio no `index.md` do site; *slides* com as mesmas tabelas. `[FATO]`
- PDDL e planos de referência em `github.com/ipc2023-classical/ipc2023-dataset` (sem licença declarada). Quatro domínios têm versão normalizada, porque muitos planejadores não suportavam os recursos originais. `[FATO]`
- Relatório publicado: `taitler2024international` (citável).

### IBM / Delfi (por instância, planejadores ótimos)

- 2.439 tarefas, 85 nomes de domínio (com variantes), 17 planejadores do portfólio do Delfi, tempo limite de 1.800 s. Falha recebe o valor artificial 10.000. **Tarefas que nenhum dos 17 resolve foram excluídas**, o que censura a amostra. `[FATO]` (README do repositório)
- Os grafos (descrição do problema e estrutura abstrata) já vêm prontos, mas a 4B usará as *features* próprias da Fase 3.

## O que falta e quem resolve

| Item | Quem | Observação |
|---|---|---|
| Pedir aos organizadores os resultados por instância de 2011 e 2014 | Autor | 2011: Carlos Linares López, Ángel García-Olaya e Sergio Jiménez (UC3M); 2014: Mauro Vallati. O e-mail sai em nome do autor |
| ~~Ler o texto integral de `vallati2018what`~~ | Autor | Feito em 27/09/2026 (PDF do autor): só totais por trilha; não há tabelas por domínio |
| Conseguir o texto integral de López et al. (2015), relatório da IPC 2011 na *Artificial Intelligence* | Autor (acesso ao PDF) | Pode ter tabelas por domínio de 2011; depois, incluir no `candidatas.bib` |
| Promover `ferber2019ipc` e `ferber2022explainable` ao `referencias.bib` | Autor | Metadados reconferidos em 27/09/2026 (Crossref e arXiv). Estão com ressalva por baixo impacto (Semantic Scholar: 7 citações para o de 2022); exceção como a de Stone Soup e Delfi |
| Incluir o artigo da AI Magazine sobre a IPC 2014 no `candidatas.bib` | Coordenador | Metadados conferidos no Crossref; falta nota de leitura |
| Regra dos portfólios | Autor | Decisão prevista para o início da classificação dos planejadores |
