# Parecer editorial da primeira versão integral da dissertação

Data: 28/09/2026. Versão examinada: commit `c5eac08`. Responsável: Codex (GPT-6), com orientações de revisão editorial e auditoria de fontes. Natureza: avaliação e proposta de revisão; nenhuma alteração aplicada aos capítulos nesta sessão.

## 1. Diagnóstico

A dissertação tem uma contribuição identificável e uma base documental que permite uma redação mais forte do que a atual. Seu argumento central é relevante: reproduzir um cálculo não demonstra a validade de uma recomendação, e observar diferenças entre planejadores não demonstra que as características escolhidas permitam antecipá-las. A pesquisa também oferece uma conexão defensável com engenharia de software: avaliar decisões entre configurações de agentes com referências fortes, informação disponível no momento da decisão e medidas de resultado explícitas.

A primeira versão integral ainda não comunica todo esse trabalho. Os capítulos de resultados funcionam como sínteses dos relatórios internos; a fundamentação preserva trechos escritos antes dos experimentos; e algumas ressalvas dos registros se perderam na passagem para a prosa. Há também erros localizados e conclusões que precisam de maior precisão. **O estado recomendado é: precisa de revisão estrutural e de correções factuais antes da revisão final do autor e do envio ao orientador.**

É necessário corrigir a avaliação anterior de que restava apenas a revisão visual. A existência das chaves bibliográficas e a integridade do DOCX foram verificadas, mas essas verificações não asseguram fidelidade de cada afirmação à evidência, coerência entre capítulos ou qualidade da argumentação.

### Escopo e limites deste parecer

Foram lidos os capítulos 1–8, pré-textuais e apêndices, o plano de escrita, as decisões e o estado do projeto, os relatórios das Fases 3, 4 e 4B, o dossiê e a curadoria da Fase 5. Foram confrontados pontos materiais com os registros EXP-12, EXP-14, EXP-18, EXP-19, EXP-21, EXP-24 e EXP-25, a tabela de correção de Holm e notas de leitura pertinentes. A estrutura textual do DOCX foi inspecionada diretamente no XML; não houve inspeção visual de páginas.

O verificador bibliográfico encontrou **110 chaves distintas**, todas presentes na bibliografia aprovada. Esse resultado confirma a disponibilidade das referências, não a validade de todas as paráfrases. Não foi refeita nesta sessão a auditoria integral das fontes primárias nem foram reexecutados experimentos. Os achados abaixo distinguem divergências documentais confirmadas de recomendações de redação e interpretação.

## 2. O que preservar

- **A sequência de investigação:** auditoria, reprodução, correções, reexecução e ampliação. Ela permite ao leitor entender como a conclusão foi sendo restringida.
- **A distinção entre domínio e instância:** é essencial para comparar o problema de 2010 com os desenhos posteriores.
- **A taxonomia multidimensional:** organiza a descrição dos sistemas e torna visível a diferença entre técnica, implementação e portfólio. Seu valor descritivo permanece mesmo quando seu uso em seleção não melhora o desempenho.
- **Os papéis separados dos LLMs:** seleção, geração de planos, geração com verificador e tradução pedem avaliações distintas.
- **A natureza exploratória da Ponte:** as hipóteses e os limites são parte da contribuição, especialmente por não haver piloto organizacional.
- **A rastreabilidade:** os registros e dados permitem desenvolver os capítulos sem inventar resultados ou iniciar uma nova campanha experimental.

## 3. Correções prioritárias de conteúdo e consistência

P1 identifica problemas que alteram o entendimento da pesquisa; P2 identifica lacunas de exposição e acabamento. As localizações referem-se à versão examinada.

### E01 — P1: atualizar as promessas da introdução ao trabalho executado

**Localização:** [Introdução](capitulos/01-introducao.md), Q2 e objetivo específico 6; [Auditoria](capitulos/03-revisitando-2010.md), final de “As métricas UML como instrumento”.

A introdução diz que Q2 precisa controlar a reordenação do PDDL; o capítulo 3 ainda anuncia a comparação “com controle da ordem de escrita do modelo”. O capítulo 4 e a decisão de 27/09 registram que esse controle foi dispensado. A introdução também promete “testar” a escolha de configurações de agentes, enquanto a Fase 5 foi explicitamente redefinida como exploratória.

**Tratamento:** formular Q4 como investigação de conexões e hipóteses; substituir o objetivo por “formular e discutir hipóteses de aplicação”. Explicitar que a robustez à serialização permaneceu uma limitação. Reproduzir as cinco perguntas canônicas do plano ou registrar qualquer reformulação de alcance. Não apresentar o trabalho futuro como experimento realizado.

**Base:** plano, seções 5 e 10; capítulo 4, limitações. Divergência confirmada, confiança alta.

### E02 — P1: corrigir a descrição da taxonomia original

**Localização:** [Fundamentos](capitulos/02-fundamentos.md), abertura, seção sobre planejadores e síntese final.

O capítulo 2 repete “seis categorias” e “rótulos mutuamente exclusivos”. O capítulo 3 e a [taxonomia auditada](../auditoria/taxonomia-tecnicas.md) registram **onze rótulos não exclusivos**. Seis técnicas destacadas nas conclusões originais não são a totalidade da classificação.

**Tratamento:** corrigir número e exclusividade. A crítica é à mistura de dimensões e às atribuições sem respaldo, não à existência de múltiplos rótulos por planejador. Evitar chamar as quatro dimensões novas de estatisticamente “independentes”; são dimensões descritivas distintas, cujos valores podem estar associados.

**Base:** capítulo 3, seção “A taxonomia de técnicas”; `auditoria/taxonomia-tecnicas.md`, abertura. Divergência confirmada, confiança alta.

### E03 — P1: calibrar a resposta a Q2 ao contraste efetivamente testado

**Localização:** [Resultados](capitulos/05-resultados.md), “Métricas de modelagem e features modernas”, e [Conclusões](capitulos/08-conclusoes.md), Q2.

O texto conclui que os conjuntos não acrescentam poder preditivo um ao outro. No EXP-12, entretanto, as perdas do *random forest* são 189 com SAS+, 151 com métricas extraídas do PDDL e 148 com ambos. Há melhora numérica da combinação. Os testes registrados em `correcao-multipla/holm.csv` comparam seletores com o SBS; não estabelecem equivalência entre conjuntos nem testam diretamente todo contraste incremental entre eles.

**Tratamento:** dizer que nenhum conjunto ou combinação demonstrou superar o SBS e que os resultados não estabelecem ganho incremental robusto. Preservar a diferença numérica observada, sem convertê-la em ganho estatisticamente demonstrado. Se o texto quiser responder literalmente ao ganho incremental entre conjuntos, será necessária uma comparação adicional explicitamente exploratória, com justificativa e controle de multiplicidade; isso é uma opção de aprofundamento, não condição para corrigir a redação agora.

Também distinguir **métricas UML originais**, disponíveis nos domínios de 2010, de **aproximações extraídas do PDDL**, usadas na ampliação. Chamá-las indistintamente de “métricas UML” sugere uma equivalência de instrumentos que o próprio EXP-07 restringe.

**Base:** [EXP-12](../experimentos/execucoes/2026-09-26-nivel4-publicados.md), tabela de resultados; [Holm](../experimentos/analise/correcao-multipla/holm.csv). Diagnóstico do alcance dos testes, confiança alta. A formulação forte também aparece no relatório da Fase 3; corrigir a cadeia documental quando a revisão for aplicada.

### E04 — P1: separar resultado numérico, significância e equivalência

**Localização:** capítulos 5, 6 e 8.

“Empata estatisticamente”, no capítulo 6, transforma ausência de diferença significativa em equivalência. No capítulo 5, “nenhum seletor supera” também pode apagar ganhos numéricos sem significância: no EXP-24, a versão 4D completa perde 35 instâncias contra 52 do SBS na trilha satisficing de 2018, com todos os planejadores, mas p ajustado de 0,375.

**Tratamento:** usar “não foi detectada diferença significativa” no primeiro caso e “nenhum seletor demonstrou ganho estatisticamente significativo” no segundo. Quando as perdas forem maiores em todas as alternativas de um recorte, a afirmação descritiva pode ser mais direta. Não equiparar resultado inconclusivo a prova de inutilidade ou equivalência.

**Base:** [EXP-24](../experimentos/execucoes/2026-09-27-r29-instancias.md), tabela e interpretação; EXP-14 e tabela de Holm. Confiança alta.

### E05 — P1: tornar inequívoca a apresentação dos p-valores

**Localização:** capítulo 5, tabela de seletores do Nível 4.

A tabela mistura p bruto de 0,13 com p ajustado de 0,068 e expressões como “não significativo”. Para o método de 2010 com PDDL, o CSV registra p bruto de 0,1261 e p ajustado de 0,3784 na família de sete comparações.

**Tratamento:** usar colunas separadas para p bruto e p ajustado, indicar a família de testes e a direção da diferença. Identificar também o recorte das versões por técnica; a faixa “170 a 387” esconde diferenças entre D1, D2 e as quatro dimensões juntas. Informar que o teste é por domínio, mesmo quando a perda total é expressa em instâncias.

**Base:** `experimentos/analise/correcao-multipla/holm.csv`. Divergência de apresentação confirmada, confiança alta.

### E06 — P1: corrigir denominadores e unidades que foram comprimidos na síntese

**Localização:** capítulo 5, reexecução e IPCs.

- **50 de 63 e 18 de 38 não são parcelas de uma mesma comparação.** O primeiro resultado compara contagens de problemas resolvidos do EXP-05; o segundo compara notas do EXP-19 usando o rótulo original de origem. Este último explicita 38/62 e a ressalva do G21, cuja origem corrigida é 34/66. A prosa atual conecta as duas análises como se compartilhassem população e medida.
- **“Seis modelos por recorte” está incorreto.** A tabela final do EXP-21 registra seis com todos os planejadores e sete sem portfólios.
- **Dez unidades incluem os dois recortes de portfólio.** São cinco combinações edição × trilha, cada qual com e sem portfólios. “Dez unidades [...] quando todos os planejadores são incluídos” mistura o total com um recorte.
- **“13 tarefas originais” deve ser “13 domínios originais”** no trecho de correlações UML × SAS+, cuja unidade é agregada por domínio.

**Tratamento:** separar as duas medidas do Nível 3 em frases ou linhas próprias; informar o universo de cada percentual e os filtros; distinguir recorte completo e sem portfólios. Adotar um pequeno quadro de fluxo da amostra: disponível → características obtidas → elegível → usado em cada análise. O método do EXP-24 inclui apenas instâncias com características e resolvidas por algum planejador do recorte; essa condição precisa aparecer no capítulo.

**Base:** EXP-05, EXP-19, tabela final do [EXP-21](../experimentos/execucoes/2026-09-27-q5-ipc.md), configuração e tabela do EXP-24. Confiança alta.

### E07 — P1: distinguir previsão de resolução de comparação relativa entre famílias

**Localização:** capítulo 4, “Famílias de técnica e modelos”; capítulo 5, resposta a Q5.

Q5 pergunta por desempenho relativo de famílias. A regressão descrita prevê, para cada família, se algum integrante resolve a instância. Uma AUC favorável nessa tarefa não demonstra que o modelo escolha entre famílias concorrentes: pode estar identificando dificuldade geral. O mapa comparativo por domínio e o teste de seleção por instância respondem a partes diferentes dessa pergunta.

**Tratamento:** explicitar essa operacionalização e seu limite. Organizar a resposta em três passos: diferenças observadas entre famílias; previsão de resolução; utilidade da previsão para escolher. Informar sobre quais modelos se calcula a AUC mediana, quantos ficaram sem modelo por falta de variação e que AUC não é porcentagem de problemas resolvidos. Preservar o ganho localizado da topologia sem generalizá-lo a todas as famílias.

**Base:** método do EXP-21 e do EXP-25; capítulo 4. Avaliação conceitual do desenho documentado, confiança alta.

### E08 — P1: recuperar a regra de pontuação do seletor LLM

**Localização:** capítulo 6, “LLM como seletor de planejador”.

O EXP-14 pontua descrições taxonômicas idênticas pela cobertura média do grupo. A comparação com catálogo nominal usa também pontuação por identidade exata. Na primeira regra, três modelos ficam significativamente piores que o SBS depois de Holm; na pontuação exata da condição anônima, só o Gemini. O capítulo informa o primeiro resultado e passa para a condição nominal sem explicar a mudança de medida.

**Tratamento:** apresentar as duas regras e comparar anonimato e nomes sob a mesma regra exata. Explicar por que a perda pode ter parte decimal. Acrescentar os elementos do protocolo que afetam a interpretação: PDDL e instância p01 como entrada, truncamento de três arquivos, descrições idênticas e temperatura padrão por modelo. Isso evita atribuir todo efeito à reputação ou ao nome do planejador.

**Base:** [EXP-14](../experimentos/execucoes/2026-09-26-x3-llm-seletor.md), configuração e correção estatística; EXP-15; `holm.csv`. O padrão de escolhas é observado; a explicação “escolher o mais famoso” permanece hipótese.

### E09 — P1: reconciliar o custo, sem substituir o total por uma soma presumida

**Localização:** capítulo 6, segundo parágrafo.

O texto afirma que US$ 10,51 mais US$ 2,04 totalizam US$ 12,49. A soma é US$ 12,55. O registro do EXP-23 distingue custo pela soma das chamadas e uso acumulado da chave; a divergência já existe no relatório-fonte.

**Tratamento:** reconciliar soma de chamadas e uso registrado pelo provedor, identificando o perímetro de cada valor. Enquanto isso, apresentar os valores como medidas distintas e registrar a diferença de US$ 0,06. Não trocar automaticamente o total para US$ 12,55 nem inventar explicação para a discrepância.

**Base:** [EXP-23](../experimentos/execucoes/2026-09-27-x1-ofuscado.md), configuração, e relatório da Fase 4. A inconsistência aritmética é confirmada; sua causa permanece não verificada.

### E10 — P1: delimitar o que foi validado em X2 e X4

**Localização:** capítulo 6, planejador com verificador e tradutor.

Em X2, “seis são corretos” sugere equivalência semântica estabelecida. O EXP-18 usa validação cruzada de planos nos problemas p01–p05 e registra expressamente que a equivalência foi testada por exemplos, não provada. O tradutor também recebe p01 em PDDL, além da descrição natural; essa condição foi omitida na síntese do capítulo.

Em X4, o aumento de oito para treze planos válidos mostra o resultado do ciclo com retorno do VAL. Sem condição comparável de novas tentativas e orçamento adicional sem esse retorno, não se deve atribuir todo o ganho exclusivamente ao verificador. A ausência de plano por esgotamento de tokens é uma falha operacional; não demonstra que o modelo chegaria a um plano correto com mais orçamento.

**Tratamento:** usar “passaram nas verificações realizadas” em X2, informar as cinco instâncias e separar incompatibilidade de assinatura, erro detectado e caso não avaliado. Em X4, falar no desempenho observado do ciclo e manter o custo adicional e a ausência de controle como limites.

**Base:** [EXP-18](../experimentos/execucoes/2026-09-27-x2-llm-tradutor.md), avaliação e limites; EXP-17. Confiança alta quanto ao alcance documentado.

### E11 — P1: retirar afirmações causais ou universais não asseguradas pelo desenho

**Localização:** capítulos 2 e 4, principalmente.

“Assim, cada diferença em relação a 2010 pode ser atribuída a uma causa”, na abertura do método, promete identificação causal que a sequência de estudos não fornece: na ampliação mudam conjuntamente dados, planejadores e instrumentos. O capítulo 2 atribui a melhora entre gerações de LLMs a arquitetura, “não a mais dados”, sem uma ablação apresentada para separar essas causas. Também converte a existência do campo de seleção de algoritmos em confirmação geral de que características observáveis predizem o vencedor.

**Tratamento:** restringir isolamento de alterações aos cenários em que ele ocorreu; descrever as demais camadas como comparação sob condições documentadas. Distinguir resultados teóricos, evidência empírica localizada e motivação de pesquisa. Uma formulação de problema, como a de Rice, não garante que qualquer conjunto de características seja preditivo.

Na seção de características, substituir “antes de qualquer execução de planejador” por disponibilidade anterior à decisão de seleção, sem acesso ao resultado dos competidores. A sondagem executa computação heurística; não deve parecer uma medida puramente estática. Marcar como exploratória a decomposição de topologia feita depois da análise principal, conforme o EXP-25.

### E12 — P1: integrar a literatura aprovada ao término da Fase 5

**Localização:** capítulos 2 e 7.

As chaves `fan2026dependencyrouter`, `zhou2026agentasarouter`, `madeyski2026triage` e `chen2026risa` foram aprovadas, mas não aparecem nos capítulos. O capítulo 2 ainda afirma que os preprints não são usados como evidência e que a ponte não tem elo intermediário publicado, enquanto o capítulo 7 usa SWE-Router como evidência de fronteira. O acervo aprovado permite uma apresentação mais concreta e coerente.

**Tratamento recomendado:**

| Fonte já aprovada | Função na argumentação | Limite a preservar |
|---|---|---|
| DepFixRouter / Fan | Triagem anterior ao agente e disponibilidade temporal dos sinais | Atualizações de dependência; diagnóstico, não qualidade final do reparo |
| Agent-as-a-Router / Zhou | Diferença entre descrever a tarefa e fornecer histórico de desempenho | Benchmark e relatório técnico; não comprova ganho organizacional |
| Triage / Madeyski | Hipótese concorrente sobre métricas de código e condições de refutação | Protocolo propositivo, sem resultado empírico próprio |
| Risa / Chen | Seleção entre tentativas e limites do ganho sobre uma referência simples | Não é seleção entre configurações; requer traços internos de MoE |
| SWE-Router / Son | Escalonamento após trajetória parcial | Evidência de benchmark, sem validação em uma equipe específica |
| SALLMA / Becattini | Separação arquitetural entre configuração e execução | Apoio arquitetural qualitativo |

Não é obrigatório dar o mesmo espaço a todas. Fan, Zhou e Madeyski oferecem conexões especialmente diretas com o argumento da dissertação; Risa pode funcionar como contraponto breve.

**Cuidado com os insumos:** a síntese E8 ainda diz “testado no SWE-bench Lite” para Triage e inclui Agent-as-a-Router em “produção real”. Isso conflita com as notas corrigidas de 28/09. Usar as notas atualizadas e a curadoria aprovada como referência editorial; corrigir a síntese quando a revisão for implementada.

**Base:** [Curadoria](../ponte-software/relatorio/curadoria-fontes-se-ia.md), notas individuais e busca das chaves nos capítulos. Confiança alta quanto à ausência e às divergências internas. Não houve nova busca externa nesta sessão.

### E13 — P2: corrigir remissões e material de bastidor no documento compartilhado

**Localização:** capítulos 1–5 e apêndices; montagem.

A inspeção textual do DOCX confirma avisos “Rascunho gerado por IA” no início dos capítulos 1–3. Também confirma que a tabela da validação original no capítulo 5 aparece como **Tabela 6**, embora o parágrafo a chame de “Tabela 1”. O capítulo 3 usa títulos manuais; os posteriores usam legendas processadas. O filtro incrementa o contador inclusive em tabelas sem legenda. A remissão “Tabela A.1” dos apêndices também não segue a numeração produzida.

**Tratamento:** manter a declaração de IA nos pré-textuais e o estado de rascunho em metadados; uniformizar legendas e fontes; adotar identificadores e remissões resolvidas pela montagem; conferir listas e referências cruzadas no arquivo gerado. Atualizar campos no Word, isoladamente, não corrige números digitados manualmente na prosa.

Os apêndices prometem codificação completa, scripts e dados, mas entregam sobretudo caminhos internos. Para compartilhar com um leitor sem acesso ao repositório privado, incluir as tabelas essenciais ou preparar um suplemento versionado acessível, com instruções de acesso. Publicar o repositório não é requisito nem ação autorizada por este parecer.

## 4. Arquitetura e fluidez: a pesquisa precisa ocupar o centro do texto

### 4.1 Reequilibrar fundamentação e resultados

Contagem aproximada por palavras separadas por espaços, removendo metadados iniciais e comentários HTML, mas incluindo tabelas e títulos:

| Parte | Palavras aproximadas | Avaliação editorial |
|---|---:|---|
| Capítulo 2 — Fundamentos | 6.264 | Extenso e denso; vários parágrafos acumulam trabalhos e números |
| Capítulo 3 — Auditoria | 3.510 | Substancial, mas repete explicações dos capítulos 2 e 4 |
| Capítulo 4 — Método | 4.340 | Bem documentado; ainda usa linguagem de execução do projeto |
| Capítulo 5 — Resultados | 2.236 | Condensa excessivamente a maior parte da contribuição empírica |
| Capítulo 6 — LLMs | 1.424 | Não tem tabela quantitativa de resultados; só quadro taxonômico |
| Capítulo 7 — Ponte | 2.000 | Coerente, mas perde parte da concretude do dossiê e da curadoria |

Essas proporções não impõem uma meta de páginas. Mostram onde investir: recuperar evidência e interpretação nos capítulos 5 e 6 e reduzir enumerações no capítulo 2. O leitor precisa compreender por que cada análise foi necessária e como o resultado modifica a conclusão, sem consultar os registros EXP a cada passagem.

### 4.2 Dar uma função própria a cada capítulo

| Capítulo | Função recomendada | Alteração principal |
|---|---|---|
| 1 | Apresentar o problema, as perguntas e a contribuição alcançada | Atualizar promessas; antecipar o resultado central com seu alcance |
| 2 | Preparar conceitos necessários à leitura dos experimentos | Organizar por problemas e contrastes, não pela sequência de oito eixos da busca |
| 3 | Mostrar o que a auditoria mudou na interpretação de 2010 | Concentrar o diagnóstico histórico e encaminhar as decisões operacionais ao método |
| 4 | Permitir compreender e reproduzir a avaliação | Definir unidades, variáveis, filtros, referências e protocolos sem cronologia operacional excessiva |
| 5 | Apresentar evidência e discussão de Q1, Q2 e Q5 | Desenvolver resultados por pergunta, explicando diferenças entre reprodução, predição e seleção |
| 6 | Comparar os papéis dos LLMs e seus limites | Separar protocolo, resultados e interpretação; acrescentar tabelas por condição e modelo |
| 7 | Derivar aplicabilidade exploratória para engenharia de software | Integrar fontes recentes, exemplos e protocolo hipotético, mantendo o limite de evidência |
| 8 | Responder às perguntas e explicitar contribuições | Concluir a partir dos resultados, sem repetir todo o percurso nem generalizar resultados nulos |

Manter os oito capítulos é suficiente. Não há necessidade de reorganizar toda a dissertação ou renumerar Q1–Q5: basta explicar que Q5 é apresentada junto ao núcleo experimental antes de Q3 e Q4.

### 4.3 Substituir repetição por progressão

“A pergunta permanece, mas o método não se sustenta” reaparece na introdução, fundamentos, auditoria, resultados, Ponte e conclusões. A ideia é central, mas sua repetição em quase a mesma forma reduz o avanço do argumento.

Distribuição proposta: na introdução, enunciar a contribuição; nos fundamentos, explicar o que a literatura torna plausível; na auditoria, identificar o problema; nos resultados, mostrar a evidência; na Ponte, explicitar a consequência; nas conclusões, responder em conjunto. Usar remissões curtas para o que já foi demonstrado.

O capítulo 2 merece especial atenção: reduzir parágrafos com muitos sistemas, datas, porcentagens e citações; abrir cada subseção com sua pergunta; agrupar trabalhos pelo que concordam ou divergem; terminar com a implicação para o desenho desta dissertação. Evitar qualificações como “o trabalho mais limpo” e alegações amplas como “nunca aplicado” baseadas apenas no que uma busca encontrou.

## 5. Como apresentar melhor os experimentos

### 5.1 Um padrão para cada bloco de resultados

Cada análise deve responder, em prosa contínua apoiada pela tabela pertinente:

1. Que dúvida ela resolve e por que a etapa anterior não bastava?
2. Qual é a unidade avaliada, a amostra elegível e a referência?
3. Qual é o resultado, em uma medida com direção e denominador claros?
4. Qual é a incerteza e o que foi ou não testado?
5. O que muda na resposta à pergunta de pesquisa?

Não transformar essas perguntas em cinco subtítulos repetidos. Usá-las como critério de revisão dos parágrafos. A conclusão deve vir perto da evidência correspondente.

### 5.2 Evidência já existente que merece aparecer no corpo

| Peça proposta | Conteúdo e benefício | Base existente |
|---|---|---|
| Quadro de desenho e fluxo da amostra | Pergunta, unidade, entradas, resultado, filtros e comparação | Capítulo 4; EXP-12, EXP-21, EXP-24, EXP-25 |
| Tabela da reexecução | Contagens e notas separadas, diferenças de origem e casos excepcionais | EXP-05 e EXP-19 |
| Tabela de cobertura, qualidade e tempo | Mostrar concretamente quando a medida altera a leitura do desempenho | EXP-20 e EXP-22 |
| Gráfico de perdas no Nível 4 | VBS e SBS como referências; todos os seletores relevantes, unidade em instâncias | `nivel4-publicados/resumo.csv`; `correcao-multipla/holm.csv` |
| Mapa de desempenho por família e domínio | Mostrar as regiões de vantagem que médias globais escondem | `q5-ipc/mapa_familias.csv` |
| Tabela ou gráfico pareado de AUC | SAS+ versus combinação, por família, edição e trilha; identificar recortes | `topologia-q5/modelos.csv` |
| Tabela de seleção por instância | Preservar ganhos numéricos, significância local/global e efeito dos portfólios | `r29-instancias/resumo.csv`; `topologia-q5/seletores.csv` |
| Painéis dos experimentos LLM | X3 anônimo/nominal; X1 original/ofuscado; X4 inicial/final; X2 por categoria | Registros e resultados de X1–X4 |

Essas peças devem ser selecionadas pela função explicativa, não adicionadas como decoração. Uma versão enxuta pode priorizar perdas do Nível 4, comparação de AUC e resultados LLM, deixando tabelas extensas no suplemento. Gráficos devem mostrar os valores medidos; intervalos de confiança só podem ser incluídos se calculados por procedimento apropriado. O EXP-21 informa que a rodada não produziu intervalos de confiança.

### 5.3 Recuperar os resultados positivos e intermediários

O texto insiste no insucesso da seleção e deixa em segundo plano entregas que demonstram trabalho científico: a reprodução célula a célula; a recuperação e validação dos dados de competição; a validação do extrator de topologia; os efeitos diferentes de cobertura, tempo e comprimento do plano; a heterogeneidade localizada entre famílias; a correção de planos no ciclo com VAL; e a distinção entre erro de tradução e incompatibilidade do instrumento de avaliação.

O mapa característica × técnica do relatório da Fase 4B, por exemplo, oferece associações concretas que o capítulo 5 quase não discute. Ele pode entrar com a ressalva original: coeficientes de variáveis correlacionadas descrevem o modelo, não demonstram efeito causal de uma característica isolada. Isso atende melhor à pergunta do título e ajuda o leitor a entender o que foi aprendido mesmo sem um seletor superior.

### 5.4 Tornar as medidas compreensíveis

Definir, antes do primeiro resultado: cobertura, perda, SBS, VBS, AUC, unidade do teste e correção de Holm. Mostrar um exemplo de perda com Storage: a diferença entre a nota do melhor planejador observado e a do recomendado. Explicar por que uma perda no Nível 2 é em pontos de nota, no Nível 4 em instâncias não resolvidas e no R-29 em falhas por instância. Não apresentar esses números como uma série diretamente comparável.

Na análise por família, distinguir cobertura do melhor integrante por domínio de cobertura da união dos integrantes por instância. Na validação, esclarecer que o SBS é escolhido no treino de cada partição; o vencedor calculado sobre todo o conjunto serve para descrição e pode não coincidir com o de cada partição.

## 6. Como aprofundar o capítulo de aplicabilidade em software

O capítulo 7 já evita prometer eficácia local. O próximo ganho é explicar mecanismos e situações concretas, reduzindo a repetição de cautelas. Recomenda-se uma seção “Decisões ao longo de uma tarefa de software” com três momentos: triagem anterior à execução, escalonamento após exploração e coordenação/verificação de tentativas. Cada momento deve conectar resultado de planejamento, fonte de software e hipótese correspondente.

**Exemplo hipotético a desenvolver:** uma atualização de dependência abre um PR e falha na integração contínua. Antes de executar um agente, estão disponíveis título, versão alterada e informações iniciais; depois de uma exploração curta, surgem a localização da falha e o resultado de testes. Uma política poderia encaminhar o caso a diagnóstico, reparo ou revisão humana. O exemplo precisa indicar quais sinais existem em cada momento, qual decisão informam e como a escolha seria comparada a uma configuração fixa. Nenhum ganho numérico deve ser inventado.

Um segundo exemplo, mais breve, pode contrastar correção localizada com refatoração distribuída. A função é mostrar como dependências entre ações, estado parcial do repositório, verificação e necessidade de replanejamento aproximam o trabalho de software dos conceitos discutidos na dissertação, sem afirmar que o repositório seja um domínio PDDL completo. Testes funcionam como evidência parcial de correção; a equivalência com um verificador formal de planos deve ser explicitamente limitada.

Para cada hipótese H1–H5, acrescentar: unidade de observação, sinal disponível antes da decisão, referência, resultado observado e desenho de validação. Isso pode ser um quadro compacto de agenda futura. Deve continuar sendo protocolo proposto, sem piloto ou coleta local.

A notação `π(φ(t), ψ(a), τ) → a` também merece ajuste. Ela usa a configuração escolhida como entrada sem definir o conjunto de alternativas. Definir um conjunto A de configurações disponíveis e uma política que escolha um elemento de A a partir da tarefa, das descrições das alternativas, da trajetória e dos objetivos. Se a política é sequencial, incluir decisões de continuar, escalar, interromper ou solicitar revisão. A notação deve esclarecer a prosa; se não o fizer, um diagrama simples de decisões é preferível.

## 7. Exemplos de reformulação

As propostas abaixo ilustram a direção da revisão. Não foram inseridas no manuscrito e preservam o alcance dos dados existentes.

### 7.1 Objetivo exploratório

**Atual:** “testar, como hipótese, se o princípio de ajuste informa a escolha de configurações de agentes”.

**Proposta:** “Investigar conexões entre a seleção de planejadores e a escolha de configurações de agentes de software, formulando hipóteses e critérios para sua avaliação em estudos futuros.”

### 7.2 Resposta a Q2

**Atual:** “as métricas [...] não acrescentam poder preditivo às features SAS+, e as features SAS+ não acrescentam poder preditivo a elas”.

**Proposta:** “A combinação das duas famílias reduziu numericamente a perda do random forest, mas permaneceu acima da referência fixa: 148 instâncias, contra 143 do SBS. Os testes realizados não demonstraram superioridade dos seletores sobre essa referência. Esses resultados não estabelecem, por si sós, ausência de informação complementar entre as famílias de características.”

Fonte: EXP-12 e tabela de Holm. Não acrescenta novo teste.

### 7.3 Comparação do seletor LLM

**Atual:** “o GPT-6 Sol empata estatisticamente com o melhor planejador único”.

**Proposta:** “O GPT-6 Sol apresentou perda de 146 instâncias, contra 143 do SBS. O teste não detectou diferença significativa entre os resultados (p = 0,18); essa ausência de diferença não demonstra equivalência entre os métodos.”

Fonte: EXP-14, pontuação principal por grupo.

### 7.4 Validação do tradutor

**Atual:** “Entre esses dez, seis são corretos”.

**Proposta:** “Entre os dez pares com assinaturas compatíveis, seis passaram nas verificações cruzadas dos planos nos problemas avaliáveis de p01 a p05. O resultado fornece evidência de compatibilidade nesses testes, mas não constitui prova de equivalência semântica entre os domínios.”

Fonte: EXP-18, configuração, resultados e limites.

### 7.5 Conexão entre topologia e seleção

**Proposta de transição:** “A sondagem acrescentou informação para prever a resolução por algumas famílias. Resta verificar se esse sinal é suficiente para orientar uma escolha entre planejadores. A análise seguinte examina essa segunda exigência: compara a perda dos seletores com a de uma referência fixa escolhida no treinamento.”

Função: separar previsão de resolução e utilidade decisória, ligando Q5 ao R-29.

### 7.6 Aplicabilidade

**Proposta:** “Em uma tarefa de software, a decisão pode mudar após os primeiros testes ou a localização do código afetado. A conexão com esta pesquisa está em avaliar o valor dessa informação: ela permite escolher uma configuração com menor custo total e qualidade aceitável, em comparação com uma configuração fixa? O capítulo formula essa pergunta e suas condições de teste; sua resposta exige dados próprios de engenharia de software.”

Função: tornar a contribuição positiva e concreta, mantendo seu caráter exploratório.

## 8. Ordem recomendada de revisão e critérios de conclusão

1. **Consolidar o conteúdo canônico:** corrigir E01–E12 nos capítulos e nos relatórios/sínteses afetados, preservando decisões já tomadas e registrando divergências não resolvidas. Não alterar resultados para ajustar a narrativa.
2. **Desenvolver os capítulos 5 e 6:** recuperar protocolos essenciais, denominadores, tabelas e discussão; conferir cada célula contra a saída de análise correspondente.
3. **Integrar a Fase 5 ao capítulo 7 e aos fundamentos:** incorporar as fontes aprovadas pelo papel correto e apresentar pelo menos um exemplo hipotético completo de engenharia de software.
4. **Revisar a prosa transversalmente:** estabilizar vocabulário, tempos verbais, transições e remissões; reduzir repetições. Usar passado para o que foi realizado, presente para conceitos e interpretação, e condicional para hipóteses futuras.
5. **Reescrever resumo e conclusões por último:** refletir o alcance final, incluir resultados quantitativos representativos e evitar dizer que papéis de LLM com métricas diferentes foram comparados numa única escala de “melhor desempenho”.
6. **Conferir a montagem:** retirar bastidores do corpo, resolver legendas e remissões, completar siglas efetivamente usadas e verificar a apresentação das tabelas e referências no documento final.

O parecer pode ser considerado atendido quando o leitor conseguir identificar, sem abrir o repositório: quais perguntas foram respondidas; o que foi medido e em qual população; contra qual referência; o que os resultados permitem concluir; e o que permanece hipótese. O manuscrito deve explicar o valor dos resultados negativos sem convertê-los em ausência universal de relação entre características e desempenho.

**Prioridade prática:** começar pelos capítulos 5 e 6 e pelas correções de alcance na introdução e nas conclusões. O material existente permite uma revisão substancial sem novos experimentos. Comparações estatísticas adicionais podem ser consideradas se o autor quiser sustentar alegações mais específicas, especialmente o ganho incremental de Q2.
