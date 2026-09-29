# Avaliação geral da dissertação após a revisão editorial

Data: 28/09/2026. Versão examinada: commit `bc9737d`, com o DOCX reconstruído nesta sessão. Natureza: auditoria transversal de coerência, argumentação, evidência, referências e prontidão editorial. Nenhuma alteração foi aplicada aos capítulos nesta avaliação.

## 1. Parecer geral

A dissertação está **cientificamente coerente e pronta para a revisão do autor**, mas ainda não para ser enviada como versão final. O parecer anterior foi atendido de forma substancial: os capítulos de resultados agora expõem populações, referências, perdas, p-valores e limites; os experimentos com LLMs foram separados por função; a resposta a Q2 deixou de alegar equivalência ou ausência de informação incremental; e a Ponte passou a formular uma aplicação possível em engenharia de software sem fingir que houve piloto.

O manuscrito tem agora uma tese identificável e sustentada: **heterogeneidade de desempenho é condição para seleção, não prova de que as características medidas permitam selecionar**. Essa tese atravessa a auditoria de 2010, os experimentos posteriores, a avaliação dos LLMs e a aplicação exploratória em software. O resultado negativo deixa de parecer ausência de descoberta e passa a funcionar como contribuição metodológica.

Não foram encontrados problemas críticos que invalidem método, dados ou conclusão central. Permanecem três ajustes de alta prioridade: precisar as respostas finais a Q3 e Q5 e definir como os artefatos de reprodutibilidade serão acessíveis ao leitor. Os demais achados são de fluidez, terminologia, apresentação e acabamento.

**Veredito:** aprovada com ajustes finais. Não há necessidade de novo experimento nem de nova busca bibliográfica para concluir a Fase 6.

## 2. O que melhorou

### Coerência científica

- A distinção entre reprodução, correção, reexecução e ampliação está clara e evita tratar resultados de populações diferentes como se fossem uma única replicação.
- Q1, Q2 e Q5 são respondidas em uma sequência lógica: heterogeneidade observada, capacidade preditiva e utilidade para seleção.
- Ausência de significância deixou de ser apresentada como equivalência. Ganhos numéricos localizados são preservados sem extrapolação.
- Métricas UML originais, aproximações extraídas de PDDL, *features* SAS+ e propriedades de topologia são tratadas como instrumentos distintos.

### Comunicação dos experimentos

- O capítulo 5 agora informa unidades, denominadores, SBS, VBS, perdas e correção de Holm em quantidade suficiente para que o leitor compreenda os resultados sem consultar primeiro os registros internos.
- O capítulo 6 separa seleção, geração de planos, ciclo com verificador e tradução para PDDL. As regras de pontuação do X3, o alcance da validação do X2 e a discrepância de custo estão explícitos.
- Os resultados positivos e intermediários reaparecem: reprodução do cálculo, reexecução, qualidade e tempo, sinal localizado de topologia, efeito da ofuscação e verificação cruzada dos domínios gerados.

### Aplicabilidade

- O capítulo 7 é uma contribuição legítima da versão revisada. Ele não transfere mecanicamente métricas de planejamento para software; transfere o problema decisório e seus critérios de validação.
- A decomposição em roteamento inicial, adaptação durante a execução e verificação antes da integração torna a aplicação concreta.
- As seis hipóteses são refutáveis e incluem unidade de observação, comparação, resultado esperado e condição de refutação.

### Rastreabilidade e montagem

- O verificador encontrou **114 chaves distintas**, todas presentes em `referencias.bib`, sem chave ausente ou pendente.
- O DOCX foi reconstruído com os 11 arquivos previstos. Sua estrutura contém 10 títulos de primeiro nível, 25 tabelas, 7 legendas de quadro, 17 legendas de tabela e 114 entradas bibliográficas.
- Não foram encontrados marcadores de citação não resolvida. Os quatro textos “Atualize o campo no Word (F9)” são os campos esperados de sumário e listas, não erros de referência.

## 3. Achados remanescentes

### A01 — Alta: Q3 mistura recortes experimentais distintos

**Local:** capítulo 8, resposta a Q3.

“Como planejadores, resolveram 8 de 16 tentativas sem retorno e 13 de 16 no ciclo com verificador externo” usa os dois estágios do X4, feito na p05 de quatro domínios. O X1, que é a avaliação geral de geração sem retorno, obteve 28 de 32 planos válidos na p01 de oito domínios. A formulação atual pode levar o leitor a interpretar 8/16 como o resultado geral dos LLMs como planejadores.

**Ajuste recomendado:** nomear o recorte: “No X1, produziram 28 de 32 planos válidos. Na amostra mais difícil do X4, a primeira tentativa resolveu 8 de 16 casos e o ciclo terminou com 13 de 16”. Manter a ressalva de que X4 não isola causalmente o efeito do verificador.

### A02 — Alta: Q5 ainda aproxima previsão de resolução e desempenho relativo

**Local:** capítulo 8, resposta a Q5.

A frase “as 16 *features* SAS+ não explicam [...] o desempenho relativo de famílias” é seguida pelas AUCs dos modelos que predizem, separadamente, se uma família resolve a instância. Essa tarefa mede previsão de resolução e pode refletir dificuldade geral; o desempenho relativo só é diretamente examinado no mapa entre famílias e na seleção por instância.

**Ajuste recomendado:** conservar os três degraus já apresentados no capítulo 5 também na conclusão: as características antecipam a resolução de algumas famílias com sinal fraco e desigual; esse sinal não demonstrou capacidade robusta de discriminar a melhor alternativa; e os seletores não superaram o SBS.

### A03 — Alta para o envio: o suplemento reprodutível não tem forma de acesso definida

**Local:** apêndices A a C e contribuição “Corpus e protocolo reprodutíveis”.

Os apêndices apontam para caminhos internos do repositório, mas não informam URL, versão, DOI, arquivo suplementar ou condição de acesso. Como o repositório é privado, um leitor que receba apenas o DOCX não consegue consultar codificações, registros ou *scripts*. Isso não enfraquece os resultados descritos no corpo, mas limita a alegação de reprodutibilidade e o compartilhamento com o orientador.

**Ajuste recomendado:** antes do M3, escolher uma das alternativas: compartilhar acesso ao repositório; criar uma versão pública ou pacote suplementar congelado; ou incluir no documento as tabelas essenciais e qualificar a disponibilidade do restante. Registrar o identificador do commit ou da versão distribuída.

### A04 — Média: uma frase do X4 ainda sugere suficiência causal

**Local:** capítulo 6, seção “Geração com retorno do verificador”.

Depois de afirmar corretamente que o desenho não isola o efeito do VAL, o texto diz que as mensagens “foram suficientes” para cinco conversas chegarem a planos aceitos. A expressão volta a aproximar condição observada e causa.

**Ajuste recomendado:** “No ciclo observado, cinco conversas antes inválidas chegaram a planos aceitos depois de receber mensagens formais de erro”.

### A05 — Média: estabilizar “apoiado” versus “dirigido por IA”

**Local:** título e conclusão do capítulo 7; Q4 usa “apoiado por IA”.

“Dirigido por IA” sugere um grau maior de autonomia e pode parecer mudança de objeto. O texto efetivamente cobre agentes, ferramentas, verificadores e supervisão humana, mais próximo de “desenvolvimento de software apoiado por IA”.

**Ajuste recomendado:** adotar um termo canônico e, se “dirigido” for mantido, defini-lo na primeira ocorrência.

### A06 — Média: o capítulo 2 continua denso e parcialmente redundante

Com cerca de 6,2 mil palavras, a fundamentação é quase duas vezes maior que o capítulo de resultados. A seção final antecipa em detalhe conclusões que retornam nos capítulos 3, 5, 6 e 7. O conteúdo é pertinente, mas o ritmo perde força antes de chegar à contribuição empírica.

**Ajuste recomendado:** numa revisão de concisão, reduzir enumerações de sistemas e preservar apenas a função de cada bloco na argumentação; encurtar “O que esta revisão reposiciona” para uma transição, sem repetir respostas completas.

### A07 — Média: falta uma visão visual do desenho e dos resultados centrais

As tabelas corrigiram a falta de substância do primeiro rascunho, mas a dissertação ainda depende quase inteiramente de prosa e tabelas. Um único diagrama do desenho em camadas e um gráfico de perdas — VBS, SBS e seletores — reduziriam a carga cognitiva. Um esquema dos três estágios da Ponte também ajudaria a comunicar a aplicação.

**Ajuste recomendado:** tratar esses elementos como melhoria de comunicação, não como requisito científico. Não acrescentar gráficos que apenas repitam tabelas nem intervalos não calculados.

### A08 — Baixa: duas formulações ainda são mais fortes que a evidência

- A introdução chama a premissa de 2010 de “fundamento da seleção de algoritmos”. O fundamento do campo é formular a relação entre problema, características e desempenho; não é presumir que as características escolhidas predigam o vencedor.
- O método afirma que um seletor que não supera o SBS “não acrescenta nada”. Mais precisamente, ele não demonstra ganho para a decisão e a função objetivo avaliadas.

Esses ajustes reforçam a postura epistêmica já predominante no restante do texto.

### A09 — Acabamento obrigatório antes do M3

O DOCX precisa ser aberto no Word para atualizar os quatro campos, conferir quebras de página, continuidade de tabelas, listas, paginação e referências. Também permanecem decisões humanas sobre título definitivo, natureza do documento, ficha catalográfica e eventual folha de aprovação. A declaração de uso de IA só deve ser dada como definitiva depois da revisão do autor.

## 4. Avaliação por dimensão

| Dimensão | Avaliação | Comentário |
|---|---|---|
| Pergunta e contribuição | Muito boa | A contribuição central é clara, relevante e não depende de um resultado positivo de seleção. |
| Coerência entre perguntas, método e conclusões | Boa, com dois ajustes | A01 e A02 devem ser corrigidos porque aparecem nas respostas finais. |
| Rigor metodológico | Muito bom | Desenhos, unidades, referências e limites estão explícitos; não se exige nova coleta. |
| Apresentação dos resultados | Boa a muito boa | Evoluiu substancialmente; uma síntese visual ainda ajudaria. |
| Revisão de literatura | Muito boa | Ampla, atualizada e integrada; o principal ganho possível é concisão. |
| Ponte com engenharia de software | Muito boa no escopo exploratório | Concreta, testável e cautelosa; não promete aplicabilidade já demonstrada. |
| Referências e proveniência | Muito boa internamente | Todas as citações são válidas; falta definir acesso externo aos artefatos. |
| Clareza e fluidez | Boa | A estrutura funciona; o capítulo 2 concentra a maior densidade e repetição. |
| Prontidão formal | Parcial | Estrutura do DOCX passou; inspeção visual e elementos institucionais permanecem. |

## 5. Ordem de fechamento

1. Corrigir A01, A02 e A04 nas conclusões e no capítulo 6.
2. Decidir o acesso ao suplemento reprodutível e ajustar os apêndices.
3. Uniformizar a terminologia de software com IA e fazer uma revisão curta de concisão no capítulo 2.
4. Se houver tempo, acrescentar no máximo duas ou três peças visuais com função explicativa clara.
5. Realizar a revisão autoral e visual no Word; atualizar campos e elementos institucionais.
6. Reconstruir o DOCX, repetir a checagem de citações e fazer a conferência final antes do M3.

Com esses ajustes, a dissertação estará em condição de ser compartilhada com o orientador como uma revisão madura do trabalho de 2010. O ganho principal da versão atual não é apenas corrigir o passado: é transformar um resultado inicialmente afirmativo e frágil em uma investigação mais rigorosa sobre quando uma decisão adaptativa realmente acrescenta valor.

## 6. Estado de implementação em 29/09/2026

Os ajustes de conteúdo e comunicação deste parecer foram aplicados ao manuscrito:

| Achado | Estado | Implementação |
|---|---|---|
| A01 | Concluído | A resposta a Q3 separa o X1 — 28 de 32 planos válidos, ou 20 de 32 com nomes ofuscados — do X4 na p05 — 8 de 16 na primeira tentativa e 13 de 16 ao final do ciclo — e preserva a limitação causal. |
| A02 | Concluído | A resposta a Q5 distingue previsão de resolução por família, discriminação da melhor alternativa e utilidade do seletor contra o SBS. |
| A03 | Concluído para esta versão | Os apêndices informam URL, caráter privado, condição de acesso, versão de referência (`bc9737d`) e limites do material versionado. Antes do M3, o autor ainda precisa conceder acesso ou anexar um pacote congelado. |
| A04 | Concluído | O texto do X4 descreve a sequência observada sem atribuir causalidade suficiente às mensagens do VAL. |
| A05 | Concluído | “Desenvolvimento de software apoiado por IA” foi adotado como termo canônico no manuscrito e nos documentos vivos do projeto. |
| A06 | Concluído | O capítulo 2 foi reduzido de cerca de 6,2 mil para 5,1 mil palavras, e sua seção final passou a funcionar como transição para a parte empírica. |
| A07 | Concluído | Foram acrescentados um diagrama do desenho em camadas, um gráfico das perdas do Nível 4 e um esquema da política em três estágios. |
| A08 | Concluído | As formulações da introdução e do método foram calibradas para não presumir capacidade preditiva nem equiparar ausência de ganho a ausência absoluta de informação. |
| A09 | Parcial, depende do autor | O DOCX foi reconstruído e aberto no Pages para inspeção inicial. Permanecem a atualização dos quatro campos e a conferência final no Word, além de título, natureza do documento, ficha catalográfica, folha de aprovação e validação autoral da declaração de IA. O Pages informou fontes não instaladas; o ambiente não dispõe de Word nem LibreOffice. |

As checagens automatizadas posteriores à aplicação constam no registro da sessão e no plano. O estado “concluído” acima se refere ao ajuste editorial; não substitui a revisão autoral e institucional requerida antes do M3.
