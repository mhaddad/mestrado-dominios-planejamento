# Revisão da Dissertação — Características de Domínios × Técnicas de Planejamento

> **Documento de trabalho.** Controle e acompanhamento da evolução de cada fase.
> Atualize o painel, os checkboxes e os registros ao final de cada sessão de trabalho.

| Campo | Valor |
|---|---|
| Trabalho original | *Relação entre características de domínios e técnicas de planejamento* — Dissertação de Mestrado, Centro Universitário da FEI, 10/03/2010 |
| Autor | Matheus Haddad |
| Orientador original | Prof. Dr. Flavio Tonidandel |
| Início da revisão | 21/09/2026 |
| Última atualização | 21/09/2026 |
| Versão deste documento | 0.2 |
| Status geral | 🟡 Fase 0 em andamento |

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
| 0 | Enquadramento e artefatos | Recuperar material original e montar o ambiente de trabalho | 1 semana | 🟡 | 21/09/2026 | | Acervo organizado + ambiente pronto |
| 1 | Revisão de literatura assistida por IA | Mapear 2008–2026 | 3–4 semanas | ⚪ | | | Novo capítulo de fundamentos + base de referências |
| 2 | Auditoria da versão original | Classificar cada afirmação: mantém / reformula / descarta | 1–2 semanas (paralela à Fase 1) | ⚪ | | | Relatório de auditoria |
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
| Base de conhecimento e rastreabilidade | Obsidian (vault), Zotero |
| Redação e revisão | Claude com as skills de estilo autoral, revisão humana |

---

## 7. Fases detalhadas

### Fase 0 — Enquadramento e recuperação de artefatos

**Objetivo:** reunir o material original e preparar o ambiente para as fases seguintes.

**Atividades**

- [x] Extrair o texto da dissertação e mapear capítulos, tabelas e figuras
- [ ] Localizar os modelos originais do itSIMPLE (UML.P) dos 13 domínios (10 de treino + Storage, Zeno-travel, Elevator)
- [ ] Localizar planilhas com métricas, discretização e notas de eficiência (Tabelas 8–25)
- [ ] Documentar como foram obtidos os dados da 5ª etapa do método (execuções fora das competições): máquina, limite de tempo, versões
- [ ] Transcrever as tabelas da dissertação para CSV (dataset "2010") — **pode ser feito por IA a partir do texto, com conferência manual**
- [x] Criar repositório (código + dados + este documento)
- [ ] Criar estrutura no vault do Obsidian para notas de leitura
- [ ] Definir o formato da nova versão (monografia revisada, artigo, ou ambos)

**Como a IA acelera:** transcrição das tabelas para CSV, criação da estrutura do repositório e de *templates* de notas.

**Entregáveis:** repositório criado · `dataset-2010.csv` · acervo original catalogado

**Critério de conclusão:** dados de 2010 disponíveis em formato processável e ambiente pronto.

**Notas:**

- 21/09/2026 — Catálogo do acervo em [docs/catalogo-acervo-2010.md](../docs/catalogo-acervo-2010.md). `comp/script.sql` já contém o dataset (10 domínios × 17 características discretizadas, 100 notas de eficiência). Anomalia a resolver: domínios 6–10 têm 37 linhas de características em vez de 17. Zeno-travel e Elevator não têm PDDL no acervo, só modelos UML no itSIMPLE. Scripts de execução usam `timeout 1200` (F6).

---

### Fase 1 — Revisão de literatura assistida por IA (2008–2026)

**Objetivo:** reconstruir o capítulo de fundamentos e o estado da arte.

**Eixos de busca**

| Eixo | Tópicos | Status |
|---|---|---|
| E1 | Seleção de algoritmos e portfólios em planejamento (Rice; PbP; Fast Downward Stone Soup; IBaCoP; Delfi; Cedalion) | ⚪ |
| E2 | *Features* de tarefas de planejamento e predição de desempenho (Roberts & Howe; Fawcett et al.; representações em grafo) | ⚪ |
| E3 | Evolução dos planejadores e heurísticas (LAMA, LM-cut, *merge-and-shrink*, busca simbólica, BFWS, Madagascar) e resultados das IPCs 2008–2023 | ⚪ |
| E4 | Aprendizado para planejamento (heurísticas aprendidas, ASNets, GNNs, planejamento generalizado, aprendizado de modelos de ação) | ⚪ |
| E5 | LLMs e planejamento (PlanBench; LLM+P; LLM-Modulo; modelos de raciocínio; agentes) | ⚪ |
| E6 | Engenharia do conhecimento para planejamento (evolução do itSIMPLE, ICKEPS, Unified Planning, LLMs gerando PDDL) | ⚪ |
| E7 | Pontes conceituais (No Free Lunch; teoria da contingência; *task-technology fit*; roteamento de modelos de linguagem) | ⚪ |
| E8 | IA no desenvolvimento de software (agentes de código, SWE-bench e similares, estratégias de orquestração, estudos empíricos em equipes) | ⚪ |

**Atividades**

- [ ] Definir protocolo leve: *strings* de busca, bases, critérios de inclusão/exclusão
- [ ] Rodar buscas por eixo com apoio de IA e montar lista bruta
- [ ] Triagem por título e resumo (IA pré-classifica, autor confirma)
- [ ] Verificar existência e metadados de cada referência selecionada (Zotero)
- [ ] Leitura com extração estruturada: problema, método, dados, resultado, relação com a dissertação
- [ ] Produzir síntese por eixo
- [ ] Redigir rascunho do novo capítulo de fundamentos

**Como a IA acelera:** geração de *strings* de busca, triagem inicial, extração estruturada de artigos, primeiras sínteses por eixo. Estimativa de redução: de 6–8 para 3–4 semanas.

**Entregáveis:** base Zotero verificada · notas de leitura no Obsidian · síntese por eixo · rascunho do capítulo

**Critério de conclusão:** todos os eixos com síntese e todas as referências citadas verificadas.

**Notas:**

---

### Fase 2 — Auditoria da versão original

**Objetivo:** classificar criticamente as afirmações da dissertação. Esta fase pode rodar em paralelo à Fase 1.

**Atividades**

- [ ] Extrair todas as afirmações substantivas (IA gera a lista, autor revisa)
- [ ] Classificar cada uma: **mantém / reformula / descarta**, com justificativa
- [ ] Revisar a taxonomia de técnicas (F4) e propor uma nova, compatível com a literatura atual
- [ ] Documentar condições de obtenção dos dados (F6)
- [ ] Listar o que precisa ser reexecutado na Fase 3
- [ ] Preparar material para o **Marco M1** com o orientador

**Tabela de auditoria**

| # | Afirmação (resumo) | Local | Classificação | Justificativa | Ação |
|---|---|---|---|---|---|
| A1 | Existe relação entre características de domínios e técnicas de planejamento | Cap. 6.1 | | | |
| A2 | As características mais relevantes são nº de casos de uso por atores, atributos, agregações, ações de entrada, associações e transições | Cap. 6.1 | | | |
| A3 | Novos planejadores serão mais promissores se usarem Heuristic Search, Hierarchical, Knowledge-based, Forward-chaining, Plan-Space e Total-order | Cap. 6.1 | | | |
| A4 | O ranking permite escolher o planejador apenas com as características do domínio, independentemente do problema | Cap. 6.1 | | | |
| … | | | | | |

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

**Estrutura proposta da nova versão**

1. Introdução — a pergunta em 2010 e hoje
2. Fundamentos e estado da arte
3. Revisitando 2010 — auditoria
4. Método
5. Resultados experimentais
6. LLMs no mapa das técnicas
7. Do domínio de planejamento ao desenvolvimento de software dirigido por IA
8. Conclusões e próximos passos

**Atividades**

- [ ] Redigir capítulos a partir dos entregáveis das fases anteriores
- [ ] Revisão de consistência (IA aponta inconsistências entre capítulos, dados e referências)
- [ ] Verificação final de todas as referências e números
- [ ] Revisão de estilo na voz do autor
- [ ] Preparar resumo executivo para o orientador
- [ ] Enviar ao orientador (**Marco M3**)
- [ ] Registrar retorno e próximos passos

**Entregáveis:** nova versão do trabalho · resumo executivo · registro do retorno do orientador

**Critério de conclusão:** versão enviada e retorno registrado.

**Notas:**

---

## 8. Riscos

| # | Risco | Probabilidade | Impacto | Mitigação |
|---|---|---|---|---|
| R1 | Expansão de escopo (a Fase 5 pode virar um projeto próprio) | Alta | Alto | Manter o piloto enxuto; decisões de produto só depois do piloto |
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
| 1 | Localizar modelos do itSIMPLE e planilhas originais | 0 | Matheus | | ⚪ |
| 2 | Transcrever tabelas da dissertação para CSV | 0 | IA + conferência de Matheus | | ⚪ |
| 3 | Criar repositório e estrutura no Obsidian | 0 | Matheus + IA | | 🟡 repositório criado em 21/09/2026; falta o Obsidian |
| 4 | Definir protocolo de busca da Fase 1 | 1 | Matheus + IA | | ⚪ |

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

---

## 11. Registro de uso de IA

| Data | Fase | Ferramenta / modelo | Finalidade | Verificação feita |
|---|---|---|---|---|
| 21/09/2026 | 0 | Claude | Leitura da dissertação, diagnóstico inicial e elaboração deste plano | Revisão do autor pendente |
| 21/09/2026 | 0 | Claude Code (claude-sonnet-5) | Reorganização do repositório, criação da estrutura por fase, templates e catálogo do acervo de 2010 (`docs/catalogo-acervo-2010.md`) | Contagens e achados conferidos por comando no disco; catálogo pendente de revisão do autor |

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
