---
tipo: nota-de-leitura
eixo: E4
citekey: greco2022scaling
prioridade: B
status: lido
profundidade: texto-integral
fonte-lida: https://arxiv.org/pdf/2207.04479
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: [A5, A6]
fragilidades: [F3, F4]
perguntas: [Q2]
---

# Scaling up ML-based Black-box Planning with Partial STRIPS Models

**Greco, M.; Torralba, Á.; Baier, J.A.; Palacios, H.H. · 2022 · arXiv (preprint)**
**Link/DOI:** 10.48550/arxiv.2207.04479 (arXiv:2207.04479)

## Extração estruturada

- **Problema:** melhorar o planejamento *black-box* guiado por aprendizado de máquina (ML) em contextos onde não há um modelo simbólico completo do simulador; explorar se um modelo STRIPS incompleto, descrevendo apenas parte do problema, pode ser combinado com heurísticas/políticas aprendidas.
- **Método:** especifica um modelo STRIPS incompleto que descreve parte do domínio, permitindo o uso de heurísticas de relaxação (ex.: FF) sobre esse modelo parcial, combinadas com a orientação de heurísticas/políticas aprendidas por ML sobre o simulador *black-box*. Implementado sobre o sistema de planejamento Fast Downward (Helmert 2006).
- **Dados / benchmarks:** vários domínios de planejamento, incluindo um domínio do tipo "grade com chaves" (*Grid*) usado como exemplo detalhado.
- **Resultado principal:** especificar um modelo STRIPS incompleto que descreve apenas parte do problema é uma forma eficaz de melhorar o planejamento *black-box* baseado em ML, além de simplesmente coletar mais dados ou ajustar arquiteturas de ML; combinar as duas fontes de heurística (aprendida e de relaxação sobre o modelo parcial) reduz o esforço de busca em termos de expansão de nós.
- **Relação com a dissertação de 2010:** o artigo cita explicitamente **itSIMPLE** (Vaquero et al. 2013) — a mesma ferramenta usada por HADDAD (2010) para modelagem UML dos domínios — como referência de "modelagem de problemas de planejamento estudada em engenharia de conhecimento", no contexto de discutir como modelar parcialmente um domínio em STRIPS/PDDL. Isso é um **achado relevante**: mostra que itSIMPLE continua sendo citado como trabalho relacionado em 2022, o que fortalece a relevância da linha de modelagem/engenharia de domínios de A5/F3 (métricas UML medem o modelo e dependem do modelador) mesmo em trabalhos recentes de ML aplicado a planejamento.

## Pontos relevantes para o projeto

- **Achado de destaque para o Coordenador:** citação direta a itSIMPLE (Vaquero et al. 2013) como referência de "modelagem de problemas de planejamento estudada em engenharia de conhecimento" — confirma que a ferramenta usada em HADDAD (2010) segue relevante na literatura de 2022, ainda que apenas como contextualização breve, não como método central do artigo.
- Reforça a ideia de "modelos parciais" (não totalmente especificados) como uma linha de pesquisa ativa — potencialmente relevante para T5 (domínios artificiais) e F3 (dependência do modelador).
- Combina aprendizado de máquina *black-box* com heurísticas simbólicas parciais, mais um exemplo de técnica híbrida ausente da taxonomia A6.

## Marcações

- `[FATO]` O artigo cita Vaquero et al. (2013), itSIMPLE, na frase "Modelling planning problems is studied in knowledge engineering (Vaquero et al. 2013)" (corpo do texto, seção de discussão sobre modelagem parcial).
- `[HIPÓTESE]` A persistência de citações a itSIMPLE em 2022 sugere que a abordagem de modelagem estrutural de domínios (base metodológica de HADDAD 2010) ainda tem lugar reconhecido na literatura, mesmo que não seja usada operacionalmente neste artigo.

## Trechos literais

- "Modelling planning problems is studied in knowledge engineering (Vaquero et al. 2013). Recent efforts have looked at obtaining planning models from source code using annotations (Katz, Moshkovich, and Karpas 2018)." (corpo do artigo, discussão sobre modelagem parcial)

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://arxiv.org/pdf/2207.04479 (resumo, introdução e trecho de discussão sobre modelagem parcial e referências). Conferência humana: pendente.
