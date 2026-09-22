---
tipo: nota-de-leitura
eixo: E2
citekey: percassi2021improving
prioridade: A
status: lido
profundidade: resumo
fonte-lida: https://doi.org/10.1080/0952813x.2021.1970239
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: [A7]
fragilidades: [F5]
perguntas: [Q2]
---

# Improving Domain-Independent Heuristic State-Space Planning via Plan Cost Predictions

**Percassi, F.; Gerevini, A.E.; Scala, E.; Serina, I.; Vallati, M. · 2021 · Journal of Experimental & Theoretical Artificial Intelligence 35(6), 849–875**
**Link/DOI:** https://doi.org/10.1080/0952813x.2021.1970239

## Extração estruturada

- **Problema:** o desempenho de sistemas de planejamento domínio-independentes é fortemente afetado pela estrutura do espaço de busca, que depende do domínio de aplicação e de sua codificação; o artigo investiga como combinar aprendizado de máquina e busca heurística para melhorar o planejamento domínio-independente.
- **Método (pelo resumo):** usa aprendizado de máquina para **prever o custo de plano** de uma boa solução para uma dada instância (predição indutiva); propõe uma função heurística sensível a limites (*bound-sensitive*) que explora essa previsão dentro de um planejador de busca no espaço de estados, combinando a previsão de entrada com informação coletada durante a busca (derivada dedutivamente); como a previsão pode às vezes ser grosseiramente imprecisa, a função também reconhece quando a informação fornecida está de fato prejudicando a busca.
- **Dados/benchmarks:** não detalhado nesta leitura de resumo; avaliação experimental descrita como demonstrando "a utilidade da abordagem proposta em um esquema padrão de busca gulosa pelo melhor" (*best-first search*).
- **Resultado principal (pelo resumo):** a análise experimental demonstra a utilidade de combinar previsão de custo de plano (aprendida) com busca heurística padrão, num esquema de busca gulosa pelo melhor sensível a limites.
- **Relação com a dissertação de 2010:**
  - **A7 (corrige):** 2010 reduz eficiência a cobertura, sem entrar em tempo nem qualidade do plano. Este artigo usa **custo de plano** (uma medida direta de qualidade) como alvo de previsão e como insumo para guiar a própria busca — mostra que a comunidade de EPMs para planejamento evoluiu de "prever se/quando" (cobertura/tempo, como em Roberts & Howe e Fawcett et al.) para "prever quanto custará o plano" e usar essa previsão para melhorar diretamente a heurística de busca, uma etapa metodológica além do que 2010 cobre.
  - **F5 (evidencia superação):** ao integrar a predição de custo de plano na própria função heurística (não apenas como *ranking* posterior de planejadores), o artigo mostra um caminho em que "eficiência" deixa de ser um rótulo externo (cobertura) e passa a ser parte do mecanismo de busca — uma resposta concreta, embora não deliberada, à fragilidade F5 de 2010.
- **Features por classe (para Q2):** de modelo (a predição de custo de plano é, em si, uma saída de modelo aprendido usada como *feature*/limite dentro da heurística de busca) — não é possível, a partir do resumo, detalhar quais *features* de entrada (sintáticas, de grafo causal/DTG, de sondagem) alimentam esse modelo preditivo; recomenda-se leitura de texto integral para essa informação, central para Q2.

## Pontos relevantes para o projeto

- É a única obra do lote que integra a predição de desempenho **dentro** do mecanismo de busca (heurística sensível a limites), em vez de usá-la apenas para selecionar ou ranquear planejadores externamente — diferença de arquitetura relevante para discutir T3 (detalhar técnicas: heurística, construção da busca, subtécnicas) em uma revisão de 2010.
- Reconhece explicitamente que a previsão pode ser "grosseiramente imprecisa" e projeta a heurística para detectar quando isso ocorre — uma postura de robustez à incerteza do modelo preditivo que poderia inspirar T4 (pesos por característica) em versão revisada.
- Não foi possível obter o texto integral (o artigo está hospedado apenas no repositório institucional da Universidade de Huddersfield, protegido por verificação anti-robô que bloqueou tanto acesso direto quanto por ferramentas de busca); a leitura ficou restrita ao resumo, obtido via metadados do OpenAlex (reproduzidos do próprio editor). Uma leitura de texto integral é fortemente recomendada antes de qualquer uso mais detalhado desta obra, dado seu potencial para Q2.

## Marcações

- `[FATO]` O artigo usa aprendizado de máquina para prever o custo de plano de uma instância e incorpora essa previsão numa função heurística sensível a limites, combinando informação preditiva (indutiva) com informação coletada durante a busca (dedutiva) (Resumo).
- `[FATO]` A função heurística proposta inclui um mecanismo para reconhecer quando a previsão de custo está prejudicando a busca, em vez de apenas confiar cegamente nela (Resumo).
- `[HIPÓTESE]` Sem acesso ao texto integral, não é possível afirmar com que tipo de *features* (sintáticas, estruturais, de sondagem) o modelo de predição de custo é treinado — hipótese a verificar: dado que os coautores incluem Vallati (coautor de Fawcett et al. 2014) e Scala/Gerevini (planejadores baseados em heurísticas aditivas e *red-black*), é provável que o conjunto de *features* inclua ao menos heurísticas do estado inicial e possivelmente estruturas de grafo causal, na linha de De la Rosa et al. (2017).

## Trechos literais

1. "This paper proposes and investigates a novel way of combining machine learning and heuristic search to improve domain-independent planning. On the learning side, we use learning to predict the plan cost of a good solution for a given instance. On the planning side, we propose a bound-sensitive heuristic function that exploits such a prediction in a state-space planner." (Resumo, reproduzido via metadados OpenAlex/editor)

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de resumo via metadados do OpenAlex (reprodução do resumo submetido pelo editor à API Crossref/OpenAlex); o PDF hospedado em pure.hud.ac.uk retornou erro 403 (proteção anti-robô) em todas as tentativas de acesso direto e via ferramenta de busca web. Conferência humana: pendente — recomenda-se nova tentativa de leitura de texto integral via acesso institucional ou solicitação direta aos autores.
