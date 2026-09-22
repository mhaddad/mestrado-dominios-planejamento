---
tipo: nota-de-leitura
eixo: E7
citekey: wolpert1997no
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: https://www.cs.ubc.ca/~hutter/earg/papers07/00585893.pdf
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: [A1]
fragilidades: []
perguntas: [Q4]
---

# No Free Lunch Theorems for Optimization

**Wolpert, D.H.; Macready, W.G. · 1997 · IEEE Transactions on Evolutionary Computation, vol. 1, n. 1, p. 67–82**
**Link/DOI:** 10.1109/4235.585893 (lido via cópia espelhada em https://www.cs.ubc.ca/~hutter/earg/papers07/00585893.pdf)

## Extração estruturada

- **Problema:** entender formalmente a relação entre o desempenho de um algoritmo de otimização de caixa-preta e o problema (função de custo) sobre o qual ele roda; em particular, se é possível haver um algoritmo geral superior a outros em média sobre o conjunto de todos os problemas de otimização possíveis.
- **Método:** análise matemática (teoria da probabilidade) sobre um espaço finito de busca `X` e de valores de custo `Y`; um problema de otimização é uma função `f: X → Y`; um algoritmo é um mapeamento de amostras já visitadas para um novo ponto não visitado. Os autores provam dois teoremas "No Free Lunch" (NFL) — um para funções de custo estáticas (Teorema 1) e um para funções de custo dependentes do tempo (Teorema 2) — somando o desempenho de qualquer par de algoritmos sobre *todas* as funções de custo possíveis, com distribuição a priori uniforme sobre elas. Também desenvolvem uma interpretação geométrica (Seção IV) e aplicações de cálculo (medidas de desempenho, aspectos de teoria da informação) e discutem distinções "minimax" entre algoritmos que sobrevivem ao NFL (Seção VI).
- **Dados/benchmarks:** nenhum; é um artigo inteiramente teórico/formal, sem experimentos empíricos.
- **Resultado principal:** Teorema 1 — para qualquer par de algoritmos `a1` e `a2`, a soma de `P(dy_m | f, m, a1)` sobre todas as funções de custo `f` é idêntica à soma para `a2`; ou seja, **o desempenho médio de qualquer algoritmo, calculado sobre o conjunto de todas as funções de custo possíveis com prior uniforme, é idêntico ao de qualquer outro algoritmo** — inclusive um algoritmo aleatório. O Teorema 2 estende o resultado a problemas dependentes do tempo. A interpretação geométrica (Seção IV) mostra que o desempenho de um algoritmo é determinado pelo "alinhamento" entre o algoritmo e a distribuição de probabilidade real sobre os problemas em que ele é usado — ou seja, desempenho bom exige que conhecimento do problema esteja de alguma forma incorporado ao algoritmo.
- **Relação com a dissertação de 2010:** o NFL **não é evidência de que 2010 esteja certa nem errada** sobre a afirmação central A1 (existe relação entre características do domínio e a técnica de melhor desempenho); ele opera em outro nível de generalidade — condições em que a *média* de desempenho sobre *todas* as funções de custo, com prior uniforme, é igual para todo par de algoritmos. Os próprios autores enfatizam esse limite (Seção III-A): a NFL não impede diferenças de desempenho sobre subconjuntos de problemas, e a distribuição real de problemas enfrentados por um praticante quase nunca é uniforme. O único ponto de contato genuíno com A1 é a interpretação geométrica: desempenho bom depende de "alinhamento" entre algoritmo e a distribuição real (não uniforme) de problemas — o que é consistente com (mas não prova) a lógica geral por trás de A1, de que usar conhecimento sobre a classe de problemas (aqui, "características do domínio") pode orientar a escolha do algoritmo. O NFL não diz nada sobre UML, PDDL, cobertura ou qualquer métrica estrutural específica de 2010.

## Pontos relevantes para o projeto

- O NFL é citado com frequência como justificativa abstrata para "ajuste tarefa-técnica", mas o teorema propriamente dito é sobre médias com prior uniforme sobre *todas* as funções objetivo de um espaço de busca finito — não sobre a distribuição real (não uniforme) de problemas de um domínio, nem sobre planejamento automatizado especificamente.
- A leitura correta para a Q4 é condicional: o NFL **não prova** que ajustar a escolha de agente/modelo de IA à tarefa funciona; ele apenas mostra que **não pode existir** um agente/algoritmo universalmente superior *em média sobre todas as tarefas possíveis*, e que qualquer vantagem sistemática exige que o algoritmo esteja "alinhado" (incorpore conhecimento) com a distribuição real e não uniforme das tarefas de interesse.
- Os autores (Seção III-A) alertam explicitamente contra generalizar desempenho observado em poucos problemas de amostra para a classe inteira — um cuidado metodológico que se aplica também à amostra pequena de 2010 (F2), embora o NFL não seja a fonte formal dessa fragilidade específica.
- Distinções "minimax" (Seção VI) mostram que, mesmo sob NFL, pode haver diferenças a priori entre algoritmos quando se olha problema a problema (não em média) — ponto tecnicamente relevante para qualquer leitura que tente usar o NFL para negar a possibilidade de um "melhor planejador por domínio".

## Marcações

- `[FATO]` "The average performance of any pair of algorithms across all possible problems is identical" (Seção I, Introdução, reformulação do Teorema 1) — vale em média sobre o conjunto de *todas* as funções de custo possíveis, com prior uniforme.
- `[FATO]` "Since it is certainly true that any class of problems faced by a practitioner will not have a flat prior, what are the practical implications of the NFL theorems when viewed as a statement concerning an algorithm's performance for nonfixed f?" (Seção III-A) — os próprios autores reconhecem que problemas reais não têm distribuição uniforme, limitando a aplicação direta do teorema à prática.
- `[FATO]` "In any of these cases, m or p⃗ must 'match' or be aligned with p⃗f to get the desired behavior" (Seção IV, interpretação geométrica) — desempenho depende do alinhamento entre algoritmo e a distribuição real de problemas.
- `[HIPÓTESE]` Ligação com Q4: se a analogia entre planejamento automatizado (2010) e roteamento de agentes de IA em desenvolvimento de software for válida, o NFL forneceria apenas o argumento *negativo* (não existe agente universalmente melhor em média) e não o argumento *positivo* de que características observáveis da tarefa predizem qual agente specific terá melhor desempenho — essa segunda parte precisaria de evidência empírica própria, não do NFL.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://www.cs.ubc.ca/~hutter/earg/papers07/00585893.pdf (cópia PDF do artigo original, IEEE TEC 1997; extraída com pdftotext). Conferência humana: pendente.
