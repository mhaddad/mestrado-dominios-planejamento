---
tipo: nota-de-leitura
eixo: E3
citekey: helmert2009landmarks
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: https://ojs.aaai.org/index.php/ICAPS/article/download/13370/13218/16887
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: [A6]
fragilidades: [F4]
perguntas: [Q1]
---

# Landmarks, Critical Paths and Abstractions: What's the Difference Anyway?

**Helmert, M.; Domshlak, C. · 2009 · Proceedings of ICAPS 2009**
**Link/DOI:** https://doi.org/10.1609/icaps.v19i1.13370

## Extração estruturada

- **Problema:** as principais famílias de heurísticas admissíveis para planejamento clássico ótimo — relaxações delete (h+, hmax, hadd, hFF...), caminhos críticos (família hm), abstrações (*pattern databases*, *merge-and-shrink*) e *landmarks* — foram desenvolvidas de forma largamente isolada; faltava uma teoria que relacionasse formalmente a qualidade dessas heurísticas entre si.
- **Método:** os autores provam resultados de dominância entre as quatro famílias (ex.: heurísticas de *landmarks* dominam hmax aditivo; abstrações *merge-and-shrink* dominam *landmarks* e hmax aditivo). A partir dessas provas, derivam uma nova heurística admissível, a *landmark cut heuristic* (hLM-cut), que pode ser vista simultaneamente como heurística de *landmarks*, esquema de particionamento de custo para hmax aditivo, ou aproximação da heurística ótima (intratável) h+.
- **Dados/benchmarks:** conjunto de tarefas de planejamento ótimo de IPCs anteriores (22 domínios no segundo experimento, incluindo Blocks, Satellite, Openstacks, FreeCell, Gripper); planejador A* comparado com hLA, hm&s (abstrações *merge-and-shrink*, tamanho 10.000), hmax e busca cega, além dos vencedores da IPC-2008 (Gamer, HSP*F).
- **Resultado principal:** hLM-cut aproxima h+ com erro médio quase 7 vezes menor que a próxima melhor heurística (hLA) nos domínios testados; em planejamento ótimo, A* com hLM-cut resolve 450 tarefas (vs. 422 com hLA, 312 com Gamer), superando os planejadores vencedores da IPC-2008.
- **Relação com a dissertação de 2010:**
  - **A6 (corrige/detalha):** a obra situa *landmarks* como uma das quatro famílias de heurísticas para busca heurística (não como técnica autônoma de busca), ao lado de relaxação delete, caminhos críticos e abstrações. Isso é relevante porque 2010 trata "*Heuristic Search*" como uma única categoria de técnica de planejamento (A2) sem diferenciar qual heurística está por trás — a leitura mostra que essa categoria única esconde uma família de subtécnicas com propriedades formais distintas (dominância comprovada entre elas), o que sustenta a necessidade de detalhar as técnicas (ligação com T3 dos trabalhos futuros de 2010).
  - **F4 (evidencia a fragilidade):** reforça que a taxonomia de 2010, ao tratar "*Heuristic Search*" como categoria única e "*Knowledge-based*" separadamente (A2), não tem base clara para situar heurísticas de *landmarks*, abstrações ou caminhos críticos — todas convivem sob o mesmo rótulo amplo em 2010, mas têm relações de dominância matemática bem definidas nesta obra.

## Pontos relevantes para o projeto

- Fonte primária que formaliza a heurística LM-cut, citada como semente central do eixo E3 — relevante para notas futuras sobre planejadores ótimos que a utilizam.
- Mostra que "*landmarks*" não é uma técnica de busca à parte, mas um tipo de heurística que pode ser combinado com diferentes algoritmos de busca (A*, busca gulosa) — distinção importante para não confundir heurística com técnica de busca ao revisar A2/A6.
- Estabelece resultados formais de dominância entre heurísticas (não apenas resultados empíricos), o que é incomum na literatura de planejamento e reforça o rigor da subárea desde 2009 — ponto de contraste com o tratamento empírico e descritivo das técnicas em 2010.
- Cita explicitamente merge-and-shrink como dominante sobre *landmarks* e hmax aditivo, conectando esta nota à nota sobre helmert2014merge (mesmo eixo, mesma família de resultados).

## Marcações

- `[FATO]` As quatro famílias de heurísticas admissíveis (relaxação delete, caminhos críticos, abstrações, *landmarks*) tinham sido desenvolvidas de forma isolada antes desta obra, que prova relações formais de dominância entre elas (Resumo; Introdução).
- `[FATO]` A heurística hLM-cut, derivada dessas provas, aproxima h+ com erro muito menor que hLA e resolve mais tarefas que os vencedores da IPC-2008 em planejamento ótimo (Seção de experimentos, "Optimal Planning").
- `[HIPÓTESE]` O tratamento de "*Heuristic Search*" como categoria única em A2/A6 de 2010 provavelmente reflete o nível de detalhe dos planejadores estudados (por nome, não por heurística interna), e não uma escolha deliberada de ignorar a estrutura interna das heurísticas — mas essa escolha empobrece a taxonomia diante do que a literatura já mostrava em 2009.

## Trechos literais

1. "Current heuristic estimators for classical domain-independent planning are usually based on one of four ideas: delete relaxations, critical paths, abstractions, and, most recently, landmarks." (Resumo)
2. "Merge-and-shrink abstractions strictly dominate landmark heuristics and additive hmax heuristics." (Resumo, lista de resultados de dominância)
3. "Comparing hLM-cut to hLA, we see that hLM-cut solves significantly more tasks than hLA (450 vs. 422)." (Seção "Optimal Planning", p. 168)

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://ojs.aaai.org/index.php/ICAPS/article/download/13370/13218/16887. Conferência humana: pendente.
