---
tipo: nota-de-leitura
eixo: E3
citekey: kautz2006satplan
prioridade: B
status: lido
profundidade: texto-integral
fonte-lida: https://ipc06.icaps-conference.org/deterministic/booklet/deterministic11.pdf
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026 (aprovação delegada ao Coordenador)
afirmacoes-2010: [A6]
fragilidades: [F4]
perguntas: [Q1]
---

# SatPlan: Planning as Satisfiability

**Kautz, H.; Selman, B.; Hoffmann, J. · 2006 · Booklet da 5ª Competição Internacional de Planejamento (IPC-5), ICAPS-06**
**Link/DOI:** https://ipc06.icaps-conference.org/deterministic/booklet/deterministic11.pdf (sem DOI registrado; descrição oficial do planejador SatPlan-2006, a versão usada em 2010)

## Extração estruturada

- **Problema:** descrever a versão 2006 do SatPlan, atualização do planejador clássico de planejamento como satisfatibilidade, submetida à IPC-5 — exatamente a versão citada em `auditoria/condicoes-de-execucao-2010.md` como a usada nos experimentos de 2010.
- **Método:** SatPlan-2006 constrói um grafo de planos ao estilo GraphPlan até um comprimento k contendo todos os literais-objetivo; traduz as restrições do grafo (precondições, efeitos, exclusões mútuas) em cláusulas SAT, onde cada instância de ação ou fato em um passo de tempo é uma proposição; resolve com um SAT-solver genérico (o DPLL *siege*); se insatisfazível, incrementa k e repete; por fim, remove ações desnecessárias do plano encontrado.
- **Dados/benchmarks:** não traz uma tabela de cobertura; descreve as diferenças técnicas entre a versão 2004 e a versão 2006 (propagação de mutex, codificação com variáveis booleanas para ações e fluentes).
- **Resultado principal:** a versão 2006 evita os problemas de memória da versão 2004, propagando mutex apenas para fluentes (não para ações), permitindo resolver instâncias mais difíceis.
- **Relação com a dissertação de 2010:**
  - **A6 (evidencia inconsistência interna de 2010):** 2010 classifica SATPlan como Plan-Space, Partial-order, Forward-chaining, Graph-based e SAT-based (Tabela 4). A fonte confirma Graph-based e SAT-based diretamente. Porém, o próprio corpo do texto de 2010 (antes da Tabela 2) declara uma regra própria: "planejadores baseados em resolução de problemas de satisfabilidade são relacionados com a técnica Forward-chaining" — mas a Tabela 4 também marca SATPlan como Plan-Space **e** Partial-order, categorias que a literatura de planejamento trata tipicamente como alternativas a State-Space/Total-order, não como coexistentes com um rótulo "Forward-chaining" que pressupõe progressão a partir do estado inicial. A fonte primária não usa nenhum desses quatro termos (Plan-Space, Partial-order, Forward-chaining, Total-order) para descrever SatPlan: descreve construção de grafo, tradução SAT e busca por satisfatibilidade.

## Pontos relevantes para o projeto

- Confirma a versão exata usada em 2010 (SatPlan-2006), fechando uma lacuna de `auditoria/condicoes-de-execucao-2010.md` sobre qual edição do SatPlan foi executada.
- Evidencia que a Tabela 4 de 2010 combina, para os planejadores SAT-based, rótulos que a própria regra declarada no texto (SAT-based = Forward-chaining) e a taxonomia clássica de planejamento (Plan-Space vs. State-Space) não deveriam coexistir — ponto central para justificar, na Fase 2, uma dimensão separada para "representação de estado" (aqui, proposicional/SAT) em vez de forçar SAT-based em categorias de busca no espaço de estados ou de planos.

## Marcações

- `[FATO]` SatPlan-2006 constrói um grafo de planos ao estilo GraphPlan e traduz suas restrições em cláusulas SAT, resolvidas por um SAT-solver genérico (Resumo/Seção 1).
- `[FATO]` A própria dissertação de 2010 declara, no corpo do texto, uma regra estipulativa que rotula todo planejador SAT-based como Forward-chaining — mas a Tabela 4 também rotula SATPlan como Plan-Space e Partial-order, o que é uma inconsistência interna independente da fonte primária.

## Trechos literais

1. "SatPlan-2006 is an updated version of the planning as satisfiability approach originally proposed in (Kautz & Selman 1992; 1996) using hand-generated translations, and implemented for PDDL input in the Blackbox system (Kautz & Selman 1999)." (Seção 1)

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 23/09/2026. Leitura de texto integral em https://ipc06.icaps-conference.org/deterministic/booklet/deterministic11.pdf (PDF baixado diretamente do booklet oficial da IPC-5 e extraído com `pdftotext -layout`). Conferência humana: pendente.
