---
tipo: nota-de-leitura
eixo: E7
citekey: goodhue1995task
prioridade: A
status: lido
profundidade: resumo
fonte-lida: https://api.crossref.org/works/10.2307/249689
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: []
fragilidades: []
perguntas: [Q4]
---

# Task-Technology Fit and Individual Performance

**Goodhue, D.L.; Thompson, R.L. · 1995 · MIS Quarterly, vol. 19, n. 2, p. 213–236**
**Link/DOI:** 10.2307/249689

## Extração estruturada

- **Problema:** entender a ligação entre sistemas de informação (SI) e desempenho individual — especificamente, sob quais condições uma tecnologia de informação tem impacto positivo no desempenho de quem a usa.
- **Método:** os autores propõem um modelo teórico que combina dois programas de pesquisa complementares (utilização de SI e ajuste tarefa-tecnologia) e testam empiricamente o núcleo do modelo. A alegação central é que, para uma tecnologia de informação ter impacto positivo no desempenho individual, ela (1) precisa ser utilizada e (2) precisa ter um bom ajuste com as tarefas que apoia (*task-technology fit*, TTF). O modelo foi testado com dados de mais de 600 indivíduos em duas empresas.
- **Dados/benchmarks:** levantamento (*survey*) com mais de 600 indivíduos em duas empresas; não é um *benchmark* computacional.
- **Resultado principal:** o modelo recebeu suporte moderado ("moderately supported") pelos dados. O resumo do periódico (Crossref/JATS, texto do próprio editor) afirma que a pesquisa evidencia a importância do ajuste entre tecnologias e as tarefas dos usuários para que a tecnologia da informação tenha impacto no desempenho individual, e sugere que o *task-technology fit*, decomposto em seus componentes mais detalhados, poderia servir de base para uma ferramenta diagnóstica capaz de avaliar se os sistemas e serviços de informação de uma organização atendem às necessidades dos usuários.
- **Relação com a dissertação de 2010:** não há afirmação de 2010 (A1–A8) diretamente confirmada, corrigida ou tornada obsoleta por este resumo, porque a obra trata de ajuste entre tarefa e tecnologia de informação em organizações, não de planejamento automatizado. A conexão relevante é apenas com a **Q4** (hipótese, não evidência): o TTF é o arcabouço citado como possível ponte entre "ajuste domínio-técnica" (2010) e "ajuste tarefa-agente de IA" em desenvolvimento de software — mas essa ponte é uma analogia estrutural entre dois modelos de ajuste em domínios diferentes (SI organizacional vs. planejamento automatizado), não uma consequência lógica do artigo.

## Pontos relevantes para o projeto

- Só foi possível ler o resumo do periódico (texto do editor, via Crossref/JATS — considerado texto oficial, não paráfrase de terceiros), não o texto integral; tentativas de acesso ao PDF (AISeL, misq.umn.edu) foram bloqueadas por desafio Cloudflare (HTTP 403) e por proteção de acesso (403), respectivamente.
- O TTF original é sobre *indivíduos usando um sistema de informação para realizar tarefas de trabalho*, não sobre *escolha automática de qual sistema/agente usar para uma tarefa* — a diferença é relevante para a Q4: TTF explica o desempenho de um ajuste já dado (a pessoa já está usando aquele sistema), enquanto a Q4 pergunta sobre selecionar previamente o agente mais ajustado à tarefa, mais próximo do problema de seleção de algoritmos de Rice (1976) do que do TTF clássico.
- Amostra do estudo original (mais de 600 indivíduos, duas empresas) é evocada aqui só como referência de escala de validação empírica em pesquisa social — não deve ser comparada diretamente com a amostra pequena de 2010 (F2), que é de natureza totalmente diferente (planejadores × domínios, não pessoas × sistemas).
- Não foi possível, com apenas o resumo, extrair as dimensões específicas do construto TTF (ex.: qualidade dos dados, confiabilidade, funcionalidade) citadas em fontes secundárias sobre a teoria — qualquer detalhamento dessas dimensões no texto final precisa vir de leitura do texto integral, ainda pendente.

## Marcações

- `[FATO]` "for an information technology to have a positive impact on individual performance, the technology: (1) must be utilized and (2) must be a good fit with the tasks it supports. This new model is moderately supported by an analysis of data from over 600 individuals in two companies" (resumo, Crossref/JATS, texto do editor da MIS Quarterly).
- `[HIPÓTESE]` Ligação com Q4: a lógica de "ajuste entre o que a tarefa exige e o que a tecnologia oferece, medido de forma decomposta em componentes" é estruturalmente análoga à proposta de 2010 de usar características do domínio (decompostas em métricas UML) para escolher a técnica de planejamento — mas essa é uma transposição de domínio (SI organizacional → agentes de IA em desenvolvimento de software) que o artigo não faz nem sustenta; é uma hipótese de trabalho do projeto, não uma conclusão do TTF.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de resumo em https://api.crossref.org/works/10.2307/249689 (texto do editor, formato JATS). Tentativas de acesso ao texto integral em https://aisel.aisnet.org (bloqueado por Cloudflare) e https://misq.umn.edu (HTTP 403) não tiveram sucesso. Conferência humana: pendente.
