---
titulo: "Modelos de linguagem no mapa das técnicas"
status: rascunho-de-ia
data: 2026-09-28
fonte: llm/relatorio-fase4.md; registros EXP-14 a EXP-18 e EXP-23
---

# Modelos de linguagem no mapa das técnicas

Este capítulo responde à Q3: onde os modelos de linguagem de grande porte (LLMs) entram no mapa proposto — como planejadores, tradutores de domínio ou seletores? A resposta exige separar esses papéis. Um mesmo modelo pode ler uma descrição e recomendar um planejador, produzir uma sequência de ações em PDDL ou gerar um domínio formal a partir de linguagem natural; os desenhos, as medidas e os riscos de cada atividade são diferentes.

Quatro modelos foram avaliados via OpenRouter — Claude Sonnet 5, GPT-6 Sol, Gemini 3.1 Pro e DeepSeek V4 Pro — com raciocínio em nível *medium* e limite de 16.000 *tokens* por resposta. Os experimentos EXP-14 a EXP-18 consumiram US$ 10,51; o EXP-23, que testou nomes ofuscados, acrescentou US$ 2,04, totalizando US$ 12,49. <!-- fonte: llm/relatorio-fase4.md, seção 1 --> Os resultados são datados: eles descrevem versões e parâmetros usados em setembro de 2026, não uma propriedade permanente dos modelos.

## LLM como seletor de planejador

Nos 41 domínios do Nível 4, os modelos receberam o catálogo de planejadores descrito pela taxonomia em quatro dimensões e tiveram de escolher uma opção para cada domínio. Sem nomes de planejadores, o GPT-6 Sol empata estatisticamente com o melhor planejador único, com perda de 146 contra 143 e p = 0,18. Os demais modelos têm perdas entre 188,5 e 259; depois da correção de Holm para os quatro modelos, permanecem piores que a referência. <!-- fonte: EXP-14; experimentos/analise/correcao_multipla.py -->

O padrão de escolha é revelador: 148 das 163 respostas válidas selecionam um portfólio. Nos quatro domínios em que uma técnica antiga se destaca — System R em Blocks World e TPP, SAT em Floortile e ANS em Pipesworld sem tanques — nenhum modelo escolhe o vencedor ou a técnica correspondente. <!-- fonte: EXP-14 --> Com nome e edição da IPC visíveis, a escolha piora em três dos quatro modelos e se concentra em planejadores conhecidos: o Sonnet escolhe LAMA 2011 em 40 dos 41 domínios, e o Gemini escolhe FDSS23 em 40. <!-- fonte: EXP-15 -->

Esses resultados não demonstram que o modelo desconheça planejamento, mas não mostram que ele identifique ajuste entre domínio e técnica. Na amostra, a recomendação se comporta como uma regra fixa: selecionar a descrição mais abrangente quando o catálogo é anônimo ou o nome mais saliente quando ele é visível. Isso reproduz, com outro mecanismo, a limitação encontrada no capítulo 5: uma referência fixa forte é difícil de superar quando os sinais disponíveis não antecipam os poucos casos de especialização.

## LLM como planejador

O experimento X1 pediu aos modelos que gerassem planos a partir de PDDL. Nas instâncias p01 de oito domínios, 28 dos 32 planos foram validados pelo VAL. Duas falhas eram de formato, uma decorria de pré-condição não satisfeita e uma atingiu o limite de *tokens*. Em geral, os planos tinham o mesmo comprimento ou eram mais curtos que os do `lama-first`; em Blocks World, os quatro modelos produziram planos de 28 passos contra 36 do LAMA nessa configuração. <!-- fonte: EXP-16 --> O resultado não mede otimização: `lama-first` para no primeiro plano encontrado e não é a melhor referência em todos os domínios.

O X4 introduziu um verificador externo. Na instância p05 de quatro domínios de técnica antiga, oito dos 16 planos foram válidos na primeira tentativa e 13 dos 16 após uma ou duas rodadas em que o erro do VAL foi devolvido ao modelo. As três falhas remanescentes atingiram o limite de *tokens*, e não apresentaram um plano semanticamente incorreto. <!-- fonte: EXP-17 --> Os planos válidos também foram menores que os do `lama-first` em exemplos como Blocks World, de 86 a 90 passos contra 160, e TPP, de 73 a 75 contra 106. <!-- fonte: EXP-17 -->

No Floortile p05, GPT-6 Sol e Gemini encontraram planos válidos de 206 e 204 passos, enquanto o LAMA não encontrou plano em 300 segundos. Isso não estabelece superioridade no domínio: no Nível 4, planejadores baseados em SAT vencem Floortile, e eles não foram comparados nessa instância. <!-- fonte: EXP-17; EXP-12 --> O resultado sustenta apenas que, nessa amostra pequena, o ciclo de geração e verificação recuperou grande parte das falhas do primeiro intento.

O teste de ofuscação qualifica ainda mais a interpretação. Quando nomes de tipos, predicados, ações e objetos foram substituídos por rótulos sem significado, o número de planos válidos caiu de 28 para 20 em 32 pares; nenhum caso inválido tornou-se válido. Das oito perdas, cinco respostas consumiram os 16.000 *tokens* sem chegar a um plano e três produziram planos incorretos. <!-- fonte: EXP-23 --> Familiaridade lexical, portanto, interfere no resultado, sobretudo pelo custo de raciocínio. A queda é menor do que a relatada em avaliações anteriores de planejamento com LLMs [@valmeekam2023planbench], mas a comparação é apenas contextual: os desenhos e as instâncias não são os mesmos.

## LLM como tradutor de domínio

O experimento X2 tratou o LLM como tradutor de uma descrição em linguagem natural para PDDL, a partir de seis domínios do LLM+P [@liu2023llmp]. Dos 24 domínios gerados, 23 têm sintaxe válida. Sintaxe, porém, não equivale a modelo equivalente: apenas dez têm a mesma assinatura de ações da referência — nomes, número de parâmetros, tipos e ordem — e só neles a comparação automática é possível. Entre esses dez, seis são corretos, três têm erro real de pré-condição e um é um artefato do VAL. <!-- fonte: EXP-18 -->

Os dez casos comparáveis não são uma amostra aleatória; eles são justamente os que coincidiram com a referência em uma convenção formal. A taxa de equivalência nos outros 14 permanece desconhecida. Parte da diferença pode refletir erro e parte, liberdade de modelagem: a descrição não determina nomes, tipos ou a ordem dos parâmetros. Essa separação retoma uma lição do capítulo 5: algumas medidas atribuídas ao domínio dependem das escolhas de quem o representa. Como tradutor, o LLM produz uma proposta de modelo que exige validação contra requisitos, problemas conhecidos ou uma referência formal; ele não é, nesse papel, uma técnica de busca.

## Posição na taxonomia

A taxonomia em quatro dimensões é ampliada para acomodar os papéis observados. A ampliação não pretende reduzir o funcionamento interno dos modelos a uma heurística clássica; ela registra a função que desempenham no sistema avaliado.

::: quadro
| Papel | D1: algoritmo e busca | D2: heurística | D3: representação | D4: arquitetura |
|---|---|---|---|---|
| LLM como planejador | Geração de plano por modelo de linguagem, sem busca explícita observável | Não aplicável | PDDL tratado como texto | Planejador único |
| LLM com verificador | Igual ao anterior | Não aplicável | Igual ao anterior | Geração e teste por verificador formal externo |
| LLM como seletor | Não aplicável | Não aplicável | Não aplicável | Seletor de portfólio sem treino, a partir da descrição do domínio |
| LLM como tradutor | Etapa anterior ao planejamento | Não aplicável | Linguagem natural para PDDL | Fora do mapa de técnicas |

: Posição dos LLMs na taxonomia de técnicas
:::

::: fonte
Fonte: Autor, a partir do relatório da Fase 4 e de `auditoria/taxonomia-tecnicas.md`, seção 6.1.
:::

Os dois primeiros papéis introduzem valores novos nas dimensões de algoritmo e de representação; o terceiro ocupa a arquitetura de seleção, em posição comparável à de seletores treinados como Delfi e IBaCoP [@katz2018delfi; @cenamor2016ibacop], mas não foi comparado diretamente com esses sistemas. O tradutor fica fora do mapa porque sua saída é o próprio objeto que um planejador posterior recebe.

## Resposta a Q3 e limites

A resposta a Q3 é que os LLMs entram no mapa principalmente como técnica de planejamento quando geram planos e operam com verificação formal externa. Nesse papel, produzem planos válidos na maioria das instâncias pequenas e médias testadas, e o retorno do VAL corrige uma parte substancial das falhas. <!-- fonte: EXP-16; EXP-17 --> Como tradutores, são capazes de gerar PDDL sintaticamente válido, mas exigem validação semântica. Como seletores, não demonstram ganho sobre o melhor planejador único e não identificam os domínios em que técnicas antigas se destacam. <!-- fonte: EXP-14; EXP-15; EXP-18 -->

Essa conclusão é deliberadamente restrita. Houve uma chamada por par modelo × instância, sem repetição; X1, X4 e X2 usam poucas instâncias; parte dos domínios é amplamente conhecida; e somente o X1 recebeu a condição com nomes ofuscados. As datas de corte de treinamento não foram verificadas, e não há teste de escala para instâncias maiores. Os resultados, por isso, não permitem concluir que LLMs substituem planejadores clássicos, nem que o ganho observado permaneceria sob outro modelo, orçamento, domínio ou verificador.

O principal achado metodológico é mais modesto: separar geração, verificação, seleção e modelagem evita atribuir a um único rótulo — “LLM como planejador” — resultados que pertencem a componentes diferentes. O próximo capítulo usa essa separação para discutir, apenas como hipótese, a escolha de configurações de agentes no desenvolvimento de software.
