---
tipo: nota-de-leitura
eixo: E8
citekey: fan2026dependencyrouter
prioridade: B
status: verificado
profundidade: texto-integral
fonte-lida: https://arxiv.org/abs/2609.25911
metadados: verificada-na-fonte-primaria
referencia-verificada: true
afirmacoes-2010: [A1, A3]
fragilidades: [F5]
perguntas: [Q4]
---

# When Should Dependency Updates Invoke Repair Agents? A Lightweight Routing Study

**Fan, L.; Yin, J.; Chen, Y. · 2026 · arXiv (v1, 22/09/2026)**
**Link/DOI:** https://arxiv.org/abs/2609.25911. O PDF se apresenta como artigo do 17th International Conference on Internetware (Internetware 2026, ACM, 5 p.), com DOI 10.1145/3834680.3834727; em 28/09/2026 esse DOI não resolvia (404 no doi.org, sem registro no Crossref). `[A CONFIRMAR]` a versão publicada; a citação é da versão lida, o *preprint*.

## Extração estruturada

- **Problema:** *pull requests* de atualização de dependência (Dependabot, Renovate) são frequentes e quase sempre rotineiros, mas uma parte pequena exige reparo de compatibilidade. Acionar um agente de reparo em toda atualização gasta chamadas de modelo, tempo de CI, contexto e atenção de revisão. O artigo trata isso como **roteamento pré-agente**: decidir quais atualizações escalar antes de qualquer diagnóstico ou reparo.
- **Método:** DepFixRouter, um ordenador de risco leve (SVM linear e regressão logística sobre TF-IDF do texto, metadados e projeções SVD), com orçamento ajustável (rotear os *k*% de maior risco). Separa três regimes de disponibilidade das *features*: só o que existe na criação do PR (título e indicadores de *bot*/dependência); o PR inicial antes de qualquer reação humana (T0); e o histórico completo, que inclui o que os desenvolvedores fizeram depois. Validação cruzada em 5 partições agrupadas por repositório.
- **Dados:** 500 candidatos do GitHub, coletados por termos de *bot* de dependência combinados com termos de reparo (amostra enriquecida de propósito); 497 com rótulo binário, 72 positivos (14,5%). Rótulos de um único anotador, com segunda passada nos casos ambíguos. Piloto de diagnóstico com 60 PRs (20 do topo do ranking, 20 ao acaso, 20 da base), com o DeepSeek (`deepseek-chat`, temperatura 0).
- **Resultado principal:** só com sinais disponíveis na criação do PR, rotear os 20% de maior risco captura 37 dos 72 reparos (recall 0,514; precisão 37,4% contra a taxa-base de 14,5%) e reduz as chamadas por reparo capturado de 6,90 (rotear tudo ou ao acaso) para 2,68 (Tabela 2). Com o histórico completo, o recall sobe a 0,653, mas os autores atribuem a diferença a informação retrospectiva (*hindsight*), inutilizável na hora de decidir. No piloto, o roteamento reduz as chamadas em 66,7% e os *tokens* em 66,1% e mantém 4 dos 5 verdadeiros positivos do diagnóstico em todos os casos, mas cobre só 4 dos 12 reparos reais da amostra (Tabela 3). O piloto mede a decisão de escalar o diagnóstico, não a geração de *patch*.
- **Relação com a dissertação de 2010:** **A1, A3** [por analogia, `[HIPÓTESE]`]. É o mesmo gesto de 2010, características observáveis antes da execução orientam a escolha do recurso, mas a escolha é binária (acionar ou não o agente caro), não entre técnicas. O cuidado central do artigo, separar o que está disponível antes da decisão do que só se sabe depois, é o mesmo cuidado que 2010 teve ao extrair as métricas do modelo antes de rodar os planejadores. **F5**: a medida de sucesso aqui é custo por caso capturado, não só cobertura.

## Pontos relevantes para o projeto

- É a evidência empírica mais direta, no lote da Fase 5, para o nível de **triagem** da tese provisória da Ponte (`ponte-software/relatorio/curadoria-fontes-se-ia.md`): uma política leve decide quando vale acionar o agente custoso.
- O ganho é real mas modesto e medido num único tipo de tarefa (atualização de dependência), com amostra enriquecida e rótulo de um anotador. Não sustenta, sozinho, generalização para outras tarefas de desenvolvimento.
- O contraste criação × histórico completo é uma lição de método transferível: *features* que parecem preditivas podem estar contaminadas por informação posterior à decisão. Vale para qualquer desenho futuro de seleção de configuração de agente.
- Os sinais usados são texto e metadados do PR, não métricas estruturais do código; o artigo não testa métricas de código.

## Trechos literais

"We frame this as a pre-agent routing problem: deciding which dependency-update pull requests should be escalated before downstream diagnosis or repair attempts." (resumo)

"A creation-time-safe LinearSVC using only PR titles and bot/dependency flags reaches 0.488 repair F1 and captures 51.4% of repairs within the top 20% routed pull requests, improving calls per captured repair from 6.90 under route-all or random policies to 2.68." (resumo)

"The central methodological lesson is therefore to evaluate deployment-time routing separately from retrospective repair mining." (seção 6)

## Marcações

- `[FATO]` Com sinais disponíveis na criação do PR, o topo de 20% do ranking reúne 51,4% dos reparos, e as chamadas por reparo capturado caem de 6,90 para 2,68 (Tabela 2).
- `[FATO]` O histórico completo eleva o recall a 0,653, mas carrega informação retrospectiva; os autores o tratam como diagnóstico, não como desempenho de implantação (seção 4.2).
- `[FATO]` O piloto de 60 casos mede só a escalada do diagnóstico, não reparo nem CI (seção 4.3 e ameaças à validade).
- `[HIPÓTESE]` Para a Q4, o artigo apoia a triagem como primeiro nível de uma política de escolha de configuração, não a seleção entre configurações.

## Uso de IA nesta nota

Claude Code (claude-opus-5-5), 28/09/2026. Leitura de texto integral do PDF do arXiv (v1), extraído com `pdftotext`; números conferidos nas Tabelas 1 a 3 e no resumo; metadados conferidos na API do arXiv; DOI declarado testado no doi.org e no Crossref (sem registro). Promoção aprovada pelo autor em 28/09/2026.
