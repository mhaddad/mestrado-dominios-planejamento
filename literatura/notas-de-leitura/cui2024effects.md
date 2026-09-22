---
tipo: nota-de-leitura
eixo: E8
citekey: cui2024effects
prioridade: B
status: lido
profundidade: resumo
fonte-lida: https://www.microsoft.com/en-us/research/publication/the-effects-of-generative-ai-on-high-skilled-work-evidence-from-three-field-experiments-with-software-developers/
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: [A1]
fragilidades: [F5]
perguntas: [Q4]
---

# The Effects of Generative AI on High Skilled Work: Evidence from Three Field Experiments with Software Developers

**Cui, Z.; Demirer, M.; Jaffe, S.; Musolff, L.; Peng, S.; Salz, T. · 2025 (SSRN)/2026 (Management Science)**
**Link/DOI:** https://doi.org/10.2139/ssrn.4945566 ; versão publicada: https://doi.org/10.1287/mnsc.2025.00535

## Extração estruturada

- **Problema:** medir o efeito causal de ferramentas de IA generativa (assistente de código) sobre a produtividade de desenvolvedores de software em contextos organizacionais reais, e como esse efeito varia entre desenvolvedores.
- **Método:** três ensaios controlados randomizados (RCTs) de campo, conduzidos em três organizações distintas: Microsoft, Accenture e uma empresa Fortune 100 não identificada; mais de 4.800 desenvolvedores receberam acesso a uma ferramenta de IA de completar código.
- **Dados/benchmarks:** dados combinados dos três experimentos, totalizando 4.867 desenvolvedores.
- **Resultado principal:** ao combinar os dados dos três experimentos, o acesso à ferramenta de IA gerou um aumento de 26,08% (erro-padrão 10,3%) no número de tarefas concluídas pelos desenvolvedores; desenvolvedores menos experientes tiveram maior taxa de adoção e ganhos de produtividade maiores do que os mais experientes.
- **Relação com a dissertação de 2010:** **A1** [confirma por analogia, HIPÓTESE] — o achado de que a experiência do desenvolvedor (uma característica do "operador", análoga a características de domínio em 2010) modera o efeito da ferramenta de IA é consistente com a lógica central de 2010: o desempenho de uma técnica depende de características mensuráveis do contexto em que é aplicada. **F5** [ajuda a tratar, HIPÓTESE] — a métrica de desempenho usada ("tarefas concluídas") é, como a cobertura de 2010, uma métrica de quantidade/sucesso, não de qualidade — mesma limitação estrutural (F5) que 2010 tem ao reduzir eficiência à cobertura.

## Pontos relevantes para o projeto

- É o estudo com a maior amostra e o desenho mais rigoroso (três RCTs de campo, quase 4.900 desenvolvedores) entre os itens de E8 do lote sobre efeito de IA na produtividade — mas os achados vêm de resumo indireto (página do Microsoft Research), não da leitura do artigo completo (bloqueado por login no SSRN).
- O achado de heterogeneidade por experiência do desenvolvedor (menos experientes se beneficiam mais) é um resultado de moderação diretamente relevante à Q4: sugere que a "característica" que modera o ajuste com a IA pode estar no lado do usuário humano, não apenas na tarefa — dimensão que 2010 não precisou considerar (planejadores não têm "usuário" no mesmo sentido).
- Contrasta com becker2025measuring (já no acervo), que encontrou efeito negativo de IA em repositórios grandes e complexos com desenvolvedores experientes — os dois estudos, lidos em conjunto, sugerem que o efeito da IA na produtividade de desenvolvedores é heterogêneo e sensível ao contexto, reforçando a tese central de 2010 de que "depende das características" é a resposta certa, mesmo fora de planejamento automatizado.

## Trechos literais

"a 26.08% increase (SE: 10.3%) in completed tasks among developers using the AI tool" (resumo, via página de publicação do Microsoft Research).

## Marcações

- `[FATO]` Em três RCTs de campo combinando quase 4.900 desenvolvedores, o acesso a uma ferramenta de IA de completar código aumentou em 26,08% o número de tarefas concluídas, com maior ganho para desenvolvedores menos experientes (resumo).
- `[HIPÓTESE]` Esse padrão de heterogeneidade por experiência do desenvolvedor, somado ao resultado oposto de becker2025measuring (repositórios grandes/complexos com desenvolvedores experientes), reforça por analogia a tese central de 2010 — desempenho de uma técnica depende de características do contexto — mas agora estendida também a características do usuário humano, não apenas da tarefa.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de resumo na página de publicação do Microsoft Research (a versão SSRN retornou erro 403 e a versão publicada na Management Science está em revista fechada). Conferência humana: pendente — recomenda-se localizar cópia de acesso aberto do texto completo, se existir, para elevar a profundidade da nota.
