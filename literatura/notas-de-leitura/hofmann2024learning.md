---
tipo: nota-de-leitura
eixo: E4
citekey: hofmann2024learning
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: https://www.ijcai.org/proceedings/2024/0744.pdf
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: [A4]
fragilidades: [F2]
perguntas: [Q1, Q2]
---

# Learning Generalized Policies for Fully Observable Non-Deterministic Planning Domains

**Hofmann, T.; Geffner, H. · 2024 · Proceedings of IJCAI 2024**
**Link/DOI:** 10.24963/ijcai.2024/744

## Extração estruturada

- **Problema:** estender os métodos combinatórios de aprendizado de políticas gerais desenvolvidos para planejamento clássico a domínios de planejamento totalmente observável e não determinístico (FOND — *Fully Observable Non-Deterministic*).
- **Método:** formula o aprendizado de política FOND como redução ao aprendizado de política clássica geral segura sobre a relaxação determinística ("todos os resultados") do domínio, mais detecção de becos sem saída (*dead-ends*). O domínio é representado, como nos trabalhos de Bonet/Geffner/Francès citados, por predicados e por um pool de *features* numéricas/booleanas geradas a partir deles (via a biblioteca DLPlan); as regras e o pool de *features* são obtidos resolvendo um problema SAT de custo mínimo (Answer Set Program, via *clingo*).
- **Dados/benchmarks:** 12 domínios FOND (acrobatics, beam-walk, três variantes de blocks, doors, first-responders, islands, miner, spiky-tireworld, tireworld, triangle-tireworld), tirados da distribuição FOND-SAT, com instâncias aumentadas em tamanho para teste de generalização.
- **Resultado principal:** o método entrega políticas FOND gerais corretas (com correção demonstrada formalmente) em 7 dos 12 domínios; nos outros 5, falha por explosão combinatória — excesso de fatos, tempo ou memória — antes de encontrar uma política que generalize (Tabela 1).
- **Relação com a dissertação de 2010:** relacionada a **A4** (mais características, planejadores e técnicas melhoram o ranking) de forma **matizada**: aqui, ampliar a família de problemas cobertos (de clássico para FOND) e o pool de *features* nem sempre melhora o resultado — em 5 dos 12 domínios o método simplesmente não escala, o que **relativiza A4**: nem toda ampliação de escopo/características leva a melhor generalização, ela pode também tornar o problema intratável. Isso também **ilustra F2** (amostra pequena limita conclusões) em outro sentido: mesmo com metodologia rigorosa, a cobertura de domínios continua parcial e dependente do tamanho do pool de *features* (coluna |F| da Tabela 1, de 22 a mais de 200 mil). É relevante para **Q1** (as conclusões de 2010 se sustentam com mais planejadores/domínios?) porque mostra, em outro subcampo (FOND), o mesmo padrão observado por 2010: desempenho desigual entre domínios, sem generalização automática do método a todos eles.

## Pontos relevantes para o projeto

- Estende a linha de representação por *features* de lógica de descrição (mesma família de Ståhlberg et al. 2022 e do trabalho anterior de Francès, Bonet e Geffner) para domínios não determinísticos — mostra que essa forma de representação de domínio (pool de *features* sobre predicados) é reutilizável além do caso clássico determinístico que domina o corpus de 2010.
- A Tabela 1 relaciona diretamente propriedades estruturais do domínio (número de objetos, tamanho do pool de *features*, número de restrições) ao sucesso ou fracasso da generalização — um paralelo direto, embora com métricas diferentes, ao exercício de 2010 de relacionar características de domínio a desempenho de técnica.
- A falha em 5 de 12 domínios é atribuída explicitamente a limites do resolvedor SAT (excesso de fatos, memória, complexidade máxima de *feature* fixada em 15), não a uma limitação teórica do método — distinção importante entre "a técnica não existe para esse domínio" e "a técnica não escalou computacionalmente", relevante para qualquer discussão sobre F5/F7 de 2010.

## Trechos literais

> "We extend the formulations and the resulting combinatorial methods for learning general policies over fully observable, non-deterministic (FOND) domains." (Resumo)

> "In 7 of the 12 domains, on the other hand, the learning method delivers general FOND policies, some of which will be shown to be correct in the next section." (Seção 6.1, p. 6737–6738)

> "The experiments over existing FOND benchmarks show that the approach is sufficiently practical, resulting in general FOND policies that can be understood and shown to be correct." (Seção 8, "Conclusion", p. 6740)

## Marcações

- `[FATO]` O método falhou em 5 de 12 domínios FOND testados, com motivo de falha específico indicado na Tabela 1 (explosão de fatos, esgotamento de memória ou limite de complexidade) (Tabela 1, p. 6737).
- `[FATO]` Nos 7 domínios em que teve sucesso, a política aprendida foi provada corretamente segura e completa por meio de um método adaptado de Francès et al. (2021) (Seção 6.2, "Correctness").
- `[HIPÓTESE]` O padrão de sucesso parcial e dependente de domínio, mesmo em uma técnica combinatória com garantias formais, sugere que a busca por uma característica estrutural única e universal que preveja desempenho de técnica (o objetivo original de A1/A3 em 2010) pode ser, em geral, tão difícil quanto o próprio problema de planejamento — cada família de técnica parece ter seu próprio "ponto cego" estrutural.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://www.ijcai.org/proceedings/2024/0744.pdf. Conferência humana: pendente.
