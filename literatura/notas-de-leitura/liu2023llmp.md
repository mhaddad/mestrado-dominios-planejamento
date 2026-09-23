---
tipo: nota-de-leitura
eixo: E5
citekey: liu2023llmp
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: https://arxiv.org/abs/2304.11477
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: [A1, A3, A5]
fragilidades: [F5]
perguntas: [Q3]
---

# LLM+P: Empowering Large Language Models with Optimal Planning Proficiency

**Liu, B.; Jiang, Y.; Zhang, X.; Liu, Q.; Zhang, S.; Biswas, J.; Stone, P. · 2023 · arXiv**
**Link/DOI:** https://arxiv.org/abs/2304.11477 (10.48550/arxiv.2304.11477)

## Extração estruturada

- **Problema:** LLMs sozinhos ("LLM-as-P") falham em problemas de planejamento robótico de horizonte longo; o artigo propõe combinar a competência linguística do LLM com a garantia de correção/otimalidade de um planejador clássico.
- **Método:** papel do LLM = **tradutor para PDDL** (LLM+P): o LLM recebe descrição em linguagem natural do problema mais um arquivo de domínio PDDL fornecido por especialista, gera o arquivo de problema PDDL, aciona um planejador clássico (Fast Downward, com os *aliases* `SEQ-OPT-FDSS-1`, garantidamente ótimo, ou `LAMA`, subótimo, tempo máximo de busca 200s) e traduz o plano de volta para linguagem natural. Compara com "LLM-as-P" (LLM planeja diretamente, com/sem contexto de exemplo) e com "LLM-as-P (ToT)" (*Tree of Thoughts*).
- **Dados/benchmarks:** 7 domínios de planejamento robótico adaptados de competições IPC passadas — Barman, Blocksworld, Floortile, Grippers, Storage, Termes, Tyreworld —, com 20 tarefas geradas automaticamente por domínio.
- **Modelo e data:** **GPT-4**, "o modelo mais recente em setembro de 2023" (nota de rodapé do artigo), temperatura 0, via API OpenAI.
- **Resultado principal:** Tabela I mostra taxa de sucesso (%) por domínio. LLM+P resolve a maioria dos domínios com taxas altas — Barman 100% (com `LAMA` subótimo), Blocksworld 90%, Grippers 95% (100% subótimo), Storage 85% —, mas **Floortile 0%** mesmo com LLM+P, e Termes apenas 20%. Em contraste, LLM-as-P (sem PDDL) fica em 0–35% na maioria dos domínios e 0% em Floortile e Barman.
- **Relação com a dissertação de 2010:** **A5/A1** [confirma, com deslocamento de mecanismo] — mesmo com o LLM atuando apenas como tradutor (não como raciocinador sobre a busca), o desempenho final da combinação LLM+planejador varia fortemente por domínio (de 0% em Floortile a 100% em Barman), reforçando que características do domínio afetam o desempenho da técnica — só que aqui a "técnica" é o par tradução+planejador clássico, e a causa do fracasso em Floortile é a incapacidade do LLM de especificar corretamente relações espaciais complexas na tradução, não uma limitação do planejador em si. **A3** [torna mais específica] — sugere que, se o "ranking por domínio" de 2010 fosse estendido a arquiteturas LLM+planejador, a característica relevante poderia ser algo como "complexidade da relação espacial/relacional a especificar", que não tem correspondência direta nas métricas de diagrama de casos de uso/classes/estados de 2010.

## Pontos relevantes para o projeto

- Tabela por domínio é o dado mais direto do lote para a pergunta "o desempenho de LLM em planejamento varia por domínio de planejamento" — aqui varia de 0% a 100% dentro do mesmo método (LLM+P).
- Explicitação dos modos de falha por domínio (Blocksworld: LLM-as-P não mantém `ON`/`CLEAR`; Barman: não limpa copos antes de reusar; Floortile/Termes/Storage: falha em relações espaciais e restrições de posição) — útil para discutir *por que* certos domínios são mais difíceis, algo que 2010 não discute em termos de mecanismo.
- Data do modelo registrada de forma explícita (setembro de 2023) — permite datar o resultado.
- O artigo caracteriza explicitamente esse papel como "focar o LLM na tradução, deixando a busca para o planejador clássico" — definição operacional útil do papel "tradutor" para a introdução da Q3.

## Marcações

- `[FATO]` Tabela I: LLM+P atinge 0% em Floortile e 20% em Termes, mas 85–100% em Barman, Storage e Grippers, com o mesmo método aplicado a todos os domínios ("TABLE I: Success rate % of applying LLM-AS-P... and LLM+P", coluna Floortile = 0, Barman = 20(100)).
- `[HIPÓTESE]` A queda a 0% em Floortile, atribuída pelos autores a falha de especificação de conectividade espacial na tradução, é um candidato a "característica de domínio" moderna (complexidade relacional/espacial da tradução) que poderia complementar as métricas UML de 2010 caso a revisão venha a comparar poder preditivo de diferentes conjuntos de *features* (Q2).

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://arxiv.org/abs/2304.11477 (PDF baixado do arXiv, extraído com pdftotext). Conferência humana: pendente.
