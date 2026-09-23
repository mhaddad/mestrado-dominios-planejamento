---
tipo: nota-de-leitura
eixo: E7
citekey: sterkenburg2021nofreelunch
prioridade: B
status: lido
profundidade: resumo
fonte-lida: https://api.crossref.org/works/10.1007/s11229-021-03233-1
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: [A1]
fragilidades: []
perguntas: [Q1]
---

# The no-free-lunch theorems of supervised learning

**Sterkenburg, T.F.; Grünwald, P.D. · 2021 · Synthese**
**Link/DOI:** https://doi.org/10.1007/s11229-021-03233-1

## Extração estruturada

- **Problema:** discutir os limites epistemológicos dos teoremas *No Free Lunch* (NFL) no aprendizado supervisionado, questionando a leitura cética comum de que nenhum algoritmo tem justificativa superior a outro.
- **Método:** artigo filosófico/teórico (não empírico), argumentando a partir de teoria do aprendizado e filosofia da indução (não lido além do resumo).
- **Dados/benchmarks:** não aplicável (artigo conceitual).
- **Resultado principal:** os autores sustentam que os teoremas NFL pressupõem algoritmos puramente orientados a dados, sem viés indutivo, e que a maioria dos algoritmos padrão deve ser entendida como dependente de um modelo (que representa o viés) fornecido como entrada — permitindo uma justificativa relativa ao modelo, e não uma equivalência cética universal entre algoritmos.
- **Relação com a dissertação de 2010:** **A1** [confirma por analogia, HIPÓTESE] — a tese central (algoritmos são justificáveis em relação a um modelo/viés, não de forma absoluta) é compatível com a lógica de 2010 de que a técnica de planejamento adequada depende das características do domínio (o "modelo" do problema). Sem menção a planejamento automatizado ou a agentes de IA para desenvolvimento de software.

## Pontos relevantes para o projeto

- Delimita filosoficamente o alcance do NFL, reforçando que "nenhuma técnica é universalmente melhor" não implica "toda seleção de técnica é arbitrária" — argumento útil para justificar por que a pergunta de 2010 (que técnica combina com qual domínio) é uma pergunta bem colocada.
- Não fornece evidência empírica; é um argumento conceitual sobre indução e viés.
- Leitura limitada ao resumo; risco de simplificação do argumento filosófico completo.

## Trechos literais

"most standard algorithms should be understood as model-dependent — requiring an external model representing bias as input — allowing for model-relative justification of the algorithms themselves" (resumo, paráfrase próxima dos metadados Crossref).

## Marcações

- `[FATO]` O artigo argumenta filosoficamente contra a leitura cética radical do NFL, propondo justificativa relativa a modelos (resumo).
- `[HIPÓTESE]` Essa mesma lógica de "viés relativo ao modelo/domínio" é análoga ao ajuste técnica-domínio de 2010, mas o artigo não trata de planejamento nem de IA para desenvolvimento de software.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de resumo em https://api.crossref.org/works/10.1007/s11229-021-03233-1 (metadados Crossref; PDF completo não acessível). Conferência humana: pendente.
