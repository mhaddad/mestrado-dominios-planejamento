---
tipo: nota-de-leitura
eixo: E3
citekey: xing2006maxplan
prioridade: B
status: lido
profundidade: texto-integral
fonte-lida: https://www.cse.wustl.edu/~yixin.chen/public/MaxPlan-final.pdf
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026 (aprovação delegada ao Coordenador)
afirmacoes-2010: [A6]
fragilidades: [F4]
perguntas: [Q1]
---

# MaxPlan: Optimal Planning by Decomposed Satisfiability and Backward Reduction

**Xing, Z.; Chen, Y.; Zhang, W. · 2006 · Booklet da 5ª Competição Internacional de Planejamento (IPC-5) / ICAPS-06**
**Link/DOI:** https://www.cse.wustl.edu/~yixin.chen/public/MaxPlan-final.pdf (sem DOI registrado)

## Extração estruturada

- **Problema:** planejamento ótimo (em número de passos paralelos) para problemas STRIPS proposicionais, melhorando a eficiência da abordagem "planejamento como satisfatibilidade" (SAT-based) frente ao SATPLAN.
- **Método:** MaxPlan segue o paradigma de planejamento-como-satisfatibilidade, mas inverte a direção de busca usada pelo SATPLAN: em vez de expandir o comprimento estimado do plano para frente (*forward level expansion*) até encontrar solução, MaxPlan estima um limite superior do comprimento ótimo (usando o FF para gerar um plano subótimo e paralelizá-lo) e reduz esse limite para trás (*backward level reduction*), resolvendo, a cada passo, um problema SAT decomposto por subobjetivo (*goal-oriented decomposition*), com aprendizado acumulativo de cláusulas entre iterações e poda por uma formulação de domínio multivalorado (exclusão mútua de longo alcance, *londex*).
- **Dados/benchmarks:** não traz tabela de cobertura no texto lido; descreve a arquitetura e as técnicas do planejador, submetido à faixa ótima da IPC-5 (2006).
- **Resultado principal:** a decomposição SAT proposta é descrita como significativamente mais eficiente do que o uso de um SAT-solver genérico como "caixa-preta", sem explorar a estrutura do problema.
- **Relação com a dissertação de 2010:**
  - **A6 (corrige, mas não pelo motivo da direção):** 2010 classifica MAXPLAN como Plan-Space, Partial-order, Forward-chaining, Graph-based e SAT-based (Tabela 4), a mesma combinação atribuída ao SATPlan. A fonte confirma SAT-based. Os rótulos Forward-chaining e Plan-Space/Partial-order não têm apoio na fonte: um planejador SAT não faz busca progressiva no espaço de estados nem busca no espaço de planos parciais; quem busca é o SAT-solver, sobre uma codificação proposicional de horizonte fixo.
  - **Cuidado com a "direção":** o "opposite direction" do artigo refere-se à **busca sobre o comprimento do plano** (o SATPLAN aumenta o horizonte *k* a partir de baixo; o MaxPlan parte de um limite superior e o reduz). Isso **não** é encadeamento para frente ou para trás no espaço de estados, que é o sentido de "Forward-chaining" em 2010. `[FATO]` A fonte não diz que o MaxPlan é backward-chaining. (Correção do Coordenador em 23/09/2026: a versão anterior desta nota tratava a frase como contradição direta de "Forward-chaining".)

## Pontos relevantes para o projeto

- Mostra por que a nova taxonomia precisa separar dimensões: para planejadores SAT, "direção de busca no espaço de estados" é **não aplicável**; a escolha relevante é a estratégia sobre o horizonte (crescente no SATPlan, decrescente a partir de um limite superior no MaxPlan), que 2010 não registra.
- Junto com a nota do SatPlan (`kautz2006satplan`): "Forward-chaining" não é um rótulo adequado para planejadores SAT.

## Marcações

- `[FATO]` MaxPlan usa redução de nível para trás (*backward level reduction*) sobre o **comprimento do plano**, estimando um limite superior e reduzindo-o, ao contrário da expansão de nível do SATPLAN (Seção 1, Introdução). Não se refere à direção de busca no espaço de estados.
- `[HIPÓTESE]` A classificação idêntica de SATPlan e MaxPlan em 2010 (mesmas cinco técnicas na Tabela 4) sugere que a dissertação tratou os dois planejadores SAT-based da IPC-5 como equivalentes em técnica, sem examinar a diferença de estratégia sobre o horizonte declarada pelos próprios autores do MaxPlan.

## Trechos literais

1. "This observation inspires us to search from the opposite direction, i.e. to reduce the estimated plan length from an upper bound." (Seção 1, Introdução, contrastando com "SATPLAN performs a forward level expansion search")

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 23/09/2026. Leitura de texto integral em https://www.cse.wustl.edu/~yixin.chen/public/MaxPlan-final.pdf (PDF baixado diretamente da página dos autores e extraído com `pdftotext -layout`). Conferência humana: pendente.
