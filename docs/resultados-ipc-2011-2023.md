# Resultados publicados das IPCs 2011–2023 (levantamento da Fase 4B)

Levantamento feito em 27/09/2026 (atividade 1 da Fase 4B): o que cada IPC posterior a 2010 publicou nas trilhas clássicas, em que granularidade, com que limites, e o que ainda está acessível. Serve para decidir o desenho do dataset da 4B.

> **Convenção:** `[FATO]` = conferido na fonte citada nesta data. `[HIPÓTESE]` = inferência. `[A CONFIRMAR]` = falta evidência.

## Resposta curta

- **Só a IPC 2018 tem resultados por instância acessíveis**, nas três trilhas que interessam (ótima, *satisficing*, *agile*), em JSON do *downward lab*, com tempo, memória, custo, cobertura e motivo de falha de cada execução. `[FATO]`
- **IPC 2011:** os arquivos oficiais de resultados saíram do ar (DNS de `www.plg.inf.uc3m.es` e do SVN `pleiades` não resolve) e o Internet Archive não os guardou. **Mas os resultados por instância foram recuperados** de outra fonte: o *dump* do WebPlan (Manuel Braun, 2012), arquivado no Software Heritage. Ele traz os planos válidos e o custo de cada planejador em cada problema, sem tempo de execução. O placar recalculado reproduz a ordem oficial dos 27 planejadores da *satisficing* e dos 12 da ótima. Os *slides* oficiais **não têm números**, só um mapa de calor. `[FATO]`
- **IPC 2014:** havia um `results.tar` (92 KB) no repositório do site, que também saiu do ar e não foi arquivado. O relatório dos organizadores (`vallati2018what`, lido em texto integral em 27/09/2026) publica **totais por trilha para todos os planejadores** (placar, resolvidos, Borda), mas **nenhuma tabela por domínio e planejador**; por domínio, só agregados em figuras. Os *slides* mostram só os cinco primeiros; as `table_seq_*.pdf` arquivadas tratam de **suporte a recursos do PDDL**; o artigo da AI Magazine (DOI 10.1609/aimag.v36i3.2571) não traz tabelas. `[FATO]`
- **IPC 2023:** o site publica o placar de todos os planejadores **por domínio** (7 domínios, 20 tarefas cada) nas três trilhas; não há resultados por instância publicados. Mas **eles existem e os organizadores se ofereceram para compartilhá-los**: os *slides* (p. 32) dizem que logs e propriedades extraídas foram entregues aos autores e que os de outros planejadores seriam fornecidos a quem pedisse. `[FATO]` Os logs no GitHub da competição são de compilação das imagens, não de execução.
- **Fontes derivadas:** o conjunto de dados da IBM (`ferber2019ipc`, ainda não citável) tem o **tempo por tarefa de 17 planejadores ótimos** (o portfólio do Delfi) em 2.439 tarefas das IPCs 1998–2018, com licença Apache-2.0. O Planner Museum (`lequen2026planner`) **não publicou resultados por instância**: o zip do Zenodo (CC-BY-4.0) traz *benchmarks*, receitas e scripts, e a Fase 3 já usou a tabela agregada. `[FATO]`

**Consequência para o desenho** `[HIPÓTESE]`: a análise por instância, com dados de competição, é possível em **2011** (cobertura e custo, sem tempo; trilhas *satisficing* e ótima) e **2018**. 2023 permite análise **por domínio** até os organizadores enviarem os dados; 2014, só por trilha, a menos que o autor obtenha os dados dos organizadores. Na IPC 2014 as instâncias foram escolhidas pelo desempenho dos próprios competidores, por um protocolo introduzido naquela edição (`vallati2018what`, p. 2 e 9–10), o que calibra a dificuldade por domínio e pode atenuar diferenças entre domínios. A IBM acrescenta instâncias de todas as edições até 2018, mas só para planejadores ótimos, rodados pela equipe do Delfi, e não pela competição.

## Quadro por edição

| Edição | Trilhas clássicas | Planejadores (sem linhas de base) | Domínios | Limites | Granularidade acessível | Onde |
|---|---|---|---|---|---|---|
| 2011 | *satisficing*, ótima, *multi-core* (e temporal) | 27 / 12 / 8 (listas e tabelas dos *slides*; a *satisficing* confirmada por `coles2012survey`, "27 planners") | 14 por trilha, 20 tarefas cada | 30 min, 6 GB, cluster de 11 nós (*slides*, p. 13 e 15) | **por instância** (custo, sem tempo), *satisficing* e ótima | *dump* do WebPlan no Software Heritage; *slides* e *booklet* no Internet Archive |
| 2014 | *satisficing*, ótima, *agile*, *multi-core* (e temporal) | 20 / 17 / 15 / 9 nas tabelas de `vallati2018what` (o texto diz 21 e 16 submetidos na *satisficing* e na *agile*) | 14 por trilha (Tidybot só na ótima, Thoughtful nas demais), 20 tarefas cada | 30 min (*agile*: 5 min), 4 GB; *multi-core*: 4 núcleos; cluster de 256 núcleos AMD 2,39 GHz (booklet) | total por trilha, todos os planejadores | `vallati2018what` (Tabelas 3–7); `benchmarksV1.1.zip` arquivado |
| 2018 | ótima, *satisficing*, *agile* (e *cost-bounded*) | 16 / 22 / 21 | 10 (14 com as formulações alternativas), 20 tarefas cada | 30 min (*agile*: 5 min), 8 GiB, 1 núcleo | **por instância** | `ipc2018-classical.bitbucket.io/results/` |
| 2023 | ótima, *satisficing*, *agile* | 22 / 22 / 22 | 7 (todos novos), 20 tarefas cada | 30 min (*agile*: 5 min), 8 GB, 1 núcleo; *hardware* não informado | por domínio; **por instância sob pedido** aos organizadores | `ipc2023-classical.github.io` (tabelas e *slides*) |

Contagens de 2018, 2023 e IBM: `data/ipc-2011-2023/scripts/levantar_fontes.py` → `data/ipc-2011-2023/resumo_fontes.csv`. Resultados de 2011: `scripts/webplan_2011.py` → `ipc2011_problemas.csv` e `ipc2011_resultados.csv`. As contagens de planejadores de 2011 vêm dos *slides*; as de 2014, das Tabelas 1–7 de `vallati2018what`. Nenhuma das duas foi gerada por script.

## Detalhes por fonte

### IPC 2018 (por instância)

- Arquivos `{optimal,satisficing,agile}-results.tar.bz2`, cada um com um `properties` (JSON do *downward lab*) e um relatório HTML. Execuções: 5.040 (ótima), 6.440 (*satisficing*), 6.160 (*agile*). `[FATO]`
- Campos por execução: `algorithm`, `domain`, `problem`, `coverage`, `cost`, `total_time`, `memory`, `out-of-memory`, `timeout`, `unexplained_errors`, `sat_score`/`agl_score`, `expansions`, `evaluated`, entre outros. `[FATO]`
- Os domínios `caldera`, `organic-synthesis` e `settlers` aparecem em formulações alternativas (`-split`, `-combined`). A regra de pontuação de cada variante está `[A CONFIRMAR]` no relatório HTML antes de agregar.
- Logs brutos das execuções também estão publicados (0,5 a 2,8 GB descompactados por trilha); não foram baixados.
- Os PDDL estão em `bitbucket.org/ipc2018-classical/domains` e em `downward-benchmarks`, incluído no zip do Planner Museum. `[FATO]`
- O site não declara licença para os resultados. `[FATO]`

### IPC 2011 (por instância, via WebPlan)

- A página de resultados arquivada descreve o que havia: PDFs por trilha com quatro métricas (qualidade, tempo, soluções, qualidade-tempo) e planilhas com problemas resolvidos, falhas por tempo e memória, e diagnóstico, **por problema**. Nenhum dos arquivos está acessível hoje. `[FATO]`
- Os *slides* (`ipc2011-talk.pdf`, 106 p.) **não têm números**: as tabelas finais (p. 43, 74 e 86) são mapas de calor em tons de cinza, com a ordem dos planejadores. Servem para validar a ordem, não como fonte de valores. `[FATO]` (Correção de 27/09/2026: a primeira versão deste levantamento dizia que os *slides* traziam o placar por domínio.)
- **Fonte recuperada — WebPlan:** a documentação do WebPlan (`web-plan.readthedocs.io`, página *Server Setup*, indicada pelo autor) descreve um importador dos resultados das IPCs 2008 e 2011 e um script (`get-ipc-data.sh`) que clonava `bitbucket.org/lohre/webplan_ipc_data`, com um *dump* do banco (`ipc.json`). O Bitbucket apagou o repositório em 2020, mas o **Software Heritage** o guardou (visita de 15/07/2020; revisão de 03/03/2012, "added database dump"). Proveniência completa em `brutos/2011/webplan/PROVENIENCIA.txt`, gerado pelo script. `[FATO]`
- **Conteúdo do *dump*:** 1.746 problemas (hash do conteúdo), 88 planejadores, 11.759 resultados (7.718 da IPC 2011 e 4.041 da IPC 2008). Cada resultado é um plano **válido**, com custo. **Não há tempo de execução nem motivo de falha**: ausência de registro = não resolveu. Os problemas não resolvidos por ninguém também estão no *dump* (20 por domínio em cada trilha). A pasta `problems/` do repositório tem o `domain.pddl` e o `problem.pddl` de cada problema, e a pasta `results/`, os planos. `[FATO]`
- **Validação** (`scripts/webplan_2011.py`): com a regra oficial de 2011 (melhor custo entre os participantes da trilha / custo), o placar recalculado reproduz a **ordem das tabelas finais dos *slides*** para os 27 planejadores da *satisficing* e os 12 da ótima, com os empates (Selective Max = Merge and Shrink = 169, que os *slides* dão como "*runner-up ex-aequo*"). Exatamente 9 planejadores da *satisficing* superam o LAMA-2008, como diz `coles2012survey`. `[FATO]` Os valores absolutos do placar não foram conferidos com uma fonte oficial numérica, que não temos.
- **Trilha *multi-core*: não validada.** O vencedor (ArvandHerd) confere, mas as posições 2 a 4 não reproduzem a ordem oficial. O *dump* tem duas variantes do ArvandHerd (`seq-mco` e `xseq-mco`), e a causa da diferença está `[A CONFIRMAR]`. A trilha não foi exportada.
- **Licença:** o repositório do WebPlan não declara licença para os dados `[A CONFIRMAR]`; os dados originais são das IPCs.
- `[HIPÓTESE]` Os 4.041 resultados da **IPC 2008** no mesmo *dump* podem servir à Fase 3 (auditoria dos valores "de competição" de 2010, achado G21), se a variante e as instâncias coincidirem.
- Relatórios publicados: `coles2012survey` (citável; sem tabelas numéricas) e **López, Jiménez Celorrio e García Olaya (2015)**, *The deterministic part of the seventh International Planning Competition*, Artificial Intelligence, v. 223, p. 82–119, DOI 10.1016/j.artint.2015.01.004 (metadados conferidos no Crossref em 27/09/2026; **fora dos `.bib`**, não citável). É o relatório completo da IPC 2011; se tiver tabelas com o placar, serve para conferir os valores absolutos do *dump* do WebPlan `[A CONFIRMAR]`.

### IPC 2014 (total por trilha)

- Relatórios publicados: `vallati2018what` (KER, citável, lido em texto integral; ver a nota de leitura) e o artigo da AI Magazine (Vallati et al., 2015), **fora dos `.bib`**.
- `vallati2018what` tem os totais por trilha de todos os planejadores (Tabelas 3–7), a complementaridade por portfólio-oráculo (Tabela 8) e agregados por domínio em figuras. **Não tem resultados por domínio e planejador.** Há inconsistências internas (Tabela 8 × Tabela 3), registradas na nota.
- **`benchmarksV1.1.zip` (fornecido pelo autor em 27/09/2026; guardado em `data/ipc-2011-2023/brutos/2014/`, fora do Git):** idêntico à cópia arquivada do site oficial (SHA-256 `477c2b7c…172635`, conferido em 27/09/2026). Tem **só PDDL** (1.438 arquivos: domínios e problemas das trilhas `seq-sat`, `seq-opt`, `seq-agl`, `seq-mco` e `tempo-sat`), **nenhum resultado**. Serve para extrair as características dos domínios de 2014. `[FATO]`
- Na trilha ótima do V1.1, Barman tem 14 problemas, Maintenance 5 e Tetris 17: são 20 menos as tarefas insolúveis que `vallati2018what` (p. 23) relata (6, 15 e 3). A versão 1.1 retirou as insolúveis. As demais trilhas têm 20 por domínio; o Openstacks traz um arquivo de domínio por problema. `[FATO]`
- **Slides oficiais** (Chrpa, Vallati e McCluskey; cópia do Internet Archive e cópia enviada pelo autor em 27/09/2026): só os 5 primeiros de cada trilha (3 na temporal), com os mesmos valores das Tabelas 4–7 de `vallati2018what`. Informam as submissões por trilha (p. 10): *satisficing* 21 com 1 retirado, ótima 17, *multi-core* 9, *agile* 15, temporal 6; e que não houve planejador de linha de base (p. 23). **Cuidado:** a camada de texto do PDF tem restos das animações (p. ex., IBaCoP2 com 162,73 e RIDA na *multi-core* em páginas intermediárias); só a última página de cada trilha vale. `[FATO]`
- **Booklet dos participantes** ("Description of Participating Planners — Deterministic Track", Vallati, Chrpa e McCluskey, junho de 2014, 136 p.; cópia enviada pelo autor em 27/09/2026, SHA-256 `6c1ca173…9ec957`): **nenhum resultado da competição**. O prefácio remete os "detailed results" ao site, que saiu do ar. Traz o que faltava sobre o ambiente: *cluster* de 256 núcleos (AMD 2,39 GHz QuadCore), Linux, até 1.800 s, 4 GB de RAM e 200 GB de disco por execução, 7.400 horas de computação no total. O prefácio não menciona os 5 min da *agile* nem os 4 núcleos da *multi-core* (ver `vallati2018what`). Contagens: *satisficing* 20 submetidos de 43 inscritos, *multi-core* 9/17, ótima 17/34, *agile* 15/21, temporal 6/9; 66 pessoas em 31 equipes; 10 domínios na temporal. O "20" da *satisficing* bate com as tabelas do artigo e com os *slides* depois da retirada (21 − 1). `[FATO]`
- O booklet é a fonte primária das descrições técnicas dos planejadores de 2014: serve para classificá-los na taxonomia 4D e para a regra dos portfólios. Vários se descrevem como portfólios (IBaCoP2, ArvandHerd, MIPlan/DPMPlan, NuCeLaR, FDSS 2014, FD Uniform, FD Cedalion, BiFD, USE). IBaCoP2 e AllPACA escolhem planejadores com *random forest* sobre *features* de PDDL/SAS+ (35 e 65 *features*, respectivamente); são comparáveis diretos dos extratores da Fase 3. As tabelas de cobertura do RIDA e do Gamer são experimentos dos próprios autores com *benchmarks* de 2011, não dados da IPC 2014. `[FATO]` O booklet inteiro não está nos `.bib`; só o resumo do FD Cedalion (`seipp2014fast`) está.
- Os PDFs `table_seq_*.pdf` informam que recursos do PDDL cada planejador suporta. É útil para separar "não resolveu" de "não suporta" (cuidado listado no plano).

### IPC 2023 (por domínio; por instância sob pedido)

Página conferida em 27/09/2026 (último *commit* do site: 25/02/2025).

- Tabelas de cobertura (ótima) e de placar (*satisficing*, *agile*) por domínio no `index.md` do site; os *slides* têm as mesmas tabelas. As somas de todas as linhas conferem com a coluna SUM. `[FATO]`
- **Dados por instância sob pedido:** os *slides* (p. 32) dizem: "logs and parsed properties available to authors. Let us know if you want access to logs of other planners and we will be happy to provide them". Organizadores: Daniel Fišer (Saarland University) e Florian Pommerening (University of Basel), `ipc2023-classical@googlegroups.com`. `[FATO]`
- **Suporte a PDDL declarado por planejador:** as regras exigiam, em cada receita Apptainer, nove rótulos `Supports...` (yes/no/partially). As 65 receitas foram lidas por `data/ipc-2011-2023/scripts/suporte_pddl_2023.py` → `suporte_pddl_2023.csv`. O que mais falta são predicados derivados (28 de 65 não suportam) e `imply` (12). Efeitos condicionais faltam em 5 entradas: `opcount4sat` (2), `dom_opt`, `dalai_opt` e `FSM`. É a base para separar "não suporta" de "não resolveu" em 2023. `[FATO]`
- **Contagens:** 22 planejadores por trilha, sem as linhas de base (2 na ótima, 1 nas outras). São 66 entradas nas tabelas e 65 receitas, porque o FSM corre na *satisficing* e na *agile* com a mesma receita. Os *slides* (p. 8) também dizem 65 imagens. `[FATO]`
- **Linha de base à frente do vencedor:** na *agile*, `baseline-lama-first` (40,28) ficou acima do vencedor DecStar-2023 (40,25). As linhas de base não concorrem. Na *satisficing*, `baseline-lama` ficou em 4º (68,76). `hapori-greedy` zerou nas trilhas *satisficing* e *agile*. `[FATO]`
- **Os 7 domínios são novos** (nenhum de IPCs anteriores; *slides*, p. 11). Não há domínio em comum com 2010, com a Fase 3 nem com as outras edições. `[FATO]`
- **Versões normalizadas:** 4 domínios foram também traduzidos automaticamente para eliminar disjunções, quantificadores e condições negativas no objetivo. As regras anunciavam que todos os planejadores rodariam nas duas versões, valendo o melhor resultado por domínio. Os *slides* dizem que as versões normalizadas não seriam publicadas, só o tradutor. `[A CONFIRMAR]` se a regra do melhor resultado foi aplicada como anunciada.
- **Métricas:** a *satisficing* usa C\*/C com planos de referência, "como em 2008 e 2018, mas diferente de 2011 e 2014" (*slides*, p. 25), que usavam o melhor custo entre os participantes. A *agile* usa 1 − log(t)/log(300), como em 2018. Placares de edições diferentes não se comparam diretamente. `[FATO]`
- **Hardware:** o site não informa; os *slides* (p. 4) só dizem que os limites foram aplicados com o `runsolver`. `[FATO]`
- **Portfólios:** na lista de participantes, cada entrada tem uma descrição de uma linha, que serve de insumo para a taxonomia 4D e a regra dos portfólios. Muitas entradas são portfólios: as 8 variantes do Hapori, Ragnarok, Stone Soup 2023, Levitron, Powerlifted e Spock. Os *slides* (p. 26) dizem que "Levitron is a portfolio of Scorpion Maidu and Powerlifted".
- **Inconsistências do site:** o *feature stop* aparece como 24/03/2023 no cronograma e como 10/03/2023 nas seções de registro e de correção de *bugs*. A entrada "Hapori IBaCop2 Sat" aparece na lista da trilha ótima (na tabela, `hapori-ibacop2-opt`).
- PDDL e planos de referência em `github.com/ipc2023-classical/ipc2023-dataset` (sem licença declarada). `[FATO]`
- Relatório publicado: `taitler2024international` (citável).

### IBM / Delfi (por instância, planejadores ótimos)

- 2.439 tarefas, 85 nomes de domínio (com variantes), 17 planejadores do portfólio do Delfi, tempo limite de 1.800 s. Falha recebe o valor artificial 10.000. **Tarefas que nenhum dos 17 resolve foram excluídas**, o que censura a amostra. `[FATO]` (README do repositório)
- Os grafos (descrição do problema e estrutura abstrata) já vêm prontos, mas a 4B usará as *features* próprias da Fase 3.

## O que falta e quem resolve

| Item | Quem | Observação |
|---|---|---|
| Pedir aos organizadores os resultados por instância de 2023, 2011 e 2014 | Autor | **2023 primeiro:** os organizadores (Fišer e Pommerening, `ipc2023-classical@googlegroups.com`) ofereceram os logs nos *slides*. 2011: já recuperado pelo WebPlan; o pedido à UC3M (Carlos Linares López e equipe) só faz sentido para ter tempos de execução e a *multi-core*. 2014: Mauro Vallati. O e-mail sai em nome do autor |
| ~~Ler o texto integral de `vallati2018what`~~ | Autor | Feito em 27/09/2026 (PDF do autor): só totais por trilha; não há tabelas por domínio |
| Conseguir o texto integral de López et al. (2015), relatório da IPC 2011 na *Artificial Intelligence* | Autor (acesso ao PDF) | Pode ter tabelas por domínio de 2011; depois, incluir no `candidatas.bib` |
| Promover `ferber2019ipc` e `ferber2022explainable` ao `referencias.bib` | Autor | Metadados reconferidos em 27/09/2026 (Crossref e arXiv). Estão com ressalva por baixo impacto (Semantic Scholar: 7 citações para o de 2022); exceção como a de Stone Soup e Delfi |
| Incluir o artigo da AI Magazine sobre a IPC 2014 no `candidatas.bib` | Coordenador | Metadados conferidos no Crossref; falta nota de leitura |
| Regra dos portfólios | Autor | Decisão prevista para o início da classificação dos planejadores |
