---
titulo: "Conclusões e próximos passos"
status: rascunho-de-ia
data: 2026-09-28
fonte: experimentos/relatorio-fase3.md; llm/relatorio-fase4.md; experimentos/relatorio-fase4b.md; ponte-software/relatorio/sintese-exploratoria.md
---

# Conclusões e próximos passos

Esta dissertação reexaminou a relação entre características de domínios de planejamento e técnicas de solução proposta em 2010. A revisão preservou a pergunta que motivou o trabalho — em que condições o problema ajuda a escolher uma estratégia de solução —, mas submeteu sua resposta original a auditoria documental, reprodução por *scripts*, reexecução sob condição única, ampliação de dados, experimentos com modelos de linguagem e uma ponte exploratória para engenharia de software.

O resultado não é a confirmação de um seletor baseado em métricas UML. É uma delimitação mais forte da pergunta: há heterogeneidade entre problemas e técnicas, mas demonstrar heterogeneidade não basta para construir uma recomendação. Um seletor precisa acrescentar informação a uma referência fixa forte, generalizar para problemas não observados e justificar seu custo e seus efeitos sobre mais de uma medida de resultado.

## Respostas às perguntas de pesquisa

**Q1 — Replicação.** As conclusões de 2010 não se sustentam como método de seleção. O procedimento é amplamente reproduzível a partir das tabelas publicadas, mas a discretização aplicada difere da regra escrita e duas taxonomias de técnicas foram usadas no mesmo cálculo. <!-- fonte: EXP-03 --> A validação original não supera uma linha de base sem características; em Storage, a linha de base tem perda menor, e Zeno-travel e Elevator são dominados por empates. <!-- fonte: EXP-09 --> Na ampliação para 41 domínios e 29 planejadores, nenhum seletor testado supera o melhor planejador único. <!-- fonte: EXP-12; EXP-13 --> A pergunta continua pertinente; a regra de recomendação, não.

**Q2 — Continuidade das métricas.** As métricas UML que podem ser extraídas do PDDL não acrescentam poder preditivo às *features* SAS+, e estas também não acrescentam às métricas UML para escolher planejadores por domínio. Das 17 métricas originais, apenas 11 têm correspondente especificável no PDDL; parte das demais depende de decisões de modelagem. <!-- fonte: EXP-07; EXP-08 --> Na ampliação, a combinação dos conjuntos não supera o melhor planejador único. <!-- fonte: EXP-11; EXP-12 --> A conclusão é limitada ao problema de seleção e às amostras avaliadas; não afirma que métricas de modelagem sejam inúteis para outros fins.

**Q3 — Modelos de linguagem.** Os LLMs ocupam três posições distintas. Como planejadores, obtêm planos válidos na maioria das instâncias pequenas e médias testadas, sobretudo quando recebem retorno de um verificador formal externo. Como tradutores, geram PDDL sintaticamente válido com frequência, mas equivalência semântica permanece difícil de estabelecer. Como seletores, não superam o melhor planejador único e não identificam os domínios em que técnicas antigas se destacam. <!-- fonte: EXP-14 a EXP-18; EXP-23 --> A posição mais defensável no mapa é a de técnica de planejamento integrada a verificação externa, não a de seletor confiável.

**Q4 — Ponte para desenvolvimento de software.** A conexão é exploratória e metodológica. Estudos de agentes de software mostram que desempenho varia com tarefa e contexto [@rondon2025evaluating; @takerngsaksiri2025humanintheloop], e roteadores mostram que seleção condicional pode ser útil em distribuições avaliadas [@ong2024routellm; @chen2023frugalgpt]. A revisão, porém, não autoriza reutilizar métricas estruturais como seletor pronto. A contribuição aplicável é formular a escolha de configuração de agente como hipótese mensurável, comparada a uma configuração fixa forte, com validação fora do repositório ou período observado e objetivos que incluam qualidade, segurança, custo e retrabalho.

**Q5 — IPCs posteriores a 2010.** Nas IPCs de 2011 e 2018, as 16 *features* SAS+ não explicam de maneira robusta, fora do domínio, o desempenho relativo de famílias de técnica. A regressão logística tem AUC mediana de 0,59, contra 0,58 de um modelo apenas com tamanho; a árvore rasa tem mediana de 0,49. <!-- fonte: EXP-21 --> Propriedades de topologia acrescentam um sinal pequeno e desigual, vindo sobretudo de sondagem heurística, e não tornam a seleção superior ao melhor planejador único. <!-- fonte: EXP-25 --> A escolha por instância também não vence a referência fixa quando todos os planejadores estão disponíveis. <!-- fonte: EXP-24 -->

## Contribuições

As contribuições desta revisão são cinco.

1. **Auditoria rastreável da dissertação de 2010.** Foram extraídas 349 afirmações substantivas, classificadas quanto ao que se mantém, se reformula ou se descarta, e verificadas contra fontes primárias e dados do acervo. A auditoria corrige a leitura de resultados, taxonomia e origem de parte dos dados.
2. **Replicação em camadas.** O método original foi reproduzido e então submetido a correções, reexecução homogênea e ampliação de amostra. Essa sequência permite separar a fidelidade às tabelas publicadas da validade da recomendação.
3. **Taxonomia de técnicas em quatro dimensões.** Busca, heurística, representação e arquitetura substituem uma lista de rótulos sobrepostos; a taxonomia explicita portfólios, técnicas posteriores a 2010 e os papéis dos LLMs.
4. **Avaliação contemporânea com dados de competição.** A análise integra medidas extraídas de PDDL, *features* SAS+, topologia de busca e resultados por instância das IPCs, sempre distinguindo famílias, planejadores e portfólios.
5. **Ponte crítica para software com IA.** O capítulo 7 transforma o resultado negativo de seleção em salvaguardas e hipóteses falsificáveis para investigar roteamento e escalonamento de agentes, sem prometer aplicação comprovada.

## Limitações

As limitações delimitam o alcance das conclusões. A validação original tinha apenas três domínios; os domínios de validação não foram reexecutados. O Nível 4 usa cobertura por domínio, e os dados das IPCs posteriores diferem em *hardware*, limites e métricas, razão pela qual as comparações foram mantidas dentro de cada edição e trilha. Algumas famílias de técnica possuem poucos planejadores, confundindo efeito de técnica e de implementação. A análise de topologia cobre apenas duas edições com resultados acessíveis por instância e usa amostragem limitada sob hFF. <!-- fonte: experimentos/relatorio-fase3.md, seção 7; experimentos/relatorio-fase4b.md, seção 7 -->

Os experimentos com LLMs têm amostras pequenas, uma chamada por par modelo × instância e domínios conhecidos, além de limites explícitos de *tokens*. Eles não medem variabilidade entre repetições, generalização para tarefas maiores ou desempenho de versões futuras dos modelos. <!-- fonte: llm/relatorio-fase4.md, seção 7 --> A ponte para engenharia de software não inclui piloto, coleta de dados organizacionais ou teste de política de roteamento; todas as suas hipóteses requerem investigação própria.

## Próximos passos

Há três direções de trabalho futuro. A primeira é metodológica: criar cenários de seleção que preservem grupos inteiros de domínio, repositório ou período para teste, comparem com melhor escolha fixa e *virtual best* e controlem comparações múltiplas. A segunda é empírica: testar se sinais estáticos, histórico de desempenho e sinais produzidos durante exploração curta acrescentam informação de forma incremental. A terceira é sociotécnica: medir, ao lado de correção e custo, revisão humana, segurança, manutenção e confiança da equipe.

Em planejamento, esses passos podem ampliar a análise para outras competições à medida que dados por instância se tornem acessíveis, repetir os testes com outras medidas de desempenho e investigar a interação entre portfólios e seleção. Em engenharia de software, qualquer estudo deve congelar versões de modelo e configuração, registrar tarefas e resultados por unidade, separar avaliação de exploração e definir antecipadamente a função objetivo. Uma política que pareça melhorar a taxa de resolução, mas aumente retrabalho ou reduza segurança, não deve ser considerada melhor sem tornar esse compromisso explícito.

## Encerramento

O trabalho de 2010 captou uma pergunta duradoura, mas respondeu a ela com uma amostra pequena, métricas parcialmente dependentes de modelagem e uma validação que não separava recomendação de desempenho geral. A revisão mostra que a pergunta sobre ajuste entre problema e técnica sobrevive; a inferência de que características estruturais simples permitem escolher a solução não.

Essa distinção é o resultado central da dissertação revisada. Ela preserva uma contribuição histórica do estudo original e, ao mesmo tempo, estabelece uma regra de prudência para sua aplicação contemporânea: antes de criar uma política de seleção, é preciso demonstrar que há heterogeneidade, que o sinal é incremental, que a política supera uma referência fixa e que o ganho não é obtido às custas de resultados que importam. 
