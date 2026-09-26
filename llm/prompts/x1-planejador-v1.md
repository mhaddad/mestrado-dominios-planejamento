# Prompt X1, LLM como planejador — versão 1 (26/09/2026)

Idioma: inglês, como no X3. O script `llm/x1-planejador/x1_planejador.py` substitui `{dominio}` e `{instancia}`.

## Mensagem de sistema

```
You are an expert in automated planning. You solve classical planning problems given in PDDL.
```

## Mensagem do usuário

```
Solve the following classical planning problem. Find a sequence of ground actions that
transforms the initial state into a state satisfying the goal. Every action must be
applicable in the state where it is executed, according to the domain definition.

DOMAIN (PDDL)
{dominio}

PROBLEM (PDDL)
{instancia}

Write the plan between the lines BEGIN PLAN and END PLAN, one action per line, in PDDL
syntax with the action name and its object arguments, for example:
BEGIN PLAN
(action-name object1 object2)
END PLAN
```
