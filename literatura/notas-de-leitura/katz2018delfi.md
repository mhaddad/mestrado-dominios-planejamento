---
tipo: nota-de-leitura
eixo: E1
citekey: katz2018delfi
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: https://ai.dmi.unibas.ch/papers/katz-et-al-ipc2018.pdf
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: [A1, A3]
fragilidades: [F3]
perguntas: [Q2, Q3]
---

# Delfi: Online Planner Selection for Cost-Optimal Planning

**Katz, M.; Sohrabi, S.; Samulowitz, H.; Sievers, S. · 2018 · IPC 2018 planner abstracts**
**Link/DOI:** (sem DOI; https://ai.dmi.unibas.ch/papers/katz-et-al-ipc2018.pdf)

## Extração estruturada

- **Problema:** selecionar online, para cada tarefa de planejamento (faixa ótima), qual entre 16–17 planejadores baseados em Fast Downward tem maior probabilidade de resolvê-la dentro do tempo/memória da IPC.
- **Método:** Delfi converte a representação da tarefa (a versão *lifted*/PDDL ou a versão *grounded*/SAS+) num grafo (*abstract structure graph* ou *problem description graph*) e, em seguida, numa imagem em escala de cinza de 128×128 pixels; treina uma rede neural convolucional (CNN) simples para prever, por planejador, a probabilidade de resolvê-la dentro dos limites de tempo/memória; executa o planejador de maior confiança prevista pelo tempo total disponível. Delfi 1 usa a representação *lifted*; Delfi 2, a *grounded*.
- **Dados/benchmarks:** todos os domínios das faixas clássicas de todas as IPCs, mais domínios adicionais (IPP, GEDP, compilações T0/FSC); teste nos *benchmarks* da IPC 2018 (excluindo IPC 2014, usada como validação).
- **Resultado principal:** Delfi 1 tomou o primeiro lugar na faixa clássica ótima da IPC 2018 entre 16 submissões; Delfi 2 ficou em 7º lugar. No conjunto de teste (Tabela 2), Delfi 1 resolve mais problemas do que o melhor planejador isolado (SymBA*) e do que o portfólio uniforme; dois "*set covers*" de apenas 3 planejadores bastam para cobrir tudo que qualquer um dos 16/17 planejadores do portfólio resolve.
- **Relação com a dissertação de 2010:**
  - **Q2 (alimenta diretamente):** Delfi usa como única entrada uma representação estrutural automática do domínio+problema (grafo derivado da estrutura abstrata da tarefa) convertida em imagem, e uma CNN aprende diretamente da estrutura do grafo, sem qualquer *feature* manual do tipo Roberts & Howe/Cenamor — é uma resposta concreta e recente à pergunta de Q2 (métricas estruturais de modelagem acrescentam poder preditivo às *features* de PDDL?), mostrando que estrutura de grafo automática (não UML) é suficiente como base de um seletor de planejador competitivo.
  - **A3 (corrige parcialmente):** 2010 afirma que só as características do domínio, independentemente do problema, já bastam para escolher o ranking de planejadores. Delfi é *per-instance*, não *per-domain*: a arquitetura assume que características da instância específica (não só do domínio) mudam a escolha de planejador — dentro do mesmo domínio, planejadores diferentes são escolhidos para instâncias diferentes (Tabela 3; por exemplo, no domínio NURIKABE, Delfi 1 usa 6 planejadores distintos ao longo das 20 tarefas). Isso desafia diretamente a suficiência de "só características do domínio" (A3).
  - **F3 (aponta alternativa):** a extração de características de Delfi é totalmente automática (grafo → imagem), sem depender de um modelador humano — contraste direto com F3 (métricas UML dependem do modelador e de sua interpretação).

## Pontos relevantes para o projeto

- Delfi 1 (grafo *lifted*/PDDL) supera Delfi 2 (grafo *grounded*/SAS+) no conjunto de teste, mas o oposto ocorria no conjunto de validação reduzido — mostra sensibilidade da escolha de representação a efeitos condicionais presentes nos domínios de teste, não nos de validação (seção "Post-IPC Analysis").
- Os dois "*set covers*" de tamanho 3 (que cobrem tudo que o portfólio de 16/17 planejadores resolve) são evidência empírica de que poucas técnicas complementares bastam — relevante para discutir A4 (mais planejadores/técnicas melhoram o ranking) em sentido contrário: mais planejadores no portfólio não implicam mais cobertura necessária.
- Nenhuma menção a UML, itSIMPLE ou métricas de diagrama de casos de uso/classes/estados — confirma, por omissão, que a linha "*features* estruturais para seleção de planejador" pós-2010 seguiu por representações diretas do PDDL/SAS+, não por modelagem UML.

## Trechos literais

1. "no single planner should be expected to work well on all planning domains, or even on all tasks in a particular domain." (Introduction)
2. "we found two set covers of only size 3 that cover all tasks solved by any planner" (Post-IPC Analysis)
3. "Delfi 1 often consistently chooses one or few planners in a given domain (with the exception of NURIKABE), which seems to be reasonable since we expect the same planner to be strong for different tasks across a given domain." (Post-IPC Analysis)

## Marcações

- `[FATO]` Delfi 1 tomou o primeiro lugar entre 16 submissões na faixa clássica ótima da IPC 2018; Delfi 2 ficou em 7º (seção "Post-IPC Analysis").
- `[FATO]` A entrada do modelo de seleção é exclusivamente uma imagem derivada da estrutura de grafo da tarefa (lifted ou grounded), sem *features* manuais numéricas (seção "Data Representation").
- `[HIPÓTESE]` A convergência entre "poucos planejadores complementares bastam" (*set covers* de tamanho 3) e a ideia de 2010 de um "ranking" por domínio sugere que a pergunta certa pode não ser abandonar o ranking, mas trocar a fonte das características (UML → grafo da tarefa) e o alvo (só domínio → domínio+instância).

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://ai.dmi.unibas.ch/papers/katz-et-al-ipc2018.pdf. Conferência humana: pendente.
