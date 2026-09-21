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

## Dataset

O dataset de 2010 já foi extraído da dissertação e conferido: ver [data/2010/README.md](../data/2010/README.md). Esta seção descreve o `script.sql` como artefato do acervo.

`comp/script.sql` contém dados da análise em `INSERT` (sem `CREATE TABLE`). `[FATO]`

| Tabela | Linhas | Conteúdo |
|---|---|---|
| `dominios` | 10 | Blocks World, Depot, Driver Log, Gripper, Logistic World, Mystery, Pathways, Pipes World, Satellite, TPP |
| `planejadores` | 10 | Blackbox, IPP, FF, R, LPG, Fast Downward, YAHSP, SGPlan, SATPlan, MAXPlan |
| `caracteristicas` | 17 | As 17 métricas UML |
| `tecnicas` | 13 | As 11 técnicas da dissertação mais `Linear` e `Non-Linear` |
| `dominios_caracteristicas` | 170 + 100 | Classe (Baixo/Medio/Alto) por domínio × característica, em **dois blocos** |
| `planejadores_tecnicas` | 52 + 52 | Planejador × técnica, em **dois blocos idênticos** |
| `planejamentos` | 100 | `eficiencia` (com decimais) e `nota` (0–10) por planejador × domínio |

**Integridade do arquivo.** O `script.sql` é uma concatenação com sobras. As contagens de 270 (`dominios_caracteristicas`) e 104 (`planejadores_tecnicas`) da primeira inspeção vêm de blocos alternativos ou repetidos, não de dados a mais no conjunto publicado:

- `dominios_caracteristicas`: o **bloco 1** (170 linhas, 10 domínios × 17) bate 170/170 com a dissertação. O **bloco 2** (100 linhas) refaz os domínios 6–10 com 20 características, 3 delas sem definição; difere do bloco 1 em 43 de 85 pares. Não foi publicado.
- `planejadores_tecnicas`: bloco repetido; difere da Tabela 4 (versão anterior da taxonomia).
- Linha 298 tem um **fragmento truncado** (`cteristicas VALUES(5,20,"Alto");`), resto de um `INSERT` cortado por edição manual.
- Os valores de `planejamentos` (eficiência e nota) batem 100/100 com a dissertação; a eficiência tem decimais que o texto arredondou.

Detalhes e arquivos de divergência: [data/2010/conferencia/](../data/2010/conferencia/).

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

Os 10 primeiros correspondem aos 10 domínios de treino. **Não há pasta de PDDL para Zeno-travel nem Elevator**, os outros dois domínios de validação citados no plano; só existem os modelos UML no itSIMPLE. `[FATO]` Os PDDL dos 11 domínios que existem aqui foram identificados nas IPCs de 1998–2008, e os de Zeno-travel e Elevator existem no repositório `potassco/pddl-instances`: ver [benchmarks-ipc-ate-2008.md](benchmarks-ipc-ate-2008.md).

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

A dissertação declara: 8 computadores idênticos (Core 2 Duo 2,5 GHz, 4 GB, Ubuntu 9.04), timeout de 20 minutos, cerca de 2.000 processos, planejadores nas versões originais das competições. Os scripts confirmam o `timeout 1200`. O que ainda falta (memória por processo, critério de "não resolvido", versões exatas) está em [../auditoria/condicoes-de-execucao-2010.md](../auditoria/condicoes-de-execucao-2010.md).

## Planilhas

Mapeadas em 21/09/2026 (abas e conteúdo). Nenhuma contém as **contagens brutas das métricas** (Tabelas 8–9): elas só existem na dissertação e, discretizadas, no SQL.

| Arquivo | Data | Abas | Conteúdo |
|---|---|---|---|
| `contabilizacao_problemas.ods` | 30/11/2009 | `Planilha1` | **Problemas resolvidos** por planejador × domínio (n e %), com o total de problemas por domínio; inclui Storage. Base das Tabelas 14–15. Extraído para `data/2010/problemas_resolvidos.csv`. `[FATO]` |
| `Análise dos resultados.xls` | 10/12/2009 | `Características x Técnicas`, `Tecnicas x Características`, `Impacto`, `Relevância` | Cálculo da relação característica × técnica e da relevância (variância, menor, maior, diferença). `Relevância` corresponde às Tabelas 21–23 (títulos "não relevantes / pouco relevantes / muito relevantes"). As demais abas provavelmente correspondem às Tabelas 18–20 e 24–25 `[A CONFIRMAR]`. |
| `caracteristicas_tecnicas.xls` | 19/11/2009 | `Planilha1` (46×14) | Matriz característica × técnica; parece uma versão anterior da relação das Tabelas 19–20 `[A CONFIRMAR]`. |
| `testes.ods` | 10/12/2009 | `Planilha1`, `Planilha2`, `Planilha4`, `Ponderada x Valores`, `Ponderada com 10`, `Media com 10`, `Média simples` | Testes de **agregação alternativa** (média simples, ponderada, com valor 10) e seu efeito no ranking de Storage (`Planilha4`). Ver achado G7. `[FATO]` |

Nenhuma delas foi convertida além de `contabilizacao_problemas.ods`. As demais são insumo da Fase 3 (replicação do método de 2010 como linha de base) e da auditoria.

## Modelos itSIMPLE

`itSIMPLE/examples/` tem 47 modelos `.xml` (UML.P, itSIMPLE 3.0.10). O mapa final domínio → modelo, com a evidência, está em [data/2010/modelos_itsimple_2010.csv](../data/2010/modelos_itsimple_2010.csv) (gerado por `mapear_modelos_itsimple.py`). Os 13 domínios têm modelo identificado:

| Situação | Domínio → arquivo |
|---|---|
| **4/4 métricas comparáveis batem** `[FATO]` | Blocks World → `BlocksDomainv1.xml` · Depots → `DepotDomain.xml`\* · Driver Log → `DriverLogDomain.xml`\* · Gripper → `GripperDomainv1.xml` · Logistics → `LogisticDomainv1.xml` · Mystery → `MysteryDomainv1.xml` · Pipesworld → `PipesworldDomainv1.xml` · Satellite → `SatelliteDomainv1.xml`\* · Storage → `StorageDomainv1.xml` · Zeno-travel → `ZenoTravelDomainv1.xml` · Elevator → `ElevatorDomainv1.xml` |
| **Identificado pela figura, com uma discrepância na tabela** | Pathways → `PathwaysDomainv1.xml` (Tabela 9: 4 associações; figura e XML: 2; achado G11) · TPP → `TPPPropositionalDomainv1.xml` (Tabela 9: 2 generalizações; figura e XML: 4; achado G12) |

\* Só bate com a exclusão das classes auxiliares `Utility` (ou `Global`, no Satellite): achado G2.

**Como Pathways e TPP foram resolvidos.** As contagens automáticas não bastavam. Comparei as Figuras 26 e 27 da dissertação (`data/2010/figuras/`) com o XML. No TPP, a figura tem a classe `Level`, que só existe na versão *Propositional*. No Pathways, a figura tem as mesmas 6 classes, 2 associações, 2 generalizações e as 5 ações do `Agent` que o XML. Nos dois casos, **a figura da dissertação concorda com o XML e discorda da tabela**, o que indica erro de contagem manual e não modelo errado `[HIPÓTESE]`. `PathwaysSimplePreferencesDomainv1.xml` tem contagens idênticas às da versão base e não se distingue pela figura; foi escolhida a base.

**Cautela.** Só 4 das 17 métricas são comparáveis por contagem direta, e a métrica "Agregação" não é conferível pelo XML (achado G13). Estados, ações de entrada/saída e transições não foram comparados. O modelo do acervo pode ter evoluído depois da medição de 2009.

O restante da pasta `itSIMPLE/` (`itSIMPLE`, `itGraph`, `planning`, `languages`, `lib`, `resources`…) é a própria ferramenta, em Java.

## Material adicional avaliado e descartado (`itsimple-domains`, `itsimple-planners`)

Em 21/09/2026 o autor colocou `data/itsimple-domains/` (42 XML) e `data/itsimple-planners/` (16 arquivos). Foram comparados por hash e conteúdo com o acervo, **não foram versionados e o autor os removeu do disco**. O registro fica porque as conclusões continuam valendo:

| Pasta | Versão | Relação com o acervo |
|---|---|---|
| `itsimple-domains/` | **itSIMPLE 3.1.10** (arquivos de 04/05/2010, depois da dissertação de 03/2010) | O acervo tem a **3.0.10**. Dos 41 arquivos em comum, **36 diferem só na tag `<version>`**; Gripper, Storage, Zeno-travel e GridDomainMetrics diferem só em **coordenadas de layout** de diagrama; `SettlersDomainv1.xml` é reformatado (86 mil linhas de diff). As contagens de classes, métodos, associações e generalizações são **idênticas** nos 19 arquivos comparados. Só na nova: `PaperReviewingDomainv1.xml`. Só no acervo: `BAMS`, `BlocksDomain_tf`, `GoldMinerDomainMetrics`, `OilSupplyDomainSequencialv1`, `PathwaysSimplePreferencesDomainv1`, `ZenoTravelDomainv2`. |
| `itsimple-planners/` | Arquivos de 03/11/2010 | 14 dos 16 são **idênticos** aos de `itSIMPLE/myPlanners/`. Diferem `lprpg` e `mips-xxl2008` (não são planejadores da dissertação). |

**Utilidade para as pendências da Fase 0:** nenhuma resolve uma pendência.

- Modelos de **Pathways** e **TPP**: as contagens são idênticas na 3.1.10, então a divergência (associações 2 contra 4; generalizações 4 contra 2) não vem de versão do itSIMPLE.
- **PDDL de Zeno-travel e Elevator:** os XML têm 1 problema de exemplo cada e nenhum PDDL embutido. Não recuperam os conjuntos de problemas. O itSIMPLE poderia gerar o PDDL do *domínio* a partir do modelo `[A CONFIRMAR]`, mas não os problemas.
- Planejadores: nada novo, exceto a confirmação por hash das versões (ver `auditoria/condicoes-de-execucao-2010.md`).

O `comparar_modelos_itsimple.py` aceita outra pasta de XML e um sufixo de saída (a comparação com a 3.1.10 está em `data/2010/conferencia/modelos_itsimple_3_1_10.csv`).

## O que foi excluído do versionamento

Nada foi apagado do disco. O Git ignora: metadados `.svn` (32 diretórios), objetos compilados (`.o` × 69, `.pyc` × 24) e `.DS_Store`. São regeneráveis ou sem valor de pesquisa. O restante do acervo, inclusive binários de planejadores e arquivos `*~`, está versionado.

## Pendências que restam (Fase 0)

- [ ] **Conferência manual amostral** do dataset pelo autor (Tabelas 8–9, 26, 32, 38 têm uma só fonte).
- [ ] **Zeno-travel** e **Elevator**: os PDDL existem no repositório das IPCs (ver [benchmarks-ipc-ate-2008.md](benchmarks-ipc-ate-2008.md)); falta o autor **confirmar a variante** usada em 2010.
- [ ] Reconstruir o que ainda falta das condições de execução: ver `auditoria/condicoes-de-execucao-2010.md`.
- [ ] Converter as abas de `Análise dos resultados.xls` e `caracteristicas_tecnicas.xls` quando a Fase 3 precisar reproduzir o método de 2010.
