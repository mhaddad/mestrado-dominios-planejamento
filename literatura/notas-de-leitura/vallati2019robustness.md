---
tipo: nota-de-leitura
eixo: E6
citekey: vallati2019robustness
prioridade: B
status: lido
profundidade: resumo
fonte-lida: https://icaps20subpages.icaps-conference.org/wp-content/uploads/2020/10/KEPS-2020_paper_3.pdf (cópia aberta em workshop KEPS/ICAPS 2020, mesmo título/autoria do artigo K-CAP 2019 registrado em url_registro; lidos resumo e introdução)
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: [A5]
fragilidades: [F3]
perguntas: [Q2]
---

# On the Robustness of Domain-Independent Planning Engines: The Impact of Poorly-Engineered Knowledge

**Vallati, M.; Chrpa, L. · 2019 · Proceedings of the 10th International Conference on Knowledge Capture (K-CAP '19), p. 197-204**
**Link/DOI:** https://doi.org/10.1145/3360901.3364416

## Extração estruturada

- **Problema:** avaliar a robustez de planejadores independentes de domínio diante de modelos de conhecimento mal projetados (ou maliciosamente modificados), à medida que o planejamento automatizado passa a ser usado em aplicações reais.
- **Método:** assumem a perspectiva hipotética de um atacante interessado em manipular sutilmente o conhecimento de um domínio para introduzir sobrecarga desnecessária e desacelerar o processo de planejamento; descrevem diferentes tipos de problemas de engenharia do conhecimento que não são detectáveis por validação padrão de modelos, e medem o impacto desses problemas no desempenho de vários planejadores com abordagens distintas de pré-processamento e busca.
- **Dados/benchmarks:** não detalhado nas linhas lidas (resumo e início da introdução); múltiplos planejadores com diferentes estratégias de pré-processamento/busca.
- **Resultado principal:** modelos de domínio "mal projetados" (mesmo que válidos sintaticamente) podem degradar significativamente o desempenho de planejadores independentes de domínio, revelando uma fragilidade que a validação padrão de modelos não detecta.
- **Relação com a dissertação de 2010:** **confirma e aprofunda A5** (diagramas UML medem a complexidade do domínio, e essa complexidade afeta o desempenho das técnicas): aqui a "complexidade" ou qualidade do modelo de domínio afeta diretamente o desempenho do planejador, mesmo sem alterar a semântica do domínio, reforçando a tese central de 2010 de que características do domínio (aqui, sua engenharia) impactam o desempenho técnico. Dialoga fortemente com **F3** (dependência do modelador): mostra que erros/decisões de modelagem sutis, não capturadas por métricas estruturais simples, podem ter grande impacto — o que é um alerta para a validade das métricas UML de 2010 como preditoras completas de desempenho.

## Pontos relevantes para o projeto

- É um dos achados mais diretamente relevantes do lote para o núcleo da revisão: mostra empiricamente que "qualidade de engenharia do modelo de domínio" (não apenas suas características estruturais brutas) afeta o desempenho do planejador — um matiz importante para A5 e F3.
- Nota de proveniência: a cópia lida é uma versão de workshop (KEPS 2020, ICAPS) com título e autoria idênticos ao artigo K-CAP 2019 registrado na tabela do lote; não foi possível confirmar se o conteúdo é byte-a-byte idêntico à versão publicada pela ACM (paga), portanto convém, antes de citar na dissertação final, confirmar a correspondência entre as duas versões.
- Relevante para propor, na revisão, que métricas de "qualidade de engenharia" (e não só estrutura) sejam consideradas como candidatas a features preditivas (Q2).

## Trechos literais

"In this work, to understand the impact of poorly-engineered knowledge on planning engines, we consider the perspective of a hypothetical attacker that is interested in subtly manipulating such knowledge to introduce unnecessary overheads that consequently slow down the planning process" (resumo).

## Marcações

- `[FATO]` o artigo mede, com múltiplos planejadores de abordagens distintas, o impacto de manipulações sutis (mas válidas) do conhecimento de domínio no desempenho de planejamento (resumo; introdução).
- `[HIPÓTESE]` interpretação minha: este resultado sugere que a dissertação de 2010, ao usar métricas estruturais UML (número de classes, associações etc.) como *features*, pode estar capturando apenas uma parte da variação de desempenho explicável por características do domínio — a "qualidade de engenharia" do modelo seria uma dimensão adicional não capturada por essas métricas, relevante para Q2.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de resumo e introdução de cópia aberta (mesmo título e autoria do artigo K-CAP 2019) em https://icaps20subpages.icaps-conference.org/wp-content/uploads/2020/10/KEPS-2020_paper_3.pdf, localizada por busca web pois o artigo publicado pela ACM está atrás de paywall. Conferência humana: pendente (inclusive quanto à correspondência exata entre esta versão e a publicada).

**Nota do Coordenador (23/09/2026):** a cópia lida (KEPS 2020) traz, na nota de rodapé do título, "This paper has been published in the proceedings of the ACM Conference on Knowledge Capture (K-CAP) 2019." É republicação declarada pelos autores do mesmo artigo, então a citação à versão do K-CAP 2019 é correta e a divergência entre versão lida e versão citada fica resolvida.
