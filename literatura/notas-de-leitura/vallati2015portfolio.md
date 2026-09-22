---
tipo: nota-de-leitura
eixo: E1
citekey: vallati2015portfolio
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: http://eprints.hud.ac.uk/id/eprint/24291/1/VallatiPort.pdf
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: [A6, A7]
fragilidades: [F1, F5]
perguntas: [Q1]
---

# Portfolio-based Planning: State of the Art, Common Practice and Open Challenges

**Vallati, M.; Chrpa, L.; Kitchin, D. · 2015 · AI Communications 28(4), 717–733**
**Link/DOI:** https://doi.org/10.3233/AIC-150671

## Extração estruturada

- **Problema:** revisar sistematicamente o estado da arte de planejamento baseado em portfólio, listar as decisões de projeto necessárias para configurar um portfólio de planejadores, e apontar desafios em aberto.
- **Método:** *survey* estruturado em duas partes: (1) descrição de planejadores baseados em portfólio existentes (BUS, PbP/PbP2, ASAP, FDSS/FDSS2, IBaCoP etc.); (2) taxonomia das decisões de configuração, divididas em *offline* (escopo, alvo, tamanho, estratégia de escalonamento, planejadores incorporados) e *online* (avaliação, seleção de planejadores, alocação de tempo).
- **Dados/benchmarks:** não aplicável (*survey*); cita resultados oficiais de IPC6–8 dos sistemas revisados.
- **Resultado principal:** propõe uma definição própria de "planejador baseado em portfólio" (Definição 1: seleciona e/ou combina automaticamente uma ou mais técnicas), explicitamente diferente da de Roberts & Siebers (organizadores da faixa de aprendizado da IPC 2014); classifica planejadores clássicos com "estratégia de *backup*" (Blackbox, FF, LPG e, nomeadamente, SATPlan) como **não-portfólios** ("*planning frameworks*"), por não fazerem seleção automática entre motores.
- **Relação com a dissertação de 2010:**
  - **A6 (corrige, por mudança de critério de classificação):** a obra classifica SATPlan explicitamente como um "*planning framework*", não um portfólio: "*SATPlan... includes different modules... and allows the user to select the preferred one*" — ou seja, SATPlan combina múltiplos codificadores/solucionadores SAT sob escolha do usuário, não faz seleção automática. A taxonomia de 2010 (A6: SATPlan como técnica *plan-space*) usa um critério diferente (o paradigma de busca subjacente, *planning-as-satisfiability*) do critério desta obra (se o sistema é ou não um portfólio automatizado); não há contradição factual direta, mas a comparação expõe que "técnica" em 2010 mistura níveis de análise (paradigma de busca vs. arquitetura de sistema) que esta obra separa com cuidado.
  - **F5 (evidencia a fragilidade com alternativa):** o "alvo" (*target*) de um portfólio, segundo esta taxonomia, pode ser tempo de execução, qualidade da solução ou número de problemas resolvidos — três eixos distintos, tratados como decisão de projeto explícita a justificar. 2010 (A7) reduz eficiência só a cobertura (equivalente a "número de problemas resolvidos"), sem discutir os outros dois alvos possíveis nem justificar a escolha — esta obra mostra que já em 2015 essa era reconhecida como uma escolha entre pelo menos três.
  - **F1 (evidencia a lacuna, com foco em BUS/Roberts & Howe):** dedica uma subseção inteira a BUS (Roberts & Howe) como "*the first work, in automated planning, based on the portfolio approach*" — confirma que BUS/Roberts & Howe é reconhecido pela comunidade como o marco fundacional dessa linha, reforçando por que sua ausência em 2010 (já nomeada no plano como parte de F1) é uma lacuna relevante, não uma omissão menor.

## Pontos relevantes para o projeto

- A "Definição 1" de planejador baseado em portfólio (seleção e/ou combinação automática de técnicas) é um critério preciso e citável para decidir, sem ambiguidade, se cada um dos 10 planejadores usados em 2010 (Blackbox, IPP, FF, R, LPG, Fast Downward, YAHSP, SGPlan, SATPlan, MAXPLAN) é, ele próprio, um portfólio — nenhum deles atende a esse critério da forma como a obra o define; todos são planejadores únicos (com estratégias de *backup* em alguns casos), o que valida o escopo de 2010 como comparação entre planejadores individuais, não entre portfólios.
- A taxonomia de decisões *offline*/*online* é diretamente reaproveitável como lista de verificação para desenhar experimentos reprodutíveis na revisão da dissertação de 2010 (T1–T6).
- A obra observa que uma "definição formal de portfólio de algoritmo" ainda está ausente do campo em 2015 — mesmo os autores mais avançados da área reconhecem imprecisão conceitual, o que contextualiza (sem desculpar) a taxonomia frágil de 2010 (F4).

## Trechos literais

1. "Systems like SATPlan..., which can use a variety of satisfiability engines are not considered portfolios since they do not automatically select the engine to use. In particular, we believe that SATPlan is a planning framework; it includes different modules... and allows the user to select the preferred one." (Algorithm portfolios)
2. "BUS... is the first work, in automated planning, based on the portfolio approach." (Existing portfolio-based planners, BUS)
3. "Typically these functions are very easy and concern three different performance areas, usually taken individually: runtimes, quality of solution plans... and number of solved problems." (Portfolio configuration, Target and scope)

## Marcações

- `[FATO]` A obra classifica explicitamente SATPlan como "*planning framework*", não como portfólio, por não fazer seleção automática de motor (seção "Algorithm portfolios").
- `[FATO]` A obra identifica três alvos de otimização possíveis para um portfólio de planejadores — tempo, qualidade, número de problemas resolvidos — tratados como decisão de projeto explícita (seção "Target and scope").
- `[HIPÓTESE]` Como nenhum dos 10 planejadores de 2010 atende à definição de "portfólio" desta obra, a crítica de F5 (eficiência = cobertura) deve ser lida como crítica à métrica de avaliação de planejadores individuais escolhida por 2010, não como confusão entre planejador e portfólio.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em http://eprints.hud.ac.uk/id/eprint/24291/1/VallatiPort.pdf (cópia de acesso aberto no repositório institucional da University of Huddersfield; o artigo publicado na AI Communications/IOS Press é fechado). Conferência humana: pendente.
