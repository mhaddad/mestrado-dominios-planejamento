---
tipo: nota-de-leitura
eixo: E6
citekey: vaquero2007itsimpleb
prioridade: B
status: lido
profundidade: resumo
fonte-lida: https://teses.usp.br/teses/disponiveis/3/3152/tde-19072007-174135/publico/DissertacaoRevisadaVaqueroTS.pdf (PDF baixado, lidos resumo, introdução do capítulo 1 e conclusões do capítulo 6)
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: [A5]
fragilidades: [F3]
perguntas: [Q2]
---

# itSIMPLE: ambiente integrado de modelagem e análise de domínios de planejamento automático

**Vaquero, T.S. · 2007 · Dissertação de Mestrado, Escola Politécnica da Universidade de São Paulo**
**Link/DOI:** https://doi.org/10.11606/d.3.2007.tde-19072007-174135

## Extração estruturada

- **Problema:** a especificação, modelagem e análise de domínios de planejamento automático são etapas fundamentais, mas carentes de um ambiente integrado que aproveite representações já conhecidas em Engenharia (de Software e de Requisitos) para essa tarefa.
- **Método:** proposta de um ambiente de design que integra análise de requisitos, especificação, modelagem, análise e testes de modelos de domínios de planejamento, usando múltiplas representações complementares: UML para análise estática, XML para armazenamento/exportação (ex.: para PDDL), Redes de Petri para análise dinâmica, e PDDL para testes com planejadores. Implementado na ferramenta itSIMPLE (Java).
- **Dados/benchmarks:** não é estudo empírico com planejadores das IPCs; é trabalho de ferramenta/ambiente de modelagem.
- **Resultado principal:** o ambiente e a ferramenta itSIMPLE viabilizam a modelagem de domínios reais de planejamento (de maior complexidade que os tradicionais, para os quais PDDL sozinha é exaustiva) usando linguagens mais usuais nas fases iniciais de projeto, com integração entre representações que permite ao projetista analisar o mesmo modelo sob diferentes pontos de vista.
- **Relação com a dissertação de 2010:** esta é a tese/dissertação de mestrado que **originou a ferramenta itSIMPLE**, base direta usada pela dissertação de 2010 (HADDAD) para extrair as métricas UML dos domínios. **Confirma A5** (diagramas UML medem a complexidade do domínio) na sua premissa de origem — é literalmente a justificativa conceitual para usar UML como instrumento de modelagem e análise de domínios de planejamento. Também dialoga com **F3** (métricas UML dependem do modelador): o próprio trabalho argumenta que a qualidade do modelo depende dos "sucessivos refinamentos" feitos pelo projetista, reconhecendo implicitamente essa dependência.

## Pontos relevantes para o projeto

- Fonte primária direta da ferramenta usada em 2010 — deveria estar entre as referências centrais da dissertação revisada, já que é a base metodológica do instrumento de medição (itSIMPLE).
- Traz explicitamente a ideia de que a integração entre visualizações (UML, Redes de Petri, PDDL) melhora a qualidade do modelo "devido aos sucessivos refinamentos" — argumento relevante para discutir F3 (dependência do modelador) na revisão.
- Em português, no mesmo contexto institucional (Escola Politécnica da USP) da dissertação de 2010, o que facilita comparação direta de terminologia e conceitos.

## Trechos literais

"Neste trabalho, é apresentada uma proposta de um ambiente integrado de modelagem e análise de domínios de planejamento, que leva em consideração o ciclo de vida de projeto, representado por uma ferramenta gráfica de modelagem que utiliza diferentes representações: a UML para modelar e analisar as características estáticas dos domínios" (Resumo).

## Marcações

- `[FATO]` o trabalho apresenta e implementa o ambiente/ferramenta itSIMPLE, integrando UML, XML, Redes de Petri e PDDL para modelagem e análise de domínios de planejamento automático (Resumo; Capítulo 6, Conclusões).
- `[HIPÓTESE]` interpretação minha: como esta é a fonte metodológica direta do instrumento usado em 2010, ela deveria ser citada na dissertação revisada não apenas como "trabalho relacionado", mas como referência fundacional do método — o que pode preencher parte da lacuna de revisão identificada como F1 (já que 2010 cita pouco sobre a origem do próprio itSIMPLE além de menções indiretas).

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de resumo, introdução (capítulo 1) e conclusões (capítulo 6) do PDF em https://teses.usp.br/teses/disponiveis/3/3152/tde-19072007-174135/publico/DissertacaoRevisadaVaqueroTS.pdf. Conferência humana: pendente.
