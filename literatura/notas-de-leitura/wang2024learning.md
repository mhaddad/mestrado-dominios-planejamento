---
tipo: nota-de-leitura
eixo: E4
citekey: wang2024learning
prioridade: B
status: lido
profundidade: resumo
fonte-lida: https://ojs.aaai.org/index.php/ICAPS/article/view/31526
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: [A6]
fragilidades: [F4]
perguntas: []
---

# Learning Generalised Policies for Numeric Planning

**Wang, R.X.; Thiébaux, S. · 2024 · ICAPS**
**Link/DOI:** 10.1609/icaps.v34i1.31526

## Extração estruturada

- **Problema:** estender *Action Schema Networks* (ASNets) para aprender políticas generalizadas em planejamento numérico, que apresenta variáveis de estado, pré-condições e efeitos numéricos quantitativos — fora do escopo puramente proposicional.
- **Método:** propõe uma arquitetura de rede neural capaz de raciocinar sobre variáveis numéricas diretamente e em contexto com outras variáveis, além de um algoritmo de exploração dinâmica para treinamento mais eficiente, balanceando melhor o *trade-off* exploração/aprendizado dado o maior custo computacional dos planejadores-professores numéricos.
- **Dados / benchmarks:** não especificado no resumo além de "algumas domínios" comparados a planejadores numéricos tradicionais.
- **Resultado principal:** as políticas generalizadas aprendidas conseguem superar planejadores numéricos tradicionais em alguns domínios, e o algoritmo de exploração dinâmica é, em média, muito mais rápido para aprender políticas generalizadas eficazes do que o algoritmo de treinamento original das ASNets.
- **Relação com a dissertação de 2010:** estende a família de aprendizado de políticas generalizadas (ASNets) para o fragmento numérico de PDDL, fora do escopo de HADDAD (2010) (que trata planejamento STRIPS/PDDL clássico, sem fluentes numéricos). Mais um exemplo de família técnica (redes neurais para políticas generalizadas, agora em planejamento numérico) ausente de A2/A6, reforçando F4.

## Pontos relevantes para o projeto

- Mostra a evolução da família ASNets para um fragmento de PDDL (planejamento numérico) não coberto por 2010, delimitando fronteiras de aplicabilidade da taxonomia original.
- Relevante como pano de fundo caso o Coordenador queira mapear a família "aprendizado de políticas generalizadas" como uma expansão relevante e ativa de escopo em relação a 2010.

## Trechos literais

- "We extend Action Schema Networks (ASNets) to learn generalised policies for numeric planning, which features quantitative numeric state variables, preconditions and effects." (resumo)

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de resumo em https://ojs.aaai.org/index.php/ICAPS/article/view/31526 (não foi possível baixar o PDF completo nesta sessão; a página de visualização do periódico retornou apenas HTML). Conferência humana: pendente.
