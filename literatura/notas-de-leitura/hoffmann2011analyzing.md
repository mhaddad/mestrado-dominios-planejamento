---
tipo: nota-de-leitura
eixo: E2
citekey: hoffmann2011analyzing
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: https://jair.org/index.php/jair/article/download/10709/25587
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: [A5, A8]
fragilidades: [F1]
perguntas: [Q2]
---

# Analyzing Search Topology Without Running Any Search: On the Connection Between Causal Graphs and h+

**Hoffmann, J. · 2011 · Journal of Artificial Intelligence Research 41, 155–229**
**Link/DOI:** https://doi.org/10.1613/jair.3276

## Extração estruturada

- **Problema:** a heurística de relaxação h+ (ignorar listas de remoção) tem qualidades notáveis em muitos domínios de planejamento clássico (ausência de mínimos locais), mas as provas dessas propriedades eram feitas manualmente domínio a domínio; o artigo pergunta se é possível inferir automaticamente, por análise estática do domínio (sem rodar busca), a topologia do espaço de busca sob h+.
- **Método:** formaliza a ligação entre a estrutura do **grafo causal** (derivado da representação de domínio finito de Helmert) e a topologia de h+ (mínimos locais, distância de saída). Prova que, se o grafo causal é acíclico e toda transição de variável é inversível, não há mínimos locais sob h+. Generaliza esse resultado em critérios verificáveis em tempo polinomial e implementa a ferramenta TorchLight, que combina análise global (grafo causal completo) e local (por estado, via plano relaxado). Compara com uma alternativa mais simples — sondagem de busca (*search probing*, SP) — rodando um passo de *Enforced Hill-Climbing* de FF.
- **Dados/benchmarks:** 37 domínios (todos das IPCs até IPC 2008, exceto Cyber-Security), 1160 instâncias; planejadores FF, LAMA e uma variante simplificada (EHC) usados para validar se as taxas de sucesso da análise TorchLight predizem sucesso/fracasso do planejador.
- **Resultado principal:** de 12 domínios com ausência de mínimos locais provada manualmente, TorchLight dá garantia forte em 8 e desempenho empírico forte em mais 6; a taxa de sucesso da análise (III) e da sondagem de busca (SP/SP1s) são altamente informativas para prever se um planejador terá sucesso — mais informativas que as *features* simples usadas por Roberts & Howe (2009).
- **Relação com a dissertação de 2010:**
  - **A8 (atualiza):** 2010 cita, como único trabalho relacionado sobre topologia do espaço de busca, uma obra de Hoffmann de 2001. Esta obra (JAIR 2011, publicada após a dissertação de 2010) é a formalização madura e completa dessa mesma linha de pesquisa: estabelece pela primeira vez uma conexão formal entre estrutura do grafo causal e topologia de h+, algo que a obra citada em 2010 não tinha. Uma versão revisada da dissertação deveria substituir ou complementar a citação de 2001 por esta.
  - **A5 (corrige/refina):** 2010 afirma que diagramas UML medem a complexidade do domínio, e essa complexidade afeta o desempenho das técnicas. Esta obra mostra que o determinante estrutural concreto da "dificuldade" de um domínio para busca heurística baseada em h+ é a **ciclicidade e invertibilidade do grafo causal** — uma propriedade formal, verificável algoritmicamente a partir da tradução PDDL→FDR, e não uma contagem de elementos de diagrama UML. "Consider Logistics and Blocksworld-Arm. At the level of their PDDL domain descriptions, the difference is not evident... What does the trick is to move to the finite-domain variable representation... and to consider the associated structures, notably the causal graph" (Introdução, p. 157) — evidência direta de que a complexidade relevante não é visível nem em PDDL nem, por extensão, em contagens de diagrama UML.
  - **F1 (evidencia lacuna, com ressalva temporal):** a dissertação de 2010 não cita Roberts & Howe (2009), que já usava aprendizado de máquina para prever desempenho de planejadores a partir de características do problema — e este próprio artigo de Hoffmann (2011) discute e propõe melhorar diretamente esse trabalho. Isso mostra que já em 2009–2011 havia uma linha de pesquisa ativa e diretamente relevante ao tema de 2010, não referenciada na dissertação.
- **Features por classe (para Q2):** estruturais de grafo causal/DTG (o artigo inteiro formaliza essas estruturas); de sondagem (*search probing* SP/SP1s, alternativa mais simples às análises formais de TorchLight, mostrada como competitiva).

## Pontos relevantes para o projeto

- Contém a crítica explícita e nominal às *features* de Roberts & Howe (2009): "they currently use only very simple features, like counts of predicates and action schemes, that hardly capture a domain-independent structure relevant to planner performance" (Conclusão, p. 193) — ponto de partida direto para a discussão de Q2 no capítulo revisado.
- Formaliza precisamente o que são grafo causal e DTG (*domain transition graph*) em termos de representação de domínio finito — definição técnica de referência para qualquer nota ou capítulo que discuta *features* estruturais.
- Discute explicitamente sondagem de busca (*search probing*) como alternativa mais simples e competitiva às análises formais baseadas em grafo causal — relevante para comparar custo computacional de diferentes famílias de *features* em Q2.
- Sugere, como trabalho futuro, usar a própria análise de TorchLight para "planner performance prediction, along the lines of Roberts and Howe (2009)" — mostrando que a comunidade já via essa conexão em 2011, um ano depois da dissertação de 2010.

## Marcações

- `[FATO]` A obra estabelece, pela primeira vez, uma conexão formal entre estrutura do grafo causal (acíclico + transições inversíveis) e ausência de mínimos locais sob h+ (Seção 1, Introdução).
- `[FATO]` As *features* derivadas do TorchLight e da sondagem de busca são explicitamente comparadas, na própria obra, como mais informativas que as *features* simples (contagem de predicados e esquemas de ação) usadas por Roberts & Howe (2009) (Seção 8.2, nota 13, p. 178; Conclusão, p. 193).
- `[HIPÓTESE]` A citação isolada de "Hoffmann (2001)" em 2010 (A8) provavelmente se refere a um trabalho anterior e mais simples da mesma linha (a dissertação é de 2010, este JAIR é de 2011, logo não poderia ter sido citada) — o achado relevante aqui é que essa linha de pesquisa amadureceu significativamente logo após 2010, e uma revisão da dissertação deveria incorporar essa evolução.

## Trechos literais

1. "We establish connections between causal graph structure and h+ topology." (Resumo)
2. "Roberts and Howe (2009), for example, use very simple features only. We get back to this in the conclusion." (Seção 8.2, nota de rodapé 13, p. 178)
3. "Our experimental results indicate that TorchLight's problem features, and also those of search probing, are highly informative. This has the potential to significantly improve the results of Roberts and Howe for unseen domains – they currently use only very simple features, like counts of predicates and action schemes, that hardly capture a domain-independent structure relevant to planner performance." (Conclusão, p. 193)

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://jair.org/index.php/jair/article/download/10709/25587 (baixado com `curl`, extraído com `pdftotext -layout`). Conferência humana: pendente.
