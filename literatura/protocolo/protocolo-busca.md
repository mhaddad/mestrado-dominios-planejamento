# Protocolo de busca da Fase 1

Versão 1.1 · 22/09/2026 · redigido pelo Coordenador (Claude Code, claude-opus-5). v1.1: critério X7; os triadores usavam X2 e X6 para exclusões por redundância, recodificadas em `triagem.csv` (`revisado_coordenador=recodificado`). **Aprovado pelo Coordenador em nome do autor; pendente de confirmação do autor** (modo "ponta a ponta", ver [estratégia](../../plan/fase1-estrategia-multiagentes.md)).

Revisão de literatura **leve e rastreável**, não revisão sistemática formal: o objetivo é reconstruir o capítulo de fundamentos com obras verificadas, e registrar o caminho para que a busca possa ser refeita e auditada.

---

## 1. Período, idiomas e tipos de obra

- **Período:** 2008 a 2026. Obras anteriores entram só quando são **fundacionais** para um eixo (por exemplo, Rice 1976; No Free Lunch 1997; Fast Downward 2006) e recebem a marca `classico`.
- **Idiomas:** inglês e português.
- **Tipos aceitos:** artigo de periódico; artigo de conferência ou *workshop* com anais (ICAPS, AAAI, IJCAI, ECAI, NeurIPS, ICML, ICLR, ICSE, FSE etc.); tese ou dissertação; livro ou capítulo; *preprint* do arXiv (marcado `preprint`); **literatura cinza** só para resultados oficiais das IPCs, documentação de ferramentas e *benchmarks* (marcada `cinza`).

## 2. Bases e forma de acesso

| Base | Acesso | Uso |
|---|---|---|
| Crossref | API `https://api.crossref.org/works?query.bibliographic=...` e BibTeX por DOI (`curl -LH "Accept: application/x-bibtex" https://doi.org/<DOI>`) | Localizar e verificar metadados; gerar BibTeX |
| OpenAlex | API `https://api.openalex.org/works?search=...` (campos `doi`, `title`, `authorships`, `publication_year`, `primary_location`, `abstract_inverted_index`, `cited_by_count`) | Busca principal por palavra-chave; resumo; citações para *snowballing* |
| arXiv | API `https://export.arxiv.org/api/query?search_query=...` | *Preprints* (sobretudo E4, E5, E8) |
| Semantic Scholar | API `https://api.semanticscholar.org/graph/v1/...` — **limita requisições (HTTP 429)**; usar com parcimônia e espera entre chamadas | Complemento; referências e citações de uma obra-semente |
| DBLP | **Bloqueia `curl`**; tentar pela ferramenta de *fetch* web; se falhar, não usar | Conferência de anais de computação |
| Busca web | Ferramenta de busca do agente (equivale a Google/Google Scholar) | Descoberta; páginas das IPCs, ICAPS, JAIR, AAAI |
| Páginas oficiais | Sites das IPCs, `icaps-conference.org`, JAIR, OJS da AAAI, IJCAI | Resultados das competições; texto integral aberto |

Toda linha da lista bruta registra **em qual base e com qual *string*** o item foi encontrado, e a **URL** do registro.

## 3. Perguntas por eixo e *strings* de busca

As *strings* são ponto de partida; o buscador pode refiná-las, desde que registre as que usou. Sementes (plano, seção 13, e as listadas abaixo) devem ser **localizadas numa base**, nunca completadas de memória; as não localizadas ficam com status `nao-localizada`.

### E1 — Seleção de algoritmos e portfólios em planejamento

**Pergunta:** como a seleção de algoritmos e os portfólios evoluíram em planejamento desde 2008, e que ganho sobre o *single best* relatam?
**Strings:** `"algorithm selection" planning`; `"planner portfolio"`; `"portfolio" "classical planning"`; `"planner selection" online`; `"per-instance" "algorithm selection" survey`; `"algorithm configuration" planning portfolio`.
**Sementes:** Rice (1976); PbP (Gerevini, Saetti, Vallati); Fast Downward Stone Soup (Helmert, Röger et al.); IBaCoP (Cenamor, de la Rosa, Fernández); Delfi (Katz, Sievers et al.); Cedalion (Seipp et al.); surveys de seleção de algoritmos (Kotthoff; Kerschke et al.).

### E2 — *Features* de tarefas de planejamento e predição de desempenho

**Pergunta:** que características de tarefas de planejamento predizem o desempenho de planejadores, e como foram extraídas (sintáticas, de grafo, de sondagem)?
**Strings:** `"performance prediction" planners`; `"runtime prediction" planning features`; `"empirical hardness" planning`; `"planning task" features "graph neural" planner selection`; `"learning from planner performance"`.
**Sementes:** Roberts & Howe; Fawcett et al. (2014); Hutter et al. (predição de tempo de execução); seleção de planejadores por imagem/grafo (Sievers et al.; Ma et al.).

### E3 — Evolução dos planejadores e heurísticas; IPCs 2008–2023

**Pergunta:** que famílias de técnicas definem o estado da arte em cada trilha das IPCs de 2008 a 2023, e a taxonomia de técnicas usada em 2010 ainda descreve bem o campo?
**Strings:** `"international planning competition" results 2008|2011|2014|2018|2023`; `landmarks "cost-based" planner`; `"landmark-cut" heuristic`; `"merge-and-shrink"`; `"symbolic search" "cost-optimal planning"`; `"best-first width search"`; `"planning as satisfiability" Madagascar`.
**Sementes:** Fast Downward (Helmert, 2006, `classico`); LAMA (Richter & Westphal, 2010); LM-cut (Helmert & Domshlak, 2009); *merge-and-shrink* (Helmert et al.); BFWS (Lipovetzky & Geffner); Madagascar (Rintanen); artigos-resumo de cada IPC.

### E4 — Aprendizado para planejamento

**Pergunta:** o que o aprendizado de máquina trouxe ao planejamento (heurísticas e políticas aprendidas, planejamento generalizado, aprendizado de modelos de ação), e quão bem generaliza entre domínios?
**Strings:** `"learned heuristics" classical planning`; `"action schema networks"`; `"graph neural networks" "generalized policies" planning`; `"generalized planning" survey`; `"learning action models" planning survey`; `"learning for planning" benchmark`.
**Sementes:** ASNets (Toyer et al.); GNNs para políticas generalizadas (Ståhlberg, Bonet, Geffner); STRIPS-HGN (Shen, Trevizan, Thiébaux); revisões de planejamento generalizado e de aprendizado de modelos de ação.

### E5 — LLMs e planejamento

**Pergunta:** que papéis os LLMs assumem em planejamento (planejador, tradutor para PDDL, heurística, seletor, verificador) e o que a evidência empírica mostra sobre cada um?
**Strings:** `"large language models" planning benchmark PDDL`; `PlanBench`; `"LLM+P"`; `"LLM-Modulo"`; `"large reasoning models" planning`; `"language models" "automated planning" survey`; `LLM "world model" PDDL`.
**Sementes:** PlanBench (Valmeekam et al., 2023); LLM+P (Liu et al., 2023); LLM-Modulo (Kambhampati et al., 2024); avaliações de modelos de raciocínio em planejamento; revisões sobre LLMs em planejamento automatizado.

### E6 — Engenharia do conhecimento para planejamento

**Pergunta:** como evoluíram as ferramentas e métodos de modelagem de domínios (itSIMPLE, ICKEPS, Unified Planning) e o uso de LLMs para gerar modelos PDDL? Há trabalho sobre métricas de qualidade de modelos de domínio?
**Strings:** `itSIMPLE`; `"knowledge engineering" planning tools`; `ICKEPS`; `"unified planning" framework library`; `"domain model" quality metrics planning`; `"LLM" "PDDL" generation domain`.
**Sementes:** Vaquero et al. (itSIMPLE); revisão de ferramentas de engenharia do conhecimento (Shah et al.); Unified Planning (AIPlan4EU); LLMs como geradores de domínios.

### E7 — Pontes conceituais

**Pergunta:** que arcabouços teóricos, fora do planejamento, sustentam a ideia de ajuste entre tarefa e técnica, e como o roteamento entre modelos de linguagem retoma a seleção de algoritmos?
**Strings:** `"no free lunch" optimization`; `"contingency theory" organization`; `"task-technology fit"`; `"meta-learning" "algorithm selection" cross-disciplinary`; `"instance space analysis"`; `"LLM routing"`; `"model routing" language models cost`.
**Sementes:** Wolpert & Macready (1997, `classico`); Lawrence & Lorsch (1967, `classico`); Goodhue & Thompson (1995, `classico`); Smith-Miles (meta-aprendizado para seleção de algoritmos); RouteLLM (Ong et al., 2024); FrugalGPT.

### E8 — IA no desenvolvimento de software

**Pergunta:** o que a evidência empírica mostra sobre agentes e assistentes de código (desempenho em *benchmarks*, estudos com equipes reais), e há trabalho sobre escolher a estratégia ou o agente conforme a tarefa?
**Strings:** `SWE-bench`; `"software engineering agents" LLM`; `"LLM-based agents" "software engineering" survey`; `"AI pair programming" randomized controlled trial`; `"developer productivity" AI assistant field study`; `"multi-agent" "software development" LLM`.
**Sementes:** SWE-bench (Jimenez et al., 2024); SWE-agent; Agentless; OpenHands; ensaios controlados com assistentes de código; revisões de agentes em engenharia de software.

## 4. Critérios de inclusão (I) e exclusão (X)

| Código | Critério |
|---|---|
| I1 | Publicado de 2008 a 2026, ou fundacional (`classico`) |
| I2 | Tipo aceito (seção 1) |
| I3 | Responde diretamente à pergunta do eixo |
| I4 | Metadados localizáveis e resumo acessível |
| I5 | Obra de referência do tema (muito citada, revisão, ou resultado oficial de IPC), mesmo que só tangencie a pergunta |
| X1 | Duplicata (fica a versão mais completa: periódico > conferência > *preprint*, salvo quando a conferência é a versão canônica) |
| X2 | Fora do tema do eixo |
| X3 | Sem resumo nem metadados verificáveis |
| X4 | Não acadêmico (blog, notícia), exceto literatura cinza da seção 1 |
| X5 | Idioma diferente de inglês ou português |
| X6 | Aplicação específica sem contribuição geral (ex.: planejamento para um robô específico sem método transferível) |
| X7 | Relevante, mas redundante com obra já incluída, diante do teto do eixo (acrescentado na v1.1, na revisão da triagem) |

Decisão de triagem: `incluir` / `excluir` / `talvez`, com o código do critério e uma frase de justificativa. **Prioridade de leitura:** `A` (texto integral, sustenta argumento central), `B` (nota a partir do resumo e da introdução), `C` (só citação contextual).

## 5. Tetos

Lista bruta até 60 por eixo · incluídas 12 a 20 por eixo · prioridade A 8 a 10 por eixo.

## 6. Chaves de citação

Formato `sobrenomeANOpalavra`, em minúsculas e sem acento: sobrenome do primeiro autor, ano, primeira palavra significativa do título (ex.: `rice1976algorithm`, `richter2010lama`). Colisão: sufixo `a`, `b`. A chave nasce na verificação (Onda 3) e não muda depois.

## 7. Formatos de arquivo (CSV UTF-8, vírgula, com cabeçalho)

**`busca/E{n}-bruta.csv`**
`id,eixo,titulo,autores,ano,veiculo,tipo,doi,arxiv_id,url,base,string_busca,data_busca,semente,marcas,resumo_disponivel,observacao`
- `id` = `E{n}-NNN`; `tipo` ∈ {periodico, conferencia, workshop, tese, livro, capitulo, preprint, cinza}; `semente` ∈ {sim, nao}; `marcas` ∈ {classico, preprint, cinza, vazio}; `resumo_disponivel` ∈ {sim, nao}.

**`triagem.csv`**
`id,chave_provisoria,eixo,titulo,ano,decisao,criterio,justificativa,prioridade,revisado_coordenador,confirmado_autor`

**`verificacao-metadados.csv`**
`id,chave,eixo,doi,arxiv_id,fonte_consultada,url_consultada,data_consulta,titulo_confere,autores_confere,ano_confere,veiculo_confere,discrepancias,status,texto_integral_url`
- `status` ∈ {verificada-por-agente, divergente, nao-localizada}.

## 8. Regras para os agentes

1. Nenhum item de memória: todo item vem de uma consulta registrada.
2. BibTeX só gerado a partir do registro primário (Crossref por DOI, arXiv, página da editora). Vai para `literatura/referencias/candidatas.bib`, nunca para `referencias.bib`.
3. `acervo-2010/`, `plan/` e `MEMORY.md` são intocáveis para subagentes.
4. Cada agente escreve só nos arquivos que lhe foram atribuídos.
