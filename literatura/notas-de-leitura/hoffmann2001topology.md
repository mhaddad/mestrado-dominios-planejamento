---
tipo: nota-de-leitura
eixo: E2
citekey: hoffmann2001topology
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: https://fai.cs.uni-saarland.de/hoffmann/papers/ijcai01.ps.gz
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: [A8]
fragilidades: [F1]
perguntas: [Q1]
---

# Local Search Topology in Planning Benchmarks: An Empirical Analysis

**Hoffmann, J. · 2001 · Proceedings of the 17th International Joint Conference on Artificial Intelligence (IJCAI-01), Seattle, p. 453–458**
**Link/DOI:** sem DOI (proceedings pré-DOI); PDF gerado a partir do postscript do próprio autor, https://fai.cs.uni-saarland.de/hoffmann/papers/ijcai01.ps.gz (bib do autor: https://fai.cs.uni-saarland.de/hoffmann/papers/ijcai01.bib, confirma páginas 453–458)

**Nota sobre identidade da obra:** esta é a fonte primária efetivamente citada por 2010 (referências, linha 1873 de `data/2010/extraido/texto.md`: "HOFFMANN, J. FF Local Search Topology in Planning Benchmarks: An Empirical Analysis. [...] p. 453-458. 2001."). A chave já existente no projeto `hoffmann2001ff` é uma obra **diferente** — Hoffmann & Nebel, "The FF Planning System" (JAIR 2001) — de autoria dupla e sem relação com topologia de espaços de busca. Um auditor da Onda 3 classificou as afirmações AF-189 a AF-191 comparando erroneamente com `hoffmann2001ff`; esta nota corrige a base de comparação.

## Extração estruturada

- **Problema:** entender por que planejadores heurísticos que ignoram listas de remoção (ex.: FF, HSP) têm sucesso em muitos domínios de referência — isto é, se os espaços de estados desses domínios têm topologia "simples" sob a heurística relaxada h+.
- **Método:** define formalmente um espaço de busca (estados, transições, estados-meta, estado inicial) e uma heurística h "que preserva completude". A partir daí classifica espaços de busca em 4 classes quanto a becos sem saída (*dead ends*) — **undirected, harmless, recognized, unrecognized** — e, dentro da parte relevante do espaço, define patamares (*plateaus*) — mínimo local, planície, banco (*bench*), contorno, mínimo global — conforme a existência e o tipo de saídas. Constrói o espaço de estados explícito para instâncias pequenas de 20 domínios STRIPS/ADL e mede essas propriedades usando a heurística ótima relaxada h+ (calculada exaustivamente, por isso só em instâncias pequenas). Depois repete o mesmo procedimento de coleta de dados usando a heurística aproximada do **FF** (Seção 7, "Explaining FF's Runtime Behavior"), para ver se os resultados de h+ se mantêm com a heurística realmente usada por um planejador.
- **Dados/benchmarks:** 20 domínios STRIPS e ADL, incluindo os 13 das competições (Assembly, Blocksworld, Freecell, Grid, Gripper, Logistics, Miconic-ADL, Miconic-SIMPLE, Miconic-STRIPS, Movie, Mprime, Mystery, Schedule); pelo menos 100 instâncias pequenas por domínio (exceto Gripper e Movie).
- **Resultado principal:** monta uma taxonomia de domínios de planejamento (Figura 4) cruzando duas dimensões — classe de becos sem saída (undirected/harmless/recognized/unrecognized) e existência/limite de mínimos locais — sob h+. A maioria dos domínios de competição cai no lado "simples" da taxonomia. Repetindo a análise com a heurística do FF (Figura 5), o padrão em grande parte se mantém, com poucos domínios (Grid, Assembly, Miconic-SIMPLE) ganhando mínimos locais que não existiam sob h+.
- **Relação com a dissertação de 2010:**
  - **A8 (corrige, parcialmente):** 2010 descreve corretamente que Hoffmann (2001) "analisou a topologia do domínio [...] e o desempenho da heurística [...] em espaços de busca com mínima local, contornos e bancos" e que "criou uma taxonomia para domínios de planejamento, classificando-os em indireto, inofensivo, reconhecido e não reconhecido (undirected, harmless, recognized and unrecognized)" — isso confere com a Seção 5 (Definição 10) e a Seção 6 (Figura 4) do artigo. Mas a frase seguinte de 2010, "esta análise só foi feita para as heurísticas utilizadas nos planejadores FF e HSP", está **incorreta**: a análise central do artigo (Seções 3–6, toda a taxonomia da Figura 4) usa a heurística **ótima relaxada h+**, que é teórica e não é "a heurística utilizada" por nenhum planejador real — é uma idealização, calculada exaustivamente só para poder comparar contra qualquer aproximação. Só a Seção 7 reaplica o método à heurística **efetivamente usada pelo FF**; o **HSP não é analisado empiricamente em nenhum ponto do artigo** — aparece apenas na Introdução (contexto histórico) e na Seção 8 (Conclusão), como trabalho futuro: "For the FF and HSP heuristic functions, we are going to take samples from the state spaces of larger tasks" (ver Trecho 3). Ou seja, 2010 troca o escopo real do estudo (h+ teórico, em 20 domínios; FF, empiricamente, em um subconjunto) por um escopo que nunca foi executado (FF e HSP).
  - Como observação lateral de tradução: 2010 verte "undirected" por "indireto"; o termo mais próximo em português seria "não-direcionado" (a classe descreve grafos cujas arestas são bidirecionais). Não muda a substância da citação, mas é uma imprecisão terminológica.
- **Continuação em periódico:** o mesmo estudo foi republicado, ampliado (30 domínios em vez de 20, provas formais das conexões entre estrutura do domínio e topologia), como Hoffmann, J. "Where 'Ignoring Delete Lists' Works: Local Search Topology in Planning Benchmarks." *Journal of Artificial Intelligence Research*, v. 24, p. 685–758, 27 nov. 2005. DOI: [10.1613/jair.1747](https://doi.org/10.1613/jair.1747) (confirmado via Crossref). Não li o texto integral desta versão de periódico; registro aqui só a existência e o DOI, sem nota separada, por instrução do coordenador.

## Pontos relevantes para o projeto

- É a fonte primária real por trás de A8; a nota anterior do projeto associada ao nome "Hoffmann 2001" (`hoffmann2001ff`) é sobre outro artigo — a Fase 2 deve usar `hoffmann2001topology` em qualquer citação a este trabalho específico.
- O artigo é uma análise de topologia de espaço de busca, não uma "revisão" no sentido de estado da arte — reforça a leitura da Fase 1 (insumo A8) de que a seção "Trabalhos relacionados" de 2010 é insuficiente como revisão de literatura, independentemente de a citação a Hoffmann (2001) estar substancialmente correta.
- Traz um bib próprio do autor com a citação exata (páginas 453–458, IJCAI-01, Seattle) — evidência direta e não apenas de terceiros.

## Marcações

- `[FATO]` A taxonomia de 4 classes (undirected, harmless, recognized, unrecognized) e a Figura 4 usam a heurística ótima relaxada h+, não a heurística de nenhum planejador específico (Seções 3, 5 e 6).
- `[FATO]` A aplicação da mesma metodologia à heurística do FF é a única heurística de planejador real efetivamente testada no artigo (Seção 7); HSP não é testado.
- `[HIPÓTESE]` A menção de 2010 a "FF e HSP" provavelmente veio de uma leitura apressada da Introdução (que cita FF e HSP como planejadores que usam a mesma ideia de relaxação) ou da frase de trabalhos futuros da Conclusão, confundida com o que já havia sido executado.

## Trechos literais

1. "The results suggest that, given the heuristic based on the relaxation, many planning benchmarks are simple in structure. This sheds light on the recent success of heuristic planners employing local search." (Resumo)
2. "Any search space with heuristic evaluation falls into one of the following four classes, with respect to dead ends. [...] 1. undirected [...] 2. harmless [...] 3. recognized [...] 4. unrecognized" (Definição 7, Seção 3)
3. "The stated hypotheses must be verified. For the h+ function, we are going to prove our hypotheses analytically. For the FF and HSP heuristic functions, we are going to take samples from the state spaces of larger tasks." (Seção 8, Conclusão e perspectivas — trabalho futuro, não executado neste artigo)

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 23/09/2026. Leitura de texto integral: PDF obtido convertendo o postscript original do autor (`ijcai01.ps.gz`, fai.cs.uni-saarland.de/hoffmann/papers/) com `ps2pdf` e extraído com `pdftotext -layout`. Páginas e citação exata (453–458, IJCAI-01) conferidas contra o arquivo `.bib` publicado pelo próprio autor na mesma página. DOI e dados do artigo de periódico de 2005 (JAIR) conferidos via Crossref (`10.1613/jair.1747`). Conferência humana: pendente.
