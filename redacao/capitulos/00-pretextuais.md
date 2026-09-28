---
titulo: "Elementos pré-textuais"
status: revisado-por-ia
data: 2026-09-28
fonte: guia da FEI (redacao/README.md); declaração no modelo fornecido pelo autor
---

<!-- Capa, folha de rosto e ficha catalográfica são montadas por redacao/montagem/montar.py a partir de
redacao/montagem/identificacao.json. A folha de aprovação só existe com banca (guia da FEI, p. 19). -->

# Resumo {.pretextual}

Esta dissertação revisa criticamente a relação entre características de domínios e técnicas de planejamento automático proposta em 2010. O objetivo é verificar se métricas estruturais de modelos auxiliam a seleção de planejadores e examinar a permanência dessa pergunta diante de métodos, dados e técnicas posteriores. O método combina auditoria documental da versão original, reprodução por *scripts*, correções metodológicas, reexecução homogênea de planejadores, ampliação com resultados publicados e análise por instância das Competições Internacionais de Planejamento de 2011 e 2018. A auditoria identifica limites na taxonomia, na origem dos dados e na validação original. Nos experimentos, nenhum seletor baseado nas métricas aproximadas a partir do PDDL, nas *features* SAS+ ou em sua combinação demonstrou superar o melhor planejador único. Propriedades de topologia acrescentaram sinal preditivo em parte das famílias, mas esse sinal não produziu ganho significativo de seleção. Modelos de linguagem foram avaliados como seletores, geradores de planos e tradutores: o ciclo com verificador formal produziu 13 planos válidos em 16 tentativas, enquanto o melhor seletor por modelo apresentou perda semelhante à referência fixa, sem equivalência demonstrada. Por fim, o trabalho formula hipóteses e critérios de avaliação para uma possível aplicação no desenvolvimento de software apoiado por IA. Conclui-se que a pergunta sobre ajuste entre problema e técnica permanece relevante, mas qualquer política de escolha exige comparação com referência fixa forte, validação fora da amostra e objetivos que incluam qualidade, segurança, tempo e custo. <!-- fonte: EXP-12; EXP-17; EXP-21; EXP-24; EXP-25 -->

Palavras-chave: Planejamento automático. Seleção de algoritmos. Características de domínio. Modelos de linguagem. Engenharia de software.

# Abstract {.pretextual}

This dissertation critically revisits the relationship between planning-domain characteristics and automated-planning techniques proposed in 2010. It examines whether structural model metrics can support planner selection and whether that question remains relevant in light of later methods, data, and techniques. The method combines a documentary audit of the original dissertation, script-based reproduction, methodological corrections, homogeneous re-execution of planners, an extension based on published results, and instance-level analysis of the 2011 and 2018 International Planning Competitions. The audit identifies limitations in the taxonomy, data provenance, and original validation. In the experiments, no selector based on PDDL approximations of the original metrics, SAS+ features, or their combination demonstrated an advantage over the single best planner. Search-topology properties added predictive signal for some technique families, but this signal did not yield a significant selection gain. Large language models were assessed as selectors, plan generators, and translators: the cycle with a formal verifier produced 13 valid plans in 16 attempts, while the best model-based selector had a loss close to the fixed baseline, without demonstrated equivalence. Finally, the dissertation formulates hypotheses and evaluation criteria for a possible application to AI-supported software development. It concludes that the question of matching problem and technique remains relevant, but any selection policy requires comparison with a strong fixed baseline, out-of-sample validation, and objectives that include quality, security, time, and cost.

Keywords: Automated planning. Algorithm selection. Domain features. Language models. Software engineering.

# Declaração de uso de inteligência artificial generativa {.pretextual}

<!-- Modelo fornecido pelo autor em 28/09/2026, preenchido com o uso real registrado no plano do projeto (seção 11).
A última frase só é verdadeira depois da revisão do autor, prevista para depois de 02/10/2026. -->

Declaro que durante a elaboração do presente trabalho de dissertação foram utilizadas as ferramentas de Inteligência Artificial Claude Code, com os modelos Claude Opus 5 e Claude Opus 5.5 (coordenação do trabalho) e Claude Sonnet 5 e Claude Haiku 4.5 (tarefas delegadas), desenvolvida por Anthropic, e Codex, com os modelos GPT-5 e GPT-6, desenvolvida por OpenAI, em versões de setembro de 2026. As ferramentas auxiliaram na busca, triagem, leitura e extração estruturada da literatura, na verificação dos metadados das referências, na auditoria da versão de 2010, na escrita do código de extração, execução e análise dos experimentos e na redação e revisão integral desta versão, incluindo a ponte com o desenvolvimento de software. Os experimentos do capítulo 6 avaliam, como objeto de estudo, os modelos Claude Sonnet 5, GPT-6 Sol, Gemini 3.1 Pro e DeepSeek V4 Pro, acessados pela plataforma OpenRouter; esse uso não se confunde com o apoio à elaboração do trabalho. Antes da entrega, o conteúdo gerado com apoio dessas ferramentas será revisado, validado e adaptado criticamente pelo autor. As análises, interpretações e conclusões apresentadas neste trabalho são de inteira e exclusiva responsabilidade do autor.

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

| | |
|---|---|
| ABNT | Associação Brasileira de Normas Técnicas |
| ADL | *Action Description Language* |
| AUC | Área sob a curva ROC |
| BDD | *Binary Decision Diagram* (diagrama de decisão binário) |
| CNN | *Convolutional Neural Network* (rede neural convolucional) |
| FEI | Fundação Educacional Inaciana Pe. Sabóia de Medeiros |
| GCP | *Google Cloud Platform* |
| hFF | Heurística de relaxação do planejador FF |
| IA | Inteligência artificial |
| IPC | *International Planning Competition* |
| kNN | *k-nearest neighbors* (k vizinhos mais próximos) |
| LLM | *Large Language Model* (modelo de linguagem de grande escala) |
| OCL | *Object Constraint Language* |
| PDDL | *Planning Domain Definition Language* |
| ROC | *Receiver Operating Characteristic* |
| SAS+ | Representação de tarefas de planejamento por variáveis de domínio finito |
| SAT | Problema de satisfatibilidade proposicional |
| SBS | *Single best solver* (melhor planejador único) |
| STRIPS | *Stanford Research Institute Problem Solver* |
| UML | *Unified Modeling Language* |
| VAL | Validador de planos em PDDL |
| VBS | *Virtual best solver* (oráculo) |

# Sumário {.pretextual}

::: {.campo #sumario}
:::
