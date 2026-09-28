---
titulo: "Modelos de linguagem no mapa das técnicas"
status: revisado-por-ia
data: 2026-09-28
fonte: llm/relatorio-fase4.md; registros EXP-14 a EXP-18 e EXP-23
---

# Modelos de linguagem no mapa das técnicas

Este capítulo responde à Q3: onde os modelos de linguagem de grande porte (LLMs) entram no mapa proposto — como planejadores, tradutores de domínio ou seletores? Um mesmo modelo pode recomendar um planejador, produzir uma sequência de ações ou gerar uma especificação PDDL. Essas atividades têm objetos, referências e critérios diferentes; reuni-las sob o rótulo “LLM em planejamento” ocultaria qual componente produziu cada resultado.

Quatro modelos foram avaliados via OpenRouter: Claude Sonnet 5, GPT-6 Sol, Gemini 3.1 Pro e DeepSeek V4 Pro. As chamadas usaram raciocínio em nível *medium*, limite de 16.000 *tokens* e uma repetição por par modelo × domínio ou instância. A temperatura permaneceu no padrão do provedor porque nem todos os modelos aceitavam ajuste com raciocínio ativado. <!-- fonte: llm/relatorio-fase4.md, seção 1; EXP-14 a EXP-18; EXP-23 --> Os resultados descrevem versões e parâmetros de setembro de 2026; não constituem propriedade permanente das famílias de modelos.

## Desenho das quatro avaliações

| Papel | Entrada principal | Unidade e escala | Critério de resultado | Referência ou controle |
|---|---|---|---|---|
| Seletor (X3) | PDDL, instância p01 e catálogo de 29 planejadores | 41 domínios × 4 modelos, com e sem nomes | Perda de cobertura da escolha | SBS e seletor por características do capítulo 5 |
| Gerador de plano (X1) | Domínio e problema PDDL | p01 de 8 domínios × 4 modelos | Plano aceito pelo VAL | `lama-first`; nomes originais × ofuscados |
| Gerador com verificador (X4) | PDDL e retorno do VAL após falha | p05 de 4 domínios × 4 modelos | Plano válido após até duas correções | Primeira tentativa do mesmo ciclo; `lama-first` para comprimento |
| Tradutor (X2) | Descrição natural e problema p01 em PDDL | 6 domínios × 4 modelos | Sintaxe e verificação cruzada em p01–p05 | Domínio de referência do LLM+P |

: Papéis dos LLMs e desenhos de avaliação

::: fonte
Fonte: Autor, a partir dos EXP-14 a EXP-18 e EXP-23.
:::

As medidas não formam um placar único. Um plano válido, uma escolha com pouca perda e um domínio PDDL aceito pelo tradutor respondem a perguntas diferentes. A posição taxonômica decorre da função do modelo no sistema, e não de comparar diretamente essas medidas.

### Registro de custo

Os registros anteriores ao EXP-23 informam uso acumulado de US$ 10,51 na chave do provedor. As chamadas do EXP-23 somam US$ 2,04, mas o mesmo registro informa que o uso da chave passou de US$ 10,51 para US$ 12,49. A soma aritmética dos dois valores é US$ 12,55, diferença de US$ 0,06 em relação ao painel. <!-- fonte: llm/relatorio-fase4.md, seção 1; EXP-23 --> Como a causa não foi reconciliada nos registros — por exemplo, arredondamento, crédito ou ajuste do provedor —, os valores são mantidos como medidas distintas: custo somado das chamadas e uso acumulado exibido pelo provedor.

## LLM como seletor de planejador

No X3, cada modelo recebeu o PDDL do domínio, a instância p01 e um catálogo dos 29 planejadores do Nível 4 descritos pela taxonomia em quatro dimensões. Três entradas extensas foram truncadas. O catálogo anônimo contém 21 descrições distintas: quando vários planejadores compartilham a mesma descrição, a regra principal do protocolo pontua a resposta pela cobertura média do grupo. Essa regra explica as perdas fracionárias. Uma segunda pontuação exige a identidade exata do planejador e permite comparar a condição anônima com a condição que revela nomes e edições. <!-- fonte: EXP-14; EXP-15 -->

| Modelo | Anônimo: perda por grupo | p Holm | Anônimo: perda exata | p Holm | Com nomes: perda exata | p Holm |
|---|---:|---:|---:|---:|---:|---:|
| Claude Sonnet 5 | 259,00 | 0,0073 | 218,00 | 0,1970 | 313,00 | 0,0001 |
| GPT-6 Sol | 146,00 | 0,1797 | 146,00 | 0,1970 | 185,00 | 0,0354 |
| Gemini 3.1 Pro | 253,67 | 0,0019 | 241,00 | 0,0164 | 183,00 | 0,1121 |
| DeepSeek V4 Pro | 188,46 | 0,0224 | 172,79 | 0,1970 | 187,00 | 0,1072 |
| SBS | 143,00 | — | 143,00 | — | 143,00 | — |

: Perda dos seletores LLM sob as duas regras de pontuação

::: fonte
Fonte: Autor, a partir dos EXP-14 e EXP-15 e de `experimentos/analise/correcao-multipla/holm.csv`.
:::

Na regra principal por grupo, o GPT-6 Sol perde 146 instâncias, contra 143 do SBS; o teste não detecta diferença significativa, com p ajustado de 0,1797. Essa ausência de diferença não demonstra equivalência. Os outros três modelos ficam significativamente piores após Holm. Na regra por identidade exata, somente o Gemini fica significativamente pior na condição anônima. <!-- fonte: EXP-14; experimentos/analise/correcao-multipla/holm.csv --> A conclusão sobre quais modelos são piores depende, portanto, de uma decisão legítima do protocolo: pontuar a técnica descrita ou o planejador exato.

Com nomes visíveis, as escolhas se concentram em opções conhecidas: o Sonnet escolhe LAMA-2011 em 40 dos 41 domínios, e o Gemini escolhe FDSS23 em 40. <!-- fonte: EXP-15 --> Na condição anônima, 148 das 163 respostas válidas apontam para um portfólio. Nos quatro domínios em que uma técnica antiga se destaca — System R em Blocks World e TPP, SAT em Floortile e ANS em Pipesworld sem tanques — nenhum modelo escolhe o vencedor ou sua técnica. <!-- fonte: EXP-14 -->

Os padrões são compatíveis com regras pouco condicionadas ao domínio: favorecer a descrição mais abrangente no catálogo anônimo ou um nome saliente no catálogo nominal. Essa interpretação é hipótese, não mecanismo demonstrado. O truncamento de três entradas, a granularidade da taxonomia e as descrições idênticas também limitam o sinal que o seletor poderia usar. O resultado sustentado é mais restrito: nenhum modelo demonstrou superar o SBS, e as escolhas não capturaram os casos conhecidos de especialização.

## LLM como gerador de planos

O X1 pediu um plano para a instância p01 de oito domínios. O VAL aceitou 28 das 32 respostas. Duas falhas eram de formato, uma violava uma pré-condição e uma consumiu o limite de *tokens* sem apresentar plano. <!-- fonte: EXP-16 --> Os planos válidos tinham, em geral, comprimento igual ou menor que os de `lama-first`; no Blocks World, os quatro modelos produziram 28 passos, contra 36 dessa configuração do LAMA. <!-- fonte: EXP-16 --> Essa comparação não mede otimização: `lama-first` para no primeiro plano e não é a melhor referência em todos os domínios.

### Familiaridade lexical

O EXP-23 repetiu os mesmos 32 pares depois de trocar nomes de tipos, predicados, ações e objetos por rótulos sem significado. A validade caiu de 28 para 20 planos. Nenhum par inválido com nomes originais tornou-se válido após a ofuscação. Das oito perdas, cinco respostas esgotaram 16.000 *tokens* sem apresentar plano e três produziram planos incorretos. <!-- fonte: EXP-23 -->

| Condição | Planos válidos | Falhas observadas |
|---|---:|---|
| Nomes originais | 28 de 32 | 2 de formato, 1 de pré-condição, 1 por limite de *tokens* |
| Nomes ofuscados | 20 de 32 | 5 perdas adicionais por limite de *tokens* e 3 por plano incorreto |

: Efeito da ofuscação sobre a geração de planos

::: fonte
Fonte: Autor, a partir dos EXP-16 e EXP-23.
:::

A ofuscação interfere tanto na correção quanto no orçamento de raciocínio. O resultado não permite separar familiaridade com exemplos vistos no treinamento de uma contribuição semântica dos nomes durante a resolução. Também não autoriza afirmar que mais *tokens* recuperariam todas as falhas: cinco respostas foram interrompidas pelo limite, mas o plano que produziriam permanece desconhecido.

## Geração com retorno do verificador

O X4 avaliou a p05 de quatro domínios em que técnicas antigas se destacam. Na primeira tentativa, 8 de 16 planos eram válidos. Depois de uma ou duas rodadas em que a mensagem do VAL foi devolvida ao modelo, o ciclo terminou com 13 planos válidos em 16. As três conversas restantes atingiram o limite de *tokens* sem apresentar plano final. <!-- fonte: EXP-17 -->

| Estágio do ciclo | Planos válidos | Proporção |
|---|---:|---:|
| Primeira tentativa | 8 | 50,0% |
| Depois do retorno do VAL | 13 | 81,3% |

: Planos válidos antes e depois das correções orientadas pelo VAL

::: fonte
Fonte: Autor, a partir do EXP-17.
:::

O resultado demonstra o desempenho do **ciclo observado**, que combina nova tentativa, informação do verificador e orçamento adicional. O experimento não inclui uma condição equivalente de novas tentativas sem mensagem do VAL; por isso, não isola causalmente quanto do acréscimo vem da informação do verificador. Ele mostra que mensagens formais de erro foram suficientes para que cinco conversas antes inválidas chegassem a planos aceitos.

Nos exemplos válidos, os planos também foram menores que os do `lama-first`: de 86 a 90 passos contra 160 em Blocks World e de 73 a 75 contra 106 no TPP. No Floortile p05, GPT-6 Sol e Gemini produziram planos de 206 e 204 passos, enquanto `lama-first` não encontrou plano em 300 segundos. <!-- fonte: EXP-17 --> Planejadores baseados em SAT, que vencem Floortile no Nível 4, não foram executados nessa instância; o caso não estabelece superioridade sobre o estado da arte do domínio.

## LLM como tradutor de domínio

O X2 forneceu a cada modelo uma descrição em linguagem natural e o problema p01 em PDDL, para preservar os nomes de tipos, predicados e constantes. Foram avaliados seis domínios do LLM+P e quatro modelos, totalizando 24 domínios gerados. <!-- fonte: EXP-18 --> O tradutor do Fast Downward aceitou 23 deles nos problemas avaliados, mas validade sintática não estabelece equivalência com o domínio de referência.

A comparação automática de solidez e completude exige ações com mesmos nomes, número de parâmetros, tipos e ordem. Apenas 10 dos 24 pares atendem a essa condição. Neles, planos produzidos por um domínio foram verificados no outro nos problemas p01 a p05, quando mensuráveis.

| Resultado da avaliação | Pares | Interpretação |
|---|---:|---|
| Sintaxe aceita | 23 de 24 | O domínio pode ser processado pelo tradutor |
| Assinatura compatível com a referência | 10 de 24 | Permite a verificação cruzada automática adotada |
| Passa nas verificações cruzadas | 6 de 10 | Evidência de compatibilidade nos problemas avaliados |
| Erro real de pré-condição | 3 de 10 | Diferença semântica detectada pelos planos |
| Artefato do VAL | 1 de 10 | Tipo declarado e não usado, embora as ações coincidam |

: Resultados da tradução de linguagem natural para PDDL

::: fonte
Fonte: Autor, a partir do EXP-18.
:::

Nos 14 pares com assinatura diferente, a correção semântica permanece desconhecida. Três usam nomes de ação diferentes, dois mudam o número de parâmetros e nove alteram ordem ou tipos. <!-- fonte: EXP-18 --> Parte pode ser erro; parte pode representar liberdade de modelagem, pois a descrição natural não determina essas convenções. Nos seis pares aprovados, a verificação por cinco problemas fornece evidência de compatibilidade, mas não prova equivalência semântica entre todos os estados possíveis.

O resultado liga Q3 a Q2. O tradutor não apenas converte uma descrição: toma decisões de representação que afetam o artefato recebido pelo planejador e as medidas que podem ser extraídas dele. Como no UML.P, avaliar o modelo exige distinguir propriedade da tarefa, convenção do modelador e limitação do instrumento de comparação.

## Posição dos LLMs na taxonomia

A taxonomia registra a função desempenhada no sistema, sem pretender reduzir o funcionamento interno do modelo a uma heurística clássica.

::: quadro
| Papel | D1: algoritmo e busca | D2: heurística | D3: representação | D4: arquitetura |
|---|---|---|---|---|
| LLM como gerador de plano | Geração de sequência por modelo de linguagem; busca interna não observada | Não classificada | PDDL tratado como texto | Planejador único |
| LLM com verificador | Igual ao anterior | Não classificada | Igual ao anterior | Ciclo de geração e teste com verificador formal |
| LLM como seletor | Não aplicável | Não aplicável | Não aplicável | Seletor de portfólio sem treino específico, a partir do domínio e do catálogo |
| LLM como tradutor | Etapa anterior ao planejamento | Não aplicável | Linguagem natural para PDDL | Fora do mapa de técnicas de busca |

: Posição funcional dos LLMs na taxonomia
:::

::: fonte
Fonte: Autor, a partir do relatório da Fase 4 e de `auditoria/taxonomia-tecnicas.md`, seção 6.1.
:::

O seletor ocupa função arquitetural comparável à de sistemas treinados como Delfi e IBaCoP [@katz2018delfi; @cenamor2016ibacop], mas esses sistemas não foram comparados diretamente nos experimentos. O tradutor fica fora do mapa de busca porque sua saída é a representação que um planejador posterior recebe. O ciclo com VAL acrescenta uma arquitetura verificável ao gerador, sem tornar o próprio modelo um verificador formal.

## Resposta a Q3 e alcance

Os LLMs ocupam três posições distintas. Como geradores de planos, produziram planos válidos na maioria das instâncias pequenas e médias avaliadas; o ciclo que incorpora mensagens do VAL chegou a 13 de 16 planos válidos. Como tradutores, produziram PDDL sintaticamente processável em 23 de 24 casos, mas só parte dos domínios pôde ser comparada semanticamente pelo procedimento adotado. Como seletores, nenhum demonstrou vantagem sobre o SBS nem identificou os domínios em que técnicas antigas vencem. <!-- fonte: EXP-14 a EXP-18; EXP-23 -->

A posição mais sustentada pelos experimentos é a de **gerador de planos integrado a uma arquitetura de verificação externa**. “Mais sustentada” não significa melhor que planejadores clássicos: X1 e X4 usam poucas instâncias, uma chamada por par, domínios conhecidos e uma referência clássica que não é a melhor em todos os casos. A ofuscação cobre somente X1; as datas de corte de treinamento não foram verificadas; e não há teste de escala para problemas maiores. O principal resultado metodológico é separar geração, verificação, seleção e modelagem, atribuindo a cada componente apenas a evidência que seu desenho permite.
