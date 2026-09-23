---
tipo: nota-de-leitura
eixo: E8
citekey: jimenez2024swebench
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: https://arxiv.org/abs/2310.06770
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: [A7]
fragilidades: [F5]
perguntas: [Q3, Q4]
---

# SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

**Jimenez, C.E.; Yang, J.; Wettig, A.; Yao, S.; Pei, K.; Press, O.; Narasimhan, K. · 2024 (ICLR 2024) · Princeton University / Princeton Language and Intelligence · arXiv:2310.06770**
**Link/DOI:** https://arxiv.org/abs/2310.06770

## Extração estruturada

- **Problema:** *benchmarks* de codificação existentes (ex.: HumanEval) envolvem majoritariamente problemas autocontidos, resolvíveis em poucas linhas de código, e já estão saturados — não capturam a fronteira das capacidades de modelos de linguagem (LMs) em engenharia de software real, que envolve navegar repositórios grandes, entender a interação entre funções em vários arquivos e localizar erros em código complexo.
- **Método:** os autores constroem o **SWE-bench**, um arcabouço de avaliação com 2.294 problemas de engenharia de software extraídos de *issues* reais do GitHub e dos *pull requests* que as resolveram, em 12 repositórios Python populares. Dado um estado do repositório e a descrição de uma *issue*, o modelo deve gerar um *patch* que edite o código para resolvê-la; o *patch* é avaliado executando a suíte de testes real do repositório (testes que passam a existir com a correção, chamados FAIL_TO_PASS, e testes que devem continuar passando, PASS_TO_PASS). Avaliam ChatGPT-3.5, GPT-4, Claude 2 e um modelo próprio ajustado, SWE-Llama, com dois métodos de recuperação de contexto: BM25 (busca lexical) e um "oráculo" (arquivos corretos fornecidos diretamente).
- **Dados/benchmarks:** SWE-bench (2.294 instâncias de tarefa, 12 repositórios Python populares, com subconjunto "SWE-bench Lite" também reportado); métrica principal "% Resolved" (proporção de instâncias em que o *patch* gerado faz todos os testes FAIL_TO_PASS e PASS_TO_PASS passarem), com "% Apply" como métrica auxiliar (proporção de *patches* que ao menos aplicam sem erro).
- **Resultado principal:** "The best-performing model, Claude 2, is able to solve a mere 1.96% of the issues" (resumo), usando recuperação BM25 com janela de contexto de 13 mil tokens; com recuperação "oráculo" (arquivos corretos dados diretamente), Claude 2 chega a 4,8% resolvidos. O desempenho cai conforme o comprimento do contexto aumenta (Tabela 2: Claude 2 cai de 1,96% para 1,22% ao passar de 13k para 50k tokens de contexto), atribuído à dificuldade dos modelos em localizar o código problemático em meio a muito código irrelevante — não a limitação de recuperação: aumentar o contexto do BM25 aumenta a taxa de recall dos arquivos corretos (Tabela 3), mas o desempenho cai mesmo assim. A dificuldade varia por repositório (Figura 4) e correlaciona-se com a presença de imagens embutidas na descrição da *issue* (ex.: 32% das instâncias de `matplotlib` contêm imagens, contra 2% do total).
- **Relação com a dissertação de 2010:** o artigo não trata de planejamento automatizado nem cita 2010 — não há confirmação/correção direta de A1–A8. A relação relevante é de **paralelo metodológico com A7/F5**: assim como 2010 reduz "eficiência" de um planejador a uma única métrica (cobertura = % de problemas resolvidos), o SWE-bench reduz sucesso de um modelo a uma única métrica ("% Resolved" = % de *issues* resolvidas), tratando resolver/não resolver como binário por instância, sem medir qualidade, elegância ou eficiência da solução gerada — os próprios autores reconhecem essa limitação (Seção 7, Discussão): "relying solely on this method [testes de execução] is insufficient to guarantee reliable performance of model generations, as we find automated code generations from LMs can frequently be less comprehensive, efficient, or readable compared to human-written solutions".

## Pontos relevantes para o projeto

- É o *benchmark* seminal da linha de pesquisa de agentes de engenharia de software (a "tarefa" do lado da Q4, se a analogia com planejamento automatizado for levada adiante) — qualquer proposta de "ajuste tarefa-agente" para desenvolvimento de software precisaria de uma noção operacional de tarefa como a do SWE-bench (uma *issue* real do GitHub associada a um repositório e a testes de aceitação).
- A queda de desempenho com aumento do contexto (Seção 5, "Difficulty correlates with context length") é um achado empírico específico sobre *uma* característica observável da tarefa (tamanho do contexto necessário) que afeta desempenho — estruturalmente análogo ao tipo de relação característica-do-domínio → desempenho-da-técnica que 2010 busca estabelecer, mas aqui a "característica" é do ambiente/contexto de execução, não do domínio de planejamento em si.
- A variação de dificuldade por repositório (Figura 4) é evidência de que características do "domínio" (aqui, o repositório/projeto de software) afetam o desempenho relativo dos modelos — mas o artigo não decompõe essa variação em métricas estruturais explícitas (como UML faria em 2010); fica em nível descritivo.
- Os autores notam que instâncias resolvidas por Claude 2 e por SWE-Llama 13b, mesmo com contagens totais parecidas (110 vs. 91 instâncias), se sobrepõem pouco (Claude 2 resolve só 42% do que SWE-Llama resolve) — evidência de **complementaridade de desempenho entre modelos**, o mesmo fenômeno que fundamenta o problema de seleção de algoritmos de Rice (1976) e que motiva roteamento/cascata (RouteLLM, FrugalGPT, já lidos neste lote).

## Marcações

- `[FATO]` "We introduce SWE-bench, an evaluation framework consisting of 2,294 software engineering problems drawn from real GitHub issues and corresponding pull requests across 12 popular Python repositories [...] The best-performing model, Claude 2, is able to solve a mere 1.96% of the issues" (resumo).
- `[FATO]` "in the 'oracle' setting Claude 2 and SWE-Llama 13b perform comparably, with each model resolving 110 and 91 instances respectively. Yet of these instances, Claude 2 only solves 42% of the instances solved by SWE-Llama" (Seção 5, "Difficulty differs across repositories").
- `[FATO]` "while this work evaluates models using execution-based code testing, relying solely on this method is insufficient to guarantee reliable performance of model generations, as we find automated code generations from LMs can frequently be less comprehensive, efficient, or readable compared to human-written solutions" (Seção 7, Discussão, Limitações).
- `[HIPÓTESE]` Ligação com Q4: a complementaridade de desempenho observada entre Claude 2 e SWE-Llama (baixa sobreposição nas instâncias resolvidas) sugere, por analogia com o argumento central de 2010 (nenhuma técnica domina em todos os domínios), que também no desenvolvimento de software poderia haver "ajuste" entre características da tarefa (tipo de *issue*, repositório, tamanho de contexto necessário) e o agente de IA mais adequado — mas o artigo não testa nem propõe esse ajuste; apenas relata a complementaridade, sem investigar suas causas estruturais.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://arxiv.org/abs/2310.06770 (PDF baixado do arXiv, versão publicada no ICLR 2024; extraído com pdftotext). Conferência humana: pendente.
