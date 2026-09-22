---
tipo: nota-de-leitura
eixo: E3
citekey: seipp2020saturated
prioridade: B
status: lido
profundidade: resumo
fonte-lida: https://jair.org/index.php/jair/article/view/11673
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: [A6]
fragilidades: [F4]
perguntas: []
---

# Saturated Cost Partitioning for Optimal Classical Planning

**Seipp, J.; Keller, T.; Helmert, M. · 2020 · Journal of Artificial Intelligence Research (JAIR)**
**Link/DOI:** 10.1613/jair.1.11673

## Extração estruturada

- **Problema:** combinar de forma admissível um conjunto de heurísticas admissíveis por meio da distribuição de custos de operadores entre elas (*cost partitioning*); calcular a partição de custo ótima é geralmente proibitivo computacionalmente.
- **Método:** propõe um algoritmo guloso para gerar ordens de heurísticas e usa busca por subida de encosta (*hill-climbing*) para otimizar uma ordem dada; combina ambas as técnicas e usa o máximo de múltiplas ordens como heurística.
- **Dados / benchmarks:** não especificado no resumo além de referências a experimentos comparativos com ordens aleatórias.
- **Resultado principal:** o *saturated cost partitioning* é mais rápido de computar que o particionamento ótimo e produz heurísticas de alta qualidade; combinar geração gulosa de ordens com otimização por *hill-climbing* leva a estimativas heurísticas melhores do que a melhor ordem aleatória gerada no mesmo tempo; usar o máximo de múltiplas ordens diversas melhora ainda mais a qualidade da heurística.
- **Relação com a dissertação de 2010:** detalha a família de heurísticas de abstração/particionamento de custo para planejamento ótimo, **ausente da taxonomia** de seis técnicas de A2/A6 (2010) — mais um exemplo de subfamília técnica relevante e não capturada, reforçando F4.

## Pontos relevantes para o projeto

- Junto com sievers2016analysis (mesmo lote), mostra que a família de heurísticas de abstração/particionamento de custo é tecnicamente rica (múltiplas subtécnicas: *merge-and-shrink*, *saturated cost partitioning*) e ausente de A6.
- Publicado em JAIR, veículo de peso, o que reforça a relevância da família para uma taxonomia revisada.

## Trechos literais

- "Saturated cost partitioning is an alternative that is much faster to compute and has been shown to yield high-quality heuristics. However, its greedy nature makes it highly susceptible to the order in which the heuristics are considered." (resumo)

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de resumo em https://jair.org/index.php/jair/article/view/11673 (não foi possível baixar o PDF completo nesta sessão; a página de visualização do periódico retornou apenas HTML). Conferência humana: pendente.
