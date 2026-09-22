---
tipo: nota-de-leitura
eixo: E6
citekey: gestrin2024nl2plan
prioridade: B
status: lido
profundidade: resumo
fonte-lida: https://arxiv.org/pdf/2405.04215 (PDF baixado, lidos resumo e introdução)
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: [T1]
fragilidades: [F3]
perguntas: [Q3]
---

# NL2Plan: Robust LLM-Driven Planning from Minimal Text Descriptions

**Gestrin, E.; Kuhlmann, M.; Seipp, J. · 2024 · arXiv preprint**
**Link/DOI:** https://doi.org/10.48550/arxiv.2405.04215

## Extração estruturada

- **Problema:** modelar tarefas de planejamento em formatos como PDDL é tedioso e propenso a erro; planejar diretamente com LLMs não oferece garantias de qualidade ou corretude do plano. O artigo busca unir as vantagens das duas abordagens.
- **Método:** apresentam o NL2Plan, primeiro sistema totalmente automático para gerar tarefas PDDL completas a partir de descrições mínimas em linguagem natural. Usa um LLM para extrair incrementalmente as informações necessárias do texto curto de entrada, criando uma descrição PDDL completa de domínio e problema, que é então resolvida por um planejador clássico. Adiciona etapas de raciocínio específicas de PDDL, feedback automatizado de senso comum e sugestões de correção guiadas pelo planejador.
- **Dados/benchmarks:** sete domínios de planejamento, cinco dos quais são novos (não presentes nos dados de treino do LLM), comparado a uma baseline que usa LLM + validador de sintaxe.
- **Resultado principal:** NL2Plan supera a baseline em todos os domínios exceto Blocksworld (onde a baseline mostra sinais claros de memorização); modela corretamente vários domínios quase perfeitamente, chegando a modelar 260% mais tarefas perfeitamente que a baseline quando usado de forma independente.
- **Relação com a dissertação de 2010:** **confirma parcialmente a intenção de T1** (trabalho futuro de 2010: extração automática das métricas/modelo no itSIMPLE), realizando — por outra via tecnológica (LLM, não UML/itSIMPLE) — a automação completa da construção do modelo de domínio a partir de descrição mínima. Dialoga com **F3**: ao automatizar toda a cadeia (extração → PDDL → solução), reduz a dependência de um modelador humano especialista, embora ainda dependa da qualidade da descrição textual de entrada. Alimenta **Q3**.

## Pontos relevantes para o projeto

- É um dos exemplos mais completos do lote de "T1 realizado por outros meios": automação de ponta a ponta da modelagem de domínio, o que 2010 apontava como desejável mas não implementado.
- O cuidado metodológico de usar domínios *não vistos* no treino do LLM (cinco de sete) é uma boa prática a mencionar ao avaliar a robustez de alegações sobre "generalização" de LLMs em outros artigos do lote.
- Uso do termo "*assistive modeling tool*" é relevante: os autores não alegam substituição total do modelador humano, apenas auxílio substancial — posição mais cautelosa que útil para nuançar a narrativa de automação total.

## Trechos literais

"We present NL2Plan, the first fully automatic system for generating complete PDDL tasks from minimal natural language descriptions" (resumo).

## Marcações

- `[FATO]` o artigo avalia o NL2Plan em sete domínios (cinco inéditos para o LLM) e mostra desempenho superior à baseline LLM+validador em todos exceto Blocksworld (resumo; seção de resultados).
- `[HIPÓTESE]` interpretação minha: este trabalho é um dos candidatos mais fortes, entre os lidos neste lote, para ilustrar como o trabalho futuro T1 de 2010 acabou sendo perseguido — não pela extensão do itSIMPLE, mas por uma trilha tecnológica totalmente diferente (LLMs), quinze anos depois.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de resumo e introdução do PDF em https://arxiv.org/pdf/2405.04215. Conferência humana: pendente.
