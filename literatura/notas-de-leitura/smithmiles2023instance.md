---
tipo: nota-de-leitura
eixo: E7
citekey: smithmiles2023instance
prioridade: A
status: lido
profundidade: resumo
fonte-lida: https://api.crossref.org/works/10.1145/3572895
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: [A3, A7]
fragilidades: [F5, F2]
perguntas: [Q1, Q2]
---

# Instance Space Analysis for Algorithm Testing: Methodology and Software Tools

**Smith-Miles, K.; Muñoz, M.A. · 2023 (registro Crossref: 2022) · ACM Computing Surveys, vol. 55, n. 12, artigo 255, p. 1–31**
**Link/DOI:** 10.1145/3572895

## Extração estruturada

- **Problema:** como testar algoritmos de forma objetiva e avaliar a diversidade das instâncias de teste usadas, em vez de reportar apenas o desempenho médio de um algoritmo sobre um conjunto escolhido de problemas — prática padrão que pode esconder pontos fortes e fracos específicos.
- **Método:** *Instance Space Analysis* (ISA), metodologia que representa as instâncias de teste como vetores de *features* e estende o arcabouço do *algorithm selection problem* de Rice (1976) para permitir a visualização de todo o espaço de instâncias possíveis. O artigo é um tutorial abrangente sobre a metodologia (que vem evoluindo há vários anos), detalhando os algoritmos e as ferramentas de software que vêm permitindo sua adoção em múltiplas disciplinas.
- **Dados/benchmarks:** um estudo de caso comparando algoritmos para *university timetabling* (montagem de grade horária universitária) ilustra a metodologia e as ferramentas.
- **Resultado principal:** em vez de reportar desempenho médio sobre um conjunto de problemas de teste, a ISA permite entender como o desempenho de um algoritmo varia em diferentes regiões do espaço de instâncias — revelando pontos fortes e fracos que ficariam ocultos na média; também permite avaliar objetivamente vieses no conjunto de instâncias de teste escolhido e avaliar a adequação (cobertura) de *benchmark suites*.
- **Relação com a dissertação de 2010:** **A3** [problematiza] — 2010 afirma que, só com as características do domínio (independentemente do problema específico), o ranking já escolhe os planejadores com melhor desempenho; a lógica da ISA sugere que "desempenho médio por classe de características" pode esconder variação relevante dentro da própria classe, e que a diversidade real das instâncias dentro de um domínio precisaria ser mapeada explicitamente (não assumida) para uma afirmação como A3 se sustentar. **A7** [problematiza diretamente] — a crítica central da ISA a "reportar desempenho médio sobre um conjunto escolhido de problemas" atinge em cheio o uso de cobertura agregada como métrica única de eficiência em 2010 (mesma lógica da fragilidade F5, já mapeada no plano). **F5** [ajuda a tratar] — fornece arcabouço e ferramentas concretas para ir além de médias agregadas. **F2** [ajuda a tratar] — a ISA foi desenvolvida em parte para avaliar objetivamente se um conjunto pequeno ou enviesado de instâncias de teste (situação análoga aos 10+3 domínios de 2010) é representativo do espaço de problemas mais amplo.

## Pontos relevantes para o projeto

- Só foi possível ler o resumo (Crossref/JATS, texto do editor da ACM), não o texto integral; a ACM Digital Library bloqueia acesso sem assinatura e não há cópia de acesso aberto confirmada (Unpaywall: `is_oa: false`).
- Nota de datação: o Crossref registra o ano de publicação como 2022 (data de registro do DOI), mas o volume/número da revista (55(12), artigo 255) e o *proceedings/issue date* citado em outras fontes correspondem a 2023; a chave `smithmiles2023instance` segue o ano usado na triagem do lote — a data exata deve ser conferida contra o registro definitivo da ACM antes da citação final.
- A ISA é a evolução direta do arcabouço de Rice (1976)/Smith-Miles (2009) já registrado na nota de `smithmiles2009cross`; formam, juntos, a trajetória conceitual "seleção de algoritmos → meta-aprendizado → análise do espaço de instâncias" que 2010 não conhece.
- Ferramentas de software mencionadas no resumo (não detalhadas por falta de acesso ao texto integral) seriam relevantes para T1/T2 (extração e agregação automática de métricas) se a leitura completa for feita depois.

## Marcações

- `[FATO]` "Instance Space Analysis (ISA) is a methodology to (a) support objective testing of algorithms and (b) assess the diversity of test instances. [...] Rather than reporting algorithm performance on average across a chosen set of test problems, as is standard practice, the ISA methodology offers a more nuanced understanding of the unique strengths and weaknesses of algorithms across different regions of the instance space that may otherwise be hidden on average" (resumo, Crossref/JATS).
- `[HIPÓTESE]` Ligação com F2/F5 de 2010: se a metodologia ISA fosse aplicada aos domínios de 2010 (10 de treino + 3 de validação), provavelmente revelaria que o pequeno número de domínios testados cobre uma fração limitada e potencialmente enviesada do espaço de instâncias de planejamento automatizado possível — mas essa é uma extrapolação do projeto a partir da lógica geral da ISA, não um teste que o artigo tenha feito com dados de planejamento automatizado.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de resumo em https://api.crossref.org/works/10.1145/3572895 (texto do editor, formato JATS). Tentativa de acesso ao texto integral via ACM Digital Library, ResearchGate e site do MATILDA (matilda.unimelb.edu.au) não teve sucesso (Unpaywall: `is_oa: false`). Conferência humana: pendente.
