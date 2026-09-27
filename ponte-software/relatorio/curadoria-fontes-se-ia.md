---
tipo: curadoria-de-fontes
fase: 5
data: 2026-09-27
status: duas-fontes-promovidas-demais-candidatas
---

# Curadoria dirigida — engenharia de software com IA, roteamento e orquestração

## Propósito e regra de uso

Esta curadoria amplia a Ponte com fontes mais próximas da decisão de configurar e escalar agentes em tarefas de software. Ela não altera ainda a base argumentativa citável do Capítulo 7: as obras marcadas como candidatas estão em `candidatas.bib`, foram verificadas no registro primário, mas só entram em `referencias.bib` depois da aprovação do autor em `literatura/referencias/revisao-referencias.md`.

O ganho não é simplesmente adicionar referências. É separar três perguntas que a formulação inicial da ponte ainda reunia em uma só:

1. **Triagem:** vale acionar um agente custoso para esta tarefa?
2. **Escalonamento:** depois de observar sinais iniciais, deve-se continuar, trocar ou intensificar a configuração?
3. **Orquestração:** como combinar agentes, verificadores, memória e resolução de desacordo sem tratar o agente como uma caixa-preta isolada?

Esse desdobramento torna mais precisa a conexão com a dissertação. Características do domínio não precisam escolher diretamente um “melhor agente”; elas podem informar uma política em etapas, que decide se a tarefa merece exploração, qual configuração recebe orçamento e quando a evidência é suficiente para interromper ou escalar.

## Pergunta e busca dirigida

**Pergunta.** Que evidência recente, diretamente ligada à engenharia de software apoiada por IA, sustenta ou limita a formulação da escolha de configuração de agente como seleção condicional?

**Data e fontes consultadas:** 27/09/2026; páginas primárias do arXiv, IEEE Xplore e ScienceDirect. Strings de descoberta: `software engineering agents routing task LLM`; `agent routing coding tasks`; `adaptive orchestration multi-agent software engineering LLM evaluation`; `software engineering LLM agent task classification routing`.

## Matriz de evidências

| Fonte | Tipo e proximidade | O que de fato examina | Uso potencial na dissertação | Limite que não pode ser ocultado | Situação |
|---|---|---|---|---|---|
| Fan, Yin e Chen (2026), *DepFixRouter* | Evidência direta; preprint | Roteia *pull requests* de atualização de dependência antes de chamar diagnóstico/reparo. Com 497 casos rotulados e piloto de 60 casos, mede chamadas e *tokens*. | Sustenta a noção de **triagem pré-agente**: uma política pode economizar recursos sem tentar resolver toda tarefa com o mesmo agente. | Recorte estreito (dependências); mede diagnóstico, não qualidade final do *patch*; preprint muito recente. | Candidata `fan2026dependencyrouter` — prioridade A |
| Son et al. (2026), *SWE-Router* | Evidência direta; preprint/workshop | Executa alguns turnos baratos, usa a trajetória parcial e só então continua ou escala. | Sustenta a distinção entre *features* estáticas e **sinais de execução**. É o contraponto mais claro à hipótese de que métricas estruturais bastariam. | Resultado descrito no preprint; não demonstra benefício em uma organização real. | **Promovida** `son2026swerouter` — evidência de fronteira |
| Zhou et al. (2026), *Agent-as-a-Router* | Evidência direta; relatório técnico vivo | Formula roteamento de tarefas de programação como ciclo contexto–ação–feedback e avalia arrependimento acumulado em *benchmark* de cerca de 10 mil tarefas. | Dá vocabulário para **memória de desempenho** e para avaliação sequencial, não só acurácia de um classificador. | Relatório vivo, não revisão por pares; o *benchmark* não equivale a fluxo de trabalho humano. | Candidata existente `zhou2026agentasarouter` — prioridade A |
| Chen et al. (2026), *Risa* | Evidência direta, mas de outro nível; preprint | Usa traços de roteamento de MoE para diversificar trajetórias e arbitrar *patches* em SWE-bench Verified. | Mostra que sinais internos/da trajetória podem apoiar **exploração e compromisso**, além do texto da *issue*. | Não é roteamento entre configurações de agente; usa arquitetura MoE e *benchmark*. | Candidata `chen2026risa` — prioridade B |
| Madeyski (2026), *Triage* | Protocolo propositivo; preprint | Propõe usar saúde do código e metadados para encaminhar tarefas a níveis de modelo e define condições falsificáveis para que isso compense. | Útil como hipótese concorrente: métricas de qualidade podem ser candidatas a sinal, mas não presumidas como seletor pronto. | O próprio resumo apresenta protocolo/condições, não uma demonstração empírica concluída. | Candidata existente `madeyski2026triage` — prioridade B |
| Becattini, Verdecchia e Vicario (2025), *SALLMA* | Arquitetura de software; artigo de workshop revisado | Propõe camadas operacional (intenção e orquestração) e de conhecimento (metamodelos e configurações) para sistemas LLM multiagente. | Ajuda a converter a hipótese em arquitetura: separar decisão de roteamento, execução e memória/configuração. | Prova de conceito; não testa a seleção condicional para tarefas de programação. | **Promovida** `becattini2025sallma` — apoio arquitetural |
| Cheikh Tourad e Lachgar (2026), *Multi-LLM Prototype* | Infraestrutura adjacente; artigo em periódico | Decompõe pedidos, pontua modelos por critérios interpretáveis e trata desacordo por uma sequência explícita. | Referência de desenho para tornar a política auditável: critérios, conflitos e rastros de decisão. | Não é estudo de engenharia de software nem evidência de eficácia de roteamento de agentes de código. | Candidata `tourad2026multillm` — prioridade C |

## Conexões que a nova evidência torna mais fortes

### 1. Da seleção única à política sequencial

[HIPÓTESE] A formulação mais fiel à engenharia de software não é `tarefa → agente`, mas uma política com portas de decisão:

```text
tarefa + contexto estático
        │
        ├─ rotina / baixo risco ─────────────→ fluxo econômico + verificação
        │
        └─ sinal de complexidade ou risco ─→ exploração curta
                                                   │
                                      trajetória, testes, custo, incerteza
                                                   │
                              manter / escalar / pedir revisão / interromper
```

Esta é uma inferência da combinação das fontes, não um resultado da dissertação. Ela evita a promessa forte de que uma métrica inicial identifica, sozinha, o agente ideal. Também fornece uma ponte mais honesta com os resultados das Fases 3, 4 e 4B: se características estáticas têm pouco sinal fora de domínio, elas podem continuar úteis como *gate* inicial, mas precisam ser combinadas com evidência produzida durante a execução.

### 2. A unidade de decisão passa a ser configuração e estágio

O termo “agente” é granularidade insuficiente. Para uma mesma base de modelo, mudam ao menos ferramentas, permissões, orçamento de passos, estratégia de exploração, teste/verificador, memória, revisão humana e regra de parada. [HIPÓTESE] A unidade comparada deve ser uma configuração em determinado estágio da tarefa. Isso explica por que uma avaliação de “modelo A versus B” dificilmente basta para orientar o trabalho de engenharia.

### 3. Resultado aceitável é vetor, não taxa de sucesso

[HIPÓTESE] Uma política só deve ser considerada preferível se for comparada a uma configuração fixa forte em um vetor de resultado: correção verificada, segurança, custo, latência, retrabalho de revisão e efeito posterior no repositório. O caso de atualizações de dependência ilustra bem o ponto: reduzir chamadas de LLM é útil apenas se não deslocar custo ou risco para a revisão humana ou para produção.

### 4. O papel real das características de domínio

Em vez de assumir que acoplamento, cobertura ou saúde do código predizem diretamente o vencedor, a versão enriquecida da hipótese é:

> [HIPÓTESE] Características estáticas, contexto da tarefa e sinais parciais de execução podem ter papéis diferentes numa política de configuração de agentes: triagem, alocação inicial, gatilho de escalonamento e explicação posterior. A utilidade de cada grupo deve ser demonstrada separadamente, inclusive fora de repositórios vistos.

Isso preserva a contribuição crítica da dissertação: a pergunta “há sinal preditivo?” vem antes de “como construir o seletor?”.

## Decisão editorial recomendada

Com as duas fontes aprovadas pelo autor, o Capítulo 7 pode ganhar uma subseção intitulada **“Da escolha de agente à política de escalonamento”**. Ela deve:

- usar as fontes atuais para estabelecer seleção condicional, heterogeneidade de tarefas e limites empíricos;
- usar as fontes A como evidência contemporânea de triagem e roteamento em tarefas de software;
- usar SALLMA apenas para descrever uma possível separação arquitetural entre orquestração, configuração e execução;
- manter os preprints explicitamente como evidência de fronteira, jamais como prova definitiva de aplicabilidade industrial;
- não incluir *Multi-LLM Prototype* no argumento central: ele é inspiração de infraestrutura, não evidência direta de engenharia de software.

## Próximo passo de pesquisa, sem piloto

1. ~~O autor decide quais candidatas da prioridade A/B promover para a bibliografia citável~~ — feito em 27/09/2026: `becattini2025sallma` e `son2026swerouter`.
2. ~~Para cada fonte aprovada, produzir nota de leitura integral e extrair somente afirmações compatíveis com seu desenho e população~~ — feito em 27/09/2026; notas em `literatura/notas-de-leitura/`.
3. ~~Revisar a escada de inferência do dossiê~~ — feito em 27/09/2026: acrescentada evidência complementar de roteamento e apoio arquitetural, preservando como hipótese a eficácia em qualquer equipe ou repositório específico.
4. ~~Integrar a síntese final disponível da Fase 4B~~ — feito em 27/09/2026. Os EXP-21 e EXP-24 reforçam, no recorte de planejamento, a exigência de política sequencial e validação por unidade mantida fora; não demonstram que sinais estáticos sejam inúteis nem antecipam o comportamento de agentes de software.

## Registros primários

- Fan, Yin e Chen (2026): <https://arxiv.org/abs/2609.25911>
- Son et al. (2026): <https://arxiv.org/abs/2607.00053>
- Zhou et al. (2026): <https://arxiv.org/abs/2606.22902>
- Chen et al. (2026): <https://arxiv.org/abs/2608.22191>
- Madeyski (2026): <https://arxiv.org/abs/2604.07494>
- Becattini, Verdecchia e Vicario (2025): <https://doi.org/10.1109/SATrends66715.2025.00006>
- Cheikh Tourad e Lachgar (2026): <https://doi.org/10.1016/j.softx.2026.102782>
