---
titulo: "Elementos pré-textuais"
status: rascunho-de-ia
data: 2026-09-28
fonte: guia da FEI (redacao/README.md); declaração no modelo fornecido pelo autor
---

<!-- Capa, folha de rosto e ficha catalográfica são montadas por redacao/montagem/montar.py a partir de
redacao/montagem/identificacao.json. A folha de aprovação só existe com banca (guia da FEI, p. 19). -->

# Resumo {.pretextual}

Esta dissertação revisa criticamente a relação entre características de domínios e técnicas de planejamento automático proposta em 2010. O objetivo é verificar se métricas estruturais de modelos UML permitem selecionar planejadores e examinar a permanência dessa pergunta diante de métodos, dados e técnicas posteriores. O método combina auditoria documental da versão original, reprodução por *scripts*, correções metodológicas, reexecução homogênea de planejadores, ampliação com resultados publicados e análise de dados por instância das Competições Internacionais de Planejamento de 2011 e 2018. A auditoria identifica limites na taxonomia, na origem dos dados e na validação original. Os experimentos mostram que as métricas UML extraíveis do PDDL e as *features* SAS+ não superam de modo robusto o melhor planejador único; propriedades de topologia de busca acrescentam sinal modesto e desigual, sem produzir uma política de seleção generalizável. Modelos de linguagem são avaliados como seletores, planejadores e tradutores: obtêm melhores resultados como geradores de planos com verificador formal externo, mas não superam a referência fixa como seletores. Por fim, o trabalho formula uma ponte exploratória para o desenvolvimento de software dirigido por IA. Conclui-se que a pergunta sobre ajuste entre problema e técnica permanece válida, mas uma política de escolha exige validação fora da amostra, comparação com referência fixa forte e objetivos que incluam qualidade, segurança, tempo e custo.

Palavras-chave: Planejamento automático. Seleção de algoritmos. Características de domínio. Modelos de linguagem. Engenharia de software.

# Abstract {.pretextual}

This dissertation critically revisits the relationship between planning-domain characteristics and automated-planning techniques proposed in 2010. It examines whether structural metrics of UML models can select planners and whether that question remains valid in light of later methods, data, and techniques. The method combines a documentary audit of the original dissertation, script-based reproduction, methodological corrections, homogeneous re-execution of planners, an extension based on published results, and instance-level analysis of the 2011 and 2018 International Planning Competitions. The audit identifies limitations in the taxonomy, data provenance, and original validation. The experiments show that UML metrics extractable from PDDL and SAS+ features do not robustly outperform the single best planner; search-topology properties add a modest and uneven signal without yielding a generalizable selection policy. Large language models are assessed as selectors, planners, and translators: they perform best as plan generators coupled with an external formal verifier, but do not outperform the fixed baseline as selectors. Finally, the dissertation develops an exploratory bridge to AI-supported software development. It concludes that the question of matching problem and technique remains valid, but any selection policy requires out-of-sample validation, comparison with a strong fixed baseline, and objectives that include quality, security, time, and cost.

Keywords: Automated planning. Algorithm selection. Domain features. Language models. Software engineering.

# Declaração de uso de inteligência artificial generativa {.pretextual}

<!-- Modelo fornecido pelo autor em 28/09/2026, preenchido com o uso real registrado no plano do projeto (seção 11).
A última frase só é verdadeira depois da revisão do autor, prevista para depois de 02/10/2026. -->

Declaro que durante a elaboração do presente trabalho de dissertação foram utilizadas as ferramentas de Inteligência Artificial Claude Code, com os modelos Claude Opus 5 e Claude Opus 5.5 (coordenação do trabalho) e Claude Sonnet 5 e Claude Haiku 4.5 (tarefas delegadas), desenvolvida por Anthropic, e Codex, com o modelo GPT-5, desenvolvida por OpenAI, em versões de setembro de 2026. As ferramentas auxiliaram na busca, triagem, leitura e extração estruturada da literatura, na verificação dos metadados das referências, na auditoria da versão de 2010, na escrita do código de extração, execução e análise dos experimentos e na redação integral desta versão revisada, incluindo a ponte com o desenvolvimento de software e os capítulos finais. Os experimentos do capítulo 6 avaliam, como objeto de estudo, os modelos Claude Sonnet 5, GPT-6 Sol, Gemini 3.1 Pro e DeepSeek V4 Pro, acessados pela plataforma OpenRouter; esse uso não se confunde com o apoio à elaboração do trabalho. Antes da entrega, o conteúdo gerado com apoio dessas ferramentas será revisado, validado e adaptado criticamente pelo autor. As análises, interpretações e conclusões apresentadas neste trabalho são de inteira e exclusiva responsabilidade do autor.

# Lista de ilustrações {.pretextual}

::: {.campo #ilustracoes}
:::

# Lista de quadros {.pretextual}

::: {.campo #quadros}
:::

# Lista de tabelas {.pretextual}

::: {.campo #tabelas}
:::

# Lista de abreviaturas e siglas {.pretextual}

<!-- Completar ao fim da redação com todas as siglas usadas nos capítulos. -->

| | |
|---|---|
| ABNT | Associação Brasileira de Normas Técnicas |
| FEI | Fundação Educacional Inaciana Pe. Sabóia de Medeiros |
| IPC | *International Planning Competition* |
| LLM | *Large Language Model* (modelo de linguagem de grande escala) |
| PDDL | *Planning Domain Definition Language* |
| SAS+ | Representação de tarefas de planejamento por variáveis de domínio finito |
| SBS | *Single best solver* (melhor planejador único) |
| UML | *Unified Modeling Language* |
| VAL | Validador de planos em PDDL |
| VBS | *Virtual best solver* (oráculo) |

# Sumário {.pretextual}

::: {.campo #sumario}
:::
