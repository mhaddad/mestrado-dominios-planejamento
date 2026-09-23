---
tipo: nota-de-leitura
eixo: E1
citekey: hutter2009paramils
prioridade: B
status: lido
profundidade: resumo
fonte-lida: https://jair.org/index.php/jair/article/download/10628/25415/19763
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: []
fragilidades: [F4]
perguntas: [Q1]
---

# ParamILS: An Automatic Algorithm Configuration Framework

**Hutter, F.; Hoos, H. H.; Leyton-Brown, K.; Stützle, T. · 2009 · Journal of Artificial Intelligence Research 36**
**Link/DOI:** 10.1613/jair.2861

## Extração estruturada

- **Problema:** encontrar automaticamente, para um algoritmo alvo com parâmetros ordinais e/ou categóricos, a configuração que otimiza o desempenho sobre uma classe de instâncias de problema — evitando o ajuste manual, trabalhoso e ad hoc, dos parâmetros.
- **Método:** revisão de uma família de procedimentos de configuração baseados em busca local e proposta de técnicas novas para acelerá-los, limitando adaptativamente o tempo gasto avaliando cada configuração (o *framework* ParamILS).
- **Dados/benchmarks:** configuração de algoritmos completos e incompletos para SAT, e do solver de programação inteira mista CPLEX; comparação contra configurações padrão definidas manualmente.
- **Resultado principal:** ParamILS obteve melhorias de desempenho substanciais e consistentes em relação às configurações padrão definidas manualmente, inclusive no primeiro trabalho publicado (à época) sobre configuração automática do CPLEX.
- **Relação com a dissertação de 2010:** sem relação direta com as afirmações A1–A8 (ParamILS ajusta parâmetros de um algoritmo já escolhido; não trata da relação entre características de domínio e escolha de técnica). Toca indiretamente **F4** (taxonomia de técnicas discutível): ParamILS mostra que o desempenho de um algoritmo depende fortemente de sua configuração de parâmetros, então comparar "técnicas" (como faz 2010) sem controlar a configuração de cada planejador é uma fonte adicional de variância não isolada pela dissertação.

## Pontos relevantes para o projeto

- É a origem do *framework* de configuração automática (ILS adaptativo) citado por praticamente toda a literatura de seleção de algoritmos e portfólios do eixo E1 (AutoFolio, ASlib etc.), inclusive como pré-requisito metodológico de qualquer réplica de 2010 que queira comparar planejadores em pé de igualdade.
- Relevante para **Q1**: se uma réplica de 2010 comparar planejadores sem configurá-los automaticamente, corre o risco de medir a qualidade do ajuste manual de cada equipe, não da técnica em si.

## Trechos literais

> "Nevertheless, using our automated algorithm configuration procedures, we achieved substantial and consistent performance improvements." (Resumo)

## Marcações

- `[FATO]` O artigo demonstra ganhos de desempenho consistentes ao configurar automaticamente solvers de SAT e o CPLEX, comparado a configurações manuais padrão (Resumo).
- `[HIPÓTESE]` Comparações de "técnicas" de planejamento, como em 2010, ficam sujeitas a viés de configuração manual desigual entre planejadores, problema que ParamILS torna explícito para outras áreas de IA.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de resumo e trechos de introdução/conclusão em https://jair.org/index.php/jair/article/download/10628/25415/19763. Conferência humana: pendente.
