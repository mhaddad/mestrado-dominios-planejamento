---
tipo: nota-de-leitura
eixo: E8
citekey: peng2023impact
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: https://arxiv.org/abs/2302.06590
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: [A3]
fragilidades: []
perguntas: [Q4]
---

# The Impact of AI on Developer Productivity: Evidence from GitHub Copilot

**Peng, S.; Kalliamvakou, E.; Cihon, P.; Demirer, M. · 2023 · arXiv**
**Link/DOI:** https://arxiv.org/abs/2302.06590 (10.48550/arxiv.2302.06590)

## Extração estruturada

- **Problema:** primeiro ensaio controlado (segundo os autores) sobre o efeito causal do GitHub Copilot na produtividade de programadores profissionais em uma tarefa padronizada.
- **Método:** ensaio controlado randomizado (RCT). 95 desenvolvedores profissionais recrutados via Upwork entre 15/05/2022 e 20/06/2022 (antes da disponibilidade geral do Copilot), 45 no grupo tratado (com acesso ao Copilot e vídeo de 1 minuto de instrução) e 50 no grupo controle (sem Copilot, mas livre para usar busca e Stack Overflow); 35 concluíram a tarefa e a pesquisa em cada grupo. Tarefa: implementar um servidor HTTP em JavaScript o mais rápido possível, avaliado por bateria de 12 testes via GitHub Classroom, com tempo medido do primeiro commit ao commit que passa em todos os testes.
- **Dados/benchmarks:** amostra Upwork, maioria 25–34 anos, Índia e Paquistão, renda mediana US$ 10.000–19.000/ano, em média 6 anos de experiência em programação, 9 horas/dia de codificação relatadas.
- **Resultado principal:** grupo tratado completou a tarefa 55,8% mais rápido (tempo médio 71,17 min vs. 160,89 min no controle; IC 95% de 21–89%; p=0,0017). Efeitos heterogêneos (Tabela 1, regressão com transformação de Horvitz-Thompson): desenvolvedores com menos experiência profissional, mais horas de programação por dia, e na faixa etária 25–44 anos se beneficiaram mais do Copilot (coeficientes com p<0,05 para horas/dia e faixa etária).
- **Relação com a dissertação de 2010:** **A3** [analogia parcial, HIPÓTESE] — 2010 defende que, dado só as características do domínio, o *ranking* de técnicas já se define, independentemente do problema específico. Aqui a tarefa é única (mesmo servidor HTTP para todos), mas o efeito da mesma ferramenta varia sistematicamente por característica do *desenvolvedor* (experiência, idade, carga horária) — um eixo de heterogeneidade que 2010 não considerou (2010 varia por domínio, não por quem executa). É evidência de que, mesmo fixando a tarefa, quem a executa modula o ganho da técnica — relevante para Q4 mas não equivalente à variação por domínio de 2010.

## Pontos relevantes para o projeto

- É o RCT fundacional do campo (citado por becker2025measuring e outros do lote como referência de "ganho de 55,8%" contra o qual o efeito nulo/negativo é comparado).
- Amostra pequena e tarefa única e padronizada (implementar um servidor HTTP) — ganho de generalização em precisão de medição, perda em variedade de tipos de tarefa; não há decomposição por característica da tarefa (só há uma tarefa).
- Heterogeneidade por experiência/idade/carga horária é o único eixo de "efeito que varia" presente no estudo — relevante para a pergunta sobre variação por característica do desenvolvedor.
- Métrica de "sucesso" é binária (passar nos 12 testes) e "tempo até sucesso" — mais rica que cobertura pura de 2010 (inclui tempo), mas ainda um único critério.

## Marcações

- `[FATO]` "the treated group completed the task 55.8% faster than the control group" e "the average completion time from the treated group is 71.17 minutes and 160.89 minutes for the control group... 95% confidence interval for the improvement is between [21%, 89%]" (Resultados).
- `[FATO]` "The results show that less experienced developers (years of professional coding), developers with heavy coding load (hours of coding per day), and older developers (developers aged between 25 and 44) benefit more from Copilot" (Tabela 1 e discussão).
- `[HIPÓTESE]` A heterogeneidade por perfil do desenvolvedor, mantendo a tarefa fixa, sugere que a "característica que modula o efeito" em desenvolvimento de software assistido por IA pode residir tanto na tarefa quanto no executor — um segundo eixo que uma extensão da lógica de 2010 para Q4 precisaria distinguir explicitamente do eixo "característica da tarefa" que domina em rondon2025evaluating e takerngsaksiri2025humanintheloop.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://arxiv.org/abs/2302.06590 (PDF baixado do arXiv, extraído com pdftotext). Conferência humana: pendente.
