# Prompt X3, condição com nomes — versão 1 (26/09/2026)

Igual ao `x3-anonimo-v1.md`, exceto pela frase que apresenta o catálogo (códigos, nomes e IPC). Idioma do *prompt*: inglês, a língua do PDDL e da literatura da área (escolha de método registrada no protocolo). O script `llm/x3-seletor/x3_seletor.py` substitui `{catalogo}`, `{dominio}` e `{instancia}`.

## Mensagem de sistema

```
You are an expert in automated planning. You answer with JSON only.
```

## Mensagem do usuário

```
Below is a classical planning domain in PDDL, followed by one small problem instance of it.
Larger instances of the same domain will be given to a planner with a limit of 30 minutes
and 4 GiB of memory per instance. The goal is to solve as many instances as possible
(coverage); plan quality does not matter.

Choose the ONE planner from the catalog below that is most likely to maximize coverage
on this domain. The planners are identified by codes, names and the International
Planning Competition (IPC) in which they competed, and described by the techniques they use.

CATALOG
{catalogo}

DOMAIN (PDDL)
{dominio}

SMALL INSTANCE (PDDL)
{instancia}

Answer with a single JSON object and nothing else:
{"planner": "<code, e.g. P07>", "reason": "<at most 60 words>"}
```
