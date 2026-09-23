---
tipo: nota-de-leitura
eixo: E7
citekey: ong2024routellm
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: https://arxiv.org/abs/2406.18665
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: [A7]
fragilidades: []
perguntas: [Q3, Q4]
---

# RouteLLM: Learning to Route LLMs with Preference Data

**Ong, I.; Almahairi, A.; Wu, V.; Chiang, W.; Wu, T.; Gonzalez, J.E.; Kadous, M.W.; Stoica, I. · 2024/2025 (ICLR 2025) · arXiv:2406.18665**
**Link/DOI:** https://arxiv.org/abs/2406.18665

## Extração estruturada

- **Problema:** escolher entre um modelo de linguagem (LLM) forte e caro e um LLM fraco e barato, por consulta, equilibrando qualidade de resposta e custo — em vez de enviar todas as consultas ao modelo mais caro (garantindo qualidade, mas custo alto) ou todas ao mais barato (economizando, mas com qualidade inferior em consultas complexas).
- **Método:** arcabouço de treinamento supervisionado de roteadores binários `R^α: Q → {M_fraco, M_forte}`, aprendido a partir de dados de preferência humana (Chatbot Arena, ~80 mil confrontos, rotulados em vitória/empate/derrota entre pares de modelos). O roteador estima `P_θ(vitória do forte | consulta)` e aplica um limiar de custo `α` para decidir qual modelo usar. Quatro arquiteturas de roteador são exploradas: *ranking* ponderado por similaridade (Bradley-Terry), fatoração de matriz, classificador BERT e um LLM causal como classificador. Dois métodos de aumento de dados são testados: rótulos "dourados" (MMLU) e rótulos gerados por um LLM-juiz (GPT-4) sobre o dataset Nectar.
- **Dados/benchmarks:** Chatbot Arena (80 mil confrontos, dados de preferência humana); MMLU (múltipla escolha, ~1500 questões de validação, para aumento de dados "dourado"); GSM8K e MT Bench como *benchmarks* de avaliação fora de domínio (*out-of-domain*); Nectar (~120 mil amostras, para aumento de dados via juiz GPT-4, custando cerca de US$700).
- **Resultado principal:** os roteadores conseguem redução de custo de até 3,66× mantendo qualidade equivalente a 95% do GPT-4 em MT Bench (Tabela 6); de forma mais geral, "our approach can reduce costs by over 2 times without sacrificing response quality" (resumo). Os roteadores mantêm desempenho ao rotear entre pares de modelos forte/fraco não vistos no treino, sem re-treinamento. O aumento de dados (rótulos dourados ou de LLM-juiz) é decisivo: roteadores treinados só com dados brutos da Chatbot Arena têm desempenho fraco em MMLU e GSM8K, mas superam a linha de base aleatória em todos os *benchmarks* após o aumento. O custo de operação do próprio roteador é pequeno frente ao custo de geração do LLM (até 0,4% do custo do GPT-4 para o roteador mais caro, Tabela 7).
- **Relação com a dissertação de 2010:** o artigo não trata de planejamento automatizado nem cita 2010 — a relação é de **analogia estrutural**, não de confirmação/correção direta de nenhuma afirmação A1–A8. O ponto de contato mais próximo é **A7** [contraste instrutivo]: assim como 2010 reduz "eficiência" a uma única métrica (cobertura), este artigo evita esse reducionismo ao definir explicitamente duas métricas complementares e não intercambiáveis — custo (`c`) e qualidade (`r`, *performance gap recovered*) — e uma métrica composta (APGR) que integra o trade-off sobre múltiplos limiares de custo, em vez de um único número.

## Pontos relevantes para o projeto

- É o exemplo mais direto, neste lote, de "seleção de agente conforme a tarefa" aplicado a LLMs: a arquitetura do roteador (consulta → estimativa de qual modelo ganha → decisão binária) é estruturalmente próxima ao problema de seleção de algoritmos de Rice (1976) citado nas notas de Smith-Miles, mas aplicado a modelos de linguagem em vez de planejadores ou algoritmos clássicos.
- O uso de dados de preferência humana (não características estruturais explícitas da tarefa) como sinal de treino é uma diferença de método importante frente à proposta de 2010 (que usa métricas estruturais de UML) — relevante para não confundir "ajuste tarefa-técnica aprendido a partir de desempenho observado" (RouteLLM, Q3/Q4) com "ajuste tarefa-técnica baseado em características estruturais explícitas do domínio" (2010, Q2).
- Os autores reconhecem como limitação que "real-world applications may have distributions that differ substantially from these benchmarks" (Seção 6) — precaução metodológica análoga à que se aplicaria à generalização das conclusões de 2010 para além dos 10+3 domínios testados.
- Métricas específicas (CPT, APGR) poderiam servir de inspiração metodológica para operacionalizar de forma mais fina a "eficiência" na revisão da dissertação (F5), caso a Q4 avance para uma proposta concreta de avaliação de agentes de IA por tarefa.

## Marcações

- `[FATO]` "we introduce a training framework for learning efficient router models that dynamically select between a stronger and weaker LLM during inference [...] our approach can reduce costs by over 2 times without sacrificing response quality" (resumo).
- `[FATO]` "Our routers are able to achieve significant cost savings while maintaining quality" — Tabela 6: CPT(50%) de 3,66× em MT Bench (mantendo 95% da qualidade do GPT-4), 1,41× em MMLU e 1,49× em GSM8K (Seção 5.4).
- `[FATO]` "While training routers solely on D_arena results in poor performance on MMLU and GSM8K, augmenting the training data with an LLM judge or in-domain data enables our routers to outperform the random baseline across all benchmarks" (Seção 6, Conclusão).
- `[HIPÓTESE]` Ligação com Q3/Q4: a arquitetura de roteamento binário entre modelo "forte" e "fraco" por consulta é uma instância concreta e já operacional do tipo de "ajuste tarefa-agente" que a Q4 propõe investigar para agentes de IA no desenvolvimento de software — mas RouteLLM roteia por *qualidade de resposta observada em benchmarks gerais* (Chatbot Arena, MMLU, GSM8K, MT Bench), não por *características estruturais da tarefa de engenharia de software* (o equivalente, em 2010, às métricas UML do domínio); estender esse tipo de roteador para tarefas de desenvolvimento de software com *features* estruturais explícitas da tarefa (ao estilo de 2010) é hipótese do projeto, não algo que este artigo estabeleça.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://arxiv.org/abs/2406.18665 (PDF baixado do arXiv, versão publicada no ICLR 2025; extraído com pdftotext). Conferência humana: pendente.
