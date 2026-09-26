# Prompt X2, LLM como tradutor (linguagem natural → PDDL) — versão 1 (26/09/2026)

Idioma: inglês. O script `llm/x2-tradutor/x2_tradutor.py` substitui `{descricao}` (o `domain.nl` do LLM+P) e `{problema}` (o `p01.pddl` do LLM+P).

## Mensagem de sistema

```
You are an expert in automated planning and in the Planning Domain Definition Language (PDDL).
```

## Mensagem do usuário

```
Write the PDDL domain file for the planning domain described below in natural language.
An example problem file for this domain is also given: your domain must use exactly the
same domain name, types, predicates and constants that the problem file uses, so that this
and other problems of the same domain can be solved with it.

DOMAIN DESCRIPTION (natural language)
{descricao}

EXAMPLE PROBLEM (PDDL)
{problema}

Write only the domain file, between the lines BEGIN DOMAIN and END DOMAIN.
```
