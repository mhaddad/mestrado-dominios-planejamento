---
tipo: nota-de-leitura
eixo: E4
citekey: yang2022pg3
prioridade: B
status: lido
profundidade: texto-integral
fonte-lida: https://www.ijcai.org/proceedings/2022/0650.pdf
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: [A2, A6]
fragilidades: [F4]
perguntas: [Q3, Q4]
---

# PG3: Policy-Guided Planning for Generalized Policy Generation

**Yang, R.; Silver, T.; Curtis, A.; Lozano‐Pérez, T.; Kaelbling, L.P. · 2022 · IJCAI**
**Link/DOI:** 10.24963/ijcai.2022/650

## Extração estruturada

- **Problema:** sintetizar políticas de planejamento que generalizem entre múltiplos problemas do mesmo domínio (*generalized planning*); as funções de pontuação usadas para guiar a busca por políticas (GPS — *generalized policy search*) têm limitações (avaliação de política e comparação de planos).
- **Método:** propõe PG3 (*Policy-Guided Planning for Generalized Policy Generation*), que usa uma política candidata para guiar o planejamento nas tarefas de treino, pontuando a política pela concordância entre o plano encontrado com sua orientação e a própria política; combina ideias de avaliação de política e comparação de planos.
- **Dados / benchmarks:** domínios PDDL de treino (não detalhados no trecho lido); comparação com baselines (avaliação de política, comparação de planos, contagem de metas, *behavior cloning* com redes neurais em grafo).
- **Resultado principal:** PG3 supera formulações alternativas de GPS (avaliação de política pura e comparação de planos pura), sendo capaz de descobrir eficientemente políticas compactas em domínios PDDL; há garantias teóricas de otimalidade de PG3 em um cenário simplificado.
- **Relação com a dissertação de 2010:** representa uma família de técnica — busca de políticas generalizadas guiada por planejamento — **ausente** da taxonomia de A2/A6 de HADDAD (2010), que não contempla a ideia de uma política única aplicável a múltiplas instâncias do mesmo domínio. Isso **estende/atualiza** a fragilidade F4. Também é conceitualmente relevante para **Q4** (ajuste tarefa-estratégia para escolher configurações de agentes de IA): a lógica de PG3 — usar uma política candidata para guiar a busca e pontuar sua adequação — é estruturalmente próxima da ideia de selecionar/ajustar uma estratégia (técnica) a uma tarefa (domínio), e para **Q3** (papel de LLMs como seletores/geradores de política).

## Pontos relevantes para o projeto

- Introduz uma família de técnica de planejamento generalizado (política única para múltiplas instâncias) totalmente fora do escopo de 2010, relevante para atualizar F4.
- A analogia entre "pontuar uma política candidata pela sua capacidade de guiar planejamento" e "escolher a técnica/estratégia certa para uma tarefa" é hipótese de conexão com Q4, não afirmação direta do artigo.
- Cita explicitamente limitações de planejamento generalizado em domínios com estocasticidade e observabilidade parcial como trabalho futuro, delimitando o escopo determinístico desta linha de pesquisa (compatível com o escopo de HADDAD 2010).

## Marcações

- `[FATO]` PG3 supera avaliação de política e comparação de planos como funções de pontuação para busca de políticas generalizadas (seção 6, Conclusion).
- `[HIPÓTESE]` A lógica de pontuação de PG3 (usar uma política/estratégia candidata para guiar a solução e avaliar sua adequação) é estruturalmente análoga ao problema de ajuste tarefa-estratégia de Q4, mas o artigo não trata de seleção de agentes de IA para desenvolvimento de software.

## Trechos literais

- "In this work, we proposed PG3 as a new approach for generalized planning. We demonstrated theoretically and empirically that PG3 outperforms alternative formulations of GPS, such as policy execution and plan comparison." (seção 6, Conclusion)

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://www.ijcai.org/proceedings/2022/0650.pdf (resumo, introdução e conclusão). Conferência humana: pendente.
