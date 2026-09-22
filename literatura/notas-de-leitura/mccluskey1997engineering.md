---
tipo: nota-de-leitura
eixo: E6
citekey: mccluskey1997engineering
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: https://eprints.hud.ac.uk/id/eprint/7859/1/aijreport.pdf
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: [A5]
fragilidades: [F3]
perguntas: [Q2]
---

# Engineering and compiling planning domain models to promote validity and efficiency

**T. L. McCluskey, J. M. Porteous · 1997 · Artificial Intelligence, v. 95, n. 1, p. 1–65**
**Link/DOI:** https://eprints.hud.ac.uk/id/eprint/7859/1/aijreport.pdf · DOI: 10.1016/S0004-3702(97)00034-9

## Extração estruturada

- **Problema:** a pesquisa clássica em planejamento tratava o domínio no nível do literal/proposição, sem método rigoroso de construção do modelo; isso deixava a engenharia de conhecimento "esparsa" e dependente de decisões ad hoc do modelador, com efeitos pouco compreendidos sobre a validade e a eficiência do planejador.
- **Método:** propõe um método sistemático, com apoio de ferramentas, para construir modelos de domínio "orientados a objeto" — operadores definidos em termos de como mudam o estado de objetos (em vez de literais), estados definidos como amálgamas de "substates" de objetos. Distingue duas classes de ferramentas: (i) para captura e validação inicial do modelo; (ii) para "compilação" (operacionalização) do modelo validado em uma forma mais eficiente para o planejador, incluindo geração automática de macro-operadores e de ordens de metas (goal orders, via a técnica PRECEDE). Avalia empiricamente o ganho de desempenho de planejar com modelos compilados vs. não compilados, usando um planejador de ordem total (FMD) com três estratégias de busca (BS, DS, HS), em quatro famílias de domínios (STRIPS, Extended-STRIPS, R³/Tyre-like e Tyre World), com amostras de problemas geradas aleatoriamente (RDM3, RDM5, RDM7, RDM8).
- **Dados/benchmarks:** domínios STRIPS, Extended-STRIPS, R³ e Tyre World; medição de tempo de CPU, número de nós expandidos e comprimento médio de solução, sob limites de recurso variáveis, com três estratégias de busca do planejador FMD (BS, DS, HS), configurações compiladas vs. não compiladas.
- **Resultado principal:** as configurações compiladas (modelo orientado a objeto + macros + ordens de metas) são consistentemente superiores às não compiladas, resolvendo mais problemas com muito menos tempo de CPU e memória e soluções mais curtas; no Tyre World, o uso de macros teve efeito desprezível (as ordens de metas dominaram o ganho), enquanto em STRIPS/Extended-STRIPS o uso de macros chegou a ~80% dos nós gerados, caindo para ~40% no domínio R³. No Tyre World, o tempo de solução para o problema mais difícil citado na literatura (Barrett & Weld, ~6 horas nos primeiros experimentos, 123 segundos no melhor algoritmo dos próprios autores) foi resolvido pelas configurações compiladas com "virtually no variation" a 1 segundo de CPU.
- **Relação com a dissertação de 2010:** é a obra fundacional (1997) da linha de engenharia de modelos orientados a objeto que desemboca no itSIMPLE e na dissertação de 2010; demonstra, décadas antes das métricas UML de 2010, que a *forma de construção e compilação* do modelo de domínio — e não apenas seu "conteúdo" — determina de forma dramática o desempenho do planejador, o que é evidência histórica direta para [F3] e qualifica [A5]: a complexidade medida por diagramas (aqui: número de sorts, operadores, macros) é confundida com decisões de engenharia (compilação, ordens de metas) que os autores mostram serem responsáveis pela maior parte do ganho observado, não a "complexidade intrínseca" do domínio.

## Pontos relevantes para o projeto

- Estabelece o vocabulário "orientado a objeto" para modelos de domínio (sorts, substates, transições de objeto) que é o antecedente direto da modelagem UML do itSIMPLE — útil para a seção de trabalhos relacionados sobre a origem da linha E6.
- Mostra empiricamente (Tabela 4, p. 53; Seção 5.5) que a mesma "quantidade" de complexidade de domínio pode gerar desempenhos radicalmente diferentes dependendo de como o modelo é compilado — argumento direto contra tratar métricas estruturais brutas como preditoras robustas de desempenho sem controlar o processo de engenharia.
- Introduz a distinção entre "modelo de domínio inicial" (para validação) e "modelo compilado" (para eficiência de planejamento), antecipando a distinção entre modelar (itSIMPLE/UML) e gerar entrada eficiente para o planejador (PDDL) que a dissertação de 2010 não problematiza.
- Discute explicitamente (Seção 6, Related Work) outras linhas de modelagem orientada a objeto contemporâneas (PLANRIK, KADS) — referências úteis para contextualizar [F1] em uma revisão ampliada.
- Conclusão do artigo já antecipa, em 1997, a necessidade de "a set of standards for planning domain encodings so that models can be exchanged easily between research groups, and properties of these models can be universally understood" — um precursor direto da motivação de T1/T2 na dissertação de 2010.

## Trechos literais

- "This paper postulates a rigorous method for the construction of classical planning domain models. [...] The method results in an 'object-centred' specification of the domain that lifts the representation from the level of the literal to the level of the object." (Abstract)
- "The results indicate that the compiled configurations are relatively superior, producing generally shorter solutions using much less cpu time and much less space compared to the uncompiled configurations." (Seção 5.5.1, p. 54)
- "Barrett and Weld describe this domain as being 'fairly difficult', and quote a figure of 6 hours for solution time for early experiments in the domain [3, pp 99]. [...] Our results show that the problems were trivial for the compiled configurations, and that there was virtually no variation in solution time for each problem (at 1 second of CPU)." (Seção 5 [Tyre World], p. 53)

## Marcações

- `[FATO]` Modelos de domínio compilados (orientados a objeto, com macros e ordens de metas) resolvem substancialmente mais problemas, com menos tempo de CPU/memória e soluções mais curtas, do que modelos não compilados do mesmo domínio (Tabela 4 e Seção 5.5, p. 53–54).
- `[FATO]` O uso relativo de macros variou de ~80% dos nós processados (STRIPS/Extended-STRIPS) a ~40% (domínio R³), mostrando que o ganho de compilação não é uniforme entre domínios e depende de propriedades estruturais específicas de cada um (Seção 5.5.3, p. 55).
- `[HIPÓTESE]` (minha interpretação) Este artigo sugere que, se a dissertação de 2010 tivesse controlado o processo de compilação/tradução UML→PDDL (por exemplo, medindo desempenho antes e depois de otimizações de codificação), poderia ter separado o efeito de "característica do domínio" do efeito de "qualidade da engenharia do modelo" — distinção que o próprio McCluskey, quase 25 anos depois (McCluskey et al. 2017 [@mccluskey2017engineering]), viria a formalizar como parte da "qualidade" do modelo.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://eprints.hud.ac.uk/id/eprint/7859/1/aijreport.pdf. Conferência humana: pendente.
