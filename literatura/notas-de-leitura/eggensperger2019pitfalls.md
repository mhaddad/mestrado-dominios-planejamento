---
tipo: nota-de-leitura
eixo: E1
citekey: eggensperger2019pitfalls
prioridade: C
status: lido
profundidade: resumo
fonte-lida: https://jair.org/index.php/jair/article/download/11420/26488/21322
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: []
fragilidades: [F5]
perguntas: [Q1]
---

# Pitfalls and Best Practices in Algorithm Configuration

**Eggensperger, K.; Lindauer, M.; Hutter, F. · 2019 · Journal of Artificial Intelligence Research 64**
**Link/DOI:** 10.1613/jair.1.11420

## Extração estruturada

- **Problema:** aplicações práticas de configuração automática de algoritmos (AC) são propensas a armadilhas (muitas vezes sutis) no desenho experimental que podem invalidar o procedimento — o artigo cataloga essas armadilhas.
- **Método:** identificação e documentação de armadilhas comuns no desenho de experimentos de configuração automática (ex.: métrica objetivo tratada de forma diferente entre configuradores, má gestão de recursos em experimentos paralelos, *over-tuning*), acompanhada de boas práticas recomendadas e de uma ferramenta de código aberto (GenericWrapper4AC) que padroniza a interface entre algoritmo-alvo e configurador, limitando o consumo de recursos.
- **Dados/benchmarks:** exemplos concretos do impacto das armadilhas em resultados de configuração (não detalhados nesta leitura, restrita a resumo/introdução/conclusão).
- **Resultado principal:** os autores identificam que a maioria das armadilhas decorre de (i) tratamento inconsistente da função objetivo entre configuradores, (ii) problemas na alocação/monitoramento de recursos computacionais, e (iii) diferentes formas de *over-tuning*; propõem recomendações e uma ferramenta genérica para preveni-las.
- **Relação com a dissertação de 2010:** sem relação direta com A1–A8 (o artigo é sobre configuração de parâmetros de algoritmos, não sobre seleção de técnica por características de domínio). Toca **F5** (eficiência reduzida a cobertura): o artigo alerta explicitamente que "medir a métrica errada" é uma armadilha comum em comparações empíricas de algoritmos — reforça, por generalização, a crítica de que reduzir eficiência a cobertura (como em 2010, A7) pode ser uma simplificação problemática se não for justificada.

## Pontos relevantes para o projeto

- Cataloga rigor metodológico para comparações empíricas de algoritmos (mesmo que fora do domínio de planejamento), com lições transferíveis para qualquer réplica de 2010 que compare planejadores: cuidado com gestão de recursos computacionais e com a métrica de desempenho escolhida.
- Relevante para **Q1**: se a revisão quiser reproduzir ou ampliar as comparações de 2010 com mais planejadores, esta é uma referência direta de boas práticas experimentais a seguir, algo que 2010 não discute metodologicamente.
- A ferramenta GenericWrapper4AC (padronização de interface algoritmo-configurador) é um exemplo de infraestrutura de rigor experimental ausente em 2010.

## Trechos literais

> "Empirically comparing algorithms correctly is hard. [...] Subtle mistakes, such as measuring the wrong metric or running parallel experiments without meticulous resource management, can heavily bias the outcome." (Seção 7, Conclusion)

## Marcações

- `[FATO]` Os autores atribuem a maioria das armadilhas de configuração automática a tratamento inconsistente da função objetivo, gestão de recursos e *over-tuning* (Seção 7, Conclusion).
- `[HIPÓTESE]` O alerta sobre "medir a métrica errada" é transferível à crítica F5 de 2010: reduzir eficiência a cobertura, sem medir tempo ou qualidade do plano, é uma escolha metodológica que precisaria de justificativa explícita à luz destas boas práticas.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de resumo, introdução e conclusão em https://jair.org/index.php/jair/article/download/11420/26488/21322. Conferência humana: pendente.
