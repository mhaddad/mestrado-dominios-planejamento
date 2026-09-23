---
tipo: nota-de-leitura
eixo: E6
citekey: vallati2021importance
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: https://arxiv.org/abs/2010.07710
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: [A5]
fragilidades: [F3]
perguntas: [Q2]
---

# On the Importance of Domain Model Configuration for Automated Planning Engines

**Mauro Vallati, Lukáš Chrpa, Thomas Leo McCluskey, Frank Hutter · 2021 · Journal of Automated Reasoning, v. 65, n. 6, p. 727–773**
**Link/DOI:** https://arxiv.org/abs/2010.07710 (preprint idêntico ao publicado, arXiv:2010.07710) · DOI: 10.1007/s10817-021-09592-1

## Extração estruturada

- **Problema:** versão estendida e aprofundada de Vallati et al. (2015; ver nota [@vallati2015effective]): investiga sistematicamente como a *configuração* do modelo de domínio PDDL (ordem de predicados, operadores, pré-condições e efeitos) afeta o desempenho de planejadores independentes de domínio, incluindo o efeito de macro-operadores aprendidos automaticamente e comparações de competição (IPC).
- **Método:** (i) gera 50 configurações aleatórias de cada modelo de domínio da trilha Agile do IPC 2014 e mede o impacto sobre 12 planejadores; (ii) introduz técnicas de configuração automática offline (aprendizado) e online (heurísticas) para melhorar modelos para um planejador-alvo; (iii) investiga o posicionamento de macro-operadores no modelo estendido.
- **Dados/benchmarks:** 13 domínios da IPC 2014 Agile track (Barman, Cave-Diving, Child-Snack, CityCar, Floortile, GED, Hiking, Maintenance, Parking, Tetris, Thoughtful, Transport, Visitall — Openstacks excluído por ter modelo variável por problema), 20 instâncias por domínio, 12 planejadores (Cedalion, arvandherd, Mpc/Madagascar, Jasper, Mercury, SIW, Bfs-f, Probe, Yahsp3, Freelunch, use, IbaCoP). Métricas: IPC score, PAR10, cobertura; cada execução repetida 3 vezes (mediana).
- **Resultado principal:** a configuração aleatória do modelo já produz flutuações grandes e estatisticamente significativas de desempenho (teste de Wilcoxon, p=0,05) para a maioria dos planejadores — por exemplo, o IPC score de Probe varia entre 63 e 37 apenas por reordenação do mesmo modelo semântico. Rankings de competição não são estáveis: Probe, 8º lugar pela mediana cumulativa, pôde alcançar o 2º lugar com configuração favorável e cair para 11º com configuração adversarial. A configuração automática (offline) pode gerar acelerações de até 25 vezes; o posicionamento de um único macro-operador pode gerar melhorias de até 3 ordens de magnitude no PAR10. Planejadores baseados no framework Fast Downward (que reordena operadores alfabeticamente no pré-processamento) são consistentemente menos sensíveis à configuração.
- **Relação com a dissertação de 2010:** reforça e amplia a evidência de [@vallati2015effective] para [F3] e [Q2] em escala maior (12 planejadores, 13 domínios da IPC oficial vs. 6/7). Qualifica [A5]: mostra que a "complexidade" percebida de um domínio, medida por qualquer proxy estrutural (incluindo métricas de diagramas UML como em 2010), pode estar confundida com a ordem de serialização do modelo — um artefato de engenharia, não do domínio em si. É a evidência mais forte do lote para [Q2], por oferecer números concretos de tamanho de efeito (fator de até 25× por configuração; até 3 ordens de magnitude por posição de macro) e por discutir diretamente a validade de comparações entre planejadores em competições, tema estrutural da metodologia de 2010.

## Pontos relevantes para o projeto

- Fornece números de tamanho de efeito diretamente citáveis para [Q2]: "up-to-25-fold speedup" por configuração de modelo e "up-to-3-orders-of-magnitude" por posição de macro.
- Tabela 1 (p. 10) documenta, planejador a planejador, a amplitude best/worst do IPC score e da cobertura sob 50 configurações aleatórias — dado quantitativo direto sobre o tamanho do efeito da configuração por planejador.
- Discute explicitamente a instabilidade de rankings de competição sob reconfiguração do modelo, o que é diretamente relevante à metodologia de ranking de planejadores por domínio da dissertação de 2010.
- Observação de que planejadores Fast-Downward-based são menos sensíveis à ordem (por pré-processamento próprio) é um contraponto relevante para qualquer generalização de "técnica x é mais sensível que técnica y a característica do domínio" — deve ser controlada em replicações futuras (T1–T6, especialmente T4/T6).
- Conclusão do artigo propõe explicitamente rodar cada instância de benchmark com uma configuração de modelo diferente, gerada aleatoriamente, como prática recomendada para comparações mais estáveis entre planejadores — recomendação metodológica direta para qualquer replicação da dissertação de 2010.

## Trechos literais

- "The main empirical finding in this article is that it is possible to configure domain models to improve the performance of domain-independent planning engines. [...] Our results indicate that the configuration of domain models can lead to up-to-25-fold speedup, and that the correct positioning of a single macro operator can result in up-to-3-orders-of-magnitude runtime improvements." (Seção 1, Introdução)
- "Probe shows the largest score fluctuation, its IPC score ranges between 63 and 37. [...] Besides the top performing planner (Cedalion), it is apparent that competitions ranks are not stable and are significantly affected by the exploited domain model configuration." (Seção 5.2, p. 9–10)
- "The ordering of elements of domain models significantly affects the runtime performance of state of the art domain-independent planning engines, regardless of the search technique they exploit, or their implementation details." (Seção 9, Conclusão)

## Marcações

- `[FATO]` Reconfigurações puramente sintáticas (ordem) de modelos PDDL semanticamente idênticos produzem variações de desempenho estatisticamente significativas em 12 planejadores e 13 domínios da IPC 2014, ao ponto de alterar posições relativas em competições simuladas (Seção 5.2, Tabelas 1 e 6).
- `[FATO]` Configuração automática do modelo pode gerar acelerações de até 25× (offline) e reposicionamento de macros pode gerar até 3 ordens de magnitude de melhoria (Seção 9).
- `[HIPÓTESE]` (minha interpretação) Como a dissertação de 2010 não relata controle sobre a ordem/serialização dos modelos PDDL gerados a partir do UML no itSIMPLE, é possível que parte da variação de cobertura entre domínios atribuída a características estruturais (UML) esteja parcialmente confundida com este efeito de configuração — o que fragiliza a interpretação causal de [A1]/[A5] tal como formulada em 2010, sem invalidar a correlação observada.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://arxiv.org/abs/2010.07710 (preprint idêntico ao artigo publicado no Journal of Automated Reasoning). Conferência humana: pendente.
