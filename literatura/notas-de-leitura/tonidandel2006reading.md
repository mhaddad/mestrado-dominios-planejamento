---
tipo: nota-de-leitura
eixo: E6
citekey: tonidandel2006reading
prioridade: A
status: lido
profundidade: texto-integral
fonte-lida: PDF fornecido pelo autor em 23/09/2026 (Springer, LNAI 4140, p. 532-541)
metadados: verificada-por-agente
referencia-verificada: true   # no referencias.bib desde 23/09/2026 (exceção por decisão do autor)
afirmacoes-2010: [A1, A5, T1]
fragilidades: [F3]
perguntas: [Q2]
---

# Reading PDDL, Writing an Object-Oriented Model

**Tonidandel, F.; Vaquero, T. S.; Silva, J. R. · 2006 · Advances in Artificial Intelligence – IBERAMIA-SBIA 2006, LNAI 4140, p. 532-541 (Springer)**
**Link/DOI:** 10.1007/11874850_57

## Extração estruturada

- **Problema:** o PDDL é declarativo e pouco intuitivo para quem não é da comunidade de planejamento; ferramentas orientadas a objetos (itSIMPLE, GIPO) exportam para PDDL, mas faltava o caminho inverso, de PDDL para um modelo orientado a objetos em UML.
- **Método:** processo de tradução de domínios PDDL do tipo STRIPS para a **UML.P** (*UML in a Planning Approach*), a notação do itSIMPLE. Tipos do PDDL viram classes; a hierarquia de tipos vira especialização; predicados de dois argumentos viram associações; predicados de um ou nenhum argumento viram atributos booleanos da classe ou da classe `Environment`; cada ação vira método da classe do **primeiro parâmetro** da ação, que passa a ser subclasse de `Agent`; os diagramas de estados são montados a partir de uma análise dos parâmetros e predicados de cada ação (listas PL e RPL, estrutura ABS).
- **Dados / benchmarks:** implementado no itSIMPLE; avaliado em Blocks World, Logistics, FreeCell "e outros" domínios STRIPS.
- **Resultado principal:** a tradução funcionou em todos os domínios testados, e a volta para PDDL reproduziu o domínio original, o que os autores tomam como prova de que a semântica é preservada. Não há medida quantitativa além disso.
- **Relação com a dissertação de 2010:**
  - **Define o instrumento de 2010.** A dissertação diz que suas características foram "extraídas da UML.P" (conclusões de 2010). Este artigo, do orientador da dissertação, é a especificação dessa notação e de como um domínio PDDL se converte nela.
  - **F3 [confirma, com mecanismo explícito]:** várias contagens que 2010 usou como características do domínio são, pela própria definição da UML.P, efeito de convenções de modelagem, não propriedades do problema:
    - a classe que recebe os métodos (e vira `Agent`) é decidida pela **ordem dos parâmetros** da ação, que o próprio artigo reconhece não ter regra no PDDL;
    - toda associação recebe multiplicidade **0..*** , porque o PDDL não informa quantidades;
    - toda classe que não age é ligada ao `Environment` por **agregação**;
    - predicados com mais de dois argumentos não são tratados.
    `[HIPÓTESE]` Isso afeta diretamente as métricas de 2010 de classes, métodos por classe, associações e agregações.
  - **Achado G13 da Fase 0** (a métrica "Agregação" tem valor em quase todos os domínios, mas não é conferível pelo XML): `[HIPÓTESE]` a regra da UML.P de agregar ao `Environment` toda classe que não age pode explicar a contagem. Conferir no XML do itSIMPLE e nas tabelas de 2010.
  - **Achado G2** (classes auxiliares fora da contagem): o artigo confirma a "General Class Structure" com as classes `Agent` e `Environment` em todo modelo, na linha do artigo de 2005 (`vaquero2005itsimple`).
  - **T1 / Q2:** a tradução de PDDL para UML.P é o caminho para extrair automaticamente as métricas de 2010 de qualquer domínio PDDL, o que a Fase 3 precisa para comparar UML com *features* de PDDL. `[FATO]` Mas a tradução impõe as convenções acima, e segundo `strobel2014planning` ela não fazia parte do itSIMPLE em 2014.

## Pontos relevantes para o projeto

- A dependência da **ordem dos parâmetros** é o espelho, na direção PDDL→UML, do achado de Vallati e colegas de que a ordem dos elementos no PDDL altera o desempenho dos planejadores (`vallati2021importance`). A ordem de escrita contamina tanto o desempenho medido quanto as métricas estruturais.
- Um extrator automático de métricas na Fase 3 precisa decidir se adota estas convenções (fidelidade a 2010) ou as neutraliza (por exemplo, contando associações sem depender da escolha do primeiro parâmetro).
- A convenção de multiplicidade fixa 0..* significa que qualquer métrica de 2010 baseada em multiplicidade é constante em modelos gerados de PDDL.

## Marcações

- `[FATO]` A UML.P impõe as classes `Agent` e `Environment`, aloca cada ação na classe do primeiro parâmetro, agrega ao `Environment` as classes que não agem e usa multiplicidade 0..* em todas as associações (seções 2.1 e 3.1).
- `[FATO]` O artigo admite que a regra do primeiro parâmetro é uma consideração dos autores, porque o PDDL não indica qual objeto é o mais importante de uma ação (seção 3.1).
- `[HIPÓTESE]` Parte da variação das métricas UML entre domínios em 2010 reflete essas convenções, e não diferenças estruturais do problema.

## Trechos literais

1. "In order to simplify the planning modeling process, UML.P proposes a General Class Structure composed by Agent class and a domain Environment class." (seção 2.1, p. 533)
2. "Any action defined in PDDL will be allocated as a method of the class of its first parameter in PL and this class will be a subclass of Agent." (seção 3.1, p. 536)
3. "since the PDDL description has no information of quantities between arguments of a predicate, the translation process just considers the multiplicity 0…* for all associations." (seção 3.1, p. 537)

Também relevante: "All the others classes will be associated to the Environment with an aggregation relation." (seção 2.1, p. 533)

## Uso de IA nesta nota

Claude Code, Coordenador (claude-opus-5-5), 23/09/2026. Leitura do texto integral do PDF fornecido pelo autor. Substitui a nota anterior, que só tinha metadados por falta de acesso. Conferência humana: pendente.
