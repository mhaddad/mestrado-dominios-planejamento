---
tipo: nota-de-leitura
eixo: E6
citekey: vallati2025knowledge
prioridade: B
status: lido
profundidade: resumo
fonte-lida: https://ojs.aaai.org/index.php/ICAPS/article/view/36142
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: []
fragilidades: [F3]
perguntas: [Q2, Q3]
---

# Knowledge Engineering for Planning and Scheduling in the LLM Era

**Vallati, M.; Barták, R.; Chrpa, L.; McCluskey, T.L.; Petrick, R.P.A. · 2025 · ICAPS 2025**
**Link/DOI:** https://doi.org/10.1609/icaps.v35i1.36142

## Extração estruturada

- **Problema:** como os LLMs podem (ou não) apoiar a engenharia do conhecimento (KE) para planejamento e escalonamento (KEPS), tendo em vista que planejamento automatizado depende de conhecimento de domínio explícito, tipicamente em PDDL.
- **Método:** artigo de posicionamento/discussão (não detalhado em profundidade a partir da página de resumo; não foi possível baixar o PDF completo, apenas a página HTML de visualização do artigo).
- **Dados/benchmarks:** não determinado a partir do resumo disponível.
- **Resultado principal:** LLMs podem auxiliar na aquisição e formulação de conhecimento, mas a expertise humana de domínio e validadores simbólicos externos continuam indispensáveis para garantir corretude, operacionalidade e completude de aplicações de planejamento.
- **Relação com a dissertação de 2010:** aborda diretamente a pergunta **Q2/Q3** da revisão — onde entram os LLMs na engenharia do conhecimento de domínios de planejamento — e dialoga com **F3** (dependência do modelador): a conclusão de que "expertise humana e validadores simbólicos permanecem indispensáveis" sugere que a dependência do modelador (humano ou humano+LLM) não desaparece, apenas se reconfigura.

## Pontos relevantes para o projeto

- É, dentro do lote, o artigo mais diretamente alinhado ao título e escopo do eixo E6 ("engenharia do conhecimento para planejamento na era dos LLMs"), útil como âncora da seção sobre esse tema na revisão.
- A posição de que LLMs não substituem validação simbólica externa é consistente com a conclusão neurossimbólica de pallagani2024prospects (eixo E5), reforçando um padrão que aparece em múltiplos trabalhos do lote.
- Acesso limitado ao PDF completo: apenas a página de visualização OJS foi obtida; o link direto para o PDF redirecionou para uma página HTML sem o arquivo. Recomenda-se nova tentativa de acesso ao texto integral em revisão futura, se a obra for promovida a prioridade A.

## Trechos literais

"While LLMs can assist in knowledge acquisition and formulation, human domain expertise and external symbolic validators remain indispensable for ensuring correctness, operationality and completeness of planning applications" (resumo, via página do artigo).

## Marcações

- `[FATO]` o artigo conclui que LLMs auxiliam mas não substituem expertise humana e validação simbólica externa na engenharia do conhecimento para planejamento (resumo).
- `[HIPÓTESE]` interpretação minha: esta conclusão, combinada com a de pallagani2024prospects (E5) sobre abordagens neurossimbólicas serem mais promissoras que LLM puro, sugere um consenso emergente na literatura 2024-2025 de que LLMs são complementares, não substitutos, dos métodos simbólicos que fundamentam tanto 2010 quanto o itSIMPLE — hipótese a testar com leitura mais aprofundada de outros trabalhos do eixo.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de resumo na página do artigo (https://ojs.aaai.org/index.php/ICAPS/article/view/36142); tentativa de download do PDF direto falhou (retornou página HTML de visualização, não o arquivo). Conferência humana: pendente.
