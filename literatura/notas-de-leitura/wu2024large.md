---
tipo: nota-de-leitura
eixo: E7
citekey: wu2024large
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: https://arxiv.org/abs/2311.13184
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: [A1, A3]
fragilidades: []
perguntas: [Q2, Q4]
---

# Large Language Model-Enhanced Algorithm Selection: Towards Comprehensive Algorithm Representation

**Wu, X.; Zhong, Y.; Wu, J.; Jiang, B.; Tan, K.C. · 2024 (IJCAI 2024) · arXiv:2311.13184**
**Link/DOI:** 10.24963/ijcai.2024/579

## Extração estruturada

- **Problema:** no problema clássico de seleção de algoritmos (Rice, 1976), as técnicas dominantes usam apenas as **características do problema** para prever qual algoritmo terá melhor desempenho, tratando os algoritmos como caixas-pretas; as **características do próprio algoritmo** (sua estrutura, código, lógica interna) permanecem pouco exploradas, em parte porque não há um método universal para extraí-las automaticamente a partir da diversidade e complexidade dos algoritmos.
- **Método:** os autores introduzem **AS-LLM**, primeiro método a usar LLMs (UniXCoder e BGE) para extrair *features* de algoritmos diretamente do texto do código-fonte, capturando aspectos estruturais e semânticos e dando ao modelo compreensão contextual e de funções de biblioteca. A representação de alta dimensão extraída pelo LLM passa por um módulo de seleção de *features*, é combinada com a representação do problema e alimenta um módulo de cálculo de similaridade que determina o algoritmo selecionado pelo grau de compatibilidade entre problema e algoritmo — modelando a relação problema-algoritmo como potencialmente **bidirecional**, e não apenas um mapeamento unidirecional problema→algoritmo. O artigo também deriva um limite teórico superior para a complexidade do modelo.
- **Dados/benchmarks:** 10 cenários do repositório ASLib (*Algorithm Selection library*), cobrindo problemas como SAT, CSP (*constraint satisfaction*) e outros, com métrica PAR10 (tempo de execução até um limite de corte, com penalidade 10× o corte em caso de *timeout*).
- **Resultado principal:** "Analyzing Table 2, it is evident that AS-LLM outperforms other methods in eight out of the ten datasets" — o AS-LLM supera os métodos comparativos (que usam apenas *features* do problema) em 8 dos 10 cenários do ASLib, com desempenho competitivo nos dois restantes (CSP-MZN-2013 e PROTEUS-2014). O estudo de ablação (Figura 2) mostra que remover o módulo de *features* de algoritmo (AS-LLM-AF) causa a maior perda de desempenho entre os módulos testados, confirmando que a informação extraída do código do algoritmo é o principal fator do ganho. Uma limitação identificada: nos dois cenários em que o AS-LLM não superou os concorrentes, a causa apontada foi a indisponibilidade de arquivos de código completos do algoritmo e descrição textual insuficiente das características do algoritmo.
- **Relação com a dissertação de 2010:** **A1** [confirma, por analogia estrutural direta] — o AS-LLM aplica exatamente a lógica de A1 (características de um lado do problema predizem qual técnica tem melhor desempenho), mas inverte a direção usual: em vez de só caracterizar o problema/domínio (como 2010 faz via UML), o AS-LLM também caracteriza o próprio algoritmo/técnica, tratando a relação como bidirecional. Isso é uma correção conceitual relevante à abordagem de 2010, que caracteriza apenas o domínio e não as técnicas de planejamento em si. **A3** [qualifica] — 2010 afirma que só as características do domínio, independentemente do problema específico, já escolhem o ranking; o AS-LLM mostra que características do *algoritmo* também carregam poder preditivo relevante (maior perda de desempenho na ablação vem de remover justamente essas *features*), sugerindo que um modelo que ignore as características da técnica (como 2010 faz implicitamente, ao tratar as técnicas apenas por rótulo/taxonomia, não por *features* extraídas) pode estar deixando poder preditivo na mesa.

## Pontos relevantes para o projeto

- É o artigo do lote que cita explicitamente Rice (1976) e formaliza o problema de seleção de algoritmos com a mesma notação usada nas notas de Smith-Miles (espaço de problemas `P`, espaço de algoritmos `A`, métrica de desempenho `M`, seletor `S: P → A`) — conecta diretamente este lote (E7) ao arcabouço de meta-aprendizado.
- Achado metodológico relevante para Q2: a comparação direta (Tabela 2) entre um método que usa só *features* de problema e o AS-LLM (que soma *features* de problema e de algoritmo) mostra ganho mensurável ao acrescentar a caracterização do algoritmo — evidência indireta (em outro domínio) de que "adicionar mais características" (aqui, do lado do algoritmo) pode melhorar a seleção, ecoando a lógica geral de T4 (pesos por característica) e A4 (mais características melhoram o ranking) de 2010, mas sem testar planejamento automatizado.
- Limitação relevante para Q4: o próprio artigo reconhece dependência de dados de algoritmo confiáveis (idealmente arquivos de código completos) — se a analogia da Q4 fosse levada a sério, "caracterizar o agente de IA" (o equivalente ao algoritmo aqui) exigiria uma fonte de informação estruturada sobre cada agente/modelo, não apenas sobre a tarefa.
- Métrica PAR10 (tempo até corte, com penalidade por *timeout*) é mais rica que a cobertura binária usada em 2010 (F5): penaliza gradualmente o insucesso em vez de reduzi-lo a "resolveu/não resolveu".

## Marcações

- `[FATO]` "Algorithm selection aims to choose the appropriate algorithm for each problem instance from a set of algorithms [Rice, 1976]" e a formalização subsequente do seletor `S: P → A` que otimiza `E[M(p, S(p))]` (Seção 2.1).
- `[FATO]` "Analyzing Table 2, it is evident that AS-LLM outperforms other methods in eight out of the ten datasets, while still exhibiting competitive performance in the CSP-MZN-2013 and PROTEUS-2014 scenarios" (Seção 5.2, Comparação de Desempenho).
- `[FATO]` "AS-LLM-AF exhibits the largest performance loss, underscoring the crucial role of algorithm features in algorithm selection and validating the core innovation of this study" (Seção 5.3, Estudo de Ablação).
- `[HIPÓTESE]` Ligação com Q4: se a lógica do AS-LLM (caracterizar tanto a tarefa quanto o "algoritmo"/agente, e não só a tarefa) fosse transposta para a escolha de agentes de IA no desenvolvimento de software, seria necessário um método de extrair *features* estruturais e semânticas de cada agente (ex.: a partir de sua arquitetura, *prompt* de sistema, ferramentas disponíveis) análogo ao que o AS-LLM faz a partir do código-fonte de algoritmos clássicos — o artigo não testa essa transposição, que permanece hipótese do projeto.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://arxiv.org/abs/2311.13184 (PDF baixado do arXiv, versão publicada no IJCAI 2024; extraído com pdftotext). Conferência humana: pendente.
