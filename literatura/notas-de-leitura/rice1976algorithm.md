---
tipo: nota-de-leitura
eixo: E1
citekey: rice1976algorithm
prioridade: A
status: lido
profundidade: resumo
fonte-lida: https://docs.lib.purdue.edu/cstech/68 (CSD-TR 116, 1974, precursor do capítulo de 1976; ver nota sobre a leitura)
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: [A1, A5]
fragilidades: [F1]
perguntas: [Q1, Q2]
---

# The Algorithm Selection Problem

**Rice, J. R. · 1976 · Advances in Computers, vol. 15, pp. 65–118 (Elsevier)**
**Link/DOI:** https://doi.org/10.1016/S0065-2458(08)60520-3

**Nota sobre a leitura:** o capítulo de 1976 (o objeto citado em `candidatas.bib`) está fechado — Elsevier não libera acesso aberto e o Unpaywall confirma `is_oa: false`, sem localização aberta. A versão em Purdue e-Pubs (`docs.lib.purdue.edu/cgi/viewcontent.cgi?article=1098`, CSD-TR 152, "revised version of CSD-TR 116, 117, and 130... to appear in Advances in Computers Vol. 15") está atrás de um desafio Cloudflare que bloqueou todas as tentativas de download automatizado. O que foi efetivamente lido, na íntegra, foi o primeiro relatório técnico da série do próprio Rice — CSD-TR 116, "The Algorithm Selection Problem — Abstract Models" (maio de 1974), disponível via CORE (`files01.core.ac.uk/download/pdf/4972185.pdf`, espelhando `docs.lib.purdue.edu/cstech/68`). O próprio relatório se declara "the first of a series of reports" que, segundo a página de metadados do CSD-TR 152, foi revisada e fundida com os relatórios 117 e 130 para formar o capítulo de 1976. O aparato formal central (espaço de problemas, espaço de algoritmos, aplicação de desempenho, aplicação de seleção, espaço de características) é exatamente o que a literatura secundária lida neste lote (Kotthoff 2014, que reproduz o mesmo diagrama; Kerschke et al. 2019; SATzilla) atribui a "Rice (1976)". Ainda assim, por não ter lido o texto final publicado, a profundidade desta nota é classificada como `resumo`, e nenhuma citação literal abaixo é atribuída ao capítulo de 1976 — todas vêm do relatório de 1974 efetivamente lido.

## Extração estruturada

- **Problema:** como formalizar, de modo abstrato e geral, o problema de escolher — entre um conjunto de algoritmos — o mais adequado para uma instância específica de um problema computacional, dado que nenhum algoritmo domina todos os demais em todas as instâncias.
- **Método:** define um "espaço de problemas" 𝒫, um "espaço de algoritmos" 𝒜, uma aplicação de desempenho p(A,x) que mede como o algoritmo A se sai no problema x, e uma "aplicação de seleção" S(x) que mapeia cada problema ao algoritmo de melhor desempenho esperado (modelo básico, Figura 1 do relatório). Em seguida, estende o modelo introduzindo um "espaço de características" (*feature space*) de dimensão menor, com uma aplicação de extração de características F que resume x antes da seleção (modelo com seleção por características, Figura 3). Propõe quatro critérios de "melhor seleção" (para todos os algoritmos; para uma subclasse de problemas; para uma subclasse de aplicações de seleção; para ambas) e cinco passos de análise: formulação, existência, unicidade, caracterização, computação.
- **Dados/benchmarks:** nenhum; é um relatório teórico, ilustrado só por exemplos abstratos (quadratura numérica por fórmulas de Newton-Cotes; escalonamento de sistemas operacionais; o jogo da velha).
- **Resultado principal:** um arcabouço matemático geral para o "problema de seleção de algoritmo", incluindo a formulação de "melhores características" como um subproblema à parte (perguntas E, F, G do relatório: que características são melhores para um algoritmo específico, para uma classe de algoritmos, para uma classe de aplicações de seleção).
- **Relação com a dissertação de 2010:**
  - **F1 (evidencia a lacuna):** 2010 não cita esta obra em nenhum lugar, apesar de propor essencialmente uma instância do "problema de seleção de algoritmo por características" de Rice — trocar "algoritmo" por "técnica de planejamento" e "características do problema" por "características do domínio extraídas em UML". O plano da revisão já sinalizava essa lacuna (seção 4, F1); a leitura confirma que se trata da referência fundacional de todo o campo — todas as demais obras lidas neste lote (Kotthoff 2014, Kerschke et al. 2019, SATzilla, PbP, IBaCoP, Cedalion) citam Rice (1976) como ponto de partida.
  - **A1 (confirma o princípio, não a operacionalização):** a afirmação central de 2010 — que características de domínio predizem a técnica de melhor desempenho — é compatível com o arcabouço de Rice, mas Rice não valida nenhum conjunto específico de características; ele mostra que escolher boas características é, em si, um subproblema formal (perguntas E/F/G) que precisa ser avaliado nos próprios termos propostos, algo que 2010 não faz para as métricas UML.
  - **A5 (contexto, não confirma nem corrige):** Rice trata de "características" em sentido amplo, não de "complexidade" de domínio; a ideia de 2010 de que diagramas UML medem complexidade, e que essa complexidade afeta desempenho, é uma escolha específica de espaço de características compatível com o arcabouço de Rice, mas que precisaria ser justificada nos termos dele (por que essas características e não outras), o que 2010 não faz.

## Pontos relevantes para o projeto

- O arcabouço de Rice separa claramente "escolher uma boa característica" de "escolher um bom algoritmo dado as características" — 2010 trata os dois como um único passo (discretização Alto/Médio/Baixo seguida direto de ranking), sem tratar a escolha das métricas UML como problema a ser validado à parte.
- A formalização de "melhor seleção para uma subclasse de problemas" (critério B) é próxima do que 2010 tenta fazer por domínio, mas Rice exige minimizar explicitamente a degradação de desempenho frente ao ótimo — 2010 não define nem mede essa degradação.
- É a referência que praticamente todo o restante deste lote usa para justificar a existência do "problema de seleção de algoritmo"; vale usá-la, na revisão, como ponto de ancoragem histórico do capítulo de trabalhos relacionados de 2010.

## Marcações

- `[FATO]` O relatório de 1974 (precursor direto do capítulo de 1976) formaliza o problema de seleção de algoritmo com um modelo básico (espaço de problemas, espaço de algoritmos, aplicação de desempenho, aplicação de seleção) e uma extensão baseada em características (Seções 2–3 do relatório).
- `[FATO]` O relatório declara explicitamente ser "the first of a series of reports", cujos títulos incluem "Concrete Examples", "Numerical Analysis", "Operating Systems", "Artificial Intelligence" (Introdução, p. 1–2).
- `[HIPÓTESE]` O capítulo de 1976 publicado (não lido diretamente) preserva esse mesmo aparato formal, com base na descrição de CSD-TR 152 como revisão fundida de CSD-TR 116/117/130 e na consistência entre o diagrama citado por Kotthoff (2014) e o diagrama do relatório de 1974 lido aqui.

## Trechos literais

1. "The models presented here are primarily aimed at algorithm selection problems with the following three characteristics: Problem Space... Algorithm Space... Performance Measure" (Seção 1, Introdução, CSD-TR 116, p. 3–4)
2. "Algorithm Selection Problem: Given all the other items in the above model, determine the selection mapping S(x)." (Seção 2, The Basic Model, CSD-TR 116, p. 5–6)
3. "The determination of the best (or even good) features is one of the most important, yet nebulous, aspects of the algorithm selection problem." (Seção 3, The Model with Selection Based on Features, CSD-TR 116, p. 12)

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral do relatório precursor CSD-TR 116 (1974) em https://docs.lib.purdue.edu/cstech/68 (recuperado via espelho CORE, `files01.core.ac.uk/download/pdf/4972185.pdf`, e extraído com `pdftotext -layout`); o capítulo de 1976 citado em `candidatas.bib` não foi acessado diretamente (Elsevier fechado; Unpaywall sem localização aberta; Purdue e-Pubs bloqueado por desafio Cloudflare em todas as tentativas via `curl` e via WebFetch). Conferência humana: pendente — recomenda-se, quando possível, obter acesso institucional ao capítulo de 1976 para confirmar que o aparato formal não mudou na revisão final.
