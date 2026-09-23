---
tipo: nota-de-leitura
eixo: E3
citekey: koehler1997extending
prioridade: B
status: lido
profundidade: texto-integral
fonte-lida: http://web.archive.org/web/20080821140756/http://www.informatik.uni-freiburg.de/~koehler/papiere/ecp-97.ps.gz
metadados: verificada-por-agente
referencia-verificada: false
afirmacoes-2010: [A6]
fragilidades: [F4]
perguntas: [Q1]
---

# Extending Planning Graphs to an ADL Subset

**Koehler, J.; Nebel, B.; Hoffmann, J.; Dimopoulos, Y. · 1997 · Recent Advances in AI Planning (ECP-97), Springer LNAI 1348, 273–285**
**Link/DOI:** https://doi.org/10.1007/3-540-63912-8_92 (versão lida: cópia arquivada do technical report em PostScript, ligada pela própria página de publicações de IPP)

## Extração estruturada

- **Problema:** estender o algoritmo Graphplan (grafo de planos), restrito a STRIPS puro, para um subconjunto de ADL com efeitos condicionais e universalmente quantificados, preservando as propriedades do algoritmo original (corretude, completude, geração de planos mais curtos, terminação em problemas sem solução).
- **Método:** o planejador IPP embute operadores com efeitos condicionais e quantificados diretamente na construção do grafo de planos, em vez de compilá-los em múltiplos operadores STRIPS (o que causaria explosão combinatória). O artigo formaliza a semântica de planos paralelos em ADL e a extração de planos a partir do grafo estendido.
- **Dados/benchmarks:** não é um artigo experimental com benchmarks; é um artigo de fundamentação algorítmica (definições formais e provas de propriedades).
- **Resultado principal:** a extensão preserva as propriedades centrais do Graphplan original, incluindo a geração de planos com paralelismo máximo (ver trecho literal).
- **Relação com a dissertação de 2010:**
  - **A6 (corrige):** 2010 classifica IPP como State-Space, Total-order, Forward-chaining e Graph-based (Tabela 4). A fonte confirma Graph-based diretamente (IPP é uma extensão do Graphplan), mas não descreve uma busca sequencial no espaço de estados nem um algoritmo Forward-chaining: o mecanismo é construção e extração de planos a partir de um grafo de planos, que por definição produz planos com ações paralelas — o que também torna discutível o rótulo "Total-order" (ordem total), já que o próprio Graphplan é caracterizado por explorar "paralelismo máximo das ações no plano".

## Pontos relevantes para o projeto

- Reforça, junto com o material lido sobre Fast Downward e FF, que "Graph-based" na literatura primária quase sempre se refere ao uso do grafo de planos do Graphplan (Blum & Furst, 1995) como estrutura auxiliar, não a uma "técnica de busca" independente — ponto central para redesenhar a dimensão "algoritmo de busca" da Fase 2.
- IPP é citado por FF (Hoffmann & Nebel, 2001) como uma das linhas que motivaram a extensão do Graphplan a linguagens mais expressivas — útil para reconstruir a árvore genealógica de técnicas do eixo E3.

## Marcações

- `[FATO]` IPP estende o Graphplan (grafo de planos) para um subconjunto de ADL, preservando suas propriedades, entre elas o paralelismo máximo de ações no plano (Seção 2).
- `[HIPÓTESE]` O rótulo "Total-order" atribuído por 2010 a IPP é inconsistente com a própria natureza do Graphplan, que gera planos com ações paralelas por construção — a classificação de 2010 provavelmente veio da leitura da página web do IPP (citada como fonte em 2010), não do artigo técnico que descreve o algoritmo.

## Trechos literais

1. "One of the distinguished features of graphplan is its ability to produce shortest plans in the sense that it exploits maximal parallelism of actions in the plan." (Seção 2, correspondente à p. 277 do artigo publicado)

## Uso de IA nesta nota

Claude Code, subagente claude-sonnet-5, 23/09/2026. Leitura de texto integral a partir de cópia arquivada (Wayback Machine) do technical report em PostScript, indicado pela própria página de publicações de IPP (`~koehler/ipp/publi.html`), convertido a PDF com Ghostscript e extraído com `pdftotext -layout`. A conversão perdeu ligaturas tipográficas ("fi", "ffi", "ff") em parte do texto; o trecho citado foi conferido para não conter essas sequências. Metadados (DOI, autores, veículo) verificados via Crossref. Conferência humana: pendente.
