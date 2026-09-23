---
tipo: nota-de-leitura
eixo: E5
citekey: silver2024generalized
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: https://arxiv.org/abs/2305.11014
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: [A1, A3, A5]
fragilidades: [F5]
perguntas: [Q2, Q3]
---

# Generalized Planning in PDDL Domains with Pretrained Large Language Models

**Silver, T.; Dan, S.; Srinivas, K.; Tenenbaum, J. B.; Kaelbling, L. P.; Katz, M. · 2024 (AAAI 2024) · arXiv (v2, dez. 2023) / AAAI Publications**
**Link/DOI:** https://ojs.aaai.org/index.php/AAAI/article/view/30006 (10.1609/aaai.v38i18.30006)

## Extração estruturada

- **Problema:** investigar se um LLM pré-treinado pode funcionar como **planejador generalizado** — não gerando um plano para uma única instância, mas sintetizando um programa (em Python) que resolve qualquer tarefa de um domínio PDDL dado um pequeno número de tarefas de treino.
- **Método:** papel do LLM = **gerador de programa/planejador generalizado** (não tradutor de PDDL nem planejador instância-a-instância). Para cada domínio, o LLM recebe o domínio e algumas tarefas de treino em PDDL e escreve um programa Python que consome uma tarefa (já *parseada*) e devolve um plano, com instrução explícita de não usar busca. Duas extensões testadas: (1) sumarização por *Chain-of-Thought* antes de sintetizar o código; (2) depuração automatizada — o programa é validado contra as tarefas de treino e, em caso de erro, o LLM recebe a exceção e tenta corrigir o código (repetido em rodadas). Compara com quatro *ablations* (sem CoT, sem depuração, sem nomes informativos no PDDL, GPT-3.5 em vez de GPT-4) e quatro baselines de planejamento generalizado da literatura (PG3, Policy Eval, Plan Compare, aleatório).
- **Dados/benchmarks:** sete domínios PDDL — Delivery, Forest, Gripper, Miconic, Ferry, Spanner (quatro padrão da literatura de planejamento generalizado) e Heavy (novo, criado pelos autores) —, avaliados em 10 sementes aleatórias e 30 tarefas de avaliação por semente, com tarefas de treino pequenas (13–20 objetos) e de avaliação bem maiores (30–250 objetos, dependendo do domínio).
- **Modelo e data:** **GPT-4** (OpenAI 2023) como configuração principal; GPT-3.5 como *ablation* de comparação. Artigo publicado em AAAI 2024 (versão arXiv original de maio de 2023).
- **Resultado principal:** Tabela 1 — fração de tarefas de avaliação resolvidas por domínio, GPT-4 completo: Forest 1,00, Delivery 0,90, Gripper 0,90, Ferry 0,80, Heavy 0,60, Spanner 0,10, **Miconic 0,01**. A remoção da depuração automática ou dos nomes informativos do PDDL derruba o desempenho em quase todos os domínios (ex.: Gripper cai de 0,90 para 0,50 sem depuração e para 0,10 sem nomes). GPT-3,5 fica em 0,00 em cinco dos sete domínios.
- **Relação com a dissertação de 2010:** **A5/A3** [confirma fortemente] — mesmo mudando radicalmente o papel do LLM (gerador de programa generalizado, não planejador de instância nem tradutor simples), o desempenho continua extremamente dependente do domínio, variando de 0,01 (Miconic) a 1,00 (Forest) com exatamente o mesmo método e modelo — um dos contrastes de domínio mais fortes do lote. Os autores atribuem a falha em Miconic e Spanner a características estruturais específicas do domínio (relações implícitas entre objetos, necessidade de raciocínio sobre transporte relacional não explícito), o que é conceitualmente próximo à intuição de 2010 de que características estruturais do domínio (associações, agregações) condicionam a técnica — só que aqui a "técnica" é síntese de programa por LLM. **A1** [amplia, com hipótese] — o padrão de falha por domínio (Miconic quase zero, Forest perfeito) é uma pista de que características relacionais específicas (não cobertas pelas métricas de diagrama de caso de uso/classe/estado de 2010) podem ser preditoras de desempenho de síntese de programa por LLM; comparar diretamente exigiria modelar esses domínios em UML, o que a obra não faz.

## Pontos relevantes para o projeto

- Terceiro papel de LLM distinto no lote (gerador de programa/política generalizada), relevante para a taxonomia de papéis pedida pela Q3, com evidência quantitativa por domínio muito clara.
- Miconic (quase falha total, 0,01) é analisado em detalhe pelos autores como limite conceitual do GPT-4 para captar uma relação implícita ("multiple buildings... relation between..."), o que é um bom exemplo textual de "por que certos domínios são difíceis para LLM" a citar na discussão de A5.
- Mostra que a robustez do resultado depende de escolhas de engenharia (depuração automática, nomes informativos no PDDL) tanto quanto do domínio em si — relevante para nuançar qualquer generalização sobre "desempenho do LLM em X domínio" como propriedade fixa.
- Conecta ao eixo E4 (o próprio artigo diz isso), então pode ser referenciado também em notas de planejamento generalizado sem LLM.

## Marcações

- `[FATO]` Tabela 1: "Gripper 0.90... Miconic 0.01... Ferry 0.80... Spanner 0.10... Forest 1.00" — GPT-4 completo (CoT + depuração automática), média de 10 sementes, 30 tarefas de avaliação por semente.
- `[FATO]` "GPT-4 has a number of consistent failure modes in Miconic. First, at the strategy proposal level... ist only implicitly based on the above relation... we believe that Miconic is just beyond the limit of GPT-4's [ability]" (seção de análise de falhas por domínio).
- `[HIPÓTESE]` A oposição entre desempenho quase perfeito (Forest, Delivery, Gripper) e quase nulo (Miconic) com o mesmo modelo e protocolo sugere que, se a revisão de 2025 quiser comparar poder preditivo de métricas estruturais (UML, como em 2010) versus *features* PDDL para desempenho de LLM (Q2), domínios como este conjunto de sete seriam um bom banco de teste, desde que fossem modelados em UML para permitir a comparação — trabalho que esta obra não fez.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://arxiv.org/abs/2305.11014 (o link de registro do lote, ojs.aaai.org, não serviu o PDF diretamente; localizei e conferi a versão arXiv com o mesmo título e autoria, extraída com pdftotext). Conferência humana: pendente.
