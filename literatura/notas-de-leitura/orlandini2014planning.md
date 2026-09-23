---
tipo: nota-de-leitura
eixo: E6
citekey: orlandini2014planning
prioridade: B
status: lido
profundidade: resumo
fonte-lida: https://api.crossref.org/works/10.3233/ia-140063
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: []
fragilidades: [F3]
perguntas: [Q2]
---

# Planning meets verification and validation in a knowledge engineering environment

**Orlandini, A.; Bernardi, G.; Cesta, A.; Finzi, A. · 2014 · Intelligenza Artificiale: The international journal of the AIxIA, v. 8, n. 1, p. 87-100**
**Link/DOI:** https://doi.org/10.3233/ia-140063

## Extração estruturada

- **Problema:** integrar técnicas de verificação e validação (V&V) formal em um ambiente de engenharia do conhecimento para planejamento baseado em *timelines* (não PDDL clássico).
- **Método:** apresentam o KEEN, ambiente que combina recursos "clássicos" de engenharia do conhecimento com serviços de validação e verificação, usando o verificador de modelos UPPAAL-TIGA para apoiar o design de sistemas de planejamento baseados em *timelines*.
- **Dados/benchmarks:** não detalhado no resumo disponível; é artigo de ferramenta/ambiente.
- **Resultado principal:** o KEEN oferece capacidades de validação de modelo de domínio, validação de planejador e verificação de plano, além de síntese automatizada de controlador para execução de planos.
- **Relação com a dissertação de 2010:** sem relação direta com A1–A8 (planejamento baseado em *timelines*, não em PDDL/UML como em 2010). Dialoga com **F3** (dependência do modelador): a integração de V&V formal ao ambiente de KE é outra estratégia para reduzir erros de modelagem, complementar à do itSIMPLE (que usa UML/Redes de Petri para análise, não verificação formal via *model checking*).

## Pontos relevantes para o projeto

- Mostra uma abordagem alternativa (verificação formal via *model checking*, com UPPAAL-TIGA) ao problema de garantir qualidade de modelos de domínio, distinta tanto do itSIMPLE (UML) quanto do GIPO (orientação a objetos) — amplia o panorama de soluções ao problema comum de F3.
- Planejamento baseado em *timelines* é um paradigma diferente do *forward-chaining*/*plan-space* discutido em 2010 (A6), relevante para nuançar a taxonomia de técnicas na revisão.

## Trechos literais

"[The system provides] domain model validation, planner validation, plan verification" (resumo, via metadados Crossref).

## Marcações

- `[FATO]` o artigo descreve o ambiente KEEN, que integra validação de modelo de domínio, validação de planejador e verificação de plano usando o verificador de modelos UPPAAL-TIGA, aplicado a planejamento baseado em *timelines* (resumo).
- `[HIPÓTESE]` interpretação minha: a existência de múltiplas estratégias concorrentes (UML/itSIMPLE, orientação a objetos/GIPO, verificação formal/KEEN) para lidar com a dependência do modelador (F3) sugere que esse é um problema estrutural da área de engenharia do conhecimento para planejamento, não específico à abordagem de 2010.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de resumo via metadados Crossref (https://api.crossref.org/works/10.3233/ia-140063); artigo completo está atrás de paywall (IOS Press/SAGE) e não foi possível localizar cópia aberta. Conferência humana: pendente.
