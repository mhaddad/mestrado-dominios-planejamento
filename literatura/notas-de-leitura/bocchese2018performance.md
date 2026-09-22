---
tipo: nota-de-leitura
eixo: E3
citekey: bocchese2018performance
prioridade: B
status: lido
profundidade: texto-integral
fonte-lida: https://pure.hud.ac.uk/ws/files/14703963/ipc_robustness.pdf
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: [A6, A7]
fragilidades: [F4, F5, F6]
perguntas: [Q1]
---

# Performance robustness of AI planners in the 2014 International Planning Competition

**Bocchese, A.; Fawcett, C.; Vallati, M.; Gerevini, A.; Hoos, H. · 2018 · AI Communications**
**Link/DOI:** 10.3233/aic-170537

## Extração estruturada

- **Problema:** investigar se o *ranking* de planejadores da IPC-2014 é robusto a variações de hardware, versões de software (compilador C++, Python, Java) e limites de tempo/memória — ou seja, se o desempenho relativo entre planejadores muda conforme o ambiente de execução.
- **Método:** reexecução dos planejadores participantes da IPC-2014 (trilhas Agile e Optimal) sob diferentes configurações de hardware/software e limites de tempo/memória, comparando com o ranking oficial da competição.
- **Dados / benchmarks:** trilhas Agile (15 participantes, 14 domínios) e Optimal (17 participantes) da IPC-2014, que teve 67 participantes na parte determinística no total.
- **Resultado principal:** na trilha Optimal, **SymBA-2** (busca simbólica bidirecional cega com heurísticas de abstração por perímetro) foi declarado vencedor, com **cGamer-bd** (busca simbólica bidirecional, extensão do Gamer, vencedor da trilha correspondente em 2008) como *runner-up*. Na trilha Agile, **Yahsp3** (busca com heurísticas de *delete-relaxation*) venceu, com **Madagascar-pC** (baseado em SAT) como *runner-up*. O artigo mostra que, além dos limites de tempo/memória (já conhecidos como fatores relevantes), configurações de hardware e software também podem afetar os rankings da competição.
- **Relação com a dissertação de 2010:** fornece, com trecho literal, os vencedores da IPC-2014 e suas famílias de técnica (busca simbólica bidirecional com PDB, *delete-relaxation*, SAT), o que **corrige/detalha A6** (taxonomia de 2010, que não distingue essas subfamílias). O achado central do artigo — que rankings de cobertura dependem de configuração de hardware/software — é evidência direta em favor da fragilidade **F5** (eficiência reduzida a cobertura, A7) e **F6** (dados fora das competições podem não ser comparáveis aos oficiais), pois mostra que a própria cobertura oficial de uma IPC não é uma medida estável.

## Pontos relevantes para o projeto

- Trecho literal com vencedores e famílias de técnica da IPC-2014, útil para atualizar a taxonomia de A6/F4.
- Evidência quantitativa (não citada aqui sem o número exato, ver trecho) de que hardware/software influenciam o ranking — reforça a crítica de F5 a usar cobertura como única medida de eficiência (A7), tema central para Q1.
- Alerta metodológico relevante para qualquer replicação dos experimentos de HADDAD (2010) com dados de execução própria (F6): resultados fora do ambiente oficial da IPC podem não ser diretamente comparáveis aos rankings publicados.

## Trechos literais

- "In the Optimal track, SymBA-2, which is based on a symbolic bidirectional blind search with perimeter abstraction heuristics, was declared the winner and cGamer-bd [...] was declared as the runner-up. Finally, Yahsp3, which performs a search embedding delete-relaxed heuristics, was declared as the winner of the Agile track of IPC 2014 and Madagascar-pC, which exploits a SAT-based approach to planning, was declared the runner-up." (seção 2, "The International Planning Competition")

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://pure.hud.ac.uk/ws/files/14703963/ipc_robustness.pdf (resumo, introdução, seção sobre a IPC-2014). Conferência humana: pendente.
