---
tipo: nota-de-leitura
eixo: E7
citekey: gomez2016empirical
prioridade: B
status: lido
profundidade: resumo
fonte-lida: https://api.crossref.org/works/10.1162/neco_a_00793
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: [A1]
fragilidades: []
perguntas: [Q1]
---

# An Empirical Overview of the No Free Lunch Theorem and Its Effect on Real-World Machine Learning Classification

**Gómez, D.; Rojas, A. · 2016 · Neural Computation**
**Link/DOI:** https://doi.org/10.1162/neco_a_00793

## Extração estruturada

- **Problema:** investigar, de forma empírica, se o teorema *No Free Lunch* (NFL) — que diz que todas as estratégias de otimização têm desempenho equivalente quando promediadas sobre todos os problemas possíveis — tem efeito prático relevante sobre classificadores de aprendizado de máquina em cenários reais.
- **Método:** estudo empírico com técnicas de classificação populares aplicadas a conjuntos de dados reais (detalhes de desenho experimental não lidos; apenas o resumo).
- **Dados/benchmarks:** conjuntos de dados reais de classificação (não especificados no resumo).
- **Resultado principal:** o artigo examina como o NFL se aplica ao aprendizado de máquina no mundo real, questionando a aparente contradição entre o teorema (nenhuma estratégia é superior em média) e o esforço prático de desenvolver algoritmos melhores.
- **Relação com a dissertação de 2010:** **A1** [confirma por analogia, HIPÓTESE] — o NFL é o pano de fundo teórico que explica por que faz sentido buscar, como 2010 fez, quais características de domínio favorecem qual técnica: se nenhuma técnica é universalmente melhor, a seleção orientada por características do problema é o caminho esperado. Não há, no resumo, qualquer menção a planejamento automatizado ou a agentes de IA para desenvolvimento de software.

## Pontos relevantes para o projeto

- Fundamenta teoricamente a premissa de 2010 (não existe planejador universalmente superior) com evidência empírica sobre classificadores, não planejadores — referência de apoio conceitual, não substantiva.
- Útil para contextualizar por que a delimitação empírica do alcance do NFL (E7) é relevante para a revisão, sem estabelecer ligação direta com os rótulos de 2010 além de A1.
- Leitura limitada ao resumo; não é possível avaliar o desenho experimental nem a robustez estatística dos resultados.

## Trechos literais

"all optimization problem strategies perform equally well when averaged over all possible problems" (resumo, via metadados Crossref).

## Marcações

- `[FATO]` O artigo é um estudo empírico sobre o efeito do NFL em classificação de aprendizado de máquina (resumo).
- `[HIPÓTESE]` O NFL, tomado como pano de fundo teórico, sustenta a lógica de 2010 de que características do domínio devem orientar a escolha da técnica — mas isso não é afirmado pelo artigo, é interpretação minha.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de resumo em https://api.crossref.org/works/10.1162/neco_a_00793 (metadados Crossref; PDF completo não acessível). Conferência humana: pendente.
