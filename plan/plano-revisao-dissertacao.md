# Revisão da Dissertação — Características de Domínios × Técnicas de Planejamento

> **Documento de trabalho.** Controle e acompanhamento da evolução de cada fase.
> Atualize o painel, os checkboxes e os registros ao final de cada sessão de trabalho.

| Campo | Valor |
|---|---|
| Trabalho original | *Relação entre características de domínios e técnicas de planejamento* — Dissertação de Mestrado, Centro Universitário da FEI, 10/03/2010 |
| Autor | Matheus Haddad |
| Orientador original | Prof. Dr. Flavio Tonidandel |
| Início da revisão | 21/09/2026 |
| Última atualização | 23/09/2026 |
| Versão deste documento | 0.19 |
| Status geral | 🟢 Fase 0 concluída em 21/09/2026 · 🟢 Fase 1 concluída em 23/09/2026 (equipe multiagente) · 🟢 Fase 2 concluída em 23/09/2026 (equipe multiagente) · próxima: Marco M1 e Fase 3 |

---

## 1. Propósito

Revisar a dissertação de 2010 para **evoluir o trabalho**: atualizar o estado da arte, reconstruir o método com os recursos de hoje e verificar o que das conclusões originais se sustenta.

Desdobramentos possíveis, não obrigatórios:

- **Compartilhar com o orientador original** (Flavio Tonidandel) e, se houver interesse mútuo, continuar a conversa ou produzir algo em conjunto.
- **Aplicar no desenvolvimento de software dirigido por IA**: se a ideia de ajuste entre características do problema e técnica de solução se mostrar útil, experimentar no Ateliê de Software.
- **Produto**: se o experimento no Ateliê gerar evidência, avaliar um produto para esse contexto. Este item é hipótese e só é considerado depois da Fase 5.

**Princípio de aceleração:** usar LLMs e outras ferramentas de IA em todas as fases para comprimir o trabalho operacional (busca, leitura, código, experimentos, rascunhos). As decisões, a verificação e a autoria continuam humanas.

---

## 2. Como usar este documento

**Legenda de status:** ⚪ não iniciada · 🟡 em andamento · 🟢 concluída · 🔴 bloqueada · ⏸️ pausada

**Regras de atualização:**

1. Ao terminar uma sessão, marque os checkboxes concluídos e atualize o painel (seção 3).
2. Toda decisão relevante vai para o **Registro de decisões** (seção 10).
3. Todo uso substantivo de IA vai para o **Registro de uso de IA** (seção 11).
4. Referências só saem do status "a verificar" depois de conferidas na fonte primária (seção 13).
5. Mantenha separado o que é **resultado** (dado, experimento, fonte verificada) do que é **hipótese** (interpretação, analogia, aposta). Use as marcas `[FATO]` e `[HIPÓTESE]` quando houver risco de confusão.
6. Incremente a versão e registre a mudança no **Changelog** (seção 14).

---

## 3. Painel de fases

| # | Fase | Objetivo | Duração estimada | Status | Início | Fim | Entregável principal |
|---|---|---|---|---|---|---|---|
| 0 | Enquadramento e artefatos | Recuperar material original e montar o ambiente de trabalho | 1 semana | 🟢 | 21/09/2026 | 21/09/2026 | Acervo organizado + ambiente pronto |
| 1 | Revisão de literatura assistida por IA | Mapear 2008–2026 | 3–4 semanas (executada em 2 dias, multiagente) | 🟢 | 22/09/2026 | 23/09/2026 | 156 obras incluídas, 155 notas de leitura, 8 sínteses, `referencias.bib` com 133 obras, rascunho do capítulo 2 citável (83 chaves) |
| 2 | Auditoria da versão original | Classificar cada afirmação: mantém / reformula / descarta | 1–2 semanas (executada em 1 dia, multiagente) | 🟢 | 23/09/2026 | 23/09/2026 | 349 afirmações classificadas (265 mantém, 80 reformula, 4 descarta, após a revisão das 101 e a resolução das pendências), relatório de auditoria, nova taxonomia, plano de reexecução (31 itens), material do M1 |
| 3 | Infraestrutura e replicação experimental | Replicar e estender o experimento com método atual | 4–6 semanas | ⚪ | | | Dataset, código, resultados |
| 4 | Camada LLM | Posicionar LLMs no mapa das técnicas | 2–3 semanas | ⚪ | | | Resultados comparativos |
| 5 | Ponte para desenvolvimento de software dirigido por IA | Testar o princípio de ajuste no Ateliê | 6–8 semanas (piloto começa em paralelo à Fase 3) | ⚪ | | | Relatório do piloto + decisão sobre produto |
| 6 | Redação e compartilhamento | Nova versão do trabalho + conversa com o orientador | 3–4 semanas | ⚪ | | | Nova versão + material para o orientador |

**Duração total estimada:** 4 a 5 meses em dedicação parcial. Sem o apoio de IA, a estimativa seria de 9 a 12 meses.

### Marcos de conversa com o orientador

| Marco | Quando | O que levar | Status |
|---|---|---|---|
| M1 — Primeiro contato | Após Fase 2 | Diagnóstico da versão 2010 + perguntas de pesquisa revisadas | ⚪ |
| M2 — Resultados | Após Fases 3–4 | Resultados da replicação e da camada LLM | ⚪ |
| M3 — Nova versão | Fim da Fase 6 | Texto completo + ponte com desenvolvimento de software | ⚪ |

---

## 4. Diagnóstico da versão de 2010

### O que continua válido

- A pergunta de pesquisa: nenhum planejador é o melhor em todos os domínios, e características do domínio podem indicar a técnica mais promissora. `[FATO]` A área desenvolveu exatamente essa linha depois de 2010, sob o nome de *seleção de algoritmos* e *portfólios de planejadores*.
- A intuição de que desempenho é uma questão de **ajuste entre problema e técnica**.
- Os trabalhos futuros propostos em 2010 (extração automática de métricas, pesos, aprendizado indutivo, domínios artificiais) foram, em grande parte, realizados pela comunidade.

### Fragilidades a tratar

| # | Fragilidade | Onde aparece | Tratamento na revisão |
|---|---|---|---|
| F1 | Lacunas de revisão já em 2010: Rice (1976), Roberts & Howe (c. 2008–2009), IPC 2008 e LAMA | Cap. 2 | Fase 1 |
| F2 | Amostra pequena: 10 planejadores × 10 domínios, 3 domínios de validação | Cap. 3–5 | Fase 3 |
| F3 | Métricas UML medem o modelo, não o problema; dependem do modelador (ex.: classe *Utility* no Depots); contagem manual | Cap. 4 | Fase 3 (extração automática + teste de robustez) |
| F4 | Taxonomia de técnicas discutível: SATPLAN/MAXPLAN como *plan-space*, planejadores SAT como *forward-chaining*; técnicas coocorrem e não são separáveis por média | Cap. 3 | Fase 2 |
| F5 | Eficiência reduzida a cobertura; tempo e qualidade do plano excluídos | Cap. 5 | Fase 3 |
| F6 | Parte dos dados obtida fora das competições, com condições de execução possivelmente diferentes | Cap. 5.1.1 | Fase 2 (documentar) + Fase 3 (reexecutar) |
| F7 | Discretização Alto/Médio/Baixo por variância com poucos pontos | Cap. 4.3 | Fase 3 |

---

## 5. Perguntas de pesquisa (revisadas)

| # | Pergunta | Tipo | Fase |
|---|---|---|---|
| Q1 | As conclusões de 2010 se sustentam com mais planejadores, mais domínios e método estatístico adequado? | Replicação | 3 |
| Q2 | Métricas estruturais de modelagem, no estilo orientado a objetos, acrescentam poder preditivo às *features* modernas extraídas de PDDL? | Continuidade | 3 |
| Q3 | Onde os LLMs entram no mapa: como técnica de planejamento, como tradutores de domínio ou como seletores? | Atualização | 4 |
| Q4 | O princípio de ajuste entre características da tarefa e estratégia de solução ajuda a escolher configurações de agentes de IA no desenvolvimento de software? | Transferência | 5 |

**Observação sobre Q4.** As métricas usadas em 2010 para diagramas de classes e de estados (Genero & Piattini; In, Kim & Barry) vieram da **engenharia de software**. No desenvolvimento de software essas métricas estão em seu terreno de origem, o que torna a ponte da Fase 5 mais natural do que parece à primeira vista. `[HIPÓTESE]`

---

## 6. Princípios de uso de IA no projeto

1. **Nenhuma referência entra sem verificação na fonte primária.** LLMs inventam citações plausíveis.
2. **Nenhum número entra no texto sem vir de execução reprodutível** (script versionado + dados + configuração).
3. **Registrar ferramenta, modelo, versão e finalidade** de todo uso substantivo (seção 11). Isso protege a transparência ao compartilhar o trabalho.
4. **A IA propõe, o autor decide.** Escolhas de método, interpretação e conclusões são humanas.
5. **Congelar versões** de modelos usados em experimentos (Fase 4) e registrar datas, porque os resultados mudam com novas versões.
6. **Texto final na voz do autor.** Rascunhos gerados por IA são material de trabalho, não texto final.

### Ferramentas previstas

| Uso | Ferramentas candidatas |
|---|---|
| Busca e triagem de literatura | Claude (pesquisa avançada), Semantic Scholar, Google Scholar, Elicit, Connected Papers |
| Leitura e extração estruturada de artigos | Claude com projetos e arquivos, NotebookLM |
| Código, infraestrutura e experimentos | Claude Code, Fast Downward, Downward Lab, Unified Planning, contêineres (Apptainer/Docker) |
| Análise de dados | Python (pandas, scikit-learn), notebooks |
| Base de conhecimento e rastreabilidade | Notas de leitura em Markdown no repositório (`literatura/notas-de-leitura/`), referências em BibTeX no repositório, aprovadas pelo autor em `literatura/referencias/revisao-referencias.md` (sem Zotero desde 23/09/2026); texto em Markdown, convertido com Pandoc |
| Redação e revisão | Claude com as skills de estilo autoral, revisão humana; formatação, citações e referências no padrão ABNT (ver `redacao/README.md`) |

---

## 7. Fases detalhadas

### Fase 0 — Enquadramento e recuperação de artefatos

**Objetivo:** reunir o material original e preparar o ambiente para as fases seguintes.

**Atividades**

- [x] Extrair o texto da dissertação e mapear capítulos, tabelas e figuras
- [x] Localizar os modelos originais do itSIMPLE (UML.P) dos 13 domínios (10 de treino + Storage, Zeno-travel, Elevator) — **13 de 13 identificados** (`data/2010/modelos_itsimple_2010.csv`); Pathways e TPP pelas figuras, com discrepância na tabela (G11, G12)
- [x] Localizar planilhas com métricas, discretização e notas de eficiência (Tabelas 8–25) — mapeadas; **não existe planilha com as contagens brutas das métricas** (só dissertação e SQL discretizado)
- [x] Documentar como foram obtidos os dados da 5ª etapa do método (execuções fora das competições): máquina, limite de tempo, versões — `auditoria/condicoes-de-execucao-2010.md`; restam lacunas listadas lá
- [x] Transcrever as tabelas da dissertação para CSV (dataset "2010") — feito por extração automática do docx, conferido contra o SQL; conferência manual pelo autor concluída em 21/09/2026
- [x] Criar repositório (código + dados + este documento)
- [x] ~~Criar estrutura no vault do Obsidian para notas de leitura~~ — **cancelado**: o Obsidian não será usado neste projeto (decisão do autor, 21/09/2026). As notas de leitura ficam no repositório, em `literatura/notas-de-leitura/`
- [x] Definir o formato da nova versão — **dissertação revisada, padrão ABNT** (decisão do autor, 21/09/2026); ver `redacao/README.md`
- [x] Conferência manual do dataset de 2010 pelo autor — concluída em 21/09/2026

**Como a IA acelera:** transcrição das tabelas para CSV, criação da estrutura do repositório e de *templates* de notas.

**Entregáveis:** repositório criado · dataset de 2010 (conjunto de CSVs em `data/2010/`, em vez de um único `dataset-2010.csv`) · acervo original catalogado

**Critério de conclusão:** dados de 2010 disponíveis em formato processável e ambiente pronto.

**Notas:**

- 21/09/2026 — Catálogo do acervo em [docs/catalogo-acervo-2010.md](../docs/catalogo-acervo-2010.md).
- 21/09/2026 — **Dataset de 2010** em [data/2010/](../data/2010/README.md), gerado por scripts a partir das tabelas do docx (44 tabelas extraídas 1:1 com a numeração das legendas). Conferência contra `comp/script.sql`: 170/170 classes, 100/100 eficiências e 100/100 notas iguais; Tabela 4 = matriz das Tabelas 2–3. O SQL é uma concatenação com blocos repetidos e uma versão anterior da taxonomia de técnicas, então **não é fonte de verdade**.
- 21/09/2026 — **Condições de execução (F6)** respondidas em `auditoria/condicoes-de-execucao-2010.md`: 8 máquinas Core 2 Duo 2,5 GHz / 4 GB / Ubuntu 9.04, timeout de 20 min, ~2.000 execuções. 38 dos 100 pares de treino vêm de competição e 62 de execução própria.
- 21/09/2026 — **Modelos itSIMPLE:** 11 de 13 batem 4/4 nas métricas comparáveis (com exclusão das classes auxiliares `Utility`/`Global`). Pathways e TPP foram identificados comparando as Figuras 26 e 27 da dissertação com o XML: figura e XML concordam entre si e discordam da tabela (Pathways: 4 associações contra 2; TPP: 2 generalizações contra 4).
- 21/09/2026 — 10 achados para a auditoria em `auditoria/achados-fase0.md` (rótulo invertido de "casos de uso por atores", exclusão de classes auxiliares, Elevator inconsistente, entre outros).
- 21/09/2026 — **Benchmarks:** os PDDL do acervo foram identificados nas IPCs 1998–2008 (`potassco/pddl-instances`, commit `cf19edf`): 10 domínios 100% idênticos, Gripper 19/20 equivalentes (gerado localmente). Zeno-travel (IPC 2002) e Elevator (IPC 2000) existem no repositório; **variantes confirmadas pelo autor** (`zenotravel-strips-automatic`, `elevator-strips-simple-typed`; `automatic` e `typed` por consistência); **N = 20 nos dois, definido pelo autor** (Elevator: as 20 primeiras, por analogia com os demais). Ver `docs/benchmarks-ipc-ate-2008.md` e `data/2010/benchmarks_ipc_mapa_final.csv`.
- 21/09/2026 — **Correções aprovadas pelo autor** (Pathways/Associações 4→2; TPP/Generalização 2→4), em `data/2010/correcoes_2010.csv`. As classes Alto/Médio/Baixo devem ser recalculadas na Fase 3.
- Zeno-travel e Elevator não têm PDDL no acervo, só modelos UML.

---

### Fase 1 — Revisão de literatura assistida por IA (2008–2026)

**Objetivo:** reconstruir o capítulo de fundamentos e o estado da arte.

**Eixos de busca**

| Eixo | Tópicos | Status |
|---|---|---|
| E1 | Seleção de algoritmos e portfólios em planejamento (Rice; PbP; Fast Downward Stone Soup; IBaCoP; Delfi; Cedalion) | 🟢 21 obras |
| E2 | *Features* de tarefas de planejamento e predição de desempenho (Roberts & Howe; Fawcett et al.; representações em grafo) | 🟢 15 obras |
| E3 | Evolução dos planejadores e heurísticas (LAMA, LM-cut, *merge-and-shrink*, busca simbólica, BFWS, Madagascar) e resultados das IPCs 2008–2023 | 🟢 18 obras |
| E4 | Aprendizado para planejamento (heurísticas aprendidas, ASNets, GNNs, planejamento generalizado, aprendizado de modelos de ação) | 🟢 17 obras |
| E5 | LLMs e planejamento (PlanBench; LLM+P; LLM-Modulo; modelos de raciocínio; agentes) | 🟢 20 obras |
| E6 | Engenharia do conhecimento para planejamento (evolução do itSIMPLE, ICKEPS, Unified Planning, LLMs gerando PDDL) | 🟢 24 obras |
| E7 | Pontes conceituais (No Free Lunch; teoria da contingência; *task-technology fit*; roteamento de modelos de linguagem) | 🟢 20 obras |
| E8 | IA no desenvolvimento de software (agentes de código, SWE-bench e similares, estratégias de orquestração, estudos empíricos em equipes) | 🟢 20 obras |

**Atividades**

- [x] Definir protocolo leve: *strings* de busca, bases, critérios de inclusão/exclusão — `literatura/protocolo/protocolo-busca.md` (v1.1)
- [x] Rodar buscas por eixo com apoio de IA e montar lista bruta — 344 registros, 317 obras únicas, mais busca dirigida de 5 lacunas
- [x] Triagem por título e resumo — 156 incluídas; confirmação delegada pelo autor ao Coordenador (critérios no protocolo, seção 9)
- [x] Verificar metadados no registro primário — 156 verificadas em `candidatas.bib`; **133 aprovadas no `referencias.bib`** (sem Zotero, decisão de 23/09/2026)
- [x] Leitura com extração estruturada — 153 notas (91 de texto integral, 62 de resumo)
- [x] Produzir síntese por eixo — 8 sínteses, 17.785 palavras, todas as notas citadas
- [x] Redigir rascunho do novo capítulo de fundamentos — `redacao/capitulos/02-fundamentos.md` (rascunho de IA, revisado por parecer adversarial)

**Como a IA acelera:** geração de *strings* de busca, triagem inicial, extração estruturada de artigos, primeiras sínteses por eixo. Estimativa de redução: de 6–8 para 3–4 semanas.

**Entregáveis:** `referencias.bib` aprovado pelo autor · notas de leitura no repositório · síntese por eixo · rascunho do capítulo

**Critério de conclusão:** todos os eixos com síntese e todas as referências citadas verificadas.

**Notas:** executada em 22–23/09/2026 por equipe multiagente (`plan/fase1-estrategia-multiagentes.md`). Relatório: `literatura/relatorio-fase1.md`. Controle de qualidade: `literatura/protocolo/qc-coordenador.md`. Insumos para a Fase 2: `auditoria/insumos-fase1.md`. **Critério de conclusão cumprido em 23/09/2026:** todos os eixos têm síntese, e todas as 83 referências citadas no capítulo estão no `referencias.bib`. Por decisão do autor, o critério vale para o capítulo; as sínteses são material de trabalho (ver `literatura/sinteses/README.md`).

---

### Fase 2 — Auditoria da versão original

**Objetivo:** classificar criticamente as afirmações da dissertação. Esta fase pode rodar em paralelo à Fase 1.

**Atividades**

- [x] Extrair todas as afirmações substantivas (IA gera a lista, autor revisa) — 349 em `auditoria/afirmacoes.csv`; **revisão do autor pendente**
- [x] Classificar cada uma: **mantém / reformula / descarta**, com justificativa — `auditoria/relatorio-auditoria.md`
- [x] Revisar a taxonomia de técnicas (F4) e propor uma nova, compatível com a literatura atual — `auditoria/taxonomia-tecnicas.md`
- [x] Documentar condições de obtenção dos dados (F6) — `auditoria/condicoes-de-execucao-2010.md`, com a resposta do autor sobre o corte de instâncias
- [x] Listar o que precisa ser reexecutado na Fase 3 — `auditoria/reexecucao.md`
- [x] Preparar material para o **Marco M1** com o orientador — `auditoria/m1-orientador.md` (rascunho)

**Tabela de auditoria**

Movida para `auditoria/afirmacoes.csv` (349 afirmações, IDs AF-NNN). A tabela semente que ficava aqui (A1–A4, numeração antiga) corresponde às conclusões de 2010, rotuladas A1–A5 na Fase 1 (`literatura/protocolo/instrucoes-leitura.md`, seção 1); o veredito de cada uma está em `auditoria/relatorio-auditoria.md`, seção 6.

**Entregáveis:** relatório de auditoria · nova taxonomia de técnicas

**Critério de conclusão:** todas as afirmações classificadas e plano de reexecução definido.

**Notas:**

---

### Fase 3 — Infraestrutura e replicação experimental

**Objetivo:** responder Q1 e Q2 com amostra ampla, extração automática e método estatístico adequado.

**Desenho**

- **Domínios:** *benchmarks* das IPCs 1998–2023 (clássico, determinístico).
- **Planejadores:** os originais que ainda puderem ser executados + planejadores atuais (imagens das IPCs quando disponíveis).
- **Condições:** mesmo hardware, mesmo limite de tempo e memória para todos.
- **Medidas de desempenho:** cobertura, tempo, qualidade do plano, escore IPC.
- **Conjuntos de *features*:**
  - (a) métricas de 2010 calculadas automaticamente a partir do PDDL (ex.: hierarquia de tipos → classes e DIT; ações → casos de uso; predicados → associações e atributos);
  - (b) *features* modernas extraídas do PDDL/SAS+;
  - (c) combinação de (a) e (b).
- **Modelos de seleção:** *random forest*, *gradient boosting* e, como linha de base, o ranking por médias usado em 2010.
- **Validação:** *leave-one-domain-out*; comparação com o melhor planejador único (*single best*) e com o oráculo (*virtual best*).

**Atividades**

- [ ] Montar ambiente de execução em contêineres
- [ ] Baixar e organizar *benchmarks*
- [ ] Compilar e testar planejadores
- [ ] Implementar extrator das métricas de 2010 a partir do PDDL
- [ ] Validar o extrator contra as contagens manuais de 2010 (dataset da Fase 0)
- [ ] Implementar ou reutilizar extrator de *features* modernas
- [ ] Rodar experimentos
- [ ] Reproduzir o método de 2010 sobre os dados novos (linha de base)
- [ ] Treinar e avaliar modelos de seleção
- [ ] Testar robustez das métricas UML a variações de modelagem (F3)
- [ ] Analisar importância das *features* e responder Q1 e Q2

**Como a IA acelera:** Claude Code para infraestrutura, scripts de execução, extratores e análise. A IA escreve o código; o autor valida resultados e decisões de método. Estimativa de redução: de 8–12 para 4–6 semanas.

**Entregáveis:** repositório com código e dados · resultados · respostas a Q1 e Q2

**Critério de conclusão:** experimentos reprodutíveis a partir do repositório e resultados analisados.

**Notas:**

---

### Fase 4 — Camada LLM

**Objetivo:** responder Q3.

**Experimentos**

| # | Experimento | Pergunta | Status |
|---|---|---|---|
| X1 | LLM como planejador | Qual é o desempenho do LLM em relação aos planejadores clássicos num subconjunto de domínios? | ⚪ |
| X2 | LLM como tradutor | O LLM gera PDDL correto a partir de descrição em linguagem natural? Com que taxa de erro? | ⚪ |
| X3 | LLM como seletor | Dada a descrição do domínio, o LLM escolhe bem o planejador? Comparar com o seletor da Fase 3 | ⚪ |
| X4 | LLM + verificador | Arquitetura com validador formal (ex.: VAL) melhora X1? | ⚪ |

**Atividades**

- [ ] Selecionar subconjunto de domínios
- [ ] Definir modelos e congelar versões
- [ ] Rodar X1–X4 com registro de custos e *prompts*
- [ ] Analisar e posicionar LLMs no mapa das técnicas

**Entregáveis:** resultados X1–X4 · resposta a Q3

**Critério de conclusão:** os quatro experimentos executados e registrados.

**Notas:**

---

### Fase 5 — Ponte para desenvolvimento de software dirigido por IA

**Objetivo:** responder Q4 com um piloto no Ateliê de Software e decidir se há base para um produto.

**Analogia de trabalho** `[HIPÓTESE]`

| Planejamento automático (2010) | Desenvolvimento de software dirigido por IA |
|---|---|
| Domínio de planejamento | Tarefa de desenvolvimento (história, bug, refatoração) no contexto de um repositório |
| Características do domínio | Tamanho da mudança, clareza da especificação, cobertura de testes, acoplamento, idade do código, novidade do domínio de negócio, métricas estruturais do código |
| Técnica de planejamento | Configuração do agente: modelo, planejar-antes-de-executar ou execução direta, ciclo com testes, subagentes, grau de supervisão humana |
| Planejador | Combinação de ferramenta + modelo + estratégia |
| Eficiência (problemas resolvidos) | Tarefa aceita, retrabalho, tempo, custo, defeitos posteriores |
| Ranking de planejadores | Recomendação de configuração para uma nova tarefa |

**Hipóteses do piloto**

- **H1:** nenhuma configuração de agente é a melhor para todos os tipos de tarefa.
- **H2:** características observáveis da tarefa e do repositório ajudam a prever qual configuração tende a funcionar melhor.
- **H3:** métricas estruturais do código, derivadas das mesmas famílias usadas em 2010, contribuem para essa previsão.

**Atividades**

- [ ] Conversar com a equipe do Ateliê sobre o piloto e obter adesão (coerente com a cultura de autogestão)
- [ ] Definir as características da tarefa a registrar e como coletá-las (automaticamente quando possível)
- [ ] Definir as configurações de agente a comparar
- [ ] Definir as medidas de resultado
- [ ] Rodar o piloto com 50–100 tarefas reais ao longo de algumas semanas
- [ ] Analisar H1–H3
- [ ] Levantar soluções existentes de roteamento e orquestração de agentes
- [ ] Decidir: **adotar internamente / seguir experimentando / avaliar produto / arquivar**

**Critérios para considerar um produto** (todos precisam ser atendidos)

- [ ] H1 e H2 com evidência consistente no piloto
- [ ] Ganho mensurável de tempo, custo ou qualidade em relação à configuração padrão
- [ ] Diferencial claro em relação a soluções existentes
- [ ] Interesse validado com pelo menos algumas equipes fora do Ateliê

**Entregáveis:** protocolo do piloto · dados · relatório · decisão registrada

**Critério de conclusão:** piloto analisado e decisão registrada na seção 10.

**Notas:**

---

### Fase 6 — Redação e compartilhamento

**Objetivo:** produzir a nova versão e compartilhar com o orientador.

**Formato (definido em 21/09/2026):** dissertação revisada, seguindo o padrão ABNT de formatação, citações e referências, e as boas práticas e recomendações acadêmicas do Brasil. Detalhes, normas, retrato da versão de 2010 e opções de ferramenta em [redacao/README.md](../redacao/README.md).

**Estrutura proposta da nova versão** (ponto de partida; o autor liberou reorganizar, ampliar e criar conteúdo novo: ver seção 10)

1. Introdução — a pergunta em 2010 e hoje
2. Fundamentos e estado da arte
3. Revisitando 2010 — auditoria
4. Método
5. Resultados experimentais
6. LLMs no mapa das técnicas
7. Do domínio de planejamento ao desenvolvimento de software dirigido por IA
8. Conclusões e próximos passos

**Atividades**

- [ ] Validar a conversão do Markdown para o documento final ABNT (Pandoc, estilo CSL, modelo de referência) e decidir a montagem final; ver `redacao/README.md`
- [ ] Conferir a edição vigente das normas ABNT e o manual de normalização da FEI
- [ ] Redigir capítulos a partir dos entregáveis das fases anteriores
- [ ] Revisão de consistência (IA aponta inconsistências entre capítulos, dados e referências)
- [ ] Verificação final de todas as referências e números
- [ ] Revisão de estilo na voz do autor
- [ ] Elementos pré e pós-textuais (capa, folha de rosto, folha de aprovação, resumo e *abstract*, listas, sumário, referências) e conferência de formatação, citações e referências pela ABNT
- [ ] Declaração do uso de IA no texto, conforme as regras da instituição
- [ ] Preparar resumo executivo para o orientador
- [ ] Enviar ao orientador (**Marco M3**)
- [ ] Registrar retorno e próximos passos

**Entregáveis:** dissertação revisada (padrão ABNT) · resumo executivo · registro do retorno do orientador

**Critério de conclusão:** versão enviada e retorno registrado.

**Notas:**

---

## 8. Riscos

| # | Risco | Probabilidade | Impacto | Mitigação |
|---|---|---|---|---|
| R1 | Expansão de escopo (a Fase 5 pode virar um projeto próprio; o autor liberou ampliar a revisão para além de 2010) | Alta | Alto | Manter o piloto enxuto; decisões de produto só depois do piloto; **registrar cada expansão na seção 10 com motivo e fase afetada** |
| R2 | Referências inventadas ou erradas por IA | Alta | Alto | Princípio 1; verificação obrigatória na seção 13 |
| R3 | Volatilidade dos LLMs torna resultados obsoletos | Alta | Médio | Congelar versões e datar resultados |
| R4 | Planejadores antigos não compilam | Média | Médio | Usar imagens das IPCs; registrar o que não foi possível reproduzir |
| R5 | Custo computacional | Média | Médio | Subconjunto representativo de domínios; limites de tempo definidos |
| R6 | Confusão entre analogia e evidência na Fase 5 | Média | Alto | Marcas `[FATO]`/`[HIPÓTESE]`; conclusões só a partir dos dados do piloto |
| R7 | Piloto atrapalhar a rotina do Ateliê | Média | Médio | Coleta automática sempre que possível; adesão voluntária da equipe |

---

## 9. Próximas ações

| # | Ação | Fase | Responsável | Prazo | Status |
|---|---|---|---|---|---|
| 1 | Localizar modelos do itSIMPLE e planilhas originais | 0 | Matheus + IA | | 🟢 concluída (13 de 13 modelos; planilhas mapeadas) |
| 2 | Transcrever tabelas da dissertação para CSV | 0 | IA + conferência de Matheus | 21/09/2026 | 🟢 concluída e conferida |
| 3 | Criar repositório | 0 | Matheus + IA | 21/09/2026 | 🟢 concluída (Obsidian descartado) |
| 4 | Definir protocolo de busca da Fase 1 | 1 | Matheus + IA | 22/09/2026 | 🟢 concluída (v1.1, com o critério X7) |
| 5 | Decidir o formato da nova versão | 0 | Matheus | 21/09/2026 | 🟢 dissertação revisada, ABNT |
| 6 | Decidir onde rodar os experimentos da Fase 3 (Linux/x86) | 3 | Matheus | antes da Fase 3 | ⚪ |
| 7 | Validar a conversão Markdown → Pandoc → documento ABNT | 1, 6 | Matheus + IA | 23/09/2026 | 🟡 Pandoc 3.11 instalado; corpo e referências convertem, inclusive no capítulo inteiro (`redacao/teste-abnt/relatorio-teste.md`). Falta: escolher a variante do CSL (a genérica não imprime o nome do evento; a UFPR imprime), conferir a caixa alta da NBR 10520 e testar os elementos pré-textuais |

| 8 | Confirmar a triagem da Fase 1 | 1 | Coordenador (delegado pelo autor) | 23/09/2026 | 🟢 122 confirmadas, 29 com ressalva, 3 não citáveis (não lidas), GIPO excluído; critérios no protocolo, seção 9 |
| 9 | Revisar as referências e gerar o `referencias.bib` | 1, 6 | Matheus + Coordenador | 23/09/2026 | 🟢 **129 obras citáveis**: as 122 confirmadas aprovadas pelo autor, 5 ressalvas com ≥ 50 citações e 2 confirmadas a partir dos PDFs do autor. O capítulo 2 tem 14 chaves não citáveis a substituir ou retirar |
| 10 | Obras sem acesso | 1 | Matheus | 23/09/2026 | 🟢 `nunez2015automatic` e `tonidandel2006reading` lidas a partir dos PDFs do autor; `strobel2014planning` acrescentada; só `sette2008are` segue sem leitura (não citável). GIPO excluído |
| 11 | Decidir as quatro questões da Fase 2 listadas em `auditoria/insumos-fase1.md`, seção 5 | 2 | Matheus | 23/09/2026 | 🟢 decididas (seção 10): taxonomia em 4 dimensões; análise por domínio e por instância; UML testada contra *features* de PDDL; itSIMPLE 2005 como origem da pergunta |
| 12 | Conversar com o Tonidandel sobre o artigo do itSIMPLE de 2005 como origem da pergunta | 2, 6 | Matheus | | ⚪ entra no Marco M1 (o artigo de 2006 já foi lido a partir do PDF do autor) |
| 13 | Revisar a auditoria: ler primeiro as afirmações "reformula" e "descarta" de `auditoria/afirmacoes.csv` | 2 | Matheus + Coordenador | antes do M1 | 🟢 revisão do Coordenador por delegação do autor (`auditoria/relatorio-auditoria.md`, seções 9 e 10); leitura humana recomendada antes da redação |
| 14 | Revisar e enviar o material do Marco M1 (`auditoria/m1-orientador.md`) | 2 | Matheus | | ⚪ |
| 15 | Aprovar as fontes novas da Fase 2 no `referencias.bib` | 2, 6 | Coordenador (delegado pelo autor) | 23/09/2026 | 🟢 17 promovidas (11 da Fase 2 + 6 da resolução de pendências); `referencias.bib` com 150 obras |
| 16 | Conferir na fonte as afirmações com ação "CONFERIR" | 2, 6 | Coordenador | 23/09/2026 | 🟢 nenhuma restante; 16 de confiança baixa com decisão registrada (retirar, parafrasear ou tratar como hipótese) |
| 17 | Esclarecer a origem dos 4 valores de "competição" impossíveis (G21) | 2, 3 | Coordenador | 23/09/2026 | 🟢 vieram dos logs de execução própria de 2010; são 34 pares de competição e 66 de execução própria |
| 18 | Incluir os relatórios oficiais das IPCs no `candidatas.bib` | 2, 6 | Coordenador | 23/09/2026 | 🟢 incluídos e promovidos, com Bonet e Geffner (2001) e Weld (1994) |

---

## 10. Registro de decisões

| Data | Decisão | Motivo | Fase |
|---|---|---|---|
| 21/09/2026 | Propósito da revisão: evoluir o trabalho; compartilhamento com o orientador e aplicação no Ateliê como desdobramentos possíveis | Definição do autor | 0 |
| 21/09/2026 | Usar IA para acelerar todas as fases, com verificação humana obrigatória | Definição do autor | 0 |
| 21/09/2026 | Q4 direcionada ao desenvolvimento de software dirigido por IA | Interesse de aplicação no Ateliê | 0 |
| 21/09/2026 | Repositório privado `mhaddad/mestrado-dominios-planejamento`, com estrutura por fase; acervo de 2010 em `acervo-2010/`, somente leitura | Separar material original do trabalho derivado; preservar rastreabilidade | 0 |
| 21/09/2026 | Versionar o acervo de 2010 inteiro (cerca de 73 MB compactado), exceto `.svn`, `.o`, `.pyc` e `.DS_Store` | Cabe no GitHub sem LFS; os arquivos `*~` guardam scripts de execução úteis para documentar F6 | 0 |
| 21/09/2026 | Benchmarks das IPCs e saídas brutas de execução não serão versionados (baixados/gerados por script) | Grandes e reproduzíveis | 0 |
| 21/09/2026 | A revisão **não precisa manter a estrutura e o conteúdo de 2010**: pode ampliar e criar conteúdo novo. Cada expansão de escopo é registrada nesta seção | Definição do autor; controla o risco R1 sem impedir a evolução | 1–6 |
| 21/09/2026 | O Obsidian não será usado no projeto; as notas de leitura ficam no repositório | Definição do autor | 0 |
| 21/09/2026 | Formato da nova versão: dissertação revisada, padrão ABNT de formatação, citações e referências, e boas práticas acadêmicas brasileiras | Definição do autor | 0, 6 |
| 21/09/2026 | Padrão ABNT **sem LaTeX** (abnTeX2 descartado) | Esclarecimento do autor | 6 |
| 21/09/2026 | **Corpo do texto em Markdown no repositório, com o `.bib` do Zotero** (conversão com Pandoc). Só se cita chave existente no `.bib` verificado. Montagem final (Pandoc direto × acabamento no Word) a validar em teste na Fase 1 | Decisão do autor | 1, 6 |
| 21/09/2026 | Variantes de 2010: Zeno-travel = IPC 2002 `zenotravel-strips-automatic`; Elevator = IPC 2000 `elevator-strips-simple-typed` (mais os 11 domínios identificados por conteúdo) | Autor confirmou as variantes identificadas; `automatic` e `typed` por consistência com os demais domínios | 0, 3 |
| 21/09/2026 | Dataset de 2010 (incluindo as correções de Pathways e TPP) considerado conferido | Conferência manual do autor | 0 |
| 21/09/2026 | Zeno-travel e Elevator: N = 20 instâncias cada (Zeno: conjunto inteiro; Elevator: as 20 primeiras de 150) | Definição do autor; leitura "20 primeiras" por analogia com o padrão do acervo | 0, 3 |
| 21/09/2026 | Usar as contagens tiradas das figuras (Pathways/Associações = 2; TPP/Generalização = 4) como valores corrigidos, preservando o publicado | Autor conferiu as figuras e aprovou | 0 |
| 21/09/2026 | O repositório `potassco/pddl-instances` (commit `cf19edf`) é a fonte dos benchmarks das IPCs até 2014; edições posteriores a definir | Indicado pelo autor; cobre os domínios da dissertação | 0, 3 |
| 21/09/2026 | Manter memória de execução em `MEMORY.md` na raiz, para retomada entre sessões e entre agentes | Fases 1–6 serão executadas em sessões separadas | 0 |
| 21/09/2026 | Fonte de verdade do dataset de 2010 = tabelas publicadas na dissertação; `script.sql` e planilhas só para conferência | O SQL tem blocos repetidos, versão anterior da taxonomia e fragmento truncado | 0 |

| 22/09/2026 | Executar a Fase 1 com equipe de agentes: Coordenador em Opus 5 para planejamento, controle de qualidade e decisões; subagentes em Sonnet 5 para busca, triagem, verificação, leitura, síntese e redação. Autonomia ponta a ponta, com tudo marcado como pendente de confirmação | Definição do autor; estratégia em `plan/fase1-estrategia-multiagentes.md` | 1 |
| 22/09/2026 | Metadados verificados por agente no registro primário entram em `literatura/referencias/candidatas.bib`, **nunca** em `referencias.bib`; só o autor, via Zotero, promove uma referência | Preserva a regra de que só obra verificada é citável, sem travar o trabalho dos agentes | 1, 6 |
| 22/09/2026 | Critério de exclusão **X7** (relevante, mas redundante diante do teto do eixo), acrescentado ao protocolo v1.1 | Os triadores vinham usando X2 e X6 para redundância, o que distorcia o registro | 1 |
| 23/09/2026 | Reverter a exclusão do artigo do itSIMPLE de 2005 (`vaquero2005itsimple`) e tratá-lo como obra de prioridade A | A leitura do PDF fornecido pelo autor mostrou que ele declara, em 2005, o objetivo que a dissertação executou em 2010 | 1, 2 |
| 23/09/2026 | Usar a variante UFPR do CSL da ABNT como padrão de trabalho até decisão final | A variante genérica não imprime o nome do evento em trabalhos de conferência, e boa parte do corpus é de anais | 1, 6 |

| 23/09/2026 | **Confirmação da triagem delegada ao Coordenador**, com critérios acadêmicos padrão: revisão por pares, impacto (percentil de citação normalizado), peso do veículo, ausência de retratação e leitura efetiva. Resultado: 122 confirmadas, 29 com ressalva, 3 não citáveis até serem lidas | Definição do autor; critérios no protocolo, seção 9 | 1 |
| 23/09/2026 | **Sem Zotero.** O autor revisa as referências em `literatura/referencias/revisao-referencias.md`; o script `promover_referencias.py` gera o `referencias.bib` a partir das marcas. Substitui a parte do Zotero na decisão de 21/09/2026 sobre o `.bib` | Zotero não instalado; decisão do autor | 1, 6 |
| 23/09/2026 | GIPO (2001) excluído: sem fonte primária e coberto por `simpson2007planning` | Decisão do autor | 1 |
| 23/09/2026 | `vallati2016identifying` passa a ser citado na versão do ICAPS 2015 (`vallati2015identifying`), que foi a lida | Regra de citar a versão lida | 1 |

| 23/09/2026 | **Taxonomia de técnicas refeita em quatro dimensões** (algoritmo de busca, tipo de heurística, representação de estado, arquitetura do sistema), no lugar das seis categorias exclusivas de 2010. **Expansão de escopo** (risco R1): vira contribuição própria, a validar na Fase 3 | A taxonomia de 2010 não se sustenta contra a fonte primária (`auditoria/insumos-fase1.md`, A6); decisão do autor | 2, 3 |
| 23/09/2026 | **Análise em dois níveis, reportados separadamente:** por domínio (continuidade com 2010) e por instância (estado da arte), separando discriminação entre domínios de dificuldade dentro do domínio | A literatura migrou para a seleção por instância; A3 não se sustenta na forma de 2010; decisão do autor | 2, 3 |
| 23/09/2026 | **Métricas UML mantidas como objeto de teste, comparadas com *features* automáticas de PDDL** (grafo causal, DTG) nos mesmos domínios, com controle da ordem de serialização do modelo. Resposta direta à Q2; resultado negativo também é resultado | Lacuna confirmada por busca dirigida (nenhum trabalho compara as duas); decisão do autor | 2, 3 |
| 23/09/2026 | **O artigo do itSIMPLE de 2005 é assumido como origem da pergunta** da dissertação, que passa a ser apresentada como a primeira execução de um objetivo do projeto itSIMPLE. Conversar com o Tonidandel (coautor do artigo e orientador original) | O artigo declara em 2005 o objetivo que a dissertação executou e não foi citado em 2010; decisão do autor | 2, 6 |

| 23/09/2026 | **Das obras com ressalva, promover só as muito citadas**; o Coordenador fixou o corte em ≥ 50 citações (maior valor entre OpenAlex e Semantic Scholar), o mesmo limite já usado para *preprints*. Obras sem contagem nas duas bases não sobem | Decisão do autor; limite do Coordenador | 1, 6 |
| 23/09/2026 | Veredito do A3 revisto de "descarta" para "reformula" depois da leitura de `nunez2015automatic` | A configuração por domínio continua competitiva quando há treino no domínio | 2 |

| 23/09/2026 | `tonidandel2006reading` promovido ao `referencias.bib` como exceção à regra de citações (1 citação registrada) | Decisão do autor: obra do orientador original, que define a UML.P usada nas métricas de 2010 | 1, 2 |

| 23/09/2026 | Stone Soup, Delfi e Cedalion (`helmert2011fast`, `katz2018delfi`, `seipp2014fast`) promovidos ao `referencias.bib` por exceção à regra de citações | Decisão do autor: são as referências padrão desses planejadores; não têm contagem nas bases por serem resumos de planejadores da IPC | 1 |
| 23/09/2026 | O critério de conclusão da Fase 1 ("todas as referências citadas verificadas") vale para o capítulo, não para as sínteses, que são material de trabalho | Decisão do autor | 1 |
| 23/09/2026 | Rascunho do capítulo 2 ajustado para citar só obras do `referencias.bib`: 11 chaves trocadas por obras citáveis ou retiradas com a afirmação correspondente; Fase 1 concluída | Critério de conclusão da fase | 1 |

| 23/09/2026 | Fase 2 executada com a mesma abordagem multiagente da Fase 1, com modelos mais econômicos (Haiku 4.5) nas tarefas mecânicas; estratégia em `plan/fase2-estrategia-multiagentes.md` | Decisão do autor | 2 |
| 23/09/2026 | A taxa de acerto de 2010 é a coincidência exata de posição entre *ranking* previsto e real (G19); as variantes de agregação do `testes.ods` foram testadas e ficou a média das médias por simplicidade (G7); o corte das instâncias buscou igualar o subconjunto publicado da IPC (G14) | Respostas do autor | 2, 3 |
| 23/09/2026 | Na nova taxonomia, *Partial-order* e *Total-order* saem das técnicas e ficam como atributo do plano | Decisão do autor | 2 |
| 23/09/2026 | Demais escolhas da taxonomia (7 itens, `auditoria/taxonomia-tecnicas.md`, "Decisões"): *Knowledge-based* fora das dimensões, SGPlan como decomposição na Dimensão 1 e não como portfólio, "heurísticas aprendidas" e "grafo causal" como valores próprios, R em valor próprio, fonte de POCL a buscar | Decisão do Coordenador, a validar no M1 | 2 |
| 23/09/2026 | As Tabelas 2–4 de 2010 são descartadas e substituídas pela nova taxonomia; as Tabelas 18–25 serão recalculadas (Fase 3, R-06 e R-10) | Coerente com A6 e com as fontes primárias dos 10 planejadores | 2, 3 |
| 23/09/2026 | Regras de auditoria adotadas: trecho literal conferido por script; números derivados de tabela conferidos por script, não por agente; plausibilidade não é evidência (confiança baixa + "CONFERIR"); afirmação sobre obra citada em 2010 é conferida contra a obra que a lista de referências de 2010 indica | Falhas observadas nas Ondas 1–3 (`plan/fase2-estrategia-multiagentes.md`, seção 6) | 2 |

| 23/09/2026 | Revisão das 101 afirmações "reformula"/"descarta" feita pelo Coordenador a pedido do autor: números das IPCs conferidos nos relatórios oficiais e nos resultados brutos; 25 classificações alteradas (4 viram "descarta", 20 viram "mantém", AF-328 volta a "reformula"); achado G21 | Pedido do autor; fontes primárias das competições | 2 |

| 23/09/2026 | Pendências da auditoria resolvidas pelo Coordenador por delegação do autor: 17 referências promovidas ao `referencias.bib` pelo critério das exceções anteriores (fontes primárias de planejadores e competições); `cenamor2019insights` mantido fora; afirmações periféricas sem fonte são retiradas da versão revisada, citações diretas não conferidas viram paráfrase com fonte aprovada | Pedido do autor: "decidindo a partir do contexto do projeto [...] pelo mais coerente" | 2, 6 |
| 23/09/2026 | Os 4 pares do G21 vieram da execução própria de 2010 (logs no acervo): valores publicados preservados, origem corrigida na documentação e na Fase 3 (34 de competição, 66 de execução própria) | Evidência do acervo | 2, 3 |

---

## 11. Registro de uso de IA

| Data | Fase | Ferramenta / modelo | Finalidade | Verificação feita |
|---|---|---|---|---|
| 21/09/2026 | 0 | Claude | Leitura da dissertação, diagnóstico inicial e elaboração deste plano | Revisão do autor pendente |
| 21/09/2026 | 0 | Claude Code (claude-sonnet-5) | Reorganização do repositório, criação da estrutura por fase, templates e catálogo do acervo de 2010 (`docs/catalogo-acervo-2010.md`) | Contagens e achados conferidos por comando no disco; catálogo pendente de revisão do autor |
| 21/09/2026 | 0 | Claude Code (claude-sonnet-5) | Extração do texto e das 44 tabelas do docx; construção do dataset de 2010 em CSV; conferência contra `script.sql`, planilhas e XML do itSIMPLE; documentação das condições de execução; `MEMORY.md` | Conferência automática entre fontes independentes (SQL, planilha, XML); duas leituras iniciais erradas foram detectadas e corrigidas. **Conferência manual do autor pendente** |
| 21/09/2026 | 0 | Claude Code (claude-sonnet-5) | Leitura visual das Figuras 26 e 27 (diagramas de classes de TPP e Pathways) para identificar os modelos itSIMPLE; avaliação das pastas `itsimple-*` | Figuras lidas e conferidas contra o XML; contagens automáticas reproduzíveis por script. **Leitura visual das figuras: confirmada pelo autor em 21/09/2026** |
| 21/09/2026 | 0 | Claude Code (claude-sonnet-5) | Comparação de conteúdo entre os PDDL do acervo e o repositório `potassco/pddl-instances` (IPCs 1998–2008); construção do script e do documento | Correspondências verificadas por comparação de conteúdo e reproduzíveis por script (repositório externo em commit fixo). Variantes de Zeno-travel e Elevator: hipóteses, a confirmar |

| 22–23/09/2026 | 1 | Claude Code — Coordenador (claude-opus-5) + 45 execuções de subagentes (claude-sonnet-5) | Fase 1 inteira: protocolo, busca em 8 eixos, triagem, verificação de metadados, leitura e extração de 153 obras, 8 sínteses, rascunho do capítulo 2 e parecer crítico | Coordenador reconferiu: amostra de 32 itens da busca, todas as 115 entradas com DOI e as 19 do arXiv, 4 números centrais de notas nos PDFs originais e os 9 achados do parecer crítico. Registro completo em `literatura/protocolo/qc-coordenador.md`. **Conferência do autor pendente em tudo** |

| 23/09/2026 | 1 | Claude Code (claude-opus-5-5) | Tratamento das pendências da Fase 1: confirmação da triagem por critérios com dados do OpenAlex; resolução das duas notas com versão divergente; veículo do itSIMPLE 2005 confirmado no site oficial; limpeza mecânica do `candidatas.bib`; lista de revisão e script de promoção das referências | Critérios e resultado registrados no protocolo (seção 9) e em `triagem.csv`. **A revisão das referências é do autor** |

| 23/09/2026 | 1 | Claude Code (claude-opus-5-5) | Fechamento da Fase 1: leitura das obras enviadas pelo autor, contagem de citações das ressalvas (OpenAlex e Semantic Scholar), geração do `referencias.bib`, ajuste do capítulo 2 para citar só obras aprovadas | Cada substituição de citação no capítulo conferida contra a nota da obra substituta; conversão com Pandoc testada com o `referencias.bib`. **Revisão do texto pelo autor pendente** |

| 23/09/2026 | 2 | Claude Code — Coordenador (claude-opus-5-5) + 15 subagentes (5 claude-haiku-4-5, 10 claude-sonnet-5), alguns retomados para correção | Fase 2 inteira: extração de 349 afirmações, fontes primárias dos 10 planejadores e dos 2 trabalhos relacionados de 2010, conferência numérica, classificação, nova taxonomia, plano de reexecução, relatório de auditoria e material do M1 | Coordenador: literalidade dos trechos por script; médias, taxa de acerto e linha de base recalculadas por script; DOIs e URLs das fontes novas reconferidos; 21 revisões de classificação registradas; nota do MAXPLAN e taxonomia corrigidas. Falhas dos agentes e correções em `plan/fase2-estrategia-multiagentes.md`, seção 6. **Revisão do autor pendente** |

| 23/09/2026 | 2 | Claude Code — Coordenador (claude-opus-5-5) | Revisão das 101 afirmações "reformula"/"descarta" | Conferência em fontes primárias: relatórios das IPCs 1998–2004 (AI Magazine, JAIR) e resultados brutos das IPCs 1998 e 2006, agregados por script; listas de participantes e domínios de cada IPC cruzadas com os 38 pares de "competição" de 2010. **Leitura do autor pendente** |

| 23/09/2026 | 2 | Claude Code — Coordenador (claude-opus-5-5) | Resolução das pendências da auditoria | Conferência nos logs do acervo (G21), em Weld 1994, Bonet e Geffner 2001, relatórios das IPCs, resumo do SatPlan 2006 e site da IPC 2006; trechos das 6 notas novas e suas páginas conferidos por script contra o PDF; metadados do OJS e do Crossref. Promoção de referências por delegação do autor. **Leitura humana recomendada** |

---

## 12. Glossário

| Termo | Significado neste projeto |
|---|---|
| Seleção de algoritmos | Escolher, para cada instância de problema, o algoritmo com melhor desempenho esperado (Rice, 1976) |
| Portfólio | Conjunto de planejadores combinados, com seleção ou alocação de tempo entre eles |
| *Single best* | O planejador que, sozinho, tem o melhor desempenho médio no conjunto |
| *Virtual best* / oráculo | Desempenho obtido escolhendo sempre o melhor planejador para cada instância; limite superior |
| *Leave-one-domain-out* | Validação em que o modelo é testado num domínio que não viu no treino |
| LLM-Modulo | Arquitetura em que o LLM gera candidatos e verificadores externos validam |

---

## 13. Referências a verificar

> Levantadas no diagnóstico inicial a partir de conhecimento geral. **Nenhuma deve ser citada antes de verificada.**
>
> **Atualização de 23/09/2026:** as 22 referências desta lista foram localizadas e conferidas no registro primário durante a Fase 1, junto de outras 133. A lista viva passa a ser `literatura/protocolo/verificacao-metadados.csv` e o arquivo `literatura/referencias/candidatas.bib`. Elas continuam **não citáveis** até entrarem no `referencias.bib` exportado do Zotero pelo autor.

| Referência (provisória) | Eixo | Status |
|---|---|---|
| Rice (1976) — The algorithm selection problem | E1 | ⚪ a verificar |
| Roberts & Howe (c. 2008–2009) — predição de desempenho de planejadores | E2 | ⚪ a verificar |
| Gerevini, Saetti & Vallati — PbP (portfolio-based planner) | E1 | ⚪ a verificar |
| Helmert, Röger et al. (2011) — Fast Downward Stone Soup | E1 | ⚪ a verificar |
| Cenamor, de la Rosa & Fernández — IBaCoP | E1 | ⚪ a verificar |
| Sievers et al. (c. 2019) — Delfi | E1 | ⚪ a verificar |
| Fawcett et al. (2014) — *features* para predição de desempenho de planejadores | E2 | ⚪ a verificar |
| Richter & Westphal (2010) — LAMA | E3 | ⚪ a verificar |
| Helmert & Domshlak (2009) — LM-cut | E3 | ⚪ a verificar |
| Lipovetzky & Geffner (2012, 2017) — busca por largura, BFWS | E3 | ⚪ a verificar |
| Toyer et al. (2018) — ASNets | E4 | ⚪ a verificar |
| Ståhlberg, Bonet & Geffner (c. 2022) — GNNs para políticas generalizadas | E4 | ⚪ a verificar |
| Valmeekam et al. (2023) — PlanBench | E5 | ⚪ a verificar |
| Liu et al. (2023) — LLM+P | E5 | ⚪ a verificar |
| Kambhampati et al. (2024) — LLM-Modulo | E5 | ⚪ a verificar |
| Vaquero et al. — evolução do itSIMPLE | E6 | ⚪ a verificar |
| Unified Planning Framework (AIPlan4EU) | E6 | ⚪ a verificar |
| Wolpert & Macready (1997) — No Free Lunch | E7 | ⚪ a verificar |
| Lawrence & Lorsch (1967) — teoria da contingência | E7 | ⚪ a verificar |
| Goodhue & Thompson (1995) — *task-technology fit* | E7 | ⚪ a verificar |
| Ong et al. (2024) — RouteLLM | E7 | ⚪ a verificar |
| Jimenez et al. (2024) — SWE-bench | E8 | ⚪ a verificar |

---

## 14. Changelog

| Versão | Data | Mudança |
|---|---|---|
| 0.1 | 21/09/2026 | Criação do documento: diagnóstico, perguntas de pesquisa, fases revisadas com aceleração por IA e ponte para desenvolvimento de software |
| 0.2 | 21/09/2026 | Repositório criado e estruturado; catálogo do acervo de 2010; achado de que `comp/script.sql` contém o dataset de 2010 (ação 2 da Fase 0 muda de transcrição para exportação e conferência); pendências da Fase 0 em `docs/catalogo-acervo-2010.md` |
| 0.3 | 21/09/2026 | Fase 0 executada: dataset de 2010 em CSV com scripts e conferência; condições de execução (F6) documentadas; modelos itSIMPLE identificados (11 de 13); achados para a auditoria; `MEMORY.md` criado; Obsidian adiado; ações e decisões atualizadas |
| 0.4 | 21/09/2026 | Modelos itSIMPLE de Pathways e TPP identificados pelas figuras da dissertação (13 de 13); achados G11–G13; mapa `modelos_itsimple_2010.csv` |
| 0.5 | 21/09/2026 | Benchmarks das IPCs até 2008 mapeados (repositório `potassco/pddl-instances`); correções das métricas de Pathways e TPP aprovadas; achados G14–G17 |
| 0.6 | 21/09/2026 | Variantes de Zeno-travel e Elevator confirmadas pelo autor; mapa final de benchmarks (`benchmarks_ipc_mapa_final.csv`) |
| 0.7 | 21/09/2026 | N = 20 definido para Zeno-travel e Elevator; benchmarks totalmente mapeados |
| 0.8 | 21/09/2026 | Dataset de 2010 conferido pelo autor; ação 2 concluída |
| 0.9 | 21/09/2026 | Fase 0 concluída; formato definido (dissertação revisada, ABNT); Obsidian descartado; liberdade de escopo (não presa à estrutura de 2010); `redacao/README.md` com normas, retrato de 2010 e opções de ferramenta |
| 0.10 | 21/09/2026 | Esclarecido: padrão ABNT sem LaTeX; abnTeX2 descartado; ferramenta de redação restrita a Word ou Markdown com Pandoc |
| 0.11 | 21/09/2026 | Decidido: corpo do texto em Markdown no repositório, com `.bib` do Zotero; convenções de referências e de escrita; ação 7 passa a validar a conversão |
| 0.12 | 23/09/2026 | **Fase 1 executada em modo multiagente** (22–23/09/2026): protocolo v1.1 com o critério X7, 317 obras únicas triadas, 155 incluídas, 154 verificadas no registro primário, 153 notas de leitura, 8 sínteses, rascunho do capítulo 2 com parecer crítico, insumos para a Fase 2 e teste da conversão ABNT. Relatório em `literatura/relatorio-fase1.md`; tudo pendente de confirmação do autor |
| 0.13 | 23/09/2026 | Pendências da Fase 1 tratadas: triagem confirmada (delegada ao Coordenador), fluxo de referências sem Zotero (`revisao-referencias.md` + `promover_referencias.py`), GIPO excluído, notas com versão divergente resolvidas; ações 8 a 10 atualizadas; 4 decisões |
| 0.14 | 23/09/2026 | Quatro decisões de fundo para as Fases 2 e 3: taxonomia de técnicas em quatro dimensões (expansão de escopo, R1), análise por domínio e por instância, métricas UML testadas contra *features* de PDDL, itSIMPLE 2005 assumido como origem da pergunta; ação 12 (conversa com o Tonidandel) |
| 0.15 | 23/09/2026 | `referencias.bib` gerado (129 obras); obras enviadas pelo autor lidas (Núñez 2015, Tonidandel 2006, Strobel e Kirsch 2014); A3 revisto para "reformula"; ações 9 e 10 concluídas |
| 0.16 | 23/09/2026 | **Fase 1 concluída.** Stone Soup, Delfi e Cedalion promovidos por exceção (133 obras no `referencias.bib`); capítulo 2 ajustado e 100% citável; critério de conclusão aplicado ao capítulo |
| 0.17 | 23/09/2026 | **Fase 2 concluída** (multiagente): 349 afirmações classificadas (248 mantém, 99 reformula, 2 descarta), achados G18–G20, fontes primárias dos 10 planejadores e dos 2 trabalhos relacionados de 2010, nova taxonomia em 4 dimensões, plano de reexecução (31 itens), relatório de auditoria, material do M1; tabela semente movida para `auditoria/afirmacoes.csv`; ações 13 a 16 |
| 0.18 | 23/09/2026 | Revisão das 101 afirmações (a pedido do autor): 268 mantém, 76 reformula, 5 descarta; números das IPCs conferidos nas fontes oficiais; achado G21 (4 pares de "competição" impossíveis); R reconhecido como *regression-progression* (Bacchus, 2001) na taxonomia; ações 17 e 18 |
| 0.19 | 23/09/2026 | Pendências da auditoria resolvidas por delegação do autor: G21 esclarecido (execução própria, logs no acervo), 26 "CONFERIR" resolvidas, 17 referências promovidas (`referencias.bib` com 150), taxonomia 100% citável; totais 265/80/4; ações 13 e 15 a 18 concluídas |
