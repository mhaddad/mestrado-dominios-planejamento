---
tipo: sintese-de-eixo
eixo: E1
obras: 20
data: 2026-09-22
---

# E1 — Seleção de algoritmos e portfólios em planejamento

## 1. Pergunta e resposta curta

Como a seleção de algoritmos e os portfólios evoluíram em planejamento desde 2008, e que ganho sobre o *single best* relatam?

[FATO] O campo não nasceu em 2008: sua base formal é Rice (1976) [@rice1976algorithm], e sua primeira aplicação em planejamento é BUS, de Roberts & Howe, sistematizada depois por Vallati, Chrpa & Kitchin [@vallati2015portfolio]. A partir de 2008, a linha se profissionalizou em três ondas: (i) portfólios *offline* por domínio, calibrados por estatística sobre instâncias de treino — PbP [@gerevini2014planning], Fast Downward Stone Soup [@helmert2011fast], Cedalion [@seipp2014fast]; (ii) seleção *per-instance* com *features* automáticas cada vez mais ricas — IBaCoP [@cenamor2016ibacop], até representações de grafo e aprendizado profundo — Delfi [@katz2018delfi], GNN [@ma2020online; @sievers2019deep; @vatter2026beyond]; (iii) infraestrutura compartilhada — ASlib [@bischl2016aslib], AutoFolio [@lindauer2015autofolio], competições de seleção de algoritmo [@lindauer2019algorithm] — e um esforço recente de voltar a modelos interpretáveis [@ferber2022explainable]. O ganho sobre o *single best* é grande e recorrente: 654 vs. 605 instâncias na faixa ótima da IPC [@helmert2011fast], *speedup* médio de 31,8x em cenários gerais de seleção [@lindauer2019algorithm], acurácia subindo de 82%–87% para 91,7% entre 2020 e 2026 [@vatter2026beyond].

## 2. O que a literatura estabelece

### O problema fundacional

[FATO] Rice (1976) formaliza a seleção de algoritmo como mapeamento entre um espaço de problemas, um espaço de algoritmos, uma aplicação de desempenho e, numa extensão, um espaço de *características* extraído do problema antes da seleção [@rice1976algorithm]. Esse arcabouço é reproduzido como ponto de partida de todo *survey* do eixo [@kotthoff2014algorithm; @kerschke2019automated]. Rice já separa "escolher boas características" de "escolher um bom algoritmo dadas as características" — separação que 2010 não faz.

### Portfólios por domínio (offline)

[FATO] PbP deriva estatisticamente (teste de Wilcoxon), por domínio, um portfólio ordenado executado por *round-robin scheduling*; venceu as faixas de aprendizado da IPC6 e IPC7 [@gerevini2014planning]. Fast Downward Stone Soup mostra que combinar poucos "ingredientes" heurísticos (4 de 11) resolve 654 de 673 instâncias, contra 605 do melhor ingrediente isolado [@helmert2011fast]. Cedalion generaliza a ideia com um configurador automático (SMAC), mas reconhece que restringir-se a um único planejador "quase certamente" custou desempenho frente a um portfólio multiplanejador [@seipp2014fast].

### Seleção por instância (online)

[FATO] A comunidade migrou progressivamente de seleção por domínio para seleção por instância [@kerschke2019automated]. IBaCoP filtra planejadores por dominância de Pareto e usa 89 *features* automáticas (PDDL, grafo causal, heurísticas) para prever cobertura e tempo por instância; venceu a IPC 2014, mas os autores concluem que a diversidade do conjunto filtrado, não os modelos preditivos, explica o ganho [@cenamor2016ibacop]. Delfi converte a tarefa em imagem e treina uma CNN por planejador; venceu a faixa ótima da IPC 2018 e escolhe planejadores diferentes para instâncias distintas do mesmo domínio [@katz2018delfi]. GNNs homogêneas com escalonamento adaptativo elevam a cobertura de 87,6% para 89,7% [@ma2020online]; GNNs heterogêneas (RGCN/RGAT) com portfólio reduzido de 17 para 6 planejadores via valores de Shapley chegam a 91,7% de acurácia [@vatter2026beyond]. Uma exploração sistemática mostra que "não há receita única" e que dividir os dados sem preservar a estrutura por domínio piora a cobertura [@sievers2019deep]. Em contraponto, uma regressão linear simples e interpretável resolve aproximadamente o mesmo número de tarefas que o Delfi1 [@ferber2022explainable].

### Infraestrutura compartilhada

[FATO] SATzilla, fora de planejamento mas referência fundacional, formaliza o portfólio "(a,b)-of-n" e usa 48 *features* de SAT para prever tempo por regressão, vencendo cinco medalhas na Competição SAT 2007 [@xu2008satzilla]. ASlib padroniza formato e repositório de cenários [@bischl2016aslib]; AutoFolio configura automaticamente a própria estratégia de seleção, superando o melhor solucionador único em 8 de 13 cenários [@lindauer2015autofolio], sobre o *framework* de configuração ParamILS [@hutter2009paramils]. As competições de seleção de algoritmo relatam *speedup* médio de 31,8x do *virtual best solver*, mas nenhum sistema domina todos os cenários [@lindauer2019algorithm]. Um catálogo de boas práticas alerta que medir a métrica errada é armadilha comum em comparações empíricas [@eggensperger2019pitfalls].

## 3. Percurso 2008–2026

[FATO] 1974–1976: Rice formaliza o problema de seleção de algoritmo por características [@rice1976algorithm]. 2008: SATzilla consolida o portfólio *per-instance* com *features* de SAT [@xu2008satzilla]. 2011: Fast Downward Stone Soup estabelece uma linha de base forte de portfólio sequencial sem *features* de instância [@helmert2011fast]. 2014: PbP e Cedalion consolidam portfólios domain-specific configurados automaticamente, vencendo faixas de aprendizado das IPCs [@gerevini2014planning; @seipp2014fast]. 2015–2016: ASlib e AutoFolio criam infraestrutura compartilhada e configuração automática de seletores [@bischl2016aslib; @lindauer2015autofolio]; IBaCoP2 vence a faixa satisfativa sequencial da IPC 2014 com seleção *per-instance* baseada em 89 *features* [@cenamor2016ibacop]. 2018: Delfi desloca a seleção para representações de grafo/imagem e CNN, vencendo a faixa ótima da IPC 2018 [@katz2018delfi]. 2019: dois *surveys* (Kotthoff; Kerschke et al.) consolidam o campo e mapeiam a linhagem de *features* de planejamento desde 1999 [@kotthoff2014algorithm; @kerschke2019automated]; Sievers et al. mostram os limites da generalização de aprendizado profundo em seleção de planejador [@sievers2019deep]. 2020: GNNs com escalonamento adaptativo superam CNN [@ma2020online]. 2022: um contramovimento busca interpretabilidade com *features* simples [@ferber2022explainable]. 2026: GNNs heterogêneas com seleção de planejadores por valores de Shapley atingem 91,7% de acurácia, sem qualquer uso de LLM [@vatter2026beyond].

## 4. Relação com a dissertação de 2010

| Rótulo | Relação | O que a literatura mostra | Chaves |
|---|---|---|---|
| A1 | confirma (princípio), amplia (granularidade) | Características de domínio/instância predizem a técnica de melhor desempenho é o princípio fundacional de todo o campo (Rice) e é reconfirmado repetidamente com dados atuais, mas a unidade preditiva relevante migrou de "domínio" para "instância" | [@rice1976algorithm; @kotthoff2014algorithm; @kerschke2019automated; @xu2008satzilla; @ferber2022explainable; @katz2018delfi; @ma2020online; @sievers2019deep; @vatter2026beyond] |
| A3 | corrige | Seleção fixa por domínio tem teto de desempenho mais baixo que seleção dinâmica por instância; sistemas *per-instance* escolhem planejadores diferentes dentro do mesmo domínio | [@cenamor2016ibacop; @katz2018delfi; @kerschke2019automated] |
| A4 | amplia (com ressalva) | Mais planejadores tendem a melhorar o portfólio, mas com custo de configuração crescente; e "menos planejadores complementares" também pode bastar (*set covers* de tamanho 3) | [@seipp2014fast; @katz2018delfi] |
| A6 | corrige | Fast Downward é descrito, em múltiplas fontes primárias, como busca heurística A*/gulosa sobre diversas heurísticas, não como planejamento hierárquico HTN; SATPlan é classificado como *planning framework*, não como técnica *plan-space* no sentido de portfólio | [@helmert2011fast; @seipp2014fast; @vallati2015portfolio] |
| A7 / F5 | corrige (mostra alternativa) | Cobertura é só um de pelo menos três alvos possíveis de avaliação (tempo, qualidade, número de problemas resolvidos); portfólios de referência já usam métricas sensíveis à qualidade da solução | [@vallati2015portfolio; @helmert2011fast; @eggensperger2019pitfalls] |
| A5 | amplia (sem confirmar nem corrigir diretamente) | O arcabouço de Rice trata "características" em sentido amplo; usar diagramas UML como proxy de complexidade é uma escolha de espaço de características que precisaria ser justificada nos termos formais de Rice, o que nenhuma obra do eixo testa diretamente | [@rice1976algorithm] |
| F1 | confirma | A linhagem de portfólios e seleção de algoritmo (Rice 1976; BUS/Roberts & Howe; SATzilla; PbP; IPC) já estava ativa e crescendo antes de 2010, sem citação na dissertação | [@rice1976algorithm; @gerevini2014planning; @vallati2015portfolio; @kotthoff2014algorithm; @kerschke2019automated; @xu2008satzilla; @vallati2018what] |
| F2 | confirma (mostra alternativa) | ASlib e as competições de seleção de algoritmo mostram como *benchmarks* compartilhados sustentam amostras maiores e comparáveis, ao contrário da coleta manual de 2010 | [@bischl2016aslib; @lindauer2019algorithm; @vallati2018what; @sievers2019deep] |
| F3 | amplia (mostra alternativa) | *Features* automáticas e determinísticas (PDDL, grafo causal, SAS+, grafos de imagem) substituem a dependência do modelador humano das métricas UML, embora não garantam sozinhas ganho robusto | [@cenamor2016ibacop; @katz2018delfi; @ferber2022explainable] |
| F4 | confirma | A taxonomia de técnicas é reconhecidamente imprecisa em toda a literatura: "hierárquico", "*portfolio*" e outros termos são usados com sentidos distintos entre subcampos, e uma definição formal de portfólio ainda faltava em 2015 | [@vallati2015portfolio; @kotthoff2014algorithm; @kerschke2019automated; @xu2008satzilla; @seipp2014fast; @lindauer2015autofolio; @hutter2009paramils] |
| F6 | confirma | ASlib e as competições de seleção mostram o caminho institucional (formato + repositório padronizado) que 2010 não teve para reunir dados fora das IPCs | [@bischl2016aslib; @lindauer2019algorithm] |

## 5. Divergências e pontos em disputa

[FATO] Há desacordo sobre se modelos preditivos complexos valem o custo: Cenamor et al. atribuem o desempenho do IBaCoP à diversidade do conjunto filtrado, não aos modelos preditivos [@cenamor2016ibacop]; Ferber & Seipp mostram que uma regressão linear simples acompanha o Delfi1 baseado em CNN [@ferber2022explainable]; já Vatter et al. defendem que GNNs heterogêneas trazem ganho real sobre GNNs homogêneas e CNNs [@vatter2026beyond]. Não há consenso sobre o ponto ótimo de complexidade do modelo de seleção.

[FATO] Há também desacordo terminológico sobre o que conta como "portfólio": Vallati, Chrpa & Kitchin excluem explicitamente sistemas com "estratégia de *backup*" controlada pelo usuário, como SATPlan [@vallati2015portfolio], enquanto outras obras usam "portfolio" de forma mais frouxa, algo que Kotthoff desaconselha [@kotthoff2014algorithm] e Kerschke et al. reiteram como fonte de confusão [@kerschke2019automated].

[FATO] Sievers et al. mostram que nenhuma "receita única" de seleção por aprendizado profundo generaliza bem, e que dividir os dados sem preservar a estrutura por domínio piora a cobertura [@sievers2019deep] — ponto que qualifica, sem contradizer, o otimismo dos resultados posteriores [@vatter2026beyond].

## 6. Lacunas

[HIPÓTESE] "Não encontramos": nenhuma das 20 notas compara diretamente *features* de UML (como em 2010) contra *features* de PDDL/grafo causal/SAS+ no mesmo experimento — a literatura seguiu outro caminho sem testar a alternativa de 2010. Lacuna aberta para a Fase 3.

[FATO] Nenhuma obra do eixo trata de LLMs como seletores de planejador — nem a mais recente (2026) [@vatter2026beyond]. Responde parcialmente Q3: até a publicação mais recente lida, a fronteira de seleção de planejador não incorporou LLMs.

[FATO] O capítulo de 1976 de Rice não foi lido diretamente (Elsevier fechado, Purdue e-Pubs bloqueado); a nota se baseia no relatório técnico precursor de 1974 [@rice1976algorithm] — lacuna de acesso, não de existência.

[FATO] A nota sobre a IPC 2014 ficou restrita ao resumo por acesso pago [@vallati2018what] — não há, no eixo, relato detalhado em texto integral de nenhuma edição da IPC além dos "*planner abstracts*" de competição.

## 7. Insumos para as próximas fases

**Fase 2** (auditoria): usar a tabela da seção 4 como checklist — A6 precisa de correção documentada (Fast Downward não é hierárquico; SATPlan não é portfólio *plan-space*), e A7/F5 precisa registrar que cobertura é um entre pelo menos três alvos de avaliação possíveis [@vallati2015portfolio; @helmert2011fast].

**Fase 3** (replicação): a Definição 1 de Vallati, Chrpa & Kitchin confirma que nenhum dos 10 planejadores de 2010 é, ele próprio, um portfólio [@vallati2015portfolio], validando o escopo original; mas uma réplica deveria (a) adotar *features* automáticas de PDDL/SAS+ em vez de, ou em complemento a, métricas UML [@bischl2016aslib; @cenamor2016ibacop], (b) configurar automaticamente cada planejador antes de comparar "técnicas" [@hutter2009paramils; @lindauer2015autofolio], (c) preservar a estrutura por domínio ao dividir treino/teste [@sievers2019deep], e (d) medir tempo e qualidade, não só cobertura [@helmert2011fast; @vallati2015portfolio].

**Fase 4** (LLMs): nenhuma obra do eixo usa LLMs como seletor, tradutor ou planejador — terreno aberto (Q3), sem precedente direto no eixo para se apoiar; qualquer proposta precisaria justificar-se contra o estado da arte não-LLM atual (91,7% de acurácia, GNN heterogênea + XGBoost) [@vatter2026beyond].

## 8. Obras usadas

- bischl2016aslib — formato padronizado e repositório ASlib de cenários de seleção de algoritmo.
- cenamor2016ibacop — IBaCoP, portfólio *per-instance* configurado por *features* automáticas de PDDL/SAS+.
- eggensperger2019pitfalls — catálogo de armadilhas e boas práticas em configuração automática de algoritmos.
- ferber2022explainable — seleção de planejador interpretável com *features* simples, comparável ao Delfi baseado em CNN.
- gerevini2014planning — PbP, portfólio *offline* configurado por domínio via teste estatístico.
- helmert2011fast — Fast Downward Stone Soup, portfólio sequencial baseline sem *features* de instância.
- hutter2009paramils — ParamILS, *framework* de configuração automática de parâmetros.
- katz2018delfi — Delfi, seleção *per-instance* por CNN sobre representação de grafo/imagem, vencedor IPC 2018.
- kerschke2019automated — *survey* que formaliza e mapeia a evolução de *features* de seleção de algoritmo em planejamento.
- kotthoff2014algorithm — *survey* unificado sobre seleção de algoritmo para busca combinatória.
- lindauer2015autofolio — AutoFolio, configuração automática da própria estratégia de seleção.
- lindauer2019algorithm — relato e análise das competições de seleção de algoritmo de 2015 e 2017.
- ma2020online — seleção online de planejador com GNN homogênea e escalonamento adaptativo.
- rice1976algorithm — formalização fundacional do problema de seleção de algoritmo.
- seipp2014fast — Cedalion, configuração automática de portfólios de configurações do Fast Downward.
- sievers2019deep — exploração sistemática dos limites de generalização do aprendizado profundo na seleção de planejador.
- vallati2015portfolio — *survey* e taxonomia de planejamento baseado em portfólio.
- vallati2018what — relato da parte determinística da IPC 2014 (leitura restrita ao resumo).
- vatter2026beyond — GNN heterogênea (RGCN/RGAT) e redução de portfólio via valores de Shapley, estado da arte de 2026.
- xu2008satzilla — SATzilla, referência fundacional de portfólio *per-instance* em SAT.
