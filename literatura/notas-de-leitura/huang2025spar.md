---
tipo: nota-de-leitura
eixo: E6
citekey: huang2025spar
prioridade: C
status: lido
profundidade: resumo
fonte-lida: https://arxiv.org/pdf/2509.13691 (PDF baixado, lidos resumo, introdução e trecho da seção de métrica de complexidade de domínio)
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: [A1]
fragilidades: []
perguntas: [Q2, Q3]
---

# SPAR: Scalable LLM-based PDDL Domain Generation for Aerial Robotics

**Huang, S.; Wu, Y.; Shi, G.; Sukhatme, G.S.; Kumar, V. · 2025 · preprint (arXiv)**
**Link/DOI:** arXiv:2509.13691

## Extração estruturada

- **Problema:** projetar manualmente domínios PDDL para diversas aplicações de veículos aéreos não tripulados (UAVs) — vigilância, entrega, inspeção — é trabalhoso e propenso a erro, dificultando adoção e implantação real.
- **Método:** propõem o SPAR, *framework* que usa LLMs para gerar automaticamente domínios PDDL válidos, diversos e semanticamente corretos a partir de linguagem natural; introduzem um *dataset* de planejamento para UAVs com domínios PDDL de referência (*ground truth*) e problemas associados. Definem uma **métrica composta de complexidade de domínio PDDL**, com nove componentes: (1) número de ações, tipos de objeto, predicados e funções; (2) número médio de pré-condições e efeitos por ação; (3) *interdependency score* (referências médias de ações a um predicado/função); (4) acoplamento de ação (condições em efeitos de uma ação que aparecem como pré-condições em outras); entre outros componentes citados no texto, combinados em uma soma ponderada.
- **Dados/benchmarks:** *dataset* próprio de domínios PDDL para UAV, com pontuações de complexidade variando de 2,79 a 15,23; o domínio clássico Blocksworld tem complexidade 5,23, ficando em 17º lugar entre 30 domínios do conjunto (do mais ao menos complexo); o conjunto foi dividido em 14 domínios simples (≤5,23) e 16 complexos (>5,23).
- **Resultado principal:** não detalhado em profundidade na leitura de resumo/introdução (nota curta); os autores afirmam que os domínios gerados são avaliados quanto à sua qualidade estrutural e semântica usando essa métrica composta.
- **Relação com a dissertação de 2010:** **confirma o espírito de A1** (existe relação entre características de domínios e desempenho/dificuldade de técnicas), propondo uma métrica estrutural composta de complexidade de domínio PDDL — diretamente comparável às métricas UML discretizadas de 2010 (número de classes, atributos, associações etc.), mas aplicada a PDDL puro, sem UML. É o candidato mais direto do lote para alimentar **Q2** (se métricas estruturais de modelagem acrescentam poder preditivo às *features* de PDDL — aqui, a métrica *é* justamente uma feature estrutural de PDDL).

## Pontos relevantes para o projeto

- A métrica composta de complexidade (9 componentes: contagem de elementos, pré-condições/efeitos médios, *interdependency score*, acoplamento de ação etc.) é um ponto de partida concreto e citável para discutir Q2 — é um exemplo real de "métrica estrutural de PDDL" comparável às métricas UML de 2010.
- O uso de Blocksworld como ponto de referência (complexidade 5,23, posição 17 de 30) é um dado interessante para calibrar a métrica contra domínios clássicos conhecidos da literatura de planejamento, incluindo os usados em 2010.
- Aplicação específica (UAVs/robótica aérea) limita a generalização direta, mas a métrica em si é definida de forma independente de domínio.

## Trechos literais

"To systematically quantify the complexity of a PDDL domain, we introduce a composite metric that captures both structural and semantic characteristics of the domain" (seção sobre métrica de complexidade de domínio PDDL).

## Marcações

- `[FATO]` o artigo define e aplica uma métrica composta de nove componentes estruturais/semânticos para quantificar a complexidade de domínios PDDL, calibrada com um conjunto de 30 domínios incluindo Blocksworld (seção de métrica de complexidade).
- `[HIPÓTESE]` interpretação minha: esta métrica composta de complexidade de PDDL é, entre todos os trabalhos lidos neste lote, o mais próximo de uma resposta direta e citável à pergunta Q2 — vale considerar sua promoção a leitura de prioridade A em rodada futura, para avaliar se ela (ou algo equivalente) tem poder preditivo sobre desempenho de planejadores, o que o próprio artigo pode não testar (não verificado nesta leitura curta).

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de resumo, introdução e trecho da seção de métrica de complexidade de domínio do PDF em https://arxiv.org/pdf/2509.13691 (prioridade C, nota curta). Conferência humana: pendente.
