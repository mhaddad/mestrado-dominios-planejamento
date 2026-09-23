---
tipo: nota-de-leitura
eixo: E7
citekey: vanschoren2019metalearning
prioridade: B
status: lido
profundidade: texto-integral
fonte-lida: https://arxiv.org/abs/1810.03548
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: [A1, A4]
fragilidades: [T4]
perguntas: [Q1, Q2]
---

# Meta-Learning: A Survey

**Vanschoren, J. · 2019 · em "Automated Machine Learning" (Hutter, Kotthoff, Vanschoren, orgs.), Springer**
**Link/DOI:** https://doi.org/10.1007/978-3-030-05318-5_2 (versão de acesso aberto: arXiv:1810.03548)

## Extração estruturada

- **Problema:** revisar o estado da arte em meta-aprendizado ("aprender a aprender"): observar sistematicamente como diferentes abordagens de aprendizado de máquina se comportam em uma ampla gama de tarefas de aprendizado, e usar essa experiência (meta-dados) para aprender novas tarefas muito mais rápido.
- **Método:** capítulo de levantamento (survey), categorizando técnicas de meta-aprendizado pelo tipo de meta-dado que exploram, do mais geral (avaliações de modelo) ao mais específico à tarefa.
- **Dados/benchmarks:** não aplicável diretamente (é um survey; cobre benchmarks usados por trabalhos individuais na literatura de meta-aprendizado, não conduz experimento próprio).
- **Resultado principal:** o meta-aprendizado coleta meta-dados (configurações de algoritmo, hiperparâmetros, arquiteturas, avaliações de desempenho como acurácia e tempo, parâmetros do modelo aprendido, e *meta-features* — propriedades mensuráveis da própria tarefa) e aprende a partir desses meta-dados para orientar a busca por modelos ótimos em novas tarefas; quanto mais similares as tarefas prévias, mais tipos de meta-dado podem ser aproveitados, sendo a definição de similaridade de tarefa um desafio central.
- **Relação com a dissertação de 2010:** **A1** [confirma por analogia direta, HIPÓTESE] — meta-aprendizado é exatamente a formalização, em aprendizado de máquina, da tese central de 2010: características mensuráveis de uma tarefa (*meta-features*) predizem qual algoritmo/configuração terá melhor desempenho nela. **A4** [confirma por analogia, HIPÓTESE] — a lógica de que mais meta-dados (mais tarefas, mais avaliações, mais *meta-features*) melhoram a capacidade preditiva é a mesma lógica de A4 (mais características, planejadores e técnicas melhoram o ranking). **T4** [ajuda a tratar, HIPÓTESE] — o texto menciona uso de pesos/relevância de *meta-features*, relacionável ao trabalho futuro T4 de 2010 (pesos por característica).

## Pontos relevantes para o projeto

- Fornece o vocabulário e a formalização (meta-dados, *meta-features*, similaridade de tarefa) que 2010 usa de forma implícita e não nomeada; útil para reposicionar 2010 na literatura mais ampla de seleção de algoritmo/meta-aprendizado (conecta com bischl2016aslib, kerschke2019automated, já no acervo).
- Cita explicitamente o teorema *No Free Lunch* como justificativa da necessidade de meta-aprendizado — mesma base teórica de gomez2016empirical e sterkenburg2021nofreelunch, deste lote.
- É um capítulo de survey amplo (não específico a planejamento nem a agentes de IA para desenvolvimento de software); a ligação com Q2 (métricas estruturais como *features*) é conceitual, não uma aplicação direta feita pelo autor.
- Texto de acesso aberto no arXiv, permitindo leitura completa da introdução e categorização.

## Trechos literais

"Meta-learning [...] is the science of systematically observing how different machine learning approaches perform on a wide range of learning tasks, and then learning from this experience, or meta-data, to learn new tasks much faster than otherwise possible" (resumo).

## Marcações

- `[FATO]` O capítulo define meta-aprendizado como uso sistemático de meta-dados (incluindo *meta-features* de tarefas) para acelerar o aprendizado de novas tarefas, e cita o No Free Lunch como motivação central (resumo e introdução).
- `[HIPÓTESE]` A analogia entre *meta-features* de tarefas de aprendizado de máquina e as métricas UML de domínios de planejamento em 2010 é minha leitura; o autor não faz essa ligação com planejamento automatizado.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de resumo e introdução em https://arxiv.org/abs/1810.03548 (PDF baixado, extraído com pdftotext). Conferência humana: pendente.
