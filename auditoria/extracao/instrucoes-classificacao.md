# Instruções para os auditores (Fase 2, Onda 3)

Versão 1.1 · 23/09/2026 · Coordenador (claude-opus-5-5). Vale para todos os auditores. Português do Brasil com acentuação correta.

## 1. O que classificar

Cada linha de `auditoria/afirmacoes.csv` da sua faixa de IDs. A afirmação é o `trecho` (cópia literal de `data/2010/extraido/texto.md`, na `linha` indicada). Leia o parágrafo inteiro em volta antes de classificar.

## 2. Classes

| Classe | Quando usar |
|---|---|
| `mantém` | A afirmação está correta e sustentada como está, hoje. Pode precisar só de ajuste de redação ou de referência atualizada, sem mudar o conteúdo. |
| `reformula` | O núcleo se sustenta, mas precisa de correção, restrição, qualificação, atualização ou de evidência que 2010 não deu. Diga **o que muda**. |
| `descarta` | Errada, contrariada pela fonte primária ou pelos próprios dados de 2010, ou sem sustentação possível. Diga **por quê**, com a evidência. |

Regras de desempate:
- Descrição de método (o que foi feito) é `mantém` se descreve com fidelidade o que foi feito, **mesmo que o método seja fraco**. A fraqueza vai para a afirmação que tira conclusão dele, ou para a `acao`. Exceção: se a descrição contradiz os dados ou o acervo (ver achados G1–G20), é `reformula`.
- Afirmação histórica ou sobre outra obra que você não consegue conferir em fonte primária: `reformula`, com `acao` "conferir na fonte primária" e `confianca: baixa`. **Nunca complete de memória.**
- Descrição provavelmente correta, mas que você só consegue apoiar em plausibilidade ou "conhecimento da área": `mantém` com `confianca: baixa` e `acao` começando com "CONFERIR". Plausibilidade não é evidência. (Regra acrescentada pelo Coordenador na v1.1.)
- Afirmação sobre uma obra citada em 2010: confira **qual obra** a lista de referências de 2010 (linhas 1830 em diante do texto) indica, antes de comparar com uma nota do projeto. Mesmo autor e ano não garantem mesma obra. (v1.1)
- Afirmação datada ("é considerado o melhor sistema até então"): `mantém` se era verdade na data e o texto deixa a data clara; senão `reformula` (situar no tempo).

## 3. Fontes que você deve usar

1. `auditoria/insumos-fase1.md` — veredito da Fase 1 para as afirmações centrais A1–A8 e o estado de F1–F7, T1–T6. **Sua classificação deve ser coerente com ele.** Se discordar, classifique como achar certo e escreva `DIVERGE DO INSUMO:` no início da justificativa, explicando.
2. `auditoria/achados-fase0.md` — achados G1–G20 sobre os dados de 2010.
3. `auditoria/afirmacoes.csv`, coluna `conferencia_numerica` — resultado da conferência dos números (Onda 2). Os arquivos em `auditoria/extracao/conferencia-*.csv` têm os detalhes.
4. `auditoria/taxonomia/fontes-planejadores.csv` e as notas dos planejadores — o que cada um dos 10 planejadores diz de si na fonte primária.
5. `literatura/sinteses/` (8 sínteses) e `literatura/notas-de-leitura/` — a literatura verificada.
6. Rótulos: A1–A8, T1–T6, F1–F7 e Q1–Q4 em `literatura/protocolo/instrucoes-leitura.md`, seção 1.

## 4. Chaves bibliográficas

- Só use chaves que existam em `literatura/referencias/candidatas.bib` **e** tenham nota em `literatura/notas-de-leitura/`. Confira com `grep`.
- Na justificativa, marque a chave com `*` se ela **não** estiver em `literatura/referencias/referencias.bib` (ainda não citável no texto final).
- **Nunca invente chave, autor, ano nem resultado.** Se precisar de uma fonte que o projeto não tem, escreva na `acao`: "buscar fonte: <o que falta>".

## 5. Saída

Um CSV seu, `auditoria/extracao/classificacao-<letra>.csv` (UTF-8, vírgula, LF, aspas duplas em campos com vírgula), com cabeçalho exato:

`id,rotulo_fase1,classificacao,confianca,justificativa,acao`

- `id`: AF-NNN, **um por linha, todos os da sua faixa**.
- `rotulo_fase1`: rótulos ligados (ex.: `A3`, `A6;F4`, `T4`), ou vazio.
- `classificacao`: `mantém`, `reformula` ou `descarta` (com acento).
- `confianca`: `alta` (evidência direta: fonte primária, dados, conta reproduzível), `media` (evidência indireta ou de síntese), `baixa` (não conferido).
- `justificativa`: 1 a 3 frases, com a evidência (chaves, G-ids, tabelas, arquivos). Marque `[FATO]` e `[HIPÓTESE]` quando houver risco de confusão.
- `acao`: o que fazer na dissertação revisada (ex.: "corrigir 6,17 para 6,07", "situar no tempo", "citar kerschke2019automated", "remover"). Se exigir experimento, comece com `FASE3:` e diga o quê.

Antes de terminar, confira com Python: todos os IDs da faixa presentes uma vez; classes só entre as três; toda chave citada existe no `candidatas.bib`.

## 6. Não faça

Não edite `auditoria/afirmacoes.csv` (o Coordenador consolida), `plan/`, `MEMORY.md`, `referencias.bib`, `candidatas.bib`, notas existentes, nem `acervo-2010/`. Não faça commit.
