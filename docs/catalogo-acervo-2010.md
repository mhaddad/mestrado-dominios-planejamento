# Catálogo do acervo de 2010

Inventário do que existe em [acervo-2010/](../acervo-2010/), montado na Fase 0 a partir de inspeção dos arquivos. Serve para localizar material sem procurar à mão e para registrar o que ainda falta encontrar.

> **Convenção:** `[FATO]` = observado nos arquivos. `[A CONFIRMAR]` = inferência que precisa de conferência com a dissertação ou com o autor.
> O acervo é **somente leitura**. Não edite nada dentro de `acervo-2010/`.

Data da catalogação: 21/09/2026.

## Visão geral

| Item | Caminho | Observação |
|---|---|---|
| Dissertação (versão 2010) | `acervo-2010/dissertacao/dissertacao-haddad-2010.docx` | Renomeado a partir de `Dissertação-Matheus Haddad.docx` (acentos e espaço no nome). Conteúdo intacto. |
| Texto-base | `acervo-2010/planejadores_analise_resultados/texto_base.odt` | Rascunho anterior ao texto final `[A CONFIRMAR]`. Datado de 09/12/2009. |
| Planilhas de análise | `…/Análise dos resultados.xls`, `…/caracteristicas_tecnicas.xls`, `…/contabilizacao_problemas.ods`, `…/testes.ods` | Ver seção "Planilhas". |
| Domínios e problemas PDDL | `…/comp/<dominio>/` | 11 pastas. Ver seção "Domínios". |
| Planejadores, scripts e resultados | `…/comp/planners/` | Ver seção "Planejadores". |
| Banco de dados (dataset 2010) | `…/comp/script.sql`, `…/comp/consultas.sql` | **Achado importante.** Ver seção "Dataset". |
| itSIMPLE (ferramenta e modelos UML.P) | `…/itSIMPLE/` | Ver seção "Modelos itSIMPLE". |

Tamanho: 652 MB em disco, 3.133 arquivos. Compactado: cerca de 73 MB. O `pipesworld` (408 MB) e o `tpp` (91 MB) respondem por três quartos do volume; são problemas PDDL grandes, gerados.

## Dataset (achado para a Fase 0)

`comp/script.sql` contém os dados usados na análise, em `INSERT` (não há `CREATE TABLE`; o esquema é inferível pelo `consultas.sql`). `[FATO]`

| Tabela | Linhas | Conteúdo |
|---|---|---|
| `dominios` | 10 | Blocks World, Depot, Driver Log, Gripper, Logistic World, Mystery, Pathways, Pipes World, Satellite, TPP |
| `planejadores` | 10 | Blackbox, IPP, FF, R, LPG, Fast Downward, YAHSP, SGPlan, SATPlan, MAXPlan |
| `caracteristicas` | 17 | Métricas UML: atores, casos de uso, classes, atributos, métodos, associações, agregações, generalizações, hierarquias, DIT, estados, ações de entrada/saída, ações, transições, etc. |
| `tecnicas` | 13 | State-Space, Plan-Space, Partial-order, Total-order, Linear, Non-Linear, Hierarchical, Forward-chaining, Backward-chaining, Graph-based, Knowledge-based, SAT-based, Heuristic Search |
| `dominios_caracteristicas` | 270 | Valor **discretizado** (Baixo / Medio / Alto) de cada característica por domínio. Esperado: 10 × 17 = 170. **Anomalia:** os domínios 1–5 têm 17 linhas cada; os domínios 6–10 têm 37 (20 a mais cada). Ver abaixo. |
| `planejadores_tecnicas` | 104 | Associação planejador × técnica (a taxonomia questionada em F4) |
| `planejamentos` | 100 | Por planejador × domínio (10 × 10): `eficiencia` (numérica, ex.: 25.4) e `nota` (inteira de 0 a 10) |

Isso cobre boa parte da ação 2 do plano ("transcrever tabelas da dissertação para CSV"): em vez de transcrever a partir do texto, dá para **exportar do SQL e conferir contra as Tabelas 8–25 da dissertação**. A conferência continua obrigatória. `[A CONFIRMAR]`

Ponto de atenção: em `dominios_caracteristicas`, os domínios 6 a 10 (Mystery, Pathways, Pipes World, Satellite, TPP) têm 37 linhas cada, e não 17. Os valores existentes são só Alto / Medio / Baixo, então não se trata de valor bruto ao lado do discretizado. Hipótese: bloco de `INSERT` reinserido ou duplicado durante a montagem `[HIPÓTESE]`. Se houver valores conflitantes para o mesmo par domínio × característica, é preciso decidir qual vale, conferindo contra a dissertação. Resolver antes de gerar o `dataset-2010.csv`.

Os valores do banco são **discretizados**; as contagens brutas (nº de classes, atributos etc.) não estão no SQL. Elas devem estar nas planilhas ou nas Tabelas da dissertação.

## Domínios (`comp/`)

| Pasta | Arquivos | Domínio | Observação |
|---|---|---|---|
| `blocksworld` | 37 | Blocks World | |
| `depots` | 23 | Depots | Problemas em `pfile1…` |
| `driverlog` | 21 | Driver Log | |
| `gripper` | 27 | Gripper | Inclui `GENERATOR/` com `gripper.c` e `gerar_todos.sh` |
| `logistic` | 30 | Logistics | |
| `mystery` | 31 | Mystery | |
| `pathways` | 182 | Pathways | |
| `pipesworld` | 151 | Pipes World | 408 MB; `domain_pNN.pddl` de até 36 MB |
| `sattelite` | 45 | Satellite | Grafia da pasta preservada (*sattelite*) |
| `tpp` | 91 | TPP | 91 MB |
| `storage` | 31 | Storage | Domínio de validação `[A CONFIRMAR]` |

Os 10 primeiros correspondem aos 10 domínios de treino. **Não há pasta de PDDL para Zeno-travel nem Elevator**, os outros dois domínios de validação citados no plano. Só existem os modelos UML no itSIMPLE. `[FATO]`

## Planejadores (`comp/planners/`)

| Pasta | Planejador (tabela `planejadores`) | Conteúdo observado |
|---|---|---|
| `blackbox` | Blackbox | Executável |
| `fastdownward` | Fast Downward | Fonte com `Makefile`, `README`, `doc` |
| `ffv-2.3` | FF | v2.3 |
| `ipp`, `ipp2`, `ipplan` | IPP | Três cópias; `ipplan` tem fonte em C com `.y`/`.c` |
| `lpg` | LPG | `lpg-td-1.0` |
| `maxplan` | MAXPlan | |
| `r` | R | `bin/`, controle em Perl |
| `satplan` | SATPlan | `SatPlan2006.tgz`, `SatPlan2006_LinuxBin.tgz`, `SiegeWrapper.pl`, `berkmin561-linux` |
| `sgplan`, `sgplan6` | SGPlan | `sgplan522` e `sgplan6` |
| `yahsp` | YAHSP | |

Existe também `itSIMPLE/myPlanners/` com binários usados pela ferramenta (Plan-A, Blackbox, FF, HSP, LPRPG, Marvin, MaxPlan, Metric-FF, MIPS-XXL, SGPlan e outros). É a coleção do itSIMPLE, não necessariamente o que foi executado nos experimentos.

### Scripts e resultados

- `comp/planners/scripts/<planejador>/` — um script por planejador × domínio (`ff_depots.sh`, `ipp_tpp.sh` etc.).
- `comp/planners/resultados/<planejador>/` — saídas das execuções. Há também `resultados.zip`.
- Vários scripts existem **apenas** na forma `*.sh~` (20 arquivos sem par sem til). Por isso os arquivos com til foram mantidos no repositório.

### Condições de execução (F6)

Nos scripts inspecionados, o comando é `timeout 1200 ./<planejador> …`, ou seja, **limite de 1.200 s (20 min)**, com caminhos absolutos de `/home/matheus/mestrado/comp/…`. `[FATO]` para os scripts lidos (`ff_depots.sh~`). Falta: máquina, memória, versões exatas e se o limite foi o mesmo para todos os planejadores. `[A CONFIRMAR]`

O plano pede documentar como foram obtidos os dados da 5ª etapa do método (execuções fora das competições). O que existe aqui permite reconstruir parte disso, mas não a máquina nem a memória.

## Planilhas

| Arquivo | Data | Provável conteúdo `[A CONFIRMAR]` |
|---|---|---|
| `Análise dos resultados.xls` | 10/12/2009 | Análise final: eficiência, discretização, correlações |
| `caracteristicas_tecnicas.xls` | 19/11/2009 | Matriz planejador × técnica |
| `contabilizacao_problemas.ods` | 30/11/2009 | Contagem de problemas resolvidos por planejador × domínio (base da eficiência) |
| `testes.ods` | 10/12/2009 | Testes auxiliares |

Nenhuma foi aberta em profundidade. Falta mapear abas e ligar cada uma às tabelas da dissertação (Tabelas 8–25).

## Modelos itSIMPLE

`itSIMPLE/examples/` tem 47 modelos `.xml` (UML.P). Candidatos aos 13 domínios do plano: `[A CONFIRMAR]`

| Domínio | Arquivo(s) candidato(s) |
|---|---|
| Blocks World | `BlocksDomainv1.xml`, `BlocksDomainv2.xml`, `BlocksDomain_tf.xml` |
| Depots | `DepotDomain.xml`, `DepotDomainv2.xml` |
| Driver Log | `DriverLogDomain.xml` |
| Gripper | `GripperDomainv1.xml` |
| Logistics | `LogisticDomainv1.xml`, `LogisticDomainv2.xml` |
| Mystery | `MysteryDomainv1.xml` |
| Pathways | `PathwaysDomainv1.xml`, `PathwaysSimplePreferencesDomainv1.xml` |
| Pipes World | `PipesworldDomainv1.xml` |
| Satellite | `SatelliteDomainv1.xml` |
| TPP | `TPPMetricDomainv1.xml`, `TPPPropositionalDomainv1.xml` |
| Storage | `StorageDomainv1.xml` |
| Zeno-travel | `ZenoTravelDomainv1.xml`, `ZenoTravelDomainv2.xml` |
| Elevator | `ElevatorDomain.xml`, `ElevatorDomainv0.xml`, `ElevatorDomainv1.xml` |

Esses são os modelos que **acompanham o itSIMPLE**, que podem ter evoluído depois de 2009. O plano pede os modelos **originais usados na dissertação**. Onde há mais de uma versão, é preciso decidir qual foi a medida em 2010 (comparando as contagens com o dataset). Enquanto isso não for feito, a ação "localizar os modelos originais" fica aberta.

O restante da pasta `itSIMPLE/` (`itSIMPLE`, `itGraph`, `planning`, `languages`, `lib`, `resources`…) é a própria ferramenta, em Java.

## O que foi excluído do versionamento

Nada foi apagado do disco. O Git ignora: metadados `.svn` (32 diretórios), objetos compilados (`.o` × 69, `.pyc` × 24) e `.DS_Store`. São regeneráveis ou sem valor de pesquisa. O restante do acervo, inclusive binários de planejadores e arquivos `*~`, está versionado.

## Pendências da Fase 0 reveladas pela catalogação

- [ ] Explicar as 270 linhas de `dominios_caracteristicas` (esperado: 170; domínios 6–10 com 37 linhas em vez de 17).
- [ ] Localizar as contagens brutas das 17 características (o SQL só tem valores discretizados).
- [ ] Exportar `script.sql` para CSV e conferir contra as Tabelas 8–25 da dissertação.
- [ ] Mapear as abas das quatro planilhas e ligá-las às tabelas da dissertação.
- [ ] Decidir qual versão de cada modelo itSIMPLE corresponde à medição de 2010.
- [ ] Localizar (ou declarar ausentes) os PDDL de Zeno-travel e Elevator.
- [ ] Reconstruir as condições de execução dos planejadores (máquina, memória, versões).
