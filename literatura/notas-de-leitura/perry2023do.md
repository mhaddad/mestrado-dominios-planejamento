---
tipo: nota-de-leitura
eixo: E8
citekey: perry2023do
prioridade: B
status: lido
profundidade: texto-integral
fonte-lida: https://arxiv.org/abs/2211.03622
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: [A7]
fragilidades: [F5]
perguntas: [Q4]
---

# Do Users Write More Insecure Code with AI Assistants?

**Perry, N.; Srivastava, M.; Kumar, D.; Boneh, D. · 2023 · CCS 2023**
**Link/DOI:** https://doi.org/10.1145/3576915.3623157 (texto lido via arXiv:2211.03622)

## Extração estruturada

- **Problema:** assistentes de código com IA podem melhorar a produtividade, mas já foram encontrados produzindo código inseguro em ambientes de laboratório; falta entender como usuários reais interagem com esses assistentes em tarefas relacionadas a segurança e quais os riscos práticos resultantes.
- **Método:** estudo de usuário com 47 participantes, que realizaram cinco tarefas de programação relacionadas a segurança em três linguagens diferentes (Python, JavaScript, C), comparando participantes com e sem acesso a um assistente de IA. Três perguntas de pesquisa: (RQ1) usuários com acesso a assistente de IA escrevem código mais inseguro? (RQ2) usuários confiam no assistente de IA para escrever código seguro? (RQ3) como a linguagem/comportamento do usuário ao interagir com o assistente afeta o grau de vulnerabilidades de segurança?
- **Dados/benchmarks:** estudo de usuário original com 47 participantes; dados e aparato do estudo liberados publicamente pelos autores.
- **Resultado principal:** participantes com acesso a um assistente de IA escreveram código significativamente menos seguro do que os sem acesso; participantes com acesso ao assistente também tenderam a acreditar que haviam escrito código mais seguro, sugerindo excesso de confiança. Participantes com acesso ao assistente escreveram soluções inseguras com mais frequência em quatro das cinco tarefas de programação testadas.
- **Relação com a dissertação de 2010:** **A7** [torna a limitação mais evidente, HIPÓTESE] — 2010 definiu eficiência apenas como cobertura, ignorando qualidade do plano; este artigo mostra, no domínio de assistentes de código, que medir apenas "sucesso na tarefa" (resolver o problema de programação) esconde uma dimensão de qualidade (segurança do código) que pode piorar mesmo quando a tarefa é cumprida — evidência de que reduzir eficiência a uma única métrica (cobertura, em 2010; conclusão da tarefa, aqui) pode mascarar efeitos negativos relevantes. **F5** [ajuda a tratar, HIPÓTESE] — reforça diretamente a fragilidade F5 de 2010 (eficiência reduzida a cobertura), mostrando um caso concreto em outro domínio onde essa redução esconde um efeito importante.

## Pontos relevantes para o projeto

- É a evidência mais direta do lote de que "usar IA" pode ter efeito negativo específico (segurança), reforçando a necessidade de a Q4 não assumir que ajuste tarefa-agente implica apenas "sucesso/insucesso" — é preciso medir múltiplas dimensões de qualidade, não só conclusão da tarefa.
- Estudo com usuários reais (não é benchmark automatizado), o que traz um tipo de evidência ausente em 2010 (que usou apenas execução de planejadores, sem fator humano).
- O achado de excesso de confiança dos usuários (acreditar que o código é seguro quando não é) é um risco específico de agentes de IA que não tem análogo direto em 2010 (planejadores não geram falsa confiança no usuário).

## Trechos literais

"participants who had access to an AI assistant wrote significantly less secure code than those without access to an assistant. Participants with access to an AI assistant were also more likely to believe they wrote secure code" (resumo).

## Marcações

- `[FATO]` Em estudo com 47 participantes, o uso de assistente de IA levou a código menos seguro e a maior confiança injustificada dos usuários na segurança do próprio código, em quatro de cinco tarefas testadas (resumo e introdução).
- `[HIPÓTESE]` Esse resultado evidencia, em outro domínio, o mesmo risco metodológico da fragilidade F5 de 2010: reduzir "eficiência" a uma métrica única de sucesso mascara efeitos negativos em outras dimensões (aqui, segurança; em 2010, tempo e qualidade do plano).

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de resumo e introdução em https://arxiv.org/abs/2211.03622 (PDF baixado, extraído com pdftotext). Conferência humana: pendente.
