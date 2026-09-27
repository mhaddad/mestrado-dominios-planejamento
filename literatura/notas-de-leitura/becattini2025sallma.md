---
tipo: nota-de-leitura
eixo: E8
citekey: becattini2025sallma
prioridade: B
status: verificado
profundidade: texto-integral
fonte-lida: https://robertoverdecchia.github.io/papers/SATrends_2025.pdf
metadados: verificada-na-fonte-primaria
referencia-verificada: true
afirmacoes-2010: [A1, A3]
fragilidades: [prova-de-conceito, sem-avaliacao-de-roteamento-de-codigo]
perguntas: [Q4]
---

# SALLMA: A Software Architecture for LLM-Based Multi-Agent Systems

**Becattini, M.; Verdecchia, R.; Vicario, E. · 2025 · IEEE/ACM International Workshop on New Trends in Software Architecture (SATrends) · p. 5–8**
**Link/DOI:** https://doi.org/10.1109/SATrends66715.2025.00006

## Extração estruturada

- **Problema:** arquiteturas de um único agente LLM têm limites de customização por tarefa, memória persistente e acesso a informação validada; o artigo propõe como organizar sistemas multiagente LLM para lidar com esses problemas de arquitetura.
- **Método:** propõe a arquitetura SALLMA, com uma camada operacional que interpreta solicitações, gerencia fluxos, roteia pedidos e coordena agentes especializados, e uma camada de conhecimento que mantém catálogos de metamodelos de fluxos, configurações de agentes e modelos de implantação.
- **Dados / benchmarks:** não há *benchmark* comparativo de engenharia de software. A avaliação é uma prova de conceito funcional com tarefas ad hoc, incluindo um fluxo que exige conhecimento de padrões de projeto e outro de atendimento burocrático.
- **Resultado principal:** a prova de conceito demonstra que os fluxos podem ser executados e roteados para o fluxo cognitivo apropriado. Os autores caracterizam as observações como qualitativas, anedóticas e preliminares, e pedem avaliações industriais para medir desempenho, uso de recursos e qualidade percebida.
- **Relação com a dissertação de 2010:** [HIPÓTESE] oferece uma separação arquitetural útil para a Ponte: a política de escolha, a configuração disponível e a execução não precisam ficar no mesmo componente. Não demonstra que características de tarefa selecionam uma configuração melhor.

## Pontos relevantes para o projeto

- A camada de conhecimento dá um referente concreto para `ψ(a)`: configurações e fluxos podem ser representados, catalogados e recuperados, em vez de o “agente” ser apenas o nome do modelo.
- A camada operacional contém um *routing manager* e um gerenciador de fluxo; ela é pertinente à discussão de orquestração, não à evidência de eficácia de roteamento em tarefas de programação.
- O próprio artigo limita a força da evidência: a arquitetura é uma proposta com prova de conceito, e seus benefícios de escalabilidade, flexibilidade e testabilidade requerem validação empírica adicional.

## Marcações

- `[FATO]` SALLMA separa uma camada operacional para processamento/orquestração em tempo real de uma camada de conhecimento com metamodelos e configurações de fluxos e agentes.
- `[FATO]` A avaliação relatada é funcional e pequena; os autores a tratam como qualitativa e preliminar.
- `[HIPÓTESE]` A separação pode ajudar a tornar uma futura política de seleção de configurações de agentes auditável e reprodutível.

## Uso de IA nesta nota

Codex (GPT-5), 27/09/2026. Leitura do PDF disponibilizado pelo coautor e conferência dos metadados no registro IEEE/DOI; as afirmações acima foram comparadas com o texto integral. Promoção aprovada pelo autor em 27/09/2026.
