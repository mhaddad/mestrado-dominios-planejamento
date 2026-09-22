---
tipo: nota-de-leitura
eixo: E4
citekey: stahlberg2023learning
prioridade: B
status: lido
profundidade: resumo
fonte-lida: https://proceedings.kr.org/2023/63/
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: [A6]
fragilidades: [F4]
perguntas: [Q4]
---

# Learning General Policies with Policy Gradient Methods

**Ståhlberg, S.; Bonet, B.; Geffner, H. · 2023 · KR (Proceedings of the International Conference on Principles of Knowledge Representation and Reasoning)**
**Link/DOI:** 10.24963/kr.2023/63

## Extração estruturada

- **Problema:** métodos de aprendizado por reforço têm entregado resultados notáveis em vários cenários, mas a generalização — produzir políticas que generalizem de forma confiável e sistemática — permanece um desafio; o problema de generalização já foi abordado formalmente em planejamento clássico com métodos combinatórios, mas não com aprendizado por reforço profundo (DRL).
- **Método:** modela políticas como classificadores de transição de estado (já que ações concretas não são gerais entre instâncias); usa redes neurais em grafo (GNNs) adaptadas para estruturas relacionais para representar funções de valor e políticas sobre estados de planejamento; usa métodos ator-crítico para aprender políticas que generalizam quase tão bem quanto abordagens combinatórias.
- **Dados / benchmarks:** não especificado em detalhe no resumo/abstract lido; menciona domínios de planejamento clássico usados como *benchmarks*.
- **Resultado principal:** métodos ator-crítico conseguem aprender políticas que generalizam quase tão bem quanto as obtidas por abordagens combinatórias, evitando o gargalo de escalabilidade e o uso de pools de *features*; as limitações observadas nos métodos DRL nos *benchmarks* considerados derivam das limitações expressivas conhecidas das GNNs e do *trade-off* entre otimalidade e generalização (políticas gerais não podem ser ótimas em alguns domínios), limitações que podem ser mitigadas com predicados derivados e uma estrutura de custo alternativa.
- **Relação com a dissertação de 2010:** conecta métodos combinatórios de planejamento generalizado (linhagem de A6, com abstrações provavelmente corretas) a aprendizado por reforço profundo, mais uma família ausente da taxonomia de 2010 (F4). Relevante hipoteticamente para **Q4** (ajuste tarefa-estratégia para escolher configurações de agentes de IA): a constatação de que "políticas gerais não podem ser ótimas em alguns domínios" é uma evidência formal, em outro domínio de aplicação, de que a adequação de uma estratégia (política) depende de características do domínio/tarefa — eco conceitual da tese central de HADDAD (2010), mas fora do escopo de planejamento clássico.

## Pontos relevantes para o projeto

- Demonstra formalmente que existe um *trade-off* entre otimalidade e generalização dependente do domínio — analogamente ao argumento central de 2010 de que características do domínio determinam qual técnica funciona melhor (hipótese de conexão, não citação direta).
- Traz keywords do próprio artigo relevantes ao projeto: "*Learning action theories*", "*Symbolic reinforcement learning*" — mostrando a interseção entre aprendizado por reforço e planejamento simbólico como área ativa.

## Marcações

- `[FATO]` "the limitations of the DRL methods on the benchmarks considered [...] result from the well-understood expressive limitations of GNNs, and the tradeoff between optimality and generalization (general policies cannot be optimal in some domains)" (resumo/abstract).
- `[HIPÓTESE]` A ideia de que "políticas gerais não podem ser ótimas em alguns domínios" ecoa, em outro contexto técnico, a tese de HADDAD (2010) de que não existe uma técnica universalmente ótima e a escolha depende do domínio — conexão interpretativa minha, não afirmada pelos autores.

## Trechos literais

- "the limitations of the DRL methods on the benchmarks considered have little to do with deep learning or reinforcement learning algorithms, and result from the well-understood expressive limitations of GNNs, and the tradeoff between optimality and generalization (general policies cannot be optimal in some domains)." (resumo)

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de resumo em https://proceedings.kr.org/2023/63/ (página de detalhes do artigo nos anais do KR-2023, com resumo completo; PDF completo não baixado nesta sessão). Conferência humana: pendente.
