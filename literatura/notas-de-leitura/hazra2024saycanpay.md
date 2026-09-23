---
tipo: nota-de-leitura
eixo: E5
citekey: hazra2024saycanpay
prioridade: B
status: lido
profundidade: resumo
fonte-lida: https://ojs.aaai.org/index.php/AAAI/article/view/29991 (PDF via https://ojs.aaai.org/index.php/AAAI/article/view/29991/31739, lidos resumo e introdução)
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: [A2]
fragilidades: []
perguntas: [Q3]
---

# SayCanPay: Heuristic Planning with Large Language Models Using Learnable Domain Knowledge

**Hazra, R.; Zuidberg Dos Martires, P.; De Raedt, L. · 2024 · AAAI-24**
**Link/DOI:** https://doi.org/10.1609/aaai.v38i18.29991

## Extração estruturada

- **Problema:** LLMs geram planos com "conhecimento de mundo" vasto, mas obter planos ao mesmo tempo viáveis (respeitando pré-condições/*affordances*) e eficientes (curtos) continua um desafio.
- **Método:** combina LLMs com busca heurística: o LLM gera ações (*Say*), guiado por conhecimento de domínio aprendível que avalia viabilidade (*Can*) e recompensa/custo de longo prazo (*Pay*); a busca heurística seleciona a melhor sequência de ações.
- **Dados/benchmarks:** não detalhado no trecho lido (resumo e introdução); autores afirmam avaliação extensiva contra outras abordagens de planejamento com LLM.
- **Resultado principal:** o modelo SayCanPay supera outras abordagens de planejamento com LLM, segundo os autores, ao enquadrar o problema dentro da tradição de planejamento heurístico.
- **Relação com a dissertação de 2010:** dialoga com **A2** (2010 aponta *Heuristic Search* como uma das técnicas mais promissoras): SayCanPay reencaixa o LLM dentro do paradigma de busca heurística clássico em vez de propor um paradigma totalmente novo, o que é consistente com a relevância dessa técnica mesmo na era dos LLMs. Alimenta **Q3**.

## Pontos relevantes para o projeto

- É um exemplo de "neurossimbólico": LLM fornece heurísticas aprendidas, mas a seleção final de ações continua sendo busca heurística clássica — relevante para discutir se a taxonomia de técnicas de 2010 (heurística, plan-space etc.) ainda se aplica a sistemas híbridos com LLM.
- Útil para ilustrar, na seção de LLMs, um ponto intermediário entre "LLM como planejador" e "LLM como gerador de modelo de domínio".

## Trechos literais

"We propose to combine the power of LLMs and heuristic planning by leveraging the world knowledge of LLMs and the principles of heuristic search" (resumo).

## Marcações

- `[FATO]` o artigo propõe e avalia empiricamente um método que integra geração de ações por LLM com busca heurística guiada por conhecimento aprendido de viabilidade e custo (resumo).
- `[HIPÓTESE]` interpretação minha: a permanência da busca heurística como componente central, mesmo em sistemas híbridos com LLM, é um indício (não prova) de que a afirmação A2 de 2010 sobre a robustez da busca heurística pode continuar válida — a confirmar com mais leitura.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de resumo e introdução do PDF baixado de https://ojs.aaai.org/index.php/AAAI/article/view/29991/31739. Conferência humana: pendente.
