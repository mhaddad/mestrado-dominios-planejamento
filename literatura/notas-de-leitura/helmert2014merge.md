---
tipo: nota-de-leitura
eixo: E3
citekey: helmert2014merge
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: https://ai.dmi.unibas.ch/papers/helmert-et-al-jacm2014.pdf
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: [A6]
fragilidades: [F4]
perguntas: [Q1]
---

# Merge-and-Shrink Abstraction: A Method for Generating Lower Bounds in Factored State Spaces

**Helmert, M.; Haslum, P.; Hoffmann, J.; Nissim, R. · 2014 · Journal of the ACM 61(3), Article 16**
**Link/DOI:** https://doi.org/10.1145/2559951

## Extração estruturada

- **Problema:** como gerar heurísticas admissíveis (limites inferiores) para busca em espaços de estados descritos de forma compacta, especificamente aplicando abstrações que agregam grupos de estados em um único estado abstrato, superando as limitações de expressividade dos *pattern databases* (PDBs), que só agregam estados concordando em um subconjunto de variáveis.
- **Método:** os autores definem *sistemas de transição fatorados* (a classe maximal de sistemas de transição aos quais *merge-and-shrink* se aplica naturalmente) e adaptam a noção de bissimilaridade a esse arcabouço, de forma a garantir heurísticas perfeitas reduzindo exponencialmente o tamanho da abstração. O método opera por refinamentos sucessivos de "*merge*" (combinar variáveis/componentes) e "*shrink*" (encolher a representação por agregação de estados), com uma família de estratégias caracterizada por quatro parâmetros: estratégia de *merge*, estratégia de agregação de estado, limite de tamanho da abstração e limiar de agregação.
- **Dados/benchmarks:** conjunto de domínios padrão do IPC (Seção 8), incluindo Gripper, Movie, PSR, Schedule-Strips, Dining-Philosophers e Optical-Telegraph para os resultados teóricos de tempo polinomial, mais um conjunto mais amplo de domínios do IPC para os experimentos empíricos com estratégias aproximadas.
- **Resultado principal:** merge-and-shrink domina estritamente PDBs em teoria (classe mais geral de abstrações representável); em cinco de seis domínios com algoritmos ótimos polinomiais conhecidos (todos exceto PSR), existe uma estratégia de abstração *merge-and-shrink* em tempo polinomial que calcula uma heurística perfeita; estratégias mais aproximadas produzem heurísticas competitivas com o estado da arte em planejamento (Seção 9, Conclusão).
- **Relação com a dissertação de 2010:**
  - **A6 (detalha/corrige):** *merge-and-shrink* é apresentado como uma família de **abstrações** usada para construir heurísticas admissíveis para busca A* (heurística de busca), não como uma técnica de busca autônoma. Isso reforça, junto com a nota sobre landmarks (helmert2009landmarks), que a categoria "*Heuristic Search*" de A2/A6 de 2010 mistura o algoritmo de busca (A*, busca gulosa etc.) com o tipo de heurística usada (relaxação, abstração, *landmarks*, caminho crítico) — dimensões distintas que a taxonomia de 2010 não separa.
  - **F4 (evidencia a fragilidade):** o artigo mostra que abstrações por si só constituem uma subárea de pesquisa madura, com teoria própria (bissimilaridade, sistemas fatorados, provas de dominância), incompatível com o tratamento de "técnica" como rótulo único e plano em 2010.

## Pontos relevantes para o projeto

- Fonte de referência da família *merge-and-shrink*, citada como uma das principais famílias de abstrações do estado da arte — relevante para qualquer nota futura sobre planejadores ótimos do eixo E3 que a utilizem.
- Demonstra, com prova formal (Proposição 8.1–8.3), que abstrações por bissimilaridade com redução de rótulos conseguem resolver alguns domínios clássicos (Gripper, Movie, Schedule-Strips, Dining-Philosophers) de forma ótima em tempo polinomial, de modo totalmente independente de domínio — ponto relevante para discutir, na revisão, até que ponto características estruturais de domínios (tema central de 2010) explicam a dificuldade computacional.
- Confirma a limitação prática de PDBs frente a *merge-and-shrink* apenas em teoria: "the picture is not as clear in practice, where pattern databases have advantages because they can be implemented very efficiently" (Conclusão) — um alerta de que dominância teórica não implica superioridade empírica, relevante para qualquer comparação de técnicas em 2010 baseada só em cobertura (F5).
- Artigo longo e denso (63 páginas, com provas formais extensas); a leitura cobriu introdução, panorama metodológico e a seção de aplicação a IA/planejamento (Seção 8) e conclusão (Seção 9), sem entrar nas provas detalhadas do apêndice.

## Marcações

- `[FATO]` Merge-and-shrink domina estritamente *pattern databases* em teoria, mas PDBs mantêm vantagens práticas de implementação eficiente (Seção 9, Conclusão).
- `[FATO]` Existem estratégias de abstração *merge-and-shrink* em tempo polinomial que calculam heurísticas perfeitas em cinco dos seis domínios do IPC com algoritmos ótimos polinomiais conhecidos (Seção 8.1, Proposições 8.1–8.3).
- `[HIPÓTESE]` A distinção entre "tipo de heurística" (abstração, *landmarks*, relaxação, caminho crítico) e "algoritmo de busca" (A*, gulosa, *anytime*) é uma dimensão que falta explicitamente na taxonomia A2/A6 de 2010, e que aparece de forma consistente nesta obra e nas notas helmert2009landmarks e helmert2006fast do mesmo eixo.

## Trechos literais

1. "Merge-and-shrink abstraction is a new paradigm that, as we show, allows to compactly represent a more general class of abstractions, strictly dominating pattern databases in theory." (Resumo)
2. "The picture is not as clear in practice, where pattern databases have advantages because they can be implemented very efficiently; but merge-and-shrink contributes to the state of the art in planning." (Seção 9, Conclusão)
3. "We show that, of these six domains, in all but PSR there exist polynomial-time abstraction strategies for computing perfect merge-and-shrink heuristics." (Seção 8.1)

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://ai.dmi.unibas.ch/papers/helmert-et-al-jacm2014.pdf. Conferência humana: pendente.
