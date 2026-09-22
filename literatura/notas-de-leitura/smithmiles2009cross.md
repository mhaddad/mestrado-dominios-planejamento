---
tipo: nota-de-leitura
eixo: E7
citekey: smithmiles2009cross
prioridade: A
status: lido
profundidade: resumo
fonte-lida: https://api.crossref.org/works/10.1145/1456650.1456656
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: [A1]
fragilidades: [F1]
perguntas: [Q1, Q2, Q4]
---

# Cross-disciplinary perspectives on meta-learning for algorithm selection

**Smith-Miles, K.A. · 2009 · ACM Computing Surveys, vol. 41, n. 1, artigo 6, p. 1–25**
**Link/DOI:** 10.1145/1456650.1456656

## Extração estruturada

- **Problema:** o *algorithm selection problem* de Rice (1976) pergunta "qual algoritmo tem probabilidade de ter melhor desempenho para o meu problema?". A comunidade de aprendizado de máquina desenvolveu, a partir do início dos anos 1990, o campo de meta-aprendizado para tratar essa pergunta em problemas de classificação, mas com pouca generalização para além disso; outras disciplinas (IA, pesquisa operacional) atacaram o mesmo problema de seleção de algoritmos de formas diferentes, com terminologias diferentes, sem perceberem as semelhanças entre as abordagens.
- **Método:** artigo de revisão que apresenta um arcabouço unificado tratando o problema de seleção de algoritmos como um problema de aprendizado, usando esse arcabouço para amarrar os desenvolvimentos cross-disciplinares no enfrentamento do problema de seleção de algoritmos.
- **Dados/benchmarks:** não aplicável — é uma revisão conceitual/teórica, não um estudo empírico com dados próprios.
- **Resultado principal:** discute a generalização dos conceitos de meta-aprendizado para algoritmos de ordenação (*sorting*), previsão (*forecasting*), satisfação de restrições e otimização, e a extensão dessas ideias a bioinformática, criptografia e outros campos — ou seja, mostra que o problema "que características do problema predizem qual algoritmo funciona melhor" é tratado, de forma fragmentada, em múltiplas disciplinas, e propõe uma leitura unificada delas sob a ótica de Rice (1976): espaço de problemas, espaço de *features*, espaço de algoritmos e espaço de desempenho.
- **Relação com a dissertação de 2010:** **A1** [confirma, em termos de arcabouço geral] — a estrutura de 2010 (medir características de um domínio/problema por meio de métricas e usar essas características para indicar a técnica de planejamento com melhor desempenho) é, na terminologia deste artigo, uma instância do *algorithm selection problem* de Rice (1976): espaço de problemas = domínios de planejamento; espaço de *features* = métricas UML; espaço de algoritmos = planejadores/técnicas; espaço de desempenho = cobertura. O artigo não cita nem analisa 2010 (não poderia — é anterior, 2009), mas fornece o arcabouço formal em que a proposta de 2010 se encaixaria. **F1** [ajuda a tratar] — 2010 não cita Rice (1976) nem a literatura de seleção de algoritmos/meta-aprendizado (lacuna já mapeada no plano como F1); este artigo é a principal ponte entre essas duas literaturas para a revisão.

## Pontos relevantes para o projeto

- Só foi possível ler o resumo (Crossref/JATS, texto do editor da ACM), não o texto integral; tentativas de acesso ao PDF via ACM Digital Library, Monash Research Repository e ResearchGate não retornaram uma cópia de acesso aberto (Unpaywall confirma `is_oa: false`).
- O arcabouço de Rice (1976), descrito neste resumo, é a peça central para posicionar 2010 dentro da literatura mais ampla de seleção de algoritmos — a dissertação de 2010 resolve um caso particular desse problema geral sem o citar.
- Importante não confundir "meta-aprendizado para seleção de algoritmos" (aprender, a partir de dados de desempenho passado, qual algoritmo escolher) com o método de 2010 (um ranking fixo construído manualmente a partir de poucos domínios) — 2010 não usa aprendizado de máquina para a seleção em si, apenas cruza características com desempenho observado; a diferença é relevante para Q1 e Q2.
- Este artigo é de 2009 (não 2008, apesar de aparecer citado com essa data em algumas fontes secundárias) — a data 2009 é a registrada no Crossref e deve ser a usada na dissertação revisada.

## Marcações

- `[FATO]` "The algorithm selection problem [Rice 1976] seeks to answer the question: Which algorithm is likely to perform best for my problem? [...] there has been only limited generalization of these ideas beyond classification, and many related attempts have been made in other disciplines [...] to tackle the algorithm selection problem in different ways, introducing different terminology, and overlooking the similarities of approaches" (resumo, Crossref/JATS).
- `[HIPÓTESE]` Ligação com Q4: se o arcabouço de Rice/Smith-Miles for aplicado à escolha de agentes de IA no desenvolvimento de software (espaço de problemas = tarefas de engenharia de software; espaço de *features* = características da tarefa; espaço de algoritmos = agentes/modelos de IA disponíveis; espaço de desempenho = alguma medida de sucesso), a estrutura formal se aplicaria por analogia direta — mas isso é uma extensão proposta pelo projeto, não uma conclusão deste artigo, que não trata de LLMs nem de agentes de software.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de resumo em https://api.crossref.org/works/10.1145/1456650.1456656 (texto do editor, formato JATS). Tentativas de acesso ao texto integral (ACM Digital Library, Monash Research Repository, ResearchGate) não tiveram sucesso (Unpaywall: `is_oa: false`). Conferência humana: pendente.
