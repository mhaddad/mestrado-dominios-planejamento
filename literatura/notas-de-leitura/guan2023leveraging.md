---
tipo: nota-de-leitura
eixo: E5
citekey: guan2023leveraging
prioridade: B
status: lido
profundidade: resumo
fonte-lida: https://arxiv.org/pdf/2305.14909 (PDF baixado, lidos resumo, introdução e conclusão)
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: []
fragilidades: [F3]
perguntas: [Q3]
---

# Leveraging Pre-trained Large Language Models to Construct and Utilize World Models for Model-based Task Planning

**Guan, L.; Valmeekam, K.; Sreedharan, S.; Kambhampati, S. · 2023 · NeurIPS 2023**
**Link/DOI:** https://doi.org/10.48550/arxiv.2305.14909

## Extração estruturada

- **Problema:** métodos que usam LLMs diretamente como planejadores têm baixa confiabilidade (planos incorretos, dependência forte de feedback do ambiente); o artigo busca um paradigma alternativo.
- **Método:** usa o LLM (GPT-4) para construir um modelo de mundo explícito em PDDL, que depois é usado por planejadores clássicos independentes de domínio; o LLM também serve de interface entre PDDL e fontes de correção (validadores PDDL, humanos), traduzindo PDDL para linguagem natural e vice-versa.
- **Dados/benchmarks:** dois domínios da IPC e um domínio doméstico ("Household") mais complexo que benchmarks usuais como ALFWorld.
- **Resultado principal:** GPT-4 consegue produzir modelos PDDL de boa qualidade para mais de 40 ações, e os modelos corrigidos resolvem 48 tarefas de planejamento desafiadoras, mantendo a garantia de corretude do planejador externo e reduzindo o envolvimento humano.
- **Relação com a dissertação de 2010:** sem confirmar/corrigir diretamente nenhuma afirmação A1–A8 (não mede características UML nem cobertura de planejadores das IPCs de 2010), mas dialoga com **F3** (dependência do modelador): aqui o "modelador" de PDDL passa a ser o LLM, com humano só corrigindo, o que desloca — sem eliminar — o problema da dependência de quem constrói o modelo do domínio. Alimenta **Q3** (LLM no papel de gerador de modelo de domínio, não de planejador).

## Pontos relevantes para o projeto

- Ilustra concretamente um dos papéis possíveis do LLM na cadeia de planejamento (construtor de modelo de domínio PDDL), distinto de "LLM como planejador" — útil para estruturar a seção de LLMs da revisão (Q3).
- A limitação reconhecida pelos próprios autores — domínios de avaliação ainda mais simples que os da literatura clássica de planejamento — é relevante para avaliar se a comparação com a amostra de domínios de 2010 (F2, amostra pequena) é justa.
- Assume observabilidade completa e grounding perfeito de predicados, limitações explícitas que os autores apontam como trabalho futuro.

## Trechos literais

"We introduce a novel alternative paradigm that constructs an explicit world (domain) model in planning domain definition language (PDDL) and then uses it to plan with sound domain-independent planners" (resumo).

## Marcações

- `[FATO]` o artigo demonstra, em dois domínios da IPC e um domínio doméstico, que GPT-4 pode gerar e corrigir modelos PDDL usados depois por planejadores clássicos (seção 6, Conclusão).
- `[HIPÓTESE]` interpretação minha: esse desenho de pipeline (LLM gera modelo → planejador clássico resolve) é o que mais se aproxima, entre os trabalhos deste lote, de uma ponte direta entre a linha de 2010 (modelagem de domínio) e a era dos LLMs — ligação com Q3.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de resumo, introdução e conclusão (seção 6) do PDF em https://arxiv.org/pdf/2305.14909. Conferência humana: pendente.
