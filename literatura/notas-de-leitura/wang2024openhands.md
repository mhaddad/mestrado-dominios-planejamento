---
tipo: nota-de-leitura
eixo: E8
citekey: wang2024openhands
prioridade: B
status: lido
profundidade: texto-integral
fonte-lida: https://arxiv.org/abs/2407.16741
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: [A1]
fragilidades: []
perguntas: [Q4]
---

# OpenHands: An Open Platform for AI Software Developers as Generalist Agents

**Wang, X.; Li, B.; Song, Y.; Xu, F. F.; Tang, X.; et al. · 2024 · ICLR 2025**
**Link/DOI:** https://arxiv.org/abs/2407.16741

## Extração estruturada

- **Problema:** construir uma plataforma aberta e flexível para o desenvolvimento de agentes de IA capazes de interagir com o mundo da forma que um desenvolvedor humano faz — escrevendo código, interagindo com a linha de comando e navegando na web — de modo que novos agentes possam ser implementados e avaliados de forma padronizada.
- **Método:** descrevem a arquitetura da plataforma OpenHands (antes chamada OpenDevin): mecanismo de interação de agentes, ambiente sandbox seguro para execução de código, coordenação entre múltiplos agentes, e incorporação de benchmarks de avaliação. Realizam avaliação dos agentes atualmente incorporados sobre 15 tarefas desafiadoras.
- **Dados/benchmarks:** 15 tarefas desafiadoras, incluindo engenharia de software (por exemplo, SWE-bench) e navegação web (por exemplo, WebArena), entre outras; projeto de código aberto sob licença MIT, com mais de 2,1 mil contribuições de mais de 188 contribuidores.
- **Resultado principal:** a plataforma permite implementação de novos agentes, execução segura em ambiente isolado, colaboração entre múltiplos agentes e avaliação em benchmarks padronizados, tendo se tornado um projeto comunitário ativo com contribuições significativas de acadêmicos e indústria.
- **Relação com a dissertação de 2010:** **A1** [confirma por analogia, HIPÓTESE] — OpenHands não caracteriza tarefas por métricas estruturais como 2010 fez com UML, mas fornece a infraestrutura na qual uma futura pesquisa poderia medir o desempenho de diferentes configurações de agente por tipo de tarefa (SWE-bench vs. WebArena, por exemplo) — uma pré-condição de infraestrutura para testar a hipótese de ajuste tarefa-agente da Q4, não uma evidência direta dela.

## Pontos relevantes para o projeto

- É a plataforma aberta mais citada do lote para agentes de desenvolvimento de software com LLM, servindo de referência de infraestrutura comum a vários outros itens do lote (SWE-Gym de pan2024training é treinado para uso com agentes deste tipo, e MetaGPT/AutoGen abordam a colaboração multiagente que OpenHands também suporta).
- Explicitamente cobre múltiplas categorias de tarefa (engenharia de software, navegação web) no mesmo framework de avaliação — a comparação de desempenho entre essas categorias é o tipo de dado que poderia, no futuro, alimentar uma versão da Q4 (que tipo de tarefa favorece que tipo de agente/configuração).
- Artigo de infraestrutura/plataforma, não um estudo de ajuste tarefa-técnica; não há, no texto lido, uma análise sistemática de que características de tarefa predizem sucesso de qual agente.

## Trechos literais

"We introduce OpenHands, a platform for the development of powerful and flexible AI agents that interact with the world in similar ways to those of a human developer: by writing code, interacting with a command line, and browsing the web" (resumo).

## Marcações

- `[FATO]` O artigo descreve a arquitetura da plataforma OpenHands e reporta avaliação de agentes sobre 15 tarefas em múltiplas categorias (engenharia de software, navegação web), com adoção comunitária de mais de 188 contribuidores (resumo e conclusão).
- `[HIPÓTESE]` A cobertura de múltiplas categorias de tarefa no mesmo framework é uma pré-condição de infraestrutura útil para futuros estudos de ajuste tarefa-agente (Q4), mas o artigo em si não realiza essa análise.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de resumo, introdução e conclusão em https://arxiv.org/abs/2407.16741 (PDF baixado, extraído com pdftotext). Conferência humana: pendente.
