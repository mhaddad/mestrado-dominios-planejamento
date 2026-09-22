---
tipo: nota-de-leitura
eixo: E6
citekey: jilani2014automated
prioridade: B
status: lido
profundidade: resumo
fonte-lida: https://eprints.hud.ac.uk/id/eprint/20380/1/KEPS_2014.pdf (PDF baixado, lidos resumo e introdução)
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: [T1]
fragilidades: [F1]
perguntas: [Q2]
---

# Automated Knowledge Engineering Tools in Planning: State-of-the-art and Future Challenges

**Jilani, R.; Crampton, A.; Kitchin, D.E.; Vallati, M. · 2014 · KEPS (Knowledge Engineering for Planning and Scheduling), parte da ICAPS 2014**
**Link/DOI:** https://eprints.hud.ac.uk/id/eprint/20380/

## Extração estruturada

- **Problema:** não havia, até então, pesquisa comparativa publicada sobre ferramentas de engenharia do conhecimento (KE) para planejamento em IA que codificam automaticamente um modelo de domínio a partir da observação de traços de planos.
- **Método:** revisão e análise comparativa de ferramentas automatizadas de KE existentes, avaliando nove ferramentas diferentes contra oito critérios: requisitos de entrada, saída fornecida, linguagem, ruído nos planos, refinamento, eficiência operacional, experiência do usuário e disponibilidade.
- **Dados/benchmarks:** não é estudo empírico com domínios das IPCs; é revisão comparativa de ferramentas.
- **Resultado principal:** oferece uma visão comparativa das forças e fraquezas das ferramentas de KE automatizada existentes, servindo de insumo para pesquisa futura sobre os desafios do campo.
- **Relação com a dissertação de 2010:** dialoga diretamente com **T1** (trabalho futuro de 2010: extração automática das métricas no itSIMPLE), pois revisa exatamente a classe de ferramentas que automatizam a extração/construção de modelos de domínio — uma ambição que 2010 deixou como trabalho futuro e que aqui já existe uma linha de pesquisa dedicada (embora anterior à era dos LLMs). Também ajuda a tratar **F1** (lacunas de revisão de 2010), preenchendo uma lacuna bibliográfica sobre o estado da arte em KE automatizada por volta de 2010-2014.

## Pontos relevantes para o projeto

- Mostra que a ambição de "extração automática de métricas/modelos" (T1 de 2010) já era pauta de pesquisa ativa em KE para planejamento na mesma época, por outra via (indução a partir de traços de planos, não extração de métricas UML).
- Os oito critérios de avaliação de ferramentas (requisitos de entrada, ruído, refinamento etc.) podem servir de checklist para avaliar propostas mais recentes de automação (LLMs) no eixo E6.
- Trabalho não publicado formalmente (workshop KEPS, "Unpublished" segundo o próprio repositório), o que deve ser registrado como cautela de qualidade da fonte.

## Trechos literais

"In this paper we present a brief overview of the automated tools that can be exploited to induce planning domain models. [...] we do a comparative analysis of them [...] based on a set of criteria" (Resumo).

## Marcações

- `[FATO]` o artigo compara nove ferramentas de engenharia do conhecimento automatizada para planejamento contra oito critérios definidos (Resumo; Introdução).
- `[HIPÓTESE]` interpretação minha: a existência desta linha de pesquisa já em 2014 sugere que o trabalho futuro T1 de 2010 (extração automática de métricas no itSIMPLE) poderia ter se conectado a essa literatura de KE automatizada, o que a dissertação de 2010 não fez (ligação com F1).

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de resumo e introdução do PDF em https://eprints.hud.ac.uk/id/eprint/20380/1/KEPS_2014.pdf. Conferência humana: pendente.
