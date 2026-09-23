---
tipo: nota-de-leitura
eixo: E6
citekey: mccluskey2017engineering
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: https://eprints.hud.ac.uk/id/eprint/33581/1/main.pdf
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026
afirmacoes-2010: [A5]
fragilidades: [F3]
perguntas: [Q2]
---

# Engineering Knowledge for Automated Planning: Towards a Notion of Quality

**Thomas L. McCluskey, Tiago S. Vaquero, Mauro Vallati · 2017 · Proceedings of the ACM Conference on Knowledge Capture (K-CAP 2017), p. 1–8**
**Link/DOI:** https://eprints.hud.ac.uk/id/eprint/33581/1/main.pdf · DOI: 10.1145/3148011.3148012

## Extração estruturada

- **Problema:** não existe, na comunidade de planejamento automatizado, uma noção compartilhada e formal de "qualidade" de um modelo de domínio — a engenharia de conhecimento para planejamento (KEPS) é hoje um processo ad hoc, em que as habilidades do engenheiro de conhecimento influenciam fortemente a qualidade do modelo resultante e, por consequência, o desempenho dos planejadores.
- **Método:** artigo conceitual/definicional. Propõe definições formais de cinco propriedades de qualidade de um modelo de conhecimento de planejamento: *consistência* (existe interpretação que torna verdadeiras todas as asserções do modelo), *acurácia* (a interpretação dada pelos requisitos torna verdadeiras as asserções), *completude* (toda solução aceitável nos requisitos é alcançável pelo modelo, e vice-versa), *adequação* (a linguagem de codificação tem poder expressivo suficiente para os requisitos) e *operacionalidade* (o modelo, com um dado planejador, produz solução dentro de limites de recursos aceitáveis).
- **Dados/benchmarks:** não há experimento empírico; o artigo é teórico/definicional, com exemplos ilustrativos em PDDL e PDDL+ (ex.: operador LOAD-TRUCK; processo de sinalização de tráfego urbano).
- **Resultado principal:** formaliza que a qualidade de um modelo de domínio é multidimensional (consistência, acurácia, completude, adequação, operacionalidade) e que a *operacionalidade* — a eficiência de geração de planos com um dado planejador — depende tanto do modelo quanto do planejador e pode variar drasticamente entre codificações igualmente completas e acuradas do mesmo domínio; cita explicitamente que a ordem dos elementos no modelo tem "significant bearing on the efficiency of planning", referenciando Vallati et al. 2015.
- **Relação com a dissertação de 2010:** o artigo dá base conceitual direta a [F3]: mostra formalmente que a "qualidade" de um modelo de domínio (do qual dependeriam quaisquer métricas extraídas, como as métricas UML de 2010) tem múltiplas dimensões distintas, e que pelo menos uma delas (operacionalidade) é explicitamente sensível à ordem/codificação do modelo e não apenas ao seu "conteúdo" — o que qualifica [A5]. Cita o itSIMPLE (referência [40] do artigo) como exemplo de ferramenta que codifica requisitos em UML antes de mapear para a linguagem do planejador, situando a linha itSIMPLE dentro da discussão de KEPS e de qualidade do modelo — relevante para [T1] (extração automática de métricas no itSIMPLE), embora o artigo não proponha nem avalie métricas específicas de UML.

## Pontos relevantes para o projeto

- Oferece um vocabulário formal (consistência/acurácia/completude/adequação/operacionalidade) que pode ser usado para situar precisamente o que as métricas de diagramas UML de 2010 medem — e não medem — na dissertação revisada.
- Explicita que "the choice of representation within the same language of a domain – as well as the order in which elements are listed within the domain – have a significant bearing on the efficiency of planning", citando diretamente Vallati et al. (2015) e Riddle, Holte & Barley (2011) como evidência — reforça, por segunda fonte independente, a robustez do achado central de [@vallati2015effective] e [@vallati2021importance].
- Situa o itSIMPLE (Vaquero et al. 2013) e o KEWI/AIS-DDL como exemplos de tradução de requisitos em notação orientada a aplicação (UML) para a linguagem do planejador, apontando que "the quality of the domain model is dependent both on the initial encoding and the correctness of the translation process" — relevante para a linha itSIMPLE e para [A5]/[T1].
- Discute o ICKEPS (International Competition on Knowledge Engineering for Planning and Scheduling) e observa que a maioria das equipes não usa ferramentas de KEPS, evidência indireta de que a engenharia de modelos permanece artesanal — reforça [F3] (dependência do modelador).

## Trechos literais

- "Formulating knowledge for use in planning engines is currently something of an ad-hoc process, where the skills of knowledge engineers significantly influence the quality of the resulting planning application. On top of that, a notion of quality of the knowledge captured within a domain model is missing." (Abstract)
- "It has been shown that the choice of representation within the same language of a domain – as well as the order in which elements are listed within the domain – have a significant bearing on the efficiency of planning [32, 37]" (Seção 5, Model Quality, p. 3 — [37] = Vallati et al. 2015)
- "In some cases, the requirements are encoded firstly into a more application-oriented language such as UML in itSIMPLE [40] [...] Hence, in this case, the quality of the domain model is dependent both on the initial encoding and the correctness of the translation process." (Seção 4, p. 3)

## Marcações

- `[FATO]` O artigo formaliza cinco atributos distintos de qualidade de modelo de domínio e afirma, com citação a Vallati et al. (2015) e Riddle, Holte & Barley (2011), que a ordem dos elementos do modelo afeta significativamente a eficiência do planejamento (Seção 5).
- `[FATO]` O itSIMPLE é citado como ferramenta que traduz requisitos em UML para a linguagem do planejador, com a qualidade do modelo final dependendo tanto da codificação inicial quanto da tradução (Seção 4).
- `[HIPÓTESE]` (minha interpretação) As métricas de diagramas UML usadas em 2010 (número de classes, atributos, associações etc.) podem ser lidas, neste vocabulário, como proxies indiretas e não validadas de "adequação"/"complexidade requerida" do domínio — mas o artigo não oferece nem valida tal mapeamento; isso permanece uma lacuna a ser discutida na revisão, não uma afirmação da obra lida.

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de texto integral em https://eprints.hud.ac.uk/id/eprint/33581/1/main.pdf. Conferência humana: pendente.
