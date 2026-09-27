# Revisão da Dissertação — Características de Domínios × Técnicas de Planejamento

> **Documento de trabalho.** Controle e acompanhamento da evolução de cada fase.
> Atualize o painel, os checkboxes e os registros ao final de cada sessão de trabalho.

| Campo | Valor |
|---|---|
| Trabalho original | *Relação entre características de domínios e técnicas de planejamento* — Dissertação de Mestrado, Centro Universitário da FEI, 10/03/2010 |
| Autor | Matheus Haddad |
| Orientador original | Prof. Dr. Flavio Tonidandel |
| Início da revisão | 21/09/2026 |
| Última atualização | 27/09/2026 |
| Versão deste documento | 0.68 |
| Status geral | 🟢 Fase 0 concluída em 21/09/2026 · 🟢 Fase 1 concluída em 23/09/2026 (equipe multiagente) · 🟢 Fase 2 concluída em 23/09/2026 (equipe multiagente) · 🟢 Marco M1 em 24/09/2026 · 🟢 Fase 3 concluída em 27/09/2026 (Q1 e Q2 validadas pelo autor) · 🟢 Fase 4 concluída em 27/09/2026 · 🟡 Fase 4B em andamento · 🟡 Fase 5 exploratória iniciada em 27/09/2026 |

---

## 1. Propósito

Revisar a dissertação de 2010 para **evoluir o trabalho**: atualizar o estado da arte, reconstruir o método com os recursos de hoje e verificar o que das conclusões originais se sustenta.

Desdobramentos possíveis, não obrigatórios:

- **Compartilhar com o orientador original** (Flavio Tonidandel) e, se houver interesse mútuo, continuar a conversa ou produzir algo em conjunto.
- **Aplicar no desenvolvimento de software dirigido por IA**: investigar oportunidades e formular hipóteses sobre como o ajuste entre características do problema e técnica de solução pode ser útil nesse contexto.
- **Produto**: possibilidade futura, fora do escopo desta revisão; só pode ser considerada após validação empírica independente.

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
| 3 | Infraestrutura e replicação experimental | Replicar e estender o experimento com método atual | 4–6 semanas (executada em 4 dias) | 🟢 | 24/09/2026 | 27/09/2026 | Dataset, código, resultados; respostas a Q1 e Q2 em `experimentos/relatorio-fase3.md` |
| 4 | Camada LLM | Posicionar LLMs no mapa das técnicas | 2–3 semanas (executada em 2 dias) | 🟢 | 26/09/2026 | 27/09/2026 | Resultados comparativos |
| 4B | Panorama das IPCs posteriores a 2010 | Avaliação geral de características de domínio × técnicas com os dados publicados das IPCs 2011–2023, como base para desenhar a Ponte | 3–4 semanas `[HIPÓTESE]` | 🟡 | 27/09/2026 | | Dataset, mapa característica × técnica, resposta a Q5 |
| 5 | Ponte para desenvolvimento de software dirigido por IA | Investigar conexões, oportunidades e hipóteses entre planejamento e desenvolvimento de software com IA | 1–2 semanas `[HIPÓTESE]` | 🟡 | 27/09/2026 | | Síntese exploratória, agenda de pesquisa e hipóteses |
| 6 | Redação e compartilhamento | Nova versão do trabalho + conversa com o orientador | 3–4 semanas | 🟡 | 24/09/2026 | | Nova versão + material para o orientador |

**Duração total estimada:** 4 a 5 meses em dedicação parcial. Sem o apoio de IA, a estimativa seria de 9 a 12 meses.

### Marcos de conversa com o orientador

| Marco | Quando | O que levar | Status |
|---|---|---|---|
| M1 — Primeiro contato | Após Fase 2 | Diagnóstico da versão 2010 + perguntas de pesquisa revisadas | 🟢 enviado em 23/09/2026; retorno em 24/09/2026 (`redacao/orientador/2026-09-24-retorno-m1.md`) |
| ~~M2 — Resultados~~ | ~~Após Fases 3–4~~ | Cancelado em 25/09/2026: o autor só volta a falar com o orientador depois da reescrita geral | ⛔ |
| M3 — Nova versão | Fim da Fase 6, depois da reescrita geral | Dissertação reescrita completa, enviada **por e-mail**; o retorno do orientador vem depois e é registrado em `redacao/orientador/` | ⚪ |

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
| Q4 | Que conexões, oportunidades e hipóteses de pesquisa ligam o ajuste entre características da tarefa e estratégia de solução ao desenvolvimento de software dirigido por IA? | Exploratória | 5 |
| Q5 | Nos resultados publicados das IPCs posteriores a 2010, quais características estruturais do domínio, extraídas automaticamente do PDDL (sem UML.P), explicam o desempenho relativo das famílias de técnicas de planejamento? | Ampliação | 4B |

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

- [x] Extrair todas as afirmações substantivas (IA gera a lista, autor revisa) — 349 em `auditoria/afirmacoes.csv`; revisão delegada ao Coordenador; o autor leu as 84 "reformula"/"descarta" e aceitou a delegação para as 265 "mantém" (27/09/2026)
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

- [x] Montar ambiente de execução em contêineres — OrbStack (EXP-01, emulado, lento demais) e depois VM no GCP, x86_64 nativo (`experimentos/containers/gcp/gcp.sh`, EXP-05); nenhum recurso no GCP após 27/09/2026
- [x] Baixar e organizar *benchmarks* — IPC 1998–2014 (`potassco`, `cf19edf`) e Autoscale do Planner Museum (`723a31c0`), fora do git
- [x] Compilar e testar planejadores — os 10 de 2010 testados (EXP-01) e rodados (EXP-05); planejadores atuais dispensados: a ampliação usa dados publicados das IPCs (R-24, decisão de 26/09/2026)
- [x] Implementar extrator das métricas de 2010 a partir do PDDL — EXP-07 (`experimentos/extratores/metricas_2010_pddl.py`): 11 de 17 métricas têm correspondente no PDDL
- [x] Validar o extrator contra as contagens manuais de 2010 (dataset da Fase 0) — EXP-07: tipos e ações se reproduzem (postos 0,69–0,92); atributos, associações e atores não (0,31–0,51)
- [x] Implementar ou reutilizar extrator de *features* modernas — EXP-11 (`experimentos/extratores/features_sas.py`, tradutor do Fast Downward 26.6): 17 *features* SAS+ nas 354 instâncias de 2010
- [x] Rodar experimentos — Nível 3 (EXP-05): 3.390 execuções; qualidade dos planos (EXP-20)
- [x] Reproduzir o método de 2010 sobre os dados novos (linha de base) — sobre os dados de 2010 (Nível 1, EXP-03: 220/221 classes, 100/100 notas, 535/539 células, achados G23 e G24) e com as notas do Nível 3 (EXP-19)
- [x] Treinar e avaliar modelos de seleção — EXP-12, por domínio e com dados publicados: nenhum seletor (método de 2010, kNN, *random forest*) supera o *single best*
- [x] Testar robustez das métricas UML a variações de modelagem (F3) — EXP-08 (classes com e sem auxiliares: nenhum ranking muda) e EXP-10 (discretização com mais domínios); Agregação não reproduzível (R-13)
- [x] Analisar importância das *features* e responder Q1 e Q2 — `experimentos/relatorio-fase3.md`: Q1, a conclusão de 2010 não se sustenta como método de seleção; Q2, métricas UML e *features* SAS+ não acrescentam poder preditivo por domínio. **Validadas pelo autor em 27/09/2026**

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
| X1 | LLM como planejador | Qual é o desempenho do LLM em relação aos planejadores clássicos num subconjunto de domínios? | 🟢 EXP-16: 28 de 32 planos válidos (VAL) nas instâncias p01 de 8 domínios; planos em geral mais curtos que os do `lama-first`. EXP-23 (nomes ofuscados): 20 de 32 válidos, contra 28; 5 das 8 perdas por limite de *tokens* |
| X2 | LLM como tradutor | O LLM gera PDDL correto a partir de descrição em linguagem natural? Com que taxa de erro? | 🟢 EXP-18: sintaxe válida em 23 de 24; só 10 pares comparáveis (assinatura igual), dos quais 6 corretos; a descrição em linguagem natural deixa livres nomes, ordem e tipos dos parâmetros |
| X3 | LLM como seletor | Dada a descrição do domínio, o LLM escolhe bem o planejador? Comparar com o seletor da Fase 3 | 🟢 EXP-14 (anônima): nenhum LLM supera o *single best*; GPT-6 Sol empata (146 × 143). EXP-15 (com nomes): piora em 3 de 4 modelos; escolhas seguem a reputação (LAMA, FDSS), sem sinal de lembrança dos resultados por domínio |
| X4 | LLM + verificador | Arquitetura com validador formal (ex.: VAL) melhora X1? | 🟢 EXP-17 (p05, 4 domínios): 8 de 16 válidos na 1ª tentativa, 13 de 16 com o retorno do VAL; as 3 falhas restantes são por limite de *tokens*; o GPT e o Gemini resolvem o Floortile p05, que o LAMA não resolveu em 300 s |

**Atividades**

- [x] Selecionar subconjunto de domínios — 41 domínios do Nível 4 no X3; p01 de 8 domínios no X1; p05 de 4 no X4; 6 do LLM+P no X2
- [x] Definir modelos e congelar versões — Claude Sonnet 5, GPT-6 Sol, Gemini 3.1 Pro e DeepSeek V4 Pro, via OpenRouter; raciocínio *medium*, 16.000 *tokens*
- [x] Rodar X1–X4 com registro de custos e *prompts* — EXP-14 a EXP-18; US$ 10,51 de US$ 12. EXP-23 (27/09/2026): US$ 2,04; a primeira rodada levou a chave a US$ 12,08, acima do teto; o autor subiu o limite para US$ 13 (uso final: US$ 12,49)
- [x] Analisar e posicionar LLMs no mapa das técnicas — `llm/relatorio-fase4.md`: técnica de planejamento com verificador; tradutor fora do mapa (modelagem); seletor sem ganho. Aceito pelo autor em 27/09/2026; valores novos na taxonomia (`auditoria/taxonomia-tecnicas.md`, seção 6.1)

**Entregáveis:** resultados X1–X4 · resposta a Q3

**Critério de conclusão:** os quatro experimentos executados e registrados.

**Notas:**

---

### Fase 4B — Panorama das IPCs posteriores a 2010

**Objetivo:** responder Q5 e produzir uma avaliação geral da relação entre características de domínio e técnicas de planejamento, com os dados de 15 anos de competições, como base para desenhar a Ponte (Fase 5).

**Posição:** depois da Fase 4 e antes da Fase 5 (decisão de 25/09/2026). O sufixo evita renumerar as fases seguintes.

**Diferença em relação à Fase 3.** A Fase 3 reexecuta planejadores em condições controladas. A 4B usa **dados secundários**: os resultados publicados pelas próprias IPCs, com os domínios e planejadores de cada edição, sem reexecução. Ganha amplitude (muitos planejadores e domínios) e perde controle experimental.

**Desenho** (a detalhar no início da fase)

- **Fontes:** resultados oficiais das IPCs 2011, 2014, 2018 e 2023, trilhas clássicas (*satisficing*, ótima, *agile*); os PDDL dos domínios de cada edição; bases derivadas, se houver dados publicados (ex.: `lequen2026planner`). `[A CONFIRMAR]` formato, granularidade e disponibilidade em cada edição.
- **Unidade de análise:** instância, agregada por domínio. Comparações **dentro de cada edição**; entre edições, só com dados reexecutados em hardware uniforme.
- **Técnicas:** planejadores classificados pela taxonomia em 4 dimensões (R-10). Portfólios, que vencem trilhas desde 2011, precisam de regra própria (classificar pela técnica que resolveu a instância, pelos componentes ou como categoria à parte). Decisão do autor no início da fase.
- **Características, sem UML.P:** as *features* de PDDL/SAS+ da Fase 3, mais propriedades com fundamento teórico (grafo causal, reversibilidade, becos sem saída, topologia de busca na linha de `hoffmann2011analyzing`). Reaproveitar os extratores da Fase 3.
- **Análise:** modelos interpretáveis primeiro; importância das características; mapa característica × família de técnicas; comparação com os resultados da Fase 3 nos domínios em comum. A contribuição pretendida é o **mapa explicável por técnica**, não mais um seletor caixa-preta `[HIPÓTESE]`.

**Cuidados**

- Hardware, limites e conjunto de domínios mudam a cada edição.
- Cada planejador roda uma vez; a ordem do PDDL muda *rankings* (`vallati2021importance`).
- Separar "não resolveu" de "não suporta o recurso do PDDL" (cobertura censurada).
- Obras de trabalho ainda **não citáveis** (fora do `referencias.bib`): Ferber et al. (2019), base de domínios das IPCs com tempos de planejadores, e Ferber et al. (2022), seleção interpretável, principal trabalho a confrontar.

**Atividades**

- [x] Levantar o que cada IPC publicou (resultados por instância, limites, hardware, domínios, planejadores) — 27/09/2026, `docs/resultados-ipc-2011-2023.md`
- [x] Verificar e, se for o caso, promover ao `referencias.bib` as fontes de dados e os trabalhos a confrontar — 27/09/2026: o autor decidiu **não** promover `ferber2019ipc`, `ferber2022explainable` nem as entradas do *booklet* de 2014 (seção 10)
- [ ] Montar o dataset em `data/` com `README.md` de origem e método — em curso: 2011 (WebPlan) e 2018 por instância em `data/ipc-2011-2023/`, ambos validados contra o placar oficial (27/09/2026); recorte decidido em 27/09/2026 (`docs/fase4b-desenho.md`, D2); falta a ligação completa de 2011 aos PDDL
- [x] Classificar os planejadores na taxonomia e decidir a regra dos portfólios — 27/09/2026: regra P1 + G1/G2 (`docs/fase4b-desenho.md`, D1); 78 codificações de 2011 e 2018 em `data/ipc-2011-2023/planejadores_4d.csv`
- [ ] Extrair as características dos domínios — em curso: *features* SAS+ de 2011, 2014, 2018 e 2023 (`data/ipc-2011-2023/features_sas_ipc.csv`, 27/09/2026); PDDL de 2011 trocado para o `downward-benchmarks` e de 2014 para o ZIP oficial (o `pddl-instances` tem o floortile ótimo de 2011 errado); faltam as propriedades teóricas (topologia de busca etc.)
- [ ] Analisar e montar o mapa característica × técnica; responder Q5 — em curso: EXP-21, segunda rodada (27/09/2026, `experimentos/execucoes/2026-09-27-q5-ipc.md`): as 16 *features* SAS+ não antecipam, fora do domínio, qual família resolve (AUC mediana 0,58, igual à do tamanho); com permutação e Holm, só sobrevivem famílias de 1 a 3 planejadores; no mapa, a busca simbólica é a única que supera a progressiva, e só na ótima. Ligação de 2011 completa; falta rodar de novo com o organic-synthesis de 2018; depois, propriedades teóricas e R-29 por instância
- [ ] Seleção por instância (R-29, vindo da Fase 3): com os dados por instância de 2011 e 2018, comparar seletor por instância, seletor por domínio e *single best*, reportados separadamente (decisão do autor, 27/09/2026)
- [ ] Escrever a síntese para a Ponte: o que se transfere como hipótese para a Fase 5 e o que não se transfere

**Entregáveis:** dataset documentado · mapa característica × técnica · resposta a Q5 · síntese para a Ponte

**Critério de conclusão:** análise reprodutível a partir do repositório e síntese para a Ponte revisada pelo autor.

**Notas:**

- 27/09/2026 — Fase iniciada com a Fase 3 ainda em curso (Nível 3 no GCP), por decisão do autor. Só a comparação com a Fase 3 depende do Nível 3.
- 27/09/2026 — **Atualização do mesmo dia:** a nota abaixo ficou desatualizada. 2011 foi recuperada por instância (WebPlan, custo sem tempo); 2014 tem totais por trilha de todos os planejadores (`vallati2018what`) e o PDDL; 2023 tem os dados por instância sob pedido. Estado corrente em `docs/resultados-ipc-2011-2023.md`.
- 27/09/2026 — Levantamento das fontes (`docs/resultados-ipc-2011-2023.md`): **só a IPC 2018 tem resultados por instância acessíveis**; 2011 e 2023 só por domínio; 2014 só o total dos 5 primeiros por trilha (os arquivos de resultados de 2011 e 2014 saíram do ar e não foram arquivados). Fonte derivada por instância: IBM/Delfi (`ferber2019ipc`), 17 planejadores ótimos, 2.439 tarefas de 1998–2018. O Planner Museum não publicou dados por instância.

---

### Fase 5 — Ponte para desenvolvimento de software dirigido por IA

**Objetivo:** responder Q4 por investigação exploratória: explicitar conexões entre o que foi estudado sobre características de domínios e técnicas de planejamento e o desenvolvimento de software dirigido por IA; identificar oportunidades e formular hipóteses testáveis. Não há piloto, coleta de dados no Ateliê nem decisão de produto nesta fase.

**Início:** em paralelo à conclusão da Fase 4B (decisão do autor, 27/09/2026). A síntese da 4B entra como evidência complementar antes do fechamento da Fase 5.

**Entrada:** resultados das Fases 1–4, especialmente as sínteses E7 e E8, a taxonomia em quatro dimensões, os resultados negativos de seleção das Fases 3 e 4, e a síntese para a Ponte da Fase 4B quando estiver concluída.

**Analogia de trabalho** `[HIPÓTESE]`

| Planejamento automático (2010) | Desenvolvimento de software dirigido por IA |
|---|---|
| Domínio de planejamento | Tarefa de desenvolvimento (história, bug, refatoração) no contexto de um repositório |
| Características do domínio | Tamanho da mudança, clareza da especificação, cobertura de testes, acoplamento, idade do código, novidade do domínio de negócio, métricas estruturais do código |
| Técnica de planejamento | Configuração do agente: modelo, planejar-antes-de-executar ou execução direta, ciclo com testes, subagentes, grau de supervisão humana |
| Planejador | Combinação de ferramenta + modelo + estratégia |
| Eficiência (problemas resolvidos) | Tarefa aceita, retrabalho, tempo, custo, defeitos posteriores |
| Ranking de planejadores | Recomendação de configuração para uma nova tarefa |

**Hipóteses de pesquisa** `[HIPÓTESE]`

- **H1:** nenhuma configuração de agente é a melhor para todos os tipos de tarefa de desenvolvimento.
- **H2:** características observáveis da tarefa e do repositório podem ajudar a explicar ou prever qual configuração tende a funcionar melhor.
- **H3:** métricas estruturais de código podem ser candidatas a *features*, mas sua utilidade preditiva precisa de teste empírico próprio; a transferência das métricas UML de 2010 não é evidência suficiente.

**Atividades**

- [x] Delimitar a analogia: correspondências úteis e limites entre domínio/tarefa, técnica/configuração e eficiência/resultado — `ponte-software/relatorio/sintese-exploratoria.md` (27/09/2026)
- [x] Revisitar os resultados das Fases 1–4 para extrair evidências a favor, contra e neutras para H1–H3 — síntese exploratória, seções 2–5 (27/09/2026)
- [x] Revisar as fontes já verificadas dos eixos E7 e E8 sobre roteamento, orquestração e avaliação de agentes de código — 8 chaves citáveis conferidas por `checar_citacoes.py` (27/09/2026)
- [x] Mapear oportunidades de pesquisa e aplicação, distinguindo o que é sustentado por evidência do que depende de validação futura — síntese exploratória, seção 6 (27/09/2026)
- [x] Elaborar uma agenda de pesquisa com possíveis desenhos empíricos, sem iniciar piloto — síntese exploratória, seções 5–6 (27/09/2026)
- [ ] Incorporar a síntese para a Ponte da Fase 4B antes de fechar a interpretação

**Entregáveis:** síntese exploratória · mapa de conexões e limites · hipóteses testáveis · oportunidades e agenda de pesquisa.

**Critério de conclusão:** síntese revisada pelo autor, com toda inferência marcada como `[HIPÓTESE]` e sem alegação de validação empírica no desenvolvimento de software.

**Notas:**

- 27/09/2026 — Síntese exploratória preliminar concluída em `ponte-software/relatorio/sintese-exploratoria.md`. Há evidência de heterogeneidade por tarefa em agentes de código e de roteamento de LLMs; a transferência para um seletor de agentes em software permanece hipótese. Os resultados negativos das Fases 3 e 4 entram como limite: *features* estruturais estáticas não devem ser presumidas suficientes. Falta integrar a síntese da 4B antes de fechar a Fase 5.
- 27/09/2026 — Dossiê para o futuro Capítulo 7 em `ponte-software/relatorio/dossie-capitulo-7.md`: tese editorial, escada de inferência, conexão com os resultados negativos, três níveis de aplicabilidade, auditoria conceitual, hipóteses falseáveis e arquitetura de redação. Não é capítulo final e aguarda a síntese da 4B.

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
- [ ] Redigir capítulos a partir dos entregáveis das fases anteriores — rascunhos de IA prontos: 1 (Introdução, com seções pendentes dos resultados), 2 (Fundamentos) e 3 (Revisitando 2010); os capítulos 4 a 8 dependem das Fases 3 a 5. Ao redigir: achados G22 a G26 no capítulo de método, com remissão no capítulo 3 (decisão de 27/09/2026); capítulo 2 com os resultados do capítulo 5
- [ ] Revisão de consistência (IA aponta inconsistências entre capítulos, dados e referências)
- [ ] Verificação final de todas as referências e números
- [ ] Revisão de estilo na voz do autor
- [ ] Elementos pré e pós-textuais (capa, folha de rosto, folha de aprovação, resumo e *abstract*, listas, sumário, referências) e conferência de formatação, citações e referências pela ABNT
- [ ] Declaração do uso de IA no texto, conforme as regras da instituição
- [ ] Preparar resumo executivo para o orientador
- [ ] Enviar a dissertação reescrita ao orientador por e-mail (**Marco M3**)
- [ ] Registrar retorno e próximos passos

**Entregáveis:** dissertação revisada (padrão ABNT) · resumo executivo · registro do retorno do orientador

**Critério de conclusão:** versão enviada e retorno registrado.

**Notas:**

---

## 8. Riscos

| # | Risco | Probabilidade | Impacto | Mitigação |
|---|---|---|---|---|
| R1 | Expansão de escopo (a Fase 5 pode virar um projeto próprio; o autor liberou ampliar a revisão para além de 2010) | Alta | Alto | Manter a Fase 5 como síntese exploratória; trabalho empírico ou produto exigem decisão posterior; **registrar cada expansão na seção 10 com motivo e fase afetada** |
| R2 | Referências inventadas ou erradas por IA | Alta | Alto | Princípio 1; verificação obrigatória na seção 13 |
| R3 | Volatilidade dos LLMs torna resultados obsoletos | Alta | Médio | Congelar versões e datar resultados |
| R4 | Planejadores antigos não compilam | Média | Médio | Usar imagens das IPCs; registrar o que não foi possível reproduzir |
| R5 | Custo computacional | Média | Médio | Subconjunto representativo de domínios; limites de tempo definidos |
| R6 | Confusão entre analogia e evidência na Fase 5 | Média | Alto | Marcas `[FATO]`/`[HIPÓTESE]`; não apresentar hipótese como resultado de aplicação |
| R7 | Inferir causalidade ou eficácia no desenvolvimento de software sem dados próprios | Média | Alto | Limitar a fase a conexões, oportunidades e hipóteses; definir validação futura como trabalho posterior |

---

## 9. Próximas ações

| # | Ação | Fase | Responsável | Prazo | Status |
|---|---|---|---|---|---|
| 1 | Localizar modelos do itSIMPLE e planilhas originais | 0 | Matheus + IA | | 🟢 concluída (13 de 13 modelos; planilhas mapeadas) |
| 2 | Transcrever tabelas da dissertação para CSV | 0 | IA + conferência de Matheus | 21/09/2026 | 🟢 concluída e conferida |
| 3 | Criar repositório | 0 | Matheus + IA | 21/09/2026 | 🟢 concluída (Obsidian descartado) |
| 4 | Definir protocolo de busca da Fase 1 | 1 | Matheus + IA | 22/09/2026 | 🟢 concluída (v1.1, com o critério X7) |
| 5 | Decidir o formato da nova versão | 0 | Matheus | 21/09/2026 | 🟢 dissertação revisada, ABNT |
| 6 | Decidir onde rodar os experimentos da Fase 3 (Linux/x86) | 3 | Matheus | antes da Fase 3 | 🟢 OrbStack (23/09/2026), depois VM Spot no GCP (25/09/2026); VM apagada em 27/09/2026 |
| 7 | Validar a conversão Markdown → Pandoc → documento ABNT | 1, 6 | Matheus + IA | 23/09/2026 | 🟡 Pandoc 3.11 instalado; corpo e referências convertem, inclusive no capítulo inteiro (`redacao/teste-abnt/relatorio-teste.md`). Falta: escolher a variante do CSL (a genérica não imprime o nome do evento; a UFPR imprime), conferir a caixa alta da NBR 10520 e testar os elementos pré-textuais |

| 8 | Confirmar a triagem da Fase 1 | 1 | Coordenador (delegado pelo autor) | 23/09/2026 | 🟢 122 confirmadas, 29 com ressalva, 3 não citáveis (não lidas), GIPO excluído; critérios no protocolo, seção 9 |
| 9 | Revisar as referências e gerar o `referencias.bib` | 1, 6 | Matheus + Coordenador | 23/09/2026 | 🟢 **129 obras citáveis**: as 122 confirmadas aprovadas pelo autor, 5 ressalvas com ≥ 50 citações e 2 confirmadas a partir dos PDFs do autor. O capítulo 2 tem 14 chaves não citáveis a substituir ou retirar (situação de 23/09/2026; hoje 151 obras, e os capítulos 1 a 3 citam só chaves do `referencias.bib`) |
| 10 | Obras sem acesso | 1 | Matheus | 23/09/2026 | 🟢 `nunez2015automatic` e `tonidandel2006reading` lidas a partir dos PDFs do autor; `strobel2014planning` acrescentada; só `sette2008are` segue sem leitura (não citável). GIPO excluído |
| 11 | Decidir as quatro questões da Fase 2 listadas em `auditoria/insumos-fase1.md`, seção 5 | 2 | Matheus | 23/09/2026 | 🟢 decididas (seção 10): taxonomia em 4 dimensões; análise por domínio e por instância; UML testada contra *features* de PDDL; itSIMPLE 2005 como origem da pergunta |
| 12 | Conversar com o Tonidandel sobre o artigo do itSIMPLE de 2005 como origem da pergunta | 2, 6 | Matheus | 24/09/2026 | 🟢 coberto pelo M1 |
| 13 | Revisar a auditoria (afirmações "reformula" e "descarta") | 2 | Matheus + Coordenador | 23/09/2026 | 🟢 revisão do Coordenador por delegação; **leitura das 84 feita pelo autor** em 23/09/2026 |
| 14 | Revisar e enviar o material do Marco M1 (`auditoria/m1-orientador.md`) | 2 | Matheus | 24/09/2026 | 🟢 enviado; retorno registrado: taxonomia confirmada, demais pontos de acordo, sem artigo; G10 segue em aberto |
| 15 | Aprovar as fontes novas da Fase 2 no `referencias.bib` | 2, 6 | Coordenador (delegado pelo autor) | 23/09/2026 | 🟢 17 promovidas (11 da Fase 2 + 6 da resolução de pendências); `referencias.bib` com 150 obras |
| 16 | Conferir na fonte as afirmações com ação "CONFERIR" | 2, 6 | Coordenador | 23/09/2026 | 🟢 nenhuma restante; 16 de confiança baixa com decisão registrada (retirar, parafrasear ou tratar como hipótese) |
| 17 | Esclarecer a origem dos 4 valores de "competição" impossíveis (G21) | 2, 3 | Coordenador | 23/09/2026 | 🟢 vieram dos logs de execução própria de 2010; são 34 pares de competição e 66 de execução própria |
| 18 | Incluir os relatórios oficiais das IPCs no `candidatas.bib` | 2, 6 | Coordenador | 23/09/2026 | 🟢 incluídos e promovidos, com Bonet e Geffner (2001) e Weld (1994) |
| 19 | Decidir o limite de tempo da reexecução dos planejadores de 2010 (Nível 3) | 3 | Matheus | 24/09/2026 | 🟢 opção 1, limite calibrado por planejador (EXP-02): de 38 min (SGPlan) a 137 min (R); LPG-TD com o fator comum (76 min) e várias sementes; `experimentos/execucoes/fatores-2010.csv` |
| 20 | Delimitar e executar a síntese exploratória da Ponte, sem piloto no Ateliê | 5 | Matheus + IA | | 🟡 síntese e dossiê do futuro Capítulo 7 concluídos em `ponte-software/relatorio/`; aguarda a síntese da 4B para o fechamento |

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
| 23/09/2026 | Demais escolhas da taxonomia (7 itens, `auditoria/taxonomia-tecnicas.md`, "Decisões"): *Knowledge-based* fora das dimensões, SGPlan como decomposição na Dimensão 1 e não como portfólio, "heurísticas aprendidas" e "grafo causal" como valores próprios, R em valor próprio, fonte de POCL a buscar | Decisão do Coordenador, **validada pelo orientador no M1 (24/09/2026)** | 2 |
| 23/09/2026 | As Tabelas 2–4 de 2010 são descartadas e substituídas pela nova taxonomia; as Tabelas 18–25 serão recalculadas (Fase 3, R-06 e R-10) | Coerente com A6 e com as fontes primárias dos 10 planejadores | 2, 3 |
| 23/09/2026 | Regras de auditoria adotadas: trecho literal conferido por script; números derivados de tabela conferidos por script, não por agente; plausibilidade não é evidência (confiança baixa + "CONFERIR"); afirmação sobre obra citada em 2010 é conferida contra a obra que a lista de referências de 2010 indica | Falhas observadas nas Ondas 1–3 (`plan/fase2-estrategia-multiagentes.md`, seção 6) | 2 |

| 23/09/2026 | Revisão das 101 afirmações "reformula"/"descarta" feita pelo Coordenador a pedido do autor: números das IPCs conferidos nos relatórios oficiais e nos resultados brutos; 25 classificações alteradas (4 viram "descarta", 20 viram "mantém", AF-328 volta a "reformula"); achado G21 | Pedido do autor; fontes primárias das competições | 2 |

| 23/09/2026 | Pendências da auditoria resolvidas pelo Coordenador por delegação do autor: 17 referências promovidas ao `referencias.bib` pelo critério das exceções anteriores (fontes primárias de planejadores e competições); `cenamor2019insights` mantido fora; afirmações periféricas sem fonte são retiradas da versão revisada, citações diretas não conferidas viram paráfrase com fonte aprovada | Pedido do autor: "decidindo a partir do contexto do projeto [...] pelo mais coerente" | 2, 6 |
| 23/09/2026 | Os 4 pares do G21 vieram da execução própria de 2010 (logs no acervo): valores publicados preservados, origem corrigida na documentação e na Fase 3 (34 de competição, 66 de execução própria) | Evidência do acervo | 2, 3 |

| 23/09/2026 | Fase 3 roda numa máquina virtual do OrbStack neste Mac (Apple M4). Primeiro teste: se os binários de 2010 (ELF 32-bit i386) rodam numa máquina amd64; tempos sob emulação não são comparáveis aos de 2010 | Decisão do autor; ressalva técnica do Coordenador | 3 |
| 23/09/2026 | Redação iniciada pelos capítulos que não dependem de resultados: Introdução (rascunho) e capítulo 3 (auditoria); a dissertação de 2010 entra no `referencias.bib` como `haddad2010relacao` | Autor liberou a redação após ler a auditoria | 6 |

| 24/09/2026 | Retorno do M1: o orientador confirmou a nova taxonomia (incluindo as escolhas do Coordenador) e concordou com Q2, com a expansão de escopo (Q3, Q4) e com o desenho da Fase 3. G10 segue em aberto | Orientador, relatado pelo autor | 2, 3 |
| 24/09/2026 | **Sem artigo com os resultados da Fase 3:** o único produto é a dissertação final revisada, no padrão ABNT | Decisão do autor | 6 |

| 24/09/2026 | Máquina da Fase 3: Ubuntu 22.04 amd64 no OrbStack (não 24.04), por causa do `python2` do Fast Downward de 2010; binários de 2010 rodam por QEMU i386; chamadas tiradas dos scripts finais de 2010 (`comp/planners/scripts/`) | EXP-01 | 3 |

| 24/09/2026 | Limite da reexecução dos planejadores de 2010 = 20 min × fator de lentidão da emulação medido por planejador (mediana do tempo de relógio agora ÷ tempo de 2010); LPG-TD, estocástico, recebe a mediana dos determinísticos e roda com várias sementes | Autor escolheu a opção 1; critério do Coordenador (EXP-02) | 3 |

| 24/09/2026 | Nível 1 concluído (EXP-03): o método de 2010 é reproduzível por script; a discretização usada foi por extremos (G23), não a descrita; duas taxonomias no mesmo método (G24); G6 resolvido (nota a partir do valor preciso) | Evidência do EXP-03 | 3 |

| 24/09/2026 | Discretização: o autor considera correta a regra escrita no texto (as classes publicadas teriam erro de transcrição) e, informado de que ela deixa 7–8 métricas com uma só classe e de que as Tabelas 19–25 usaram as classes publicadas, decidiu aplicá-la como cenário do Nível 2; o Nível 1 segue com as classes publicadas | Decisão do autor (EXP-04) | 3, 6 |
| 24/09/2026 | Referência do Nível 2 = método de 2010 recalculado sem os erros aritméticos de G18; com isso, o acerto do Elevator cai de 50% para 40% e o do Zeno-travel de 40% para 30% | EXP-04 | 3 |
| 25/09/2026 | **Expansão de escopo (R1): nova Fase 4B**, panorama das IPCs posteriores a 2010 com os resultados publicados, características extraídas do PDDL sem UML.P e nova pergunta Q5. Fica depois da Fase 4 e antes da Fase 5; numerada com sufixo para não renumerar as fases seguintes | Decisão do autor: ter uma avaliação geral antes de desenhar a Ponte | 4B, 5 |
| 25/09/2026 | **A Fase 5 começa depois da Fase 4B**, e não mais em paralelo à Fase 3; vale também para a conversa com o Ateliê e o desenho do piloto | Decisão do autor: considerar os achados da 4B no desenho da Ponte | 5 |
| 27/09/2026 | **Fase 5 redefinida como investigação exploratória e iniciada em paralelo à 4B.** Não haverá piloto, coleta de dados no Ateliê nem decisão sobre produto; a fase produzirá conexões, oportunidades e hipóteses testáveis. A síntese da 4B permanece insumo obrigatório para fechar a interpretação | Decisão do autor: entender a aplicabilidade potencial da pesquisa antes de qualquer experimento no desenvolvimento de software | 5 |
| 25/09/2026 | **Marco M2 cancelado.** Depois do M1, o próximo contato com o orientador é o M3: a dissertação reescrita inteira, enviada por e-mail, com retorno posterior | Decisão do autor | 6 |
| 25/09/2026 | **Nível 3 migrado para o GCP**: VM `fase3-2010` (c2d-standard-8 Spot, 4 núcleos, us-central1-c), binários de 2010 em x86_64 nativo, limites recalibrados no próprio ambiente (`fatores-2010-gcp.csv`, 7 a 13 min) e resultados em `nivel3-2010-gcp.csv`; R por último na fila. As 259 execuções do OrbStack ficam como registro do ambiente emulado, sem misturar com as do GCP. Proteção de custo: orçamento de R$ 1.500 com avisos e desligamento automático da VM em 28/09/2026 | No OrbStack (QEMU i386) a rodada levaria ~17 dias; autor tem US$ 300 de crédito de avaliação e não quer ultrapassá-lo | 3 |
| 25/09/2026 | **Blackbox no Satellite (G25):** a rodada principal mantém a chamada dos scripts finais (sem `-M`); ao fim, roda-se a variante `blackbox-m8192` (Blackbox no Satellite com `-M 8192`, como nos logs de 2010), com resultados em `nivel3-2010-gcp-blackbox-m8192.csv`, e os dois são registrados | Em 2010 só o Satellite usou `-M 8192`; sem ela, o Blackbox falha nos problemas 11 a 20. Decisão do autor | 3 |
| 25/09/2026 | **Máquina OrbStack `fase3-amd64` apagada**; a Fase 3 segue só no GCP. Saídas brutas do OrbStack preservadas em `experimentos/execucoes/brutos/orbstack/` (fora do git; cópia conferida por MD5) e resultados em `nivel3-2010.csv` | Decisão do autor | 3 |
| 27/09/2026 | **Satellite no Nível 3 com a versão da IPC** (`domain.pddl` da raiz), e não com o domínio de 2010 (hoje em `antigo/`, G25); o Satellite não é comparável célula a célula com 2010 | Decisão do autor | 3 |
| 27/09/2026 | **TPP refeito** com as chamadas de 2010 (`Strips/`) em Blackbox, IPP, LPG-TD, YAHSP e FF, numa segunda VM criada só para isso e apagada ao fim; FF com `ff` (o `ff2` de 2010 não está no acervo, G26) | Autorização do autor; erro de chamada meu | 3 |
| 27/09/2026 | **R sem tratamento adicional**: fica com os resultados do Nível 3 como estão (Pipesworld 0/50, igual a 2010, causa não investigada além do teste das constantes) e sem o Pathways, registrado como limitação | Decisão do autor | 3 |
| 27/09/2026 | **Sem validação dos planos com VAL** no Nível 3: os planos gerados são considerados corretos | Decisão do autor | 3 |
| 27/09/2026 | **Método de 2010 com as notas do Nível 3 usa o ranking real de 2010 na validação** (os domínios de validação não são reexecutados) | Decisão do autor | 3 |
| 27/09/2026 | **Conjunto de instâncias do Nível 3 (R-19):** os subconjuntos do acervo de 2010 (G14), os mesmos da execução própria de 2010, com o Gripper gerado (G15) | Já usado no EXP-05; formalizado com o autor | 3 |
| 27/09/2026 | **Dispensados na Fase 3:** R-23 (mais planejadores da família do R), R-30 (discretização × regressão), R-31 (heurística aprendida) e planejadores atuais compilados (substituídos por dados publicados, R-24) | Baixa prioridade; foco na síntese de Q1 e Q2 | 3 |
| 27/09/2026 | **Respostas a Q1 e Q2 validadas; Fase 3 concluída.** Q1: a pergunta de 2010 se mantém, mas a conclusão de que as métricas de modelagem permitem escolher o planejador não se sustenta. Q2: nem as métricas UML nem as *features* SAS+ acrescentam poder preditivo por domínio. O relatório por instância (R-29) passa para a Fase 4B | Decisão do autor sobre `experimentos/relatorio-fase3.md` | 3 |
| 27/09/2026 | **Resposta a Q3 e propostas da Fase 4 aceitas:** (1) capítulo 6 sobre LLMs, com os três papéis separados e a conclusão de que o lugar deles no mapa é o de técnica de planejamento com verificador; (2) a taxonomia em 4 dimensões ganha os valores novos para LLMs, marcados como extensão da revisão; (3) a ligação entre X2 e F3 (a descrição não determina o modelo) entra na discussão das métricas de modelagem | Decisão do autor sobre `llm/relatorio-fase4.md` | 4, 6 |
| 27/09/2026 | **Expansão de escopo:** valores novos na taxonomia em 4 dimensões para LLMs (D1, D3, D4), fora da versão validada pelo orientador em 24/09/2026 | Resultados da Fase 4 | 4 |
| 26/09/2026 | Codificação dos 10 planejadores na taxonomia em 4 dimensões (`auditoria/taxonomia/planejadores_4d.csv`), com as decisões C1–C5, aprovada sem alteração | Revisão do autor (EXP-06) | 3 |
| 26/09/2026 | "Número total de Agregação" registrada como métrica **não reproduzível**: em 2010 foi contada de forma visual e manual nos diagramas UML.P, sem regra escrita; a AF-331 leva essa ressalva | Resposta do autor; EXP-08 mostrou que nenhum critério contado nos XML reproduz a Tabela 9 | 3, 6 |
| 26/09/2026 | Medida principal de validação (G19): **perda em relação ao *virtual best***; correlação de postos como secundária; acerto por posição só para comparar com 2010; todas reportadas ao lado da linha de base | Recomendação do Coordenador aceita pelo autor: mede a indicação do melhor planejador, não depende de desempate e é a medida do Nível 4 | 3 |
| 26/09/2026 | **Nível 4 só com dados publicados:** a cobertura por domínio do Planner Museum (29 planejadores × 42 domínios Autoscale, 30 min e 4 GiB), cruzada com as *features* extraídas do PDDL; sem execução própria. *Benchmarks*: Autoscale (substitui, no Nível 4, a recomendação de 23/09 de usar os conjuntos completos das IPCs). Consequências: análise só por domínio e só com cobertura; R-20, R-22 e R-31 ficam fora do Nível 4; a análise por instância (A1, A3) não é possível com esses dados | Decisão do autor sobre a proposta `experimentos/nivel4-proposta.md` (a proposta recomendava o híbrido) | 3 |
| 26/09/2026 | Codificação dos 29 planejadores do Planner Museum na taxonomia 4D (`auditoria/taxonomia/planejadores_museu_4d.csv`) aprovada sem alteração, incluindo a regra dos portfólios (P1), os componentes inferidos (M2) e os seis valores novos das dimensões (N1–N6) | Revisão do autor (EXP-13) | 3 |
| 26/09/2026 | **Fase 4 adiantada** enquanto o Nível 3 roda no GCP, começando pelo X3 (LLM como seletor). Modelos pelo **OpenRouter**, com os principais do mercado (seleção proposta em `llm/x3-seletor/protocolo.md`); **teto inicial de US$ 10**, a reavaliar depois | Decisão do autor | 4 |
| 26/09/2026 | X3: rodar a condição com nomes dos planejadores, para medir quanto os modelos lembram dos resultados públicos | Decisão do autor | 4 |
| 26/09/2026 | X4 em instâncias maiores (p05), restrito aos 4 domínios de técnica antiga por orçamento; trava própria de US$ 8,90 para reservar o X2 | Escolha do autor (instâncias maiores); recorte e trava pelo Coordenador, dentro do teto de US$ 10 | 4 |
| 26/09/2026 | Teto da Fase 4 elevado de US$ 10 para **US$ 12** (limite da chave no OpenRouter); travas dos scripts em US$ 11,50. Uso: rodar o X2 e completar as conversas do X4 cortadas pela trava | Decisão do autor | 4 |
| 27/09/2026 | **A Fase 4B começa com a Fase 3 ainda em curso** (Nível 3 no GCP). Só a comparação final com a Fase 3 espera o Nível 3 | Decisão do autor: aproveitar o tempo de espera do GCP | 3, 4B |
| 27/09/2026 | **Dados por instância de 2023 não serão pedidos** aos organizadores, e **as referências pendentes não serão promovidas** (`ferber2019ipc`, `ferber2022explainable`, `vallati2014eighth`, `cenamor2014ibacop`, `malitsky2014allpaca`) | Decisão do autor | 4B |
| 27/09/2026 | **Regra dos portfólios da 4B:** P1 do EXP-13 mais o critério G1 (portfólio = se descreve como tal ou faz execuções separadas de componentes completos; fases dentro de um planejador não contam) e o tipo G2 (`fixo`, `selecao`, `paralelo`); resultados sempre com e sem portfólios. Valor novo N7 na D2 | Coordenador, por delegação do autor ("optando pelas decisões mais coerentes"); `docs/fase4b-desenho.md`, D1 | 4B |
| 27/09/2026 | **Recorte do dataset da 4B:** análise principal em 2011 (ótima e *satisficing*) e 2018 (ótima, *satisficing*, *agile*), por instância agregada por domínio e só dentro de cada edição × trilha; 2014 e 2023 só descritivas; IBM fora; formulações de caldera e organic-synthesis de 2018 como domínios separados | Coordenador, por delegação do autor; `docs/fase4b-desenho.md`, D2 | 4B |
| 27/09/2026 | **Fonte do PDDL da 4B:** `downward-benchmarks` (Planner Museum) para 2011, 2018 e 2023; ZIP oficial para 2014. O `pddl-instances` fica fora da 4B | O `pddl-instances` tem o floortile ótimo de 2011 igual ao da *satisficing*; o SHA-1 do WebPlan confirma o `downward-benchmarks` | 4B |
| 27/09/2026 | **Controle da ordem de serialização dispensado** (R-27; decisão de 23/09/2026, aprovada no M1). O R-27 fica feito sem esse controle, registrado como limitação no relatório da Fase 3 e a explicar no capítulo de método | O orientador disse que não é mais necessário (relatado pelo autor). A hipótese da Fase 1 não se aplica ao experimento de 2010: os planejadores rodaram o PDDL das IPCs, não o exportado pelo itSIMPLE (exceção: o domínio do Satellite, G25, de origem não documentada), e as métricas UML são contagens que a ordem não altera. O teste restante (robustez do *ranking* à ordem do PDDL) não mudaria Q1 nem Q2 e custaria de 36 a 94 h de VM | 3, 6 |
| 27/09/2026 | **Seleção por instância (R-29) incluída na Fase 4B** como análise própria, com os dados por instância de 2011 e 2018, reportada separadamente da análise por domínio | O recorte da 4B (D2) agrega por domínio e deixava o R-29 sem responsável; é o achado central da Fase 1 (a unidade migrou para a instância). Decisão do autor | 3, 4B |
| 27/09/2026 | **Tempo e memória do Nível 3 analisados** (F5, EXP-22; o EXP-21 é da 4B), com os dados já coletados, sem nova execução | Decisão do autor na avaliação das Fases 1 a 4 | 3 |
| 27/09/2026 | **X1 com nomes ofuscados** (EXP-23): mesmas instâncias, modelos e parâmetros do EXP-16, com nomes de tipos, predicados, ações e objetos trocados por rótulos sem significado; dentro do teto de US$ 12 | Teste que faltava para a Q3 (contaminação e familiaridade lexical); decisão do autor | 4 |
| 27/09/2026 | ***Gradient boosting* dispensado** no Nível 4 | kNN e *random forest* já não superam o *single best*; decisão do autor | 3 |
| 27/09/2026 | **Delegação aceita para as 265 afirmações "mantém"** da auditoria; as linhas "revisão do autor pendente" do registro de IA passam a "revisão delegada ao Coordenador; conferência humana na redação" | Decisão do autor | 2, 6 |
| 27/09/2026 | **Capítulo 3 atualizado só na Fase 6**: os achados G22 a G26 entram no capítulo de método, com remissão no capítulo 3 | Decisão do autor | 6 |
| 27/09/2026 | **`sette2008are` excluída** (não lida, não citada); **Ghostscript mantido** no Mac do autor | Decisões do autor | 1 |
| 27/09/2026 | **Ocorrência: teto da Fase 4 ultrapassado em US$ 0,08** no EXP-23 (uso da chave em US$ 12,08). A chave fica acima do limite; nenhuma chamada nova sem decisão do autor. 7 pares do EXP-23 sem chamada | A trava confere o uso antes de cada chamada, e as chamadas em paralelo já em curso passaram dela; o OpenRouter não as bloqueou. Registro do Coordenador | 4 |
| 27/09/2026 | **Limite da chave elevado para US$ 13** para completar os 7 pares do EXP-23, em sequência (uma chamada de cada vez), com trava de US$ 12,80 | Decisão do autor | 4 |

---

## 11. Registro de uso de IA

| Data | Fase | Ferramenta / modelo | Finalidade | Verificação feita |
|---|---|---|---|---|
| 21/09/2026 | 0 | Claude | Leitura da dissertação, diagnóstico inicial e elaboração deste plano | revisão delegada ao Coordenador (decisão do autor, 27/09/2026); conferência humana na redação |
| 21/09/2026 | 0 | Claude Code (claude-sonnet-5) | Reorganização do repositório, criação da estrutura por fase, templates e catálogo do acervo de 2010 (`docs/catalogo-acervo-2010.md`) | Contagens e achados conferidos por comando no disco; catálogo: revisão delegada ao Coordenador (decisão do autor, 27/09/2026); conferência humana na redação |
| 21/09/2026 | 0 | Claude Code (claude-sonnet-5) | Extração do texto e das 44 tabelas do docx; construção do dataset de 2010 em CSV; conferência contra `script.sql`, planilhas e XML do itSIMPLE; documentação das condições de execução; `MEMORY.md` | Conferência automática entre fontes independentes (SQL, planilha, XML); duas leituras iniciais erradas foram detectadas e corrigidas. **Conferência manual do autor concluída em 21/09/2026** |
| 21/09/2026 | 0 | Claude Code (claude-sonnet-5) | Leitura visual das Figuras 26 e 27 (diagramas de classes de TPP e Pathways) para identificar os modelos itSIMPLE; avaliação das pastas `itsimple-*` | Figuras lidas e conferidas contra o XML; contagens automáticas reproduzíveis por script. **Leitura visual das figuras: confirmada pelo autor em 21/09/2026** |
| 21/09/2026 | 0 | Claude Code (claude-sonnet-5) | Comparação de conteúdo entre os PDDL do acervo e o repositório `potassco/pddl-instances` (IPCs 1998–2008); construção do script e do documento | Correspondências verificadas por comparação de conteúdo e reproduzíveis por script (repositório externo em commit fixo). Variantes de Zeno-travel e Elevator: hipóteses, a confirmar |

| 22–23/09/2026 | 1 | Claude Code — Coordenador (claude-opus-5) + 45 execuções de subagentes (claude-sonnet-5) | Fase 1 inteira: protocolo, busca em 8 eixos, triagem, verificação de metadados, leitura e extração de 153 obras, 8 sínteses, rascunho do capítulo 2 e parecer crítico | Coordenador reconferiu: amostra de 32 itens da busca, todas as 115 entradas com DOI e as 19 do arXiv, 4 números centrais de notas nos PDFs originais e os 9 achados do parecer crítico. Registro completo em `literatura/protocolo/qc-coordenador.md`. **Revisão delegada ao Coordenador (decisão do autor, 27/09/2026); conferência humana na redação** |

| 23/09/2026 | 1 | Claude Code (claude-opus-5-5) | Tratamento das pendências da Fase 1: confirmação da triagem por critérios com dados do OpenAlex; resolução das duas notas com versão divergente; veículo do itSIMPLE 2005 confirmado no site oficial; limpeza mecânica do `candidatas.bib`; lista de revisão e script de promoção das referências | Critérios e resultado registrados no protocolo (seção 9) e em `triagem.csv`. **A revisão das referências é do autor** |

| 23/09/2026 | 1 | Claude Code (claude-opus-5-5) | Fechamento da Fase 1: leitura das obras enviadas pelo autor, contagem de citações das ressalvas (OpenAlex e Semantic Scholar), geração do `referencias.bib`, ajuste do capítulo 2 para citar só obras aprovadas | Cada substituição de citação no capítulo conferida contra a nota da obra substituta; conversão com Pandoc testada com o `referencias.bib`. **Texto final é do autor** (Fase 6) |

| 23/09/2026 | 2 | Claude Code — Coordenador (claude-opus-5-5) + 15 subagentes (5 claude-haiku-4-5, 10 claude-sonnet-5), alguns retomados para correção | Fase 2 inteira: extração de 349 afirmações, fontes primárias dos 10 planejadores e dos 2 trabalhos relacionados de 2010, conferência numérica, classificação, nova taxonomia, plano de reexecução, relatório de auditoria e material do M1 | Coordenador: literalidade dos trechos por script; médias, taxa de acerto e linha de base recalculadas por script; DOIs e URLs das fontes novas reconferidos; 21 revisões de classificação registradas; nota do MAXPLAN e taxonomia corrigidas. Falhas dos agentes e correções em `plan/fase2-estrategia-multiagentes.md`, seção 6. **Revisão delegada ao Coordenador (decisão do autor, 27/09/2026); conferência humana na redação**; o autor leu as 84 "reformula"/"descarta" |

| 23/09/2026 | 2 | Claude Code — Coordenador (claude-opus-5-5) | Revisão das 101 afirmações "reformula"/"descarta" | Conferência em fontes primárias: relatórios das IPCs 1998–2004 (AI Magazine, JAIR) e resultados brutos das IPCs 1998 e 2006, agregados por script; listas de participantes e domínios de cada IPC cruzadas com os 38 pares de "competição" de 2010. **Lida pelo autor em 23/09/2026** (as 84 "reformula"/"descarta") |

| 23/09/2026 | 2 | Claude Code — Coordenador (claude-opus-5-5) | Resolução das pendências da auditoria | Conferência nos logs do acervo (G21), em Weld 1994, Bonet e Geffner 2001, relatórios das IPCs, resumo do SatPlan 2006 e site da IPC 2006; trechos das 6 notas novas e suas páginas conferidos por script contra o PDF; metadados do OJS e do Crossref. Promoção de referências por delegação do autor. **Revisão delegada ao Coordenador (decisão do autor, 27/09/2026); conferência humana na redação** |

| 23/09/2026 | 6 | Claude Code — Coordenador (claude-opus-5-5) | Rascunhos do capítulo 1 (Introdução) e do capítulo 3 (Revisitando 2010) | Números conferidos contra `auditoria/afirmacoes.csv` e `conferencia-rankings.csv`; 22 e 36 chaves conferidas por `checar_citacoes.py`, todas no `referencias.bib`; usos das obras conferidos nas notas. **Texto final é do autor** |

| 24/09/2026 | 3 | Claude Code — Coordenador (claude-opus-5-5) | EXP-01: provisionamento da máquina OrbStack e teste dos 10 planejadores de 2010 | Planos conferidos nos logs; tempos e comprimentos comparados com os logs de 2010 do acervo; desvios registrados no EXP-01 |

| 24/09/2026 | 3 | Claude Code — Coordenador (claude-opus-5-5) | EXP-02: extração dos tempos de 2010 e calibração do limite | Extração conferida contra as contagens de 2010 (43 de 48) e contra leitura manual; erro de leitura de minutos no Blackbox detectado e corrigido; achado G22 |

| 24/09/2026 | 3 | Claude Code — Coordenador (claude-opus-5-5) | EXP-03: reprodução do método de 2010 por script (Nível 1) | Cada etapa comparada célula a célula com as tabelas publicadas; regras inferidas testadas contra alternativas (discretização descrita × extremos; arredondamentos; conjuntos de técnicas) |

| 24/09/2026 | 3 | Claude Code — Coordenador (claude-opus-5-5) | EXP-04: Nível 2, cenário da discretização pela regra do texto | Referência reproduz o método de 2010 com a aritmética corrigida; efeitos comparados com a linha de base de G20 |
| 25/09/2026 | 4B | Claude Code (claude-opus-5-5) | Proposta e desenho da Fase 4B a partir da ideia do autor | Chaves citadas conferidas no `referencias.bib`; duas obras sugeridas fora dele marcadas como não citáveis; disponibilidade dos dados das IPCs marcada `[A CONFIRMAR]`. **Desenho detalhado em 27/09/2026** (`docs/fase4b-desenho.md`, decisões D1 e D2 por delegação do autor) |
| 25/09/2026 | 3 | Claude Code (claude-opus-5-5) | Operação da rodada no GCP (`gcp.sh`), conferência dos casos sem plano e achado G25 | Cada "sem plano" conferido no log bruto e comparado com os logs de 2010; variante testada localmente (gera as 20 execuções esperadas) |
| 27/09/2026 | 3 | Claude Code (claude-opus-5-5) | EXP-05: fim da rodada, conferência das chamadas de 2010, refação do TPP e resumo agora × 2010 | Cada divergência conferida nos logs brutos e nos scripts de 2010; hipótese das constantes do Pipesworld testada e descartada; resumo por script |
| 27/09/2026 | 3 | Claude Code (claude-opus-5-5) | EXP-19: método de 2010 com as notas do Nível 3 | Regra da nota conferida contra as 100 notas de 2010 (99 iguais); reuso do método do Nível 2 sem alteração; maior mudança (Blackbox × Logistics) conferida nos logs |
| 27/09/2026 | 3 | Claude Code (claude-opus-5-5) | EXP-20: qualidade dos planos do Nível 3 | Leitores de plano conferidos entre planejadores no mesmo problema; resumo do LPG-TD conferido contra 765 planos; casos extremos (R, SATPlan) conferidos nos logs |
| 27/09/2026 | 3 | Claude Code (claude-opus-5-5) | Relatório da Fase 3: síntese de Q1 e Q2 a partir dos EXP-03 a EXP-20 | Cada número tirado de um registro de experimento; chaves citadas conferidas no `referencias.bib`; respostas marcadas como hipótese até a validação do autor |
| 27/09/2026 | 4 | Claude Code (claude-opus-5-5) | Relatório da Fase 4: resposta a Q3 a partir dos EXP-14 a EXP-18 e proposta de posição dos LLMs na taxonomia 4D | Cada número tirado de um registro de experimento; chaves citadas conferidas no `referencias.bib`; comparação com seletores da literatura marcada como não feita; resposta marcada como hipótese até a validação do autor |
| 26/09/2026 | 3 | Claude Code (claude-opus-5-5) | EXP-06 (R-10: método de 2010 com a taxonomia em 4 dimensões) e EXP-07 (R-25: extrator das métricas de 2010 a partir do PDDL) | Codificação da taxonomia rastreada ao §3 de `taxonomia-tecnicas.md`, com 5 decisões (C1–C5) aprovadas pelo autor; regras do extrator fixadas antes da comparação; divergências conferidas nos arquivos PDDL. **Codificação C1–C5 aprovada pelo autor em 26/09/2026** |
| 26/09/2026 | 3 | Claude Code (claude-opus-5-5) | EXP-08: Nível 2, R-11, R-12, R-13 e R-15 | Classes alteradas e efeito nas notas previstas conferidos por script; critérios de Agregação contados nos 13 XML e comparados com a Tabela 9 |
| 26/09/2026 | 3 | Claude Code (claude-opus-5-5) | EXP-09: R-14, perda em relação ao *virtual best* | Perdas conferidas contra as notas observadas de `validacao_ranking.csv` (máximo, empates, perda ao acaso) |
| 26/09/2026 | 3 | Claude Code (claude-opus-5-5) | EXP-10: R-16, robustez da discretização com 18 domínios adicionais das IPCs 1998–2008 | Regra de seleção fixada antes de rodar; revisão (exclusão de variantes aterradas) registrada com o resultado anterior; variantes conferidas por contagem de ações |
| 26/09/2026 | 3 | Claude Code (claude-opus-5-5) | EXP-11: R-26, *features* SAS+ e comparação com as métricas UML | *Features* fixadas antes de rodar a partir da síntese E2; ajuste do Pathways verificado (só a constante duplicada sai); correlações com teste de permutação de semente fixa |
| 26/09/2026 | 3 | Claude Code (claude-opus-5-5) | Preparação do Nível 4 (R-24): artefato do Planner Museum localizado e inspecionado; Tabela 1 do suplementar extraída; proposta em `experimentos/nivel4-proposta.md` | Links do artefato lidos no PDF do artigo; tabela conferida pela soma das colunas contra a linha Total. **Decididas pelo autor em 26/09/2026** (só dados publicados, Autoscale) |
| 26/09/2026 | 3 | Claude Code (claude-opus-5-5) | EXP-12: Nível 4 com dados publicados (Planner Museum × *features* do PDDL) | Mapeamento de nomes dos domínios conferido (41 + Pathways); VBS e SBS recalculados à parte; amostra de instâncias e tempos esgotados registrados |
| 26/09/2026 | 3 | Claude Code (claude-opus-5-5) | EXP-13: classificação dos 29 planejadores do Planner Museum na taxonomia 4D e Nível 4 por técnica | 22 planejadores com fonte primária (notas de leitura e resumos oficiais das IPCs de 2018 e 2023), 7 só com fonte secundária, marcados; uma citação não lida (relatório da IPC 2014) retirada antes do commit; contagens do registro conferidas contra o CSV. Codificação aprovada pelo autor |
| 26/09/2026 | 4 | Claude Code (claude-opus-5-5); modelos avaliados via OpenRouter: claude-sonnet-5, gpt-6-sol, gemini-3.1-pro-preview, deepseek-v4-pro-0813 | EXP-14: X3, LLM como seletor, condição anônima; US$ 2,69 | Protocolo aprovado antes das chamadas; regras de avaliação fixadas antes da primeira chamada; respostas brutas versionadas; chave fora do git |
| 26/09/2026 | 4 | Claude Code (claude-opus-5-5); os mesmos 4 modelos via OpenRouter | EXP-15: X3, condição com nomes; US$ 2,64 | Única diferença para o EXP-14 é o nome e a IPC no catálogo; código commitado antes das chamadas; rodada anônima repontuada e conferida |
| 26/09/2026 | 4 | Claude Code (claude-opus-5-5); os 4 modelos via OpenRouter | EXP-16: X1, LLM como planejador; VAL e Fast Downward compilados no Mac; US$ 1,21 | Validador testado com plano embaralhado e incompleto; referência do LAMA validada; falhas de formato separadas das de conteúdo |
| 26/09/2026 | 4 | Claude Code (claude-opus-5-5); os 4 modelos via OpenRouter | EXP-17: X4, ciclo LLM + VAL nas instâncias p05; US$ 2,35 | Checagem do VAL reforçada (linha exata) e X1 reavaliado sem mudança; conversas cortadas pela trava marcadas; alarme falso do VAL investigado (meta satisfeita no estado inicial) |
| 26–27/09/2026 | 4 | Claude Code (claude-opus-5-5); os 4 modelos via OpenRouter | EXP-18: X2, LLM como tradutor; US$ 0,65; fechamento da Fase 4 (US$ 10,51 no total, conferido pela soma dos registros) | Dois artefatos da medida (assinatura das ações; checagem de tipos do VAL) e dois erros do classificador encontrados e corrigidos antes do registro |
| 27/09/2026 | 4B | Claude Code (claude-opus-5-5) | Levantamento das fontes de resultados das IPCs 2011–2023 (sites oficiais, Internet Archive, GitHub, Zenodo); script de contagem; reconferência de metadados de `ferber2019ipc` e `ferber2022explainable` | Contagens de 2018, 2023 e IBM geradas por script e conferidas com os totais publicados (18 × 280 = 5.040; 2.439 × 17); números de 2011 e 2014 tirados dos *slides*, sem script; indisponibilidade dos arquivos de 2011 e 2014 conferida no DNS e no índice do Internet Archive |
| 27/09/2026 | 4B | Claude Code (claude-opus-5-5) | Leitura do texto integral de `vallati2018what` (PDF do autor): nota reescrita; `eid` e páginas no `.bib`; levantamento da 4B atualizado | Trechos literais copiados do PDF; números conferidos contra as tabelas do artigo; três inconsistências internas do artigo registradas na nota; metadados de López et al. (2015) conferidos no Crossref |
| 27/09/2026 | 4B | Claude Code (claude-opus-5-5) | Verificação do site da IPC 2023 e dos *slides*; script de suporte a PDDL declarado (65 receitas) | Somas das tabelas conferidas; contagem de receitas conferida com os *slides* (65) e com as tabelas (66 entradas, FSM em duas trilhas); extração dos rótulos repetida por dois caminhos (API do GitHub e script) com o mesmo resultado |
| 27/09/2026 | 4B | Claude Code (claude-opus-5-5) | Recuperação dos resultados por instância da IPC 2011 a partir do *dump* do WebPlan arquivado no Software Heritage (pista do autor); script de exportação e validação | Ordem oficial reproduzida em duas trilhas e fato de `coles2012survey` conferido dentro do script (falha se não bater); *multi-core* não confere e foi excluída; erro anterior do levantamento ("*slides* com placar por domínio") encontrado ao renderizar a página e corrigido |
| 27/09/2026 | 4B | Claude Code (claude-opus-5-5) | Conferência dos *slides* e do *booklet* da IPC 2014; inclusão de três entradas no `candidatas.bib`; exportação dos resultados por execução da IPC 2018 (`scripts/ipc2018.py`) | Metadados das entradas tirados do PDF do *booklet*; números de *features* (35 e 65) conferidos no texto; somas de cobertura, nota e erros de cada algoritmo de 2018 conferidas contra a tabela *Summary* do relatório oficial dentro do script (falha se não bater); correção do levantamento sobre variantes do `settlers` |
| 27/09/2026 | 4B | Claude Code (claude-opus-5-5) | *Features* SAS+ das IPCs (`scripts/features_ipc.py`); ligação dos problemas de 2011 aos PDDL por SHA-1 (Software Heritage); decisões D1 e D2 por delegação do autor; codificação 4D de 78 planejadores × trilha a partir dos resumos oficiais (*booklet* de 2011 recuperado do Internet Archive; resumos de 2018) | Extrator da Fase 3 reaproveitado sem mudança; ligação de 2011 conferida por SHA-1, sem divergência; erro do `pddl-instances` (floortile ótimo de 2011) encontrado pela ligação e confirmado arquivo por arquivo; critério G1 revisto antes do uso por contradizer o EXP-13; o script da taxonomia falha se algum planejador dos resultados ficar sem codificação; afirmações sem fonte retiradas antes do commit |
| 27/09/2026 | 4B | Claude Code (claude-opus-5-5) | EXP-21 (Q5): mapa família × domínio e modelos por instância com validação deixando um domínio de fora | Tabelas do registro conferidas contra os CSVs de saída (uma célula e uma contagem corrigidas antes do commit); número do EXP conferido com a reserva da outra sessão; afirmações marcadas como provisórias até a ligação de 2011 e as *features* de 2018 ficarem completas |
| 27/09/2026 | 1–4 | Claude Code (claude-opus-5-5) | Avaliação geral das Fases 1 a 4 como Coordenador (feito, pendências, problemas não percebidos); estimativa do custo do teste de serialização | Citações conferidas por `checar_citacoes.py`; Nível 1, Nível 3, EXP-19 e EXP-12 reexecutados sem diferença nos CSVs; custo estimado pelas horas de `nivel3-2010-gcp.csv`; origem do PDDL de 2010 conferida em `docs/benchmarks-ipc-ate-2008.md`. **As demais correções de registro apontadas aguardam o autor** |
| 27/09/2026 | 6 | Claude Code (claude-opus-5-5) | Ajuste do capítulo 2 (rascunho de IA) para não contradizer a resposta a Q3: introdução, fecho da seção de modelos de linguagem e parágrafo de Q3 | Posição conferida na nota de `kambhampati2024llms` (LLM-Modulo com VAL); nenhuma chave nova; 83 chaves conferidas por `checar_citacoes.py`; números do capítulo 6 não trazidos para o capítulo 2. **Texto final é do autor** |
| 27/09/2026 | 6 | Claude Code (claude-opus-5-5) | Ajuste do capítulo 2 (rascunho de IA) à dispensa do controle de serialização: introdução, hipótese da seção de engenharia do conhecimento, parágrafo de Q2 e síntese final | Origem do PDDL de 2010 conferida em `docs/benchmarks-ipc-ate-2008.md` e no G25 (exceção do Satellite acrescentada); nenhuma chave nova; 83 chaves conferidas por `checar_citacoes.py`. **Texto final é do autor** |
| 27/09/2026 | 3, 4 | Claude Code (claude-opus-5-5) | Correção de Holm para as comparações com o *single best* (EXP-12, EXP-13, X3); calibração da redação de Q2 e Q3 nos relatórios e registros; limpeza de registros desatualizados | p-valores brutos recalculados a partir das escolhas por domínio e iguais aos registros; famílias de comparação fixadas antes de ver os ajustados; cada frase alterada conferida contra o registro do experimento; substância das respostas validadas não mudou. **Mudanças de redação a confirmar pelo autor** |
| 27/09/2026 | 3 | Claude Code (claude-opus-5-5) | EXP-22: tempo e memória do Nível 3 | Método (escore T\*/T com piso de 1 s, Spearman por domínio, teto de 3,5 GB) fixado antes de rodar; contagens de memória conferidas por situação e domínio; uma frase sobre líderes retirada por depender de desempate |
| 27/09/2026 | 4 | Claude Code (claude-opus-5-5); os 4 modelos via OpenRouter | EXP-23: X1 com nomes ofuscados; US$ 1,59 | Código commitado antes das chamadas; equivalência dos arquivos ofuscados conferida pelo VAL nos dois sentidos (o primeiro critério, tamanho do plano do LAMA, foi trocado antes das chamadas e registrado); respostas cortadas conferidas pelos *tokens* de raciocínio; número da literatura conferido na nota de `valmeekam2023planbench`. **Teto ultrapassado em US$ 0,08 por chamadas em paralelo** |
| 27/09/2026 | 4 | Claude Code (claude-opus-5-5); os 4 modelos via OpenRouter | EXP-23, complemento: 7 pares em sequência; US$ 0,45 | Modo sequencial commitado antes das chamadas; trava de US$ 12,80 respeitada (uso final US$ 12,49); os 32 pares reavaliados pelo VAL; resposta de formato do DeepSeek (Gripper) conferida no registro bruto |
| 27/09/2026 | 5 | Codex (GPT-5) + skill editorial `chief-editor` | Consolidação exploratória da Ponte a partir das sínteses E7/E8, relatórios das Fases 3–4 e EXP-21; atualização do README da fase | Oito chaves verificadas por `checar_citacoes.py`; fatos, inferências e hipóteses separados no relatório; sem fontes fora do `referencias.bib`; integração da 4B permanece pendente |
| 27/09/2026 | 5 | Codex (GPT-5) + skills editoriais `chief-editor` e `conceptual-challenger` | Aprofundamento da Ponte em dossiê para o Capítulo 7: escada de inferência, aplicabilidade, hipóteses concorrentes, alegações permitidas/proibidas e arquitetura de redação | Treze chaves verificadas por `checar_citacoes.py`; auditoria conceitual separa associação, causalidade e aplicação; não há alegação de produto, piloto ou eficácia local |

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
>
> **Atualização de 27/09/2026:** as 22 estão no `referencias.bib` (conferido por chave). O fluxo de aprovação não usa mais o Zotero (decisão de 23/09/2026).

| Referência (provisória) | Eixo | Status |
|---|---|---|
| Rice (1976) — The algorithm selection problem | E1 | 🟢 no `referencias.bib` |
| Roberts & Howe (c. 2008–2009) — predição de desempenho de planejadores | E2 | 🟢 no `referencias.bib` |
| Gerevini, Saetti & Vallati — PbP (portfolio-based planner) | E1 | 🟢 no `referencias.bib` |
| Helmert, Röger et al. (2011) — Fast Downward Stone Soup | E1 | 🟢 no `referencias.bib` |
| Cenamor, de la Rosa & Fernández — IBaCoP | E1 | 🟢 no `referencias.bib` |
| Sievers et al. (c. 2019) — Delfi | E1 | 🟢 no `referencias.bib` |
| Fawcett et al. (2014) — *features* para predição de desempenho de planejadores | E2 | 🟢 no `referencias.bib` |
| Richter & Westphal (2010) — LAMA | E3 | 🟢 no `referencias.bib` |
| Helmert & Domshlak (2009) — LM-cut | E3 | 🟢 no `referencias.bib` |
| Lipovetzky & Geffner (2012, 2017) — busca por largura, BFWS | E3 | 🟢 no `referencias.bib` |
| Toyer et al. (2018) — ASNets | E4 | 🟢 no `referencias.bib` |
| Ståhlberg, Bonet & Geffner (c. 2022) — GNNs para políticas generalizadas | E4 | 🟢 no `referencias.bib` |
| Valmeekam et al. (2023) — PlanBench | E5 | 🟢 no `referencias.bib` |
| Liu et al. (2023) — LLM+P | E5 | 🟢 no `referencias.bib` |
| Kambhampati et al. (2024) — LLM-Modulo | E5 | 🟢 no `referencias.bib` |
| Vaquero et al. — evolução do itSIMPLE | E6 | 🟢 no `referencias.bib` |
| Unified Planning Framework (AIPlan4EU) | E6 | 🟢 no `referencias.bib` |
| Wolpert & Macready (1997) — No Free Lunch | E7 | 🟢 no `referencias.bib` |
| Lawrence & Lorsch (1967) — teoria da contingência | E7 | 🟢 no `referencias.bib` |
| Goodhue & Thompson (1995) — *task-technology fit* | E7 | 🟢 no `referencias.bib` |
| Ong et al. (2024) — RouteLLM | E7 | 🟢 no `referencias.bib` |
| Jimenez et al. (2024) — SWE-bench | E8 | 🟢 no `referencias.bib` |

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
| 0.20 | 23/09/2026 | M1 enviado ao orientador; leitura das 84 feita pelo autor; Fase 3 no OrbStack (ressalva: binários de 2010 são 32-bit i386); rascunhos dos capítulos 1 e 3; `haddad2010relacao` no `referencias.bib` (151 obras) |
| 0.21 | 24/09/2026 | Retorno do M1 registrado: taxonomia validada pelo orientador, demais pontos de acordo; sem artigo, só a dissertação final; ações 12 e 14 concluídas |
| 0.22 | 24/09/2026 | Fase 3 iniciada: máquina OrbStack provisionada; os 10 planejadores de 2010 rodam (EXP-01); emulação 4–8× mais lenta que 2010; ação 19 (limite de tempo) |
| 0.23 | 24/09/2026 | EXP-02: limites calibrados por planejador (38 a 137 min); achado G22 (Blackbox sem limite no Depots e DriverLog em 2010); ação 19 concluída |
| 0.24 | 24/09/2026 | Nível 1 da Fase 3 concluído (EXP-03): método de 2010 reproduzido por script; achados G23 (discretização por extremos) e G24 (duas taxonomias); G6 resolvido |
| 0.25 | 24/09/2026 | EXP-04: regra de discretização do texto como cenário do Nível 2 (decisão do autor); corrigida a aritmética, acerto de 2010 cai para 50/30/40% |
| 0.26 | 25/09/2026 | Nova Fase 4B (panorama das IPCs posteriores a 2010, dados publicados, sem UML.P) entre as Fases 4 e 5; pergunta Q5; expansão de escopo registrada; Fase 5 passa a começar depois da 4B |
| 0.27 | 25/09/2026 | Marco M2 cancelado; o M3 é o envio da dissertação reescrita por e-mail, com retorno posterior; status geral atualizado |
| 0.28 | 25/09/2026 | Nível 3 migrado para o GCP (orçamento e desligamento automático); achado G25 (Blackbox com `-M 8192` só no Satellite em 2010) e variante `blackbox-m8192` para o fim da rodada; máquina OrbStack apagada, brutos preservados |
| 0.29 | 26/09/2026 | EXP-06 (R-10): taxonomia em 4 dimensões aplicada ao método de 2010, sem ganho claro sobre a linha de base; EXP-07 (R-25): extrator das métricas de 2010 a partir do PDDL |
| 0.30 | 26/09/2026 | Codificação 4D aprovada pelo autor; EXP-08: R-11 (rótulo G1), R-12 (correções G17), R-13 (classes com auxiliares; Agregação não reconstruível) e R-15 (linha de base); nenhum ranking de 2010 muda |
| 0.31 | 26/09/2026 | Agregação registrada como não reproduzível (contagem visual e manual); G19 decidido (perda em relação ao *virtual best*); EXP-09 (R-14): no Storage, único domínio discriminante, o método de 2010 perde para a linha de base |
| 0.32 | 26/09/2026 | EXP-10 (R-16): a classe Alto/Médio/Baixo depende da amostra de domínios; **Nível 2 concluído** |
| 0.33 | 26/09/2026 | EXP-11 (R-26): extrator de *features* SAS+ (grafo causal, DTG, *treewidth*); métricas UML sem correlação com elas acima do acaso |
| 0.34 | 26/09/2026 | Preparação do Nível 4: Planner Museum (29 planejadores, Autoscale 42 × 30) localizado; cobertura publicada em `data/planner-museum/`; proposta com decisões pendentes |
| 0.35 | 26/09/2026 | Nível 4 só com dados publicados (decisão do autor); EXP-12: por domínio, nenhuma característica do PDDL supera o *single best* (Levitron) |
| 0.36 | 26/09/2026 | EXP-13: 29 planejadores na taxonomia 4D; o método de 2010 por técnica perde para o *single best*; o mapa mostra técnicas antigas vencendo em poucos domínios (System R, SAT) |
| 0.37 | 26/09/2026 | Fase 4 iniciada (X3, via OpenRouter, teto de US$ 10); protocolo do X3 com proposta de modelos |
| 0.38 | 26/09/2026 | EXP-14 (X3): LLMs como seletores, condição anônima; nenhum supera o *single best*; escolhem quase sempre portfólios; gasto US$ 2,69 de US$ 10 |
| 0.39 | 26/09/2026 | EXP-15 (X3 com nomes): sem sinal de lembrança dos resultados por domínio; escolhas por reputação; gasto acumulado US$ 5,34 |
| 0.40 | 26/09/2026 | EXP-16 (X1): 28 de 32 planos válidos nas instâncias menores; acumulado US$ 6,56 |
| 0.41 | 26/09/2026 | EXP-17 (X4, parcial): o retorno do VAL recupera 3 de 6 falhas; LLMs resolvem o Floortile p05; acumulado US$ 8,92; X2 preparado, sem rodar |
| 0.42 | 27/09/2026 | EXP-18 (X2); X4 completo; **Fase 4 concluída** (X1–X4 registrados; US$ 10,51 de US$ 12) |
| 0.43 | 27/09/2026 | **Fase 4B iniciada** em paralelo ao Nível 3 (decisão do autor); levantamento das fontes das IPCs 2011–2023 (`docs/resultados-ipc-2011-2023.md`, `data/ipc-2011-2023/`) |
| 0.44 | 27/09/2026 | `vallati2018what` lido em texto integral: a IPC 2014 só tem totais por trilha publicados; protocolo de seleção de instâncias pelos competidores registrado como viés para a 4B |
| 0.45 | 27/09/2026 | Site da IPC 2023 verificado: dados por instância existem e são oferecidos sob pedido; suporte a PDDL declarado por planejador em `data/ipc-2011-2023/suporte_pddl_2023.csv` |
| 0.46 | 27/09/2026 | IPC 2011 por instância recuperada do WebPlan (Software Heritage), validada contra a ordem oficial; correção: os *slides* de 2011 não têm números |
| 0.47 | 27/09/2026 | IPC 2014: *slides* e *booklet* dos participantes conferidos (sem resultados por domínio; *hardware* de 2014 registrado; *booklet* como fonte para a 4D e a regra dos portfólios) |
| 0.48 | 27/09/2026 | Nível 3 concluído (EXP-05): 3.390 execuções no GCP, 50 de 63 pares iguais a 2010; G25 ampliado (domínio do Satellite de 2010) e G26 (chamadas de 2010 no TPP e no Pathways); VM apagada |
| 0.49 | 27/09/2026 | Fase 4B: *booklet* de 2014 e resumos do IBaCoP e do AllPACA no `candidatas.bib`; resultados por execução da IPC 2018 exportados e validados contra o relatório oficial; ZIP de 2014 movido para `brutos/` |
| 0.50 | 27/09/2026 | EXP-19: método de 2010 com as notas do Nível 3 (23 de 100 notas mudam, quase todas de competição; perda × VBS igual; Spearman sobe no Elevator); decisões: R sem tratamento, sem VAL, validação com o ranking de 2010 |
| 0.51 | 27/09/2026 | Fase 3: checkboxes atualizados; R-19 decidido; R-22 feito (EXP-20, qualidade dos planos); R-23, R-30 e R-31 dispensados; falta a síntese de Q1 e Q2 |
| 0.52 | 27/09/2026 | Relatório da Fase 3 (`experimentos/relatorio-fase3.md`) com as respostas a Q1 e Q2, para validação do autor; R-27 feito por domínio |
| 0.53 | 27/09/2026 | **Fase 3 concluída**: Q1 e Q2 validadas pelo autor; R-29 por instância passa para a Fase 4B; restaurada no painel a linha da Fase 6, substituída por engano pela ação 6 no commit `535131c` |
| 0.54 | 27/09/2026 | Fase 4: checkboxes atualizados; relatório com a resposta a Q3 e a posição dos LLMs na taxonomia (`llm/relatorio-fase4.md`), para validação do autor |
| 0.55 | 27/09/2026 | Fase 4 fechada: resposta a Q3 aceita; capítulo 6 definido; taxonomia estendida aos LLMs (seção 6.1); ligação X2–F3 no capítulo 5 |
| 0.56 | 27/09/2026 | Fase 4B: decisões D1 (portfólios) e D2 (recorte) por delegação do autor; codificação 4D de 2011 e 2018; *features* SAS+ das IPCs; ligação de 2011 aos PDDL; fonte do PDDL trocada para o `downward-benchmarks` e o ZIP oficial de 2014 |
| 0.57 | 27/09/2026 | Avaliação geral das Fases 1 a 4; controle de serialização do R-27 dispensado com o orientador e registrado como limitação da Fase 3 |
| 0.58 | 27/09/2026 | Capítulo 2 alinhado à resposta a Q3: LLM como gerador de planos com verificador externo (LLM-Modulo) e tradução como etapa de modelagem; nota de atualização no §2.5 do relatório da Fase 1 |
| 0.59 | 27/09/2026 | Capítulo 2: hipótese da serialização reescrita como limitação da medida de desempenho (ranking numa única ordem do PDDL), com a exceção do Satellite (G25); a mesma ressalva na decisão do R-27 e no relatório da Fase 3 |
| 0.60 | 27/09/2026 | Pendências da avaliação das Fases 1 a 4: correção de Holm (`experimentos/analise/correcao_multipla.py`); redação de Q2 e de Q3 calibrada nos relatórios; registros desatualizados corrigidos (ações 6 e 9, seção 13, G10, R-25, `MEMORY.md`) |
| 0.61 | 27/09/2026 | Decisões do autor sobre a avaliação das Fases 1 a 4: R-29 por instância na 4B; tempo e memória (EXP-22) e X1 ofuscado (EXP-23) a fazer; *gradient boosting* dispensado; delegação aceita para as 265 "mantém"; registro de IA atualizado; capítulo 3 na Fase 6; `sette2008are` excluída; Ghostscript mantido; custo do GCP (US$ 36,42) |
| 0.62 | 27/09/2026 | EXP-22: tempo e memória do Nível 3; o tempo não muda os *rankings* de 2010 (Spearman 0,78–1,00 em 9 de 10 domínios), a qualidade muda mais; 36 dos 393 "sem plano" são memória de 32 bits |
| 0.63 | 27/09/2026 | EXP-23: X1 com nomes ofuscados (16 de 25 válidos contra 23; perdas sobretudo por *tokens*); teto da Fase 4 ultrapassado em US$ 0,08; relatório da Fase 4 atualizado |
| 0.64 | 27/09/2026 | EXP-23 completo (32 pares): 20 de 32 planos válidos com nomes ofuscados, contra 28; limite da chave em US$ 13 (autor); uso final US$ 12,49 |
| 0.65 | 27/09/2026 | Fase 4B: EXP-21 (Q5), primeira rodada provisória; *features* de 2011 e 2014 refeitas nas fontes novas (todas traduzidas); ligação de 2011 com 307 de 560 conferidos |
| 0.66 | 27/09/2026 | Fase 5 redefinida e iniciada: investigação exploratória, sem piloto no Ateliê nem decisão de produto; Q4, atividades, riscos e entregáveis ajustados para conexões, oportunidades e hipóteses testáveis |
| 0.67 | 27/09/2026 | Fase 5: síntese exploratória preliminar e README da Ponte atualizados; conexão com agentes de código e roteamento consolidada com limites explícitos; integração da síntese da 4B permanece pendente |
| 0.68 | 27/09/2026 | Fase 5 aprofundada em dossiê para o futuro Capítulo 7: escada de inferência, aplicabilidade em três níveis, auditoria conceitual, hipóteses falseáveis e arquitetura de redação; síntese da 4B ainda pendente |
