---
tipo: nota-de-leitura
eixo: E4
citekey: jimenez2012review
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: https://serjice.webs.upv.es/publications/sergio-ker11/sergio-ker11.pdf
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: [A5, A6]
fragilidades: [F3, F4]
perguntas: [Q2]
---

# A review of machine learning for automated planning

**Jiménez, S.; de la Rosa, T.; Fernández, S.; Fernández, F.; Borrajo, D. · 2012 · The Knowledge Engineering Review 27(4)**
**Link/DOI:** 10.1017/s026988891200001x

## Extração estruturada

- **Problema:** revisar as técnicas de aprendizado de máquina aplicadas ao planejamento automatizado, organizadas por alvo do aprendizado: (1) definição automática de modelos de ação de planejamento e (2) definição automática de conhecimento de controle de busca, além de uma seção sobre aprendizado por reforço relacional (RRL).
- **Método:** revisão estruturada segundo quatro eixos analíticos aplicados a cada técnica: representação do conhecimento, extração de exemplos de aprendizado, algoritmo de aprendizado e exploração do conhecimento aprendido. Cobre aprendizado de modelos determinísticos e estocásticos, sob observabilidade completa e parcial, e conhecimento de controle nas formas de macro-ações, políticas generalizadas, heurísticas generalizadas e métodos de decomposição hierárquica.
- **Dados/benchmarks:** não aplicável (artigo de revisão; discute os *benchmarks* de cada trabalho revisado individualmente, sem experimento próprio).
- **Resultado principal:** conclui que, embora sistemas de aprendizado de modelo de ação e de conhecimento de controle tenham avançado significativamente desde os anos 1990, encontrar uma representação de conhecimento eficaz que funcione **através de uma coleção de domínios** continua sendo um problema em aberto, assim como a coleta automática de bons exemplos de treino.
- **Relação com a dissertação de 2010:** o achado mais relevante para este projeto é a seção de questões em aberto, que declara explicitamente: "encontrar uma representação de conhecimento eficaz para planejamento automatizado através de uma coleção de domínios ainda é uma questão em aberto" — esta é, em essência, a mesma pergunta que **Q2** da revisão de 2026 formula (se métricas estruturais de modelagem acrescentam poder preditivo às *features* de PDDL), já presente na literatura em 2012, dois anos após a dissertação. Isso **relativiza A5**: a hipótese de 2010 de que diagramas UML capturam a complexidade relevante do domínio é apenas **uma entre várias tentativas concorrentes** de resolver o mesmo problema de representação, e a revisão de 2012 mostra que nenhuma delas havia se consolidado como solução geral até então — reforçando **F3**. Também **corrige/amplia A6**: a taxonomia de técnicas usada por Jiménez et al. (2012), organizada por "o que é aprendido" (modelo de ação vs. conhecimento de controle), é estruturalmente diferente da taxonomia de 2010, organizada por "família algorítmica" (heuristic search, hierarchical etc.) — evidência de que há taxonomias concorrentes e não convergentes na área, o que sustenta **F4**.

## Pontos relevantes para o projeto

- É a revisão mais antiga e mais próxima cronologicamente de 2010 entre as obras deste lote — útil para situar o estado da arte de aprendizado para planejamento no momento imediatamente posterior à dissertação original.
- A afirmação central sobre representação de conhecimento em aberto está diretamente ligada ao trabalho futuro **T1** de 2010 (extração automática de métricas): a revisão de 2012 mostra que a comunidade de aprendizado para planejamento já reconhecia esse desafio como central, sem tê-lo resolvido.
- Nota explicitamente que a linguagem de representação escolhida (objeto-centrada vs. outras) afeta a capacidade de aprender conhecimento eficaz, citando Martin e Geffner (2000) e Cresswell et al. (2009) — outro eco direto de A5/Q2, mas anterior aos trabalhos de lógica de descrição e GNN do restante do lote.
- Observa que representações mais expressivas (programas, fórmulas temporais, hierarquias) capturam estruturas abstratas (laços, hierarquias) relevantes para muitos domínios, mas exigem rotulação extra (anotações de início/fim de laço, tarefas abstratas) que não pode ser obtida automaticamente de execuções observadas — limitação que ecoa nos trabalhos de Srivastava et al. (2011) e Jiménez et al. (2019) do mesmo lote.

## Trechos literais

> "This paper reviews recent techniques in machine learning for the automatic definition of planning knowledge." (Resumo)

> "Finding an effective knowledge representation for AP over a collection of domains is still an open issue." (Seção 6.2, "Open Issues", p. 29–30)

> "Learning effective search control knowledge over a collection of domains is still challenging since different planning domains may present very different structures." (Seção 6.1, "Summary", p. 29)

## Marcações

- `[FATO]` A revisão organiza as técnicas por alvo do aprendizado (modelo de ação vs. conhecimento de controle de busca), não por família algorítmica de planejador (Seção 3 e Seção 4, Índice).
- `[FATO]` A seção de questões em aberto identifica explicitamente a representação de conhecimento eficaz entre domínios como problema não resolvido em 2012 (Seção 6.2, p. 29–30).
- `[HIPÓTESE]` A coexistência de múltiplas taxonomias de técnica na literatura (a de 2010, por família algorítmica; a de Jiménez et al. 2012, por alvo de aprendizado; e as usadas nos demais trabalhos deste lote, por forma de representação — grafo, lógica de descrição, espaço latente) sugere que qualquer taxonomia única corre risco de ficar rapidamente obsoleta, o que reforça a necessidade de F4 ser tratada como fragilidade estrutural, não apenas pontual, de 2010.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://serjice.webs.upv.es/publications/sergio-ker11/sergio-ker11.pdf. Conferência humana: pendente.
