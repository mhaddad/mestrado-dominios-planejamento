---
tipo: nota-de-leitura
eixo: E1
citekey: bischl2016aslib
prioridade: B
status: lido
profundidade: resumo
fonte-lida: https://arxiv.org/pdf/1506.02465
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: [A1]
fragilidades: [F2, F6]
perguntas: [Q1, Q2]
---

# ASlib: A Benchmark Library for Algorithm Selection

**Bischl, B.; Kerschke, P.; Kotthoff, L.; Lindauer, M.; Malitsky, Y.; Fréchette, A.; Hoos, H.; Hutter, F.; Leyton-Brown, K.; Tierney, K.; Vanschoren, J. · 2016 · Artificial Intelligence, v. 237 (também em arXiv:1506.02465)**
**Link/DOI:** 10.1016/j.artint.2016.04.003

## Extração estruturada

- **Problema:** a comunidade de seleção de algoritmos carece de um formato padronizado e de um repositório compartilhado de dados, o que dificulta comparar diferentes abordagens de forma justa e reproduzível.
- **Método:** proposta de um formato padronizado para representar cenários de seleção de algoritmos (instâncias, algoritmos, *features*, custos de execução) e criação de um repositório (ASlib) com número crescente de conjuntos de dados da literatura, além de uma plataforma online com análise exploratória automática (resumos de desempenho, de *features*, resultados de modelos de aprendizado de máquina padrão por cenário).
- **Dados/benchmarks:** múltiplos cenários de seleção de algoritmo de diferentes áreas (SAT, CSP, ASP, Max-SAT, planejamento, entre outras), incluindo um cenário de "quebra de simetria" descrito como altamente homogêneo (parametrizações de uma única heurística com busca A* ou IDA*), representando um problema real e sensível a tempo da literatura de pesquisa operacional.
- **Resultado principal:** o artigo não relata um experimento de desempenho único, mas entrega a infraestrutura (formato + repositório + análise automática) usada depois por AutoFolio, pelas competições de seleção de algoritmo (2015/2017) e por dezenas de trabalhos do eixo E1.
- **Relação com a dissertação de 2010:** sem relação direta com A1-A8 (não é sobre planejamento especificamente nem sobre domínios de planejamento), mas **é o pré-requisito de infraestrutura que 2010 não teve**: um formato compartilhado de cenários, *features* e desempenho por instância. Toca **F2** (amostra pequena) e **F6** (dados fora das competições): ASlib resolve exatamente o problema de dispersão de dados que 2010 enfrentou ao reunir manualmente dados de IPCs e execuções próprias.

## Pontos relevantes para o projeto

- É citado como base direta por AutoFolio (lindauer2015autofolio) e pelas competições de seleção de algoritmo (lindauer2019algorithm), ambos já revisados neste lote — funciona como nó de infraestrutura comum ao eixo E1.
- Relevante para **Q1**: se uma réplica de 2010 quiser reunir mais planejadores/domínios com rigor, o formato ASlib (ou um equivalente específico de planejamento, como IPC de ferber2019ipc) é o padrão metodológico esperado hoje, algo ausente em 2010.
- A menção a um cenário "altamente homogêneo" (mesma heurística, dois algoritmos de busca) é um lembrete útil para **F4** (taxonomia de técnicas discutível): mesmo dentro de uma "técnica" única, variações de implementação/busca podem gerar diferenças de desempenho relevantes.

## Trechos literais

> "Years of fruitful applications in a number of domains have resulted in a large amount of data, but the community lacks a standard format or repository for this data. [...] To address this problem, we introduce a standardized format for representing algorithm selection scenarios and a repository that contains a growing number of data sets from the literature." (Resumo)

## Marcações

- `[FATO]` O artigo introduz um formato padronizado e um repositório crescente de cenários de seleção de algoritmo, com análise exploratória automática por cenário (Resumo; Seção 5).
- `[HIPÓTESE]` A ausência de um formato/repositório compartilhado equivalente ao ASlib, específico para planejamento automatizado no momento de 2010, é uma condição estrutural que ajuda a explicar por que a dissertação teve de montar seus próprios dados manualmente (F6) — uma lacuna que a comunidade de planejamento só começou a fechar de forma mais sistemática depois, com iniciativas como IPC (ferber2019ipc).

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de resumo, introdução e trechos da Seção 5 em https://arxiv.org/pdf/1506.02465. Conferência humana: pendente.
