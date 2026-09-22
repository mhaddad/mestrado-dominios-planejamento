---
tipo: nota-de-leitura
eixo: E7
citekey: hu2024routerbench
prioridade: B
status: lido
profundidade: texto-integral
fonte-lida: https://arxiv.org/abs/2403.12031
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: [A1]
fragilidades: [F2]
perguntas: [Q3, Q4]
---

# RouterBench: A Benchmark for Multi-LLM Routing System

**Hu, Q.J.; Bieker, J.; Li, X.; Jiang, N.; Keigwin, B.; Ranganath, G.; Keutzer, K.; Upadhyay, S.K. · 2024 · arXiv**
**Link/DOI:** https://arxiv.org/abs/2403.12031

## Extração estruturada

- **Problema:** não existe um *benchmark* padronizado para avaliar o desempenho de sistemas de roteamento entre múltiplos LLMs, o que dificulta o progresso na área, já que nenhum LLM isolado atende de forma ótima todas as tarefas quando se equilibra desempenho e custo.
- **Método:** os autores propõem o ROUTERBENCH, um framework de avaliação que mede sistematicamente a eficácia de sistemas de roteamento de LLMs, junto com um conjunto de dados abrangente de mais de 405 mil resultados de inferência de LLMs representativos; propõem também um arcabouço teórico para roteamento de LLMs e uma análise comparativa de várias abordagens de roteamento.
- **Dados/benchmarks:** mais de 405.000 resultados de inferência coletados de LLMs representativos, cobrindo tarefas gerais e especializadas; código e dados disponíveis em github.com/withmartian/routerbench.
- **Resultado principal:** o ROUTERBENCH formaliza e avança o desenvolvimento de sistemas de roteamento de LLM e estabelece um padrão de avaliação em termos de custo de inferência (dólares) e desempenho, revelando potenciais e limitações de diferentes abordagens de roteamento em "vários campos promissores em que até roteamento simples demonstrou desempenho excepcional" (conclusão).
- **Relação com a dissertação de 2010:** **A1** [confirma por analogia direta, HIPÓTESE] — roteamento de LLM é, estruturalmente, o mesmo problema de 2010 transposto para modelos de linguagem: dado um conjunto de "técnicas" (LLMs) e uma tarefa de entrada, escolher a técnica de melhor desempenho/custo, algo que 2010 tentou fazer para planejadores a partir de características de domínio. **F2** [ajuda a tratar, HIPÓTESE] — o próprio artigo nasce da ausência de um benchmark padronizado, o que evidencia por contraste a fragilidade de amostra pequena de 2010 (F2), que não teve nenhum benchmark equivalente.

## Pontos relevantes para o projeto

- É o benchmark mais direto do lote para a lógica de "seleção de técnica" aplicada a LLMs — peça central para instanciar a Q3 (onde entram os LLMs: aqui, como opções roteáveis) e a Q4 (ajuste tarefa-modelo de IA).
- Formaliza teoricamente o problema de roteamento (Seção 3, "theoretical framework for LLM routing"), o que pode servir de referência para formalizar de modo análogo o problema original de 2010 (ajuste domínio-planejador).
- Escala de dados (405k execuções) é ordens de grandeza maior que a amostra de 2010 (13 domínios), reforçando por contraste a fragilidade F2 de 2010.
- Não trata de desenvolvimento de software especificamente nem de agentes (é sobre roteamento de consultas a LLMs em geral); a ligação com Q4 (agentes de desenvolvimento de software) é uma extensão, não o escopo do artigo.

## Trechos literais

"no single model can optimally address all tasks and applications, particularly when balancing performance with cost. This limitation has led to the development of LLM routing systems" (resumo).

## Marcações

- `[FATO]` O artigo introduz o ROUTERBENCH, um benchmark com mais de 405 mil resultados de inferência e um arcabouço teórico para avaliar sistemas de roteamento de múltiplos LLMs por custo e desempenho (resumo, introdução e conclusão).
- `[HIPÓTESE]` O problema de roteamento de LLMs é estruturalmente análogo ao problema de seleção de planejador de 2010, com "domínio" substituído por "tarefa de entrada" e "técnica de planejamento" substituída por "LLM"; essa analogia sustenta a Q3 e a Q4, mas não é afirmada pelos autores.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de resumo, introdução e conclusão em https://arxiv.org/abs/2403.12031 (PDF baixado, extraído com pdftotext). Conferência humana: pendente.
