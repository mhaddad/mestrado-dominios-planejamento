---
tipo: nota-de-leitura
eixo: E8
citekey: madeyski2026triage
prioridade: B
status: verificado
profundidade: texto-integral
fonte-lida: https://arxiv.org/abs/2604.07494
metadados: verificada-na-fonte-primaria
referencia-verificada: true
afirmacoes-2010: [A1, A3]
fragilidades: []
perguntas: [Q3, Q4]
---

# Triage: Routing Software Engineering Tasks to Cost-Effective LLM Tiers via Code Quality Signals

**Madeyski, L. · 2026 · arXiv (v1, 08/04/2026; 5 p.)**
**Link/DOI:** https://arxiv.org/abs/2604.07494 (sem DOI Crossref no momento da leitura)

> **Nota reescrita em 28/09/2026** a partir do texto integral. A versão de 22/09/2026, feita só com o resumo e a introdução, dizia que o artigo "compara três políticas de roteamento no SWE-bench Lite" e o chamava de "a peça mais forte do lote para a Q4". O artigo não tem resultado empírico: propõe um arcabouço e um protocolo de avaliação ainda não executado.

## Extração estruturada

- **Problema:** agentes de código mandam toda tarefa ao mesmo modelo de fronteira e pagam custo alto mesmo quando a tarefa é rotineira.
- **Método:** propõe o Triage, que usa métricas de saúde do código (CodeHealth, métrica proprietária que agrega mais de 25 subfatores, como complexidade ciclomática, acoplamento, tamanho e duplicação) como sinal para encaminhar cada tarefa, antes da geração, ao nível de modelo mais barato (leve, padrão, pesado) cujo resultado passe no mesmo portão de verificação (testes, *linter*, checagem de tipos). Um erro de encaminhamento é pego no portão e a tarefa volta ao nível pesado. Deriva o custo esperado por tarefa (Eq. 1) e três famílias de política: limiares heurísticos, classificador treinado e oráculo retrospectivo.
- **Dados:** nenhum dado próprio. A base empírica é um trabalho anterior (Borg et al., 2026, citado no artigo, não lido aqui): em refatoração de um só arquivo, código limpo reduz a taxa de quebra de modelos médios, e o Claude Code agêntico não mostra diferença. O artigo propõe testar isso no SWE-bench Lite (300 tarefas, 3 níveis, 3 execuções por nível: 2.700 execuções), com piloto de 50 tarefas antes.
- **Resultado principal:** analítico, não empírico. Duas condições falsificáveis para o roteamento compensar: a taxa de acerto do nível leve nas tarefas roteadas tem de superar a razão de custo entre os níveis (portão de custo), e a saúde do código tem de discriminar o nível necessário com ao menos um efeito pequeno, probabilidade de superioridade p̂ ≥ 0,56 (portão de sinal). Se um dos portões falhar, o resultado negativo é relatado como está.
- **Relação com a dissertação de 2010:** **A1, A3** [por analogia direta, `[HIPÓTESE]`]. É a proposta estruturalmente mais parecida com a de 2010 no lote: uma métrica estrutural do artefato, medida antes da execução, escolhe o recurso. Mas é **proposta**, sem teste. O próprio autor aponta o risco que as Fases 3 e 4B confirmaram para o planejamento: a métrica pode medir dificuldade da tarefa, e não ajuste entre tarefa e técnica (ameaça à validade (i) da seção 5, com desenho pareado por dificuldade para controlar).

## Pontos relevantes para o projeto

- Serve à Ponte como **hipótese concorrente com protocolo de teste pronto**, não como evidência: métricas de qualidade do código como sinal de roteamento, com condições explícitas de refutação. É o uso que a curadoria da Fase 5 já fazia ("protocolo propositivo").
- O protocolo tem o cuidado que faltou em 2010: linha de base (sempre leve, sempre pesado, ao acaso), controle de dificuldade por pareamento, tamanho de efeito em vez de só significância e piloto com critério de parada.
- A métrica central é proprietária; o autor propõe testar se os subfatores isolados bastam, para permitir replicação.
- Distinção importante para a Q4: aqui a escolha é entre níveis de capacidade do mesmo tipo de agente (mais barato ou mais caro), não entre técnicas diferentes, como em 2010.

## Trechos literais

"We design an evaluation comparing three routing policies on SWE-bench Lite (300 tasks across three model tiers): heuristic thresholds, a trained ML classifier, and a perfect-hindsight oracle." (resumo)

"the light-tier pass rate on healthy code must exceed the inter-tier cost ratio, and code health must discriminate the required model tier with at least a small effect size (p̂ ≥ 0.56)" (resumo)

"This paper presents a new idea, not yet fully proven." (fim da seção 5)

## Marcações

- `[FATO]` O artigo propõe um arcabouço e um protocolo de avaliação; não relata execução nem resultado empírico (seções 4 e 5).
- `[FATO]` A base empírica da assimetria (modelos médios se beneficiam de código limpo, modelos de fronteira não) vem de outro trabalho (Borg et al., 2026), para refatoração de um arquivo; a extensão a tarefas de vários passos é a hipótese H1 do autor.
- `[FATO]` O autor reconhece que saúde do código e dificuldade da tarefa podem se confundir (seção 5).
- `[HIPÓTESE]` Os resultados das Fases 3 e 4B (métricas estruturais não antecipam a técnica fora do domínio) são uma razão a mais para esperar que o portão de sinal seja o ponto frágil desse protocolo.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026: primeira versão, só com resumo e introdução. Claude Code (claude-opus-5-5), 28/09/2026: reescrita a partir do texto integral (PDF do arXiv v1, extraído com `pdftotext`), metadados conferidos na API do arXiv. Promoção aprovada pelo autor em 28/09/2026.
