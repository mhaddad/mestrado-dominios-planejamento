---
tipo: nota-de-leitura
eixo: E4
citekey: bonet2019learninga
prioridade: B
status: lido
profundidade: texto-integral
fonte-lida: https://ojs.aaai.org/index.php/AAAI/article/view/4120/3998
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: [A6]
fragilidades: [F4]
perguntas: [Q2]
---

# Learning Features and Abstract Actions for Computing Generalized Plans

**Bonet, B.; Francès, G.; Geffner, H. · 2019 · AAAI**
**Link/DOI:** 10.1609/aaai.v33i01.33012703

## Extração estruturada

- **Problema:** planejamento generalizado busca calcular planos que resolvam múltiplas instâncias de um domínio; formulações anteriores expressam planos generalizados como mapeamentos de valores de *features* para ações, mas assumem que as *features* e ações abstratas são dadas manualmente, não aprendidas.
- **Método:** aprendizado automático de *features* e ações abstratas a partir de predicados primitivos das instâncias e de transições de estado amostradas, via uma formulação de MaxSAT; um planejador FOND (*fully observable non-deterministic*) usa essa informação, transformada adequadamente, para produzir os planos generalizados.
- **Dados / benchmarks:** vários domínios de planejamento (não detalhados no trecho lido, mas mencionados como "several domains" nos experimentos).
- **Resultado principal:** o método combina aprendizado (formulação MaxSAT) e planejamento (planejador FOND) de forma inédita, produzindo *features* e ações abstratas automaticamente a partir de transições amostradas, com garantias de corretude e resultados experimentais reportados em vários domínios.
- **Relação com a dissertação de 2010:** relevante para **Q2** (métricas estruturais de modelagem acrescentam poder preditivo às *features* de PDDL?) — este trabalho aprende *features* a partir de predicados primitivos e transições de estado, em vez de a partir de métricas de diagramas UML como em HADDAD (2010); a comparação entre os dois tipos de *feature* (estrutural/UML vs. aprendida de transições de estado) é uma questão em aberto que este artigo não responde diretamente, mas ilustra uma alternativa concreta. Também estende a taxonomia de técnicas de A6/F4: "planejamento generalizado com *features* e ações abstratas aprendidas" é uma família não presente em 2010.

## Pontos relevantes para o projeto

- Mostra uma alternativa moderna e bem-sucedida a *features* extraídas manualmente (ou de diagramas UML, como em 2010): *features* aprendidas automaticamente de predicados primitivos e amostras de transição — ponto de comparação direto para Q2.
- Introduz outra família de técnica (planejamento generalizado com aprendizado de *features*/ações abstratas via MaxSAT + FOND) ausente de A2/A6.
- Cita lipovetzky2012width (também deste lote) como referência técnica, mostrando a interconexão da literatura de planejamento por largura/novidade com planejamento generalizado.

## Marcações

- `[FATO]` O método aprende *features* e ações abstratas automaticamente a partir de predicados primitivos e transições de estado amostradas, usando uma formulação MaxSAT (resumo; seção Introdução).
- `[HIPÓTESE]` A comparação entre *features* aprendidas (deste trabalho) e métricas estruturais de modelagem UML (HADDAD 2010) poderia, em princípio, ser testada empiricamente para responder a Q2, mas isso não foi feito neste artigo nem nesta nota.

## Trechos literais

- "a learner, based on a Max SAT formulation, yields the features and abstract actions from sampled state transitions, and a FOND planner uses this information, suitably transformed, to produce the general plans" (resumo)

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://ojs.aaai.org/index.php/AAAI/article/view/4120/3998 (resumo, introdução e seção de referências finais). Conferência humana: pendente.
