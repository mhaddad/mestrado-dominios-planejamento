# Instruções de leitura e extração (Onda 4 da Fase 1)

Versão 1.0 · 22/09/2026 · Coordenador (Claude Code, claude-opus-5). Válidas para os agentes leitores e para quem refizer a leitura.

---

## 1. A dissertação de 2010 em uma página

HADDAD (2010) estudou se características de **domínios** de planejamento indicam qual **técnica** de planejamento terá melhor desempenho. Usou 10 planejadores das IPCs (Blackbox, IPP, FF, R, LPG, Fast Downward, YAHSP, SGPlan, SATPlan, MAXPLAN) em 10 domínios, mais 3 de validação (Storage, Zeno-travel, Elevator). Modelou os domínios em UML no itSIMPLE e mediu-os com métricas de diagramas de casos de uso, classes e estados (número de classes, atributos, associações, agregações, generalizações, estados, transições etc.), discretizadas em Alto/Médio/Baixo. A eficiência de cada planejador foi a **cobertura** (percentual de problemas resolvidos), tirada das IPCs ou de execução própria. Cruzando características e técnicas, montou um **ranking de planejadores por domínio**.

Afirmações centrais, com rótulos para você referenciar na nota:

| Rótulo | Afirmação de 2010 |
|---|---|
| A1 | Existe relação entre características de domínios (extraídas da UML) e técnicas de planejamento; as mais relevantes: casos de uso por atores, atributos, agregações, ações de entrada, associações, transições |
| A2 | As técnicas mais promissoras são *Heuristic Search*, *Hierarchical*, *Knowledge-based*, *Forward-chaining*, *Plan-Space* e *Total-order* |
| A3 | Só com as características do domínio, independentemente do problema, o ranking escolhe os planejadores com melhor desempenho |
| A4 | Mais características, planejadores e técnicas melhoram o ranking |
| A5 | Diagramas UML medem a complexidade do domínio, e essa complexidade afeta o desempenho das técnicas |
| A6 | Taxonomia de técnicas: planejadores SAT tratados como *forward-chaining*; SGPlan, SATPlan e MAXPLAN como *plan-space*; Fast Downward como *hierarchical* |
| A7 | Eficiência = cobertura; tempo e qualidade do plano não entram |
| A8 | Trabalhos relacionados citados: só Hoffmann (2001, topologia do espaço de busca) e Gerevini, Saetti e Serina (2004, heurísticas do LPG) |

Trabalhos futuros propostos em 2010: **T1** extração automática das métricas no itSIMPLE; **T2** agregar automaticamente novos resultados; **T3** detalhar as técnicas (heurística, construção da busca, subtécnicas); **T4** pesos por característica; **T5** domínios artificiais; **T6** análise estatística da discretização com mais dados.

Fragilidades já conhecidas (plano, seção 4): **F1** lacunas de revisão (Rice 1976, Roberts & Howe, IPC 2008, LAMA); **F2** amostra pequena; **F3** métricas UML medem o modelo e dependem do modelador; **F4** taxonomia de técnicas discutível; **F5** eficiência reduzida a cobertura; **F6** dados fora das competições; **F7** discretização com poucos pontos.

Perguntas da revisão: **Q1** as conclusões se sustentam com mais planejadores, domínios e estatística adequada? **Q2** métricas estruturais de modelagem acrescentam poder preditivo às *features* de PDDL? **Q3** onde entram os LLMs (planejador, tradutor, seletor)? **Q4** o ajuste tarefa–estratégia ajuda a escolher configurações de agentes de IA no desenvolvimento de software?

---

## 2. Como acessar o texto

1. Se `texto_integral_url` estiver preenchido: baixe o PDF para a pasta temporária indicada no seu prompt (`curl -sL -A "Mozilla/5.0" -o arquivo.pdf <url>`) e extraia com `pdftotext -layout arquivo.pdf arquivo.txt`, ou leia o PDF com a ferramenta Read (use `pages`, no máximo 20 por vez). Páginas HTML: WebFetch.
2. Se não houver texto aberto, ou o download falhar: procure uma cópia aberta (arXiv, página do autor, repositório institucional) com busca web. Se não achar, leia o **resumo** (página do registro, `url_registro`, ou Crossref/arXiv) e declare `profundidade: resumo`.
3. Nunca descreva o conteúdo de uma obra que você não leu. Se só leu o resumo, a nota fica curta e diz isso.
4. Arquivos baixados não vão para o repositório: ficam só na pasta temporária.

## 3. Profundidade

- **Prioridade A:** texto integral (introdução, método, resultados, conclusões; seções de trabalhos relacionados quando ligam a 2010). Nota completa.
- **Prioridade B e C:** resumo, introdução e conclusão bastam. Nota curta (extração estruturada em uma linha por campo, 1 trecho literal).

## 4. Formato da nota

Arquivo `literatura/notas-de-leitura/<chave>.md` (a chave é a da coluna `chave` do lote, **não mude**). Siga o modelo `templates/nota-leitura.md`, com este cabeçalho YAML:

```yaml
---
tipo: nota-de-leitura
eixo: E?            # eixo principal
citekey: <chave>
prioridade: A|B|C
status: lido
profundidade: texto-integral | resumo
fonte-lida: <URL efetivamente lida>
metadados: verificada-por-agente
referencia-verificada: false   # só o autor muda, depois do Zotero
afirmacoes-2010: [A2, A6]      # rótulos da seção 1 que a obra confirma, corrige ou torna obsoletos; [] se nenhum
fragilidades: [F4]             # F1–F7 que a obra ajuda a tratar; [] se nenhuma
perguntas: [Q1, Q2]            # Q1–Q4 que a obra alimenta
---
```

Corpo, na ordem do modelo:

- **Título, autores, ano, veículo, DOI/link** (copie do lote).
- **Extração estruturada:** problema; método; dados/*benchmarks*; resultado principal; relação com a dissertação de 2010 (cite os rótulos A/T/F e diga se a obra **confirma**, **corrige** ou **torna obsoleta** cada afirmação, e por quê).
- **Pontos relevantes para o projeto** (2 a 5 itens).
- **Trechos literais:** até 3 (A) ou 1 (B/C), cada um com no máximo 50 palavras, entre aspas, no idioma original, com a localização (seção, página ou "resumo"). Toda afirmação da nota que carrega número ou conclusão forte precisa de um trecho que a sustente.
- **Marcações:** `[FATO]` o que a obra mostra (com o trecho ou a seção); `[HIPÓTESE]` sua interpretação, sobretudo ligações com 2010 e com a Q4.
- **Uso de IA nesta nota:** "Claude Code, subagente claude-sonnet-5, 22/09/2026. Leitura de <texto integral | resumo> em <URL>. Conferência humana: pendente."

Português do Brasil com acentuação correta; termos técnicos no original em itálico quando fizer sentido (*portfolio*, *features*, *landmarks*).

## 5. Regras

- Números tirados da obra entram só com o trecho literal ou a seção/tabela de onde vieram.
- Não cite na nota outras obras além da lida, a não ser pela chave de uma obra já existente em `literatura/referencias/candidatas.bib` (sintaxe `[@chave]`). Não invente chaves.
- Não escreva fora de `literatura/notas-de-leitura/` (e da pasta temporária). Não toque em `acervo-2010/`, `plan/`, `MEMORY.md`, `.bib`. Não faça commit.
