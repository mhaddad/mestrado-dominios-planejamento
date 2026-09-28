---
tipo: nota-de-leitura
eixo: E8
citekey: zhou2026agentasarouter
prioridade: A
status: verificado
profundidade: texto-integral
fonte-lida: https://arxiv.org/abs/2606.22902
metadados: verificada-na-fonte-primaria
referencia-verificada: true
afirmacoes-2010: [A1, A3, A4]
fragilidades: []
perguntas: [Q4]
---

# Agent-as-a-Router: Agentic Model Routing for Coding Tasks

**Zhou, P.; Tang, Z.; Ma, Y.; Tang, J.; Han, Y.; Wan, Z.; Meng, F.; Wang, W.; Zhuang, B.; Zhao, W.; You, Y. · 2026 · arXiv**
**Link/DOI:** https://arxiv.org/abs/2606.22902 (sem DOI Crossref no momento da leitura)

## Extração estruturada

- **Problema:** roteadores de LLM existentes tratam a escolha de modelo por tarefa como classificação estática e única; o artigo diagnostica que o gargalo real é "déficit de informação" — falta ao roteador estatística de desempenho por dimensão da tarefa — e propõe fechar essa lacuna com um roteador agêntico que acumula experiência de execução.
- **Método:** primeiro um estudo de ablação diagnóstico (Tabela 1), depois a proposta ACRouter (Orchestrator + Verifier + Memory, laço Context→Action→Feedback→Context) avaliada em um *benchmark* próprio, o CodeRouter-Bench: ~10 mil instâncias de tarefa com pontuações verificadas de 8 LLMs de fronteira (Claude Opus 4.6, Claude Sonnet 4.6, GPT-5.4, GLM-5, Qwen3-Max, Qwen3.5-Plus, Kimi-K2.5, MiniMax-M2.7), organizadas em 9 dimensões de tarefa de turno único (geração de código, algoritmos, correção de *bugs*, completar código, refatoração, ciência de dados, multi-turno, compreensão, geração de teste — 1.111 tarefas cada, *split* determinístico 70/30 por hash MD5) mais uma 10ª dimensão de programação agêntica retida como teste fora de distribuição (176 tarefas).
- **Dados/benchmarks:** CodeRouter-Bench (~10.000 tarefas, 8 modelos, 9+1 dimensões); comparação com roteadores estáticos heurísticos (`DimensionBest`, k-NN), roteadores de política treinada (regressão logística, TF-IDF+MLP, RouteLLM, Qwen3.5-FT) e *bandits* *online* (LinUCB, LinTS).
- **Resultado principal:** no estudo diagnóstico com Claude Sonnet 4.6 em 2.919 tarefas (Tabela 1), o roteador *zero-shot* padrão ("Vanilla") atinge 41,41% de desempenho médio (AvgPerf%); ao adicionar apenas a descrição da dimensão da tarefa ("+Dimension") o desempenho **não** melhora (41,18%); mas ao adicionar estatísticas de desempenho prévias por dimensão, coletadas em um conjunto de sondagem separado ("+Perf stats"), o desempenho sobe a 47,74% — superando o roteador heurístico `DimensionBest` (47,50%), que seleciona o melhor modelo por dimensão usando prioris completos, mas ainda distante do oráculo por tarefa (57,00%). A Tabela 11 (matriz modelo × dimensão) mostra desempenho muito heterogêneo entre modelos por dimensão — ex.: Claude Opus 4.6 lidera em correção de *bugs* (0,719) e compreensão (0,194), mas GPT-5.4 lidera em geração de teste (0,753) e Qwen3-Max em ciência de dados (0,823). Decomposição de variância (Apêndice D.3) mostra que a identidade da dimensão explica cerca de 27% da entropia da decisão ótima por tarefa.
- **Relação com a dissertação de 2010:** **A1**, **A3** e **A4** [confirma por analogia direta, HIPÓTESE] — a Tabela 11 é, estruturalmente, o equivalente do ranking de planejadores por domínio de 2010: uma matriz modelo × dimensão-de-tarefa em que nenhum modelo domina todas as dimensões, e o melhor modelo muda conforme a característica da tarefa (A1, A3). Mas a Tabela 1 separa duas coisas que importam para a Q4: informar só a dimensão da tarefa **não** melhora a escolha (41,41% → 41,18%); o ganho (47,74%) vem de dar ao roteador **estatísticas de desempenho observado** por dimensão. O que ajuda é o histórico de desempenho, não a descrição da característica — o mesmo padrão das Fases 3 e 4B, em que as características não antecipam a técnica e a escolha pelo melhor desempenho observado (*single best*) é difícil de superar. *(Correção de 28/09/2026: a versão anterior lia o salto como efeito de "conhecer a característica da tarefa".)* A constatação de que 27% da variância é explicada só pela dimensão, com o restante em conteúdo por tarefa, ecoa A4 de 2010 (mais características melhoram o ranking, mas não o esgotam).

## Pontos relevantes para o projeto

- É a evidência mais próxima, em todo o lote, do desenho exato de 2010: uma matriz explícita técnica (modelo) × característica-de-domínio (dimensão de tarefa) com desempenho medido por célula (Tabela 11) — material para uma comparação estrutural direta na dissertação revisada.
- O diagnóstico central do artigo — "informação, não raciocínio, é o gargalo" ("confirming that the bottleneck is information rather than reasoning", Apêndice D.4) — refere-se a informação de **desempenho** por dimensão, não a informação descritiva sobre a tarefa; em 2010, o equivalente é o *ranking* por notas observadas nos domínios de treino, não as métricas UML.
- Datas: publicado no arXiv em 22/06/2026 (`2606.22902`, revisão v3 de 26/06/2026); trabalho muito recente à data desta leitura (22/09/2026), com repositório de código liberado.
- Métrica AvgPerf% combina pontuação de execução (Exec pass@1), proxy+LLM-como-juiz e execução em *sandbox* Docker conforme a dimensão (Tabela 5) — mistura de critérios mais rica que a cobertura binária de 2010, mas também mais difícil de comparar diretamente entre dimensões.

## Marcações

- `[FATO]` "simply augmenting a vanilla LLM router with performance statistics at the task-dimension level yields a 15.3% relative gain, surpassing a heuristic router built on the same dimension-level priors" (resumo).
- `[FATO]` "Oracle ... 57.00 ... DimensionBest ... 47.50 ... Vanilla ... 41.41 ... +Dimension ... 41.18 ... +Perf stats ... 47.74" (Tabela 1, ablação diagnóstica com Claude Sonnet 4.6 em 2.919 tarefas).
- `[FATO]` "dimension identity captures roughly 27% of the entropy of yt: enough to explain why the DimensionBest reaches about 0.475 AvgPerf, but well short of the 0.570 per-task oracle" (Apêndice D.3, Decomposição de Variância).
- `[FATO]` Na Tabela 1, acrescentar a descrição da dimensão não melhora o roteador (41,41 → 41,18); acrescentar estatísticas de desempenho por dimensão melhora (47,74).
- `[HIPÓTESE]` A matriz modelo × dimensão (Tabela 11) é o análogo mais próximo, em agentes de código, da matriz planejador × domínio de 2010 (A1): nenhum modelo domina todas as dimensões. Mas o que torna a escolha melhor é a memória de desempenho observado, não a característica descrita, o que está mais perto dos resultados negativos das Fases 3 e 4B do que da conclusão de 2010.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://arxiv.org/abs/2606.22902 (PDF baixado do arXiv, extraído com pdftotext). Conferência humana: pendente. Claude Code (claude-opus-5-5), 28/09/2026: números da Tabela 1, o ganho relativo de 15,3%, os 27% da decomposição de variância e os trechos literais conferidos no PDF do arXiv (v3); metadados conferidos na API do arXiv. Promoção aprovada pelo autor em 28/09/2026.
