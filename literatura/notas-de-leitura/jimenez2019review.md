---
tipo: nota-de-leitura
eixo: E4
citekey: jimenez2019review
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: https://serjice.webs.upv.es/publications/sergio-ker18/sergio-ker18.pdf
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: [A5]
fragilidades: [F3, F4]
perguntas: [Q2]
---

# A review of generalized planning

**Jiménez, S.; Segovia-Aguas, J.; Jonsson, A. · 2019 · The Knowledge Engineering Review**
**Link/DOI:** 10.1017/s0269888918000231

## Extração estruturada

- **Problema:** revisar os formalismos recentes para representar, computar e avaliar planos generalizados — soluções válidas para múltiplas instâncias de planejamento — relacionando-os a formalismos preexistentes que também visam generalidade (conhecimento de controle de domínio, planejamento sob incerteza).
- **Método:** revisão estruturada em torno de quatro perguntas: como representar conjuntos de tarefas de planejamento (ações, estados iniciais e metas); como representar os próprios planos generalizados (estruturas de controle de fluxo — ramificação, laços — e variáveis quantificadas, existenciais ou universais); como executar e validar esses planos; e como computá-los e reutilizá-los.
- **Dados/benchmarks:** não aplicável (artigo de revisão); discute implementações e formalismos de trabalhos individuais (DSPlanners, controladores de estados finitos, políticas generalizadas, planos com metas indexadas etc.), incluindo o próprio Srivastava et al. (2011) deste lote.
- **Resultado principal:** conclui que planos generalizados resolvem tarefas além do alcance do planejamento clássico (múltiplas instâncias, número ilimitado de objetos, observabilidade parcial, não determinismo), mas que a escolha da representação (implícita vs. explícita, com ou sem variáveis quantificadas, com ou sem estruturas de controle) é o fator que define tanto o espaço de soluções alcançável quanto a complexidade computacional do problema — e que identificar automaticamente a melhor representação para uma tarefa dada continua sendo um problema em aberto.
- **Relação com a dissertação de 2010:** reforça, sete anos depois da primeira revisão do mesmo autor (Jiménez et al. 2012, também neste lote), a mesma lacuna central relevante para **Q2**: não existe ainda um método para derivar automaticamente a representação mais adequada de um domínio ou tarefa. Isso **relativiza A5** de forma semelhante à nota anterior — a hipótese de 2010 (UML mede a complexidade relevante do domínio) é uma escolha de representação entre muitas, e a revisão de 2019 mostra que a área ainda não convergiu para uma resposta geral, mesmo em um subcampo (planejamento generalizado) mais maduro que em 2012. A discussão de **trade-off entre expressividade e complexidade computacional** na representação do plano (não do domínio, mas da solução) é um paralelo conceitual direto ao mesmo trade-off que motivou a discretização Alto/Médio/Baixo das métricas UML em 2010, sustentando **F3** e **F4** (múltiplas taxonomias e representações concorrentes, nenhuma dominante).

## Pontos relevantes para o projeto

- Distingue claramente **representação de tarefas** (o domínio propriamente dito) de **representação de planos/soluções** (políticas, controladores, planos com laços) — distinção útil para a revisão de 2026 ao situar onde cada obra do lote E4 se encaixa: 2010 mede características da tarefa/domínio (via UML); este lote de obras, em sua maioria, mede ou aprende representações da solução (política, heurística) a partir de representações mais cruas do domínio (predicados PDDL).
- Cita a caracterização das condições sob as quais uma política generaliza a outros problemas como "um primeiro passo" para automatizar a seleção de instâncias representativas — ecoando o próprio objetivo de 2010 de usar características do domínio para prever desempenho, mas aplicado à seleção de *instâncias de treino*, não de *técnicas de planejamento*.
- Relaciona formalmente planejamento generalizado a conhecimento de controle de domínio e a planejamento sob incerteza (conformante, contingente) — mapa útil para posicionar T3 de 2010 (detalhar heurística, construção da busca e subtécnicas) frente ao estado da arte atual.

## Trechos literais

> "Generalized planning studies the representation, computation and evaluation of solutions that are valid for multiple planning instances." (Resumo)

> "The computation of a generalized plan is constrained by the given instances in the generalized planning task but also by the given representation for coding the states, actions and goals." (Seção 7, "Conclusions", p. 33)

> "The automatic derivation of alternative representations that allow more effective computation of generalized plans is a promising research direction" (Seção 7, "Conclusions", p. 33)

## Marcações

- `[FATO]` A revisão organiza os formalismos de plano generalizado por estrutura de controle de fluxo (ramificação, laços) e por tipo de variável (existencial, universal), não por família algorítmica de planejador (Seção 4.1, "Representation").
- `[FATO]` Os autores identificam explicitamente, na conclusão, que a derivação automática de representações alternativas para tarefas de planejamento generalizado é uma direção de pesquisa promissora e ainda não resolvida (Seção 7, p. 33).
- `[HIPÓTESE]` A recorrência da mesma lacuna (representação de domínio/tarefa ideal ainda desconhecida) em duas revisões do mesmo autor principal, sete anos apesar, sugere que a pergunta Q2 desta revisão de 2026 não é uma pergunta menor ou lateral, mas um problema estrutural persistente do campo de aprendizado para planejamento — o que reforça a relevância de tratá-la como pergunta central, não apenas periférica, na revisão da dissertação de 2010.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://serjice.webs.upv.es/publications/sergio-ker18/sergio-ker18.pdf. Conferência humana: pendente.
