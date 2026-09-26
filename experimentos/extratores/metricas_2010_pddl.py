"""R-25 (auditoria/reexecucao.md): extrai do PDDL as métricas de 2010, que foram contadas à mão
em modelos UML.P do itSIMPLE, e compara com os valores publicados (Tabelas 8–9, 26, 32, 38).

As regras de correspondência PDDL -> métrica foram fixadas antes da comparação, a partir das
definições das Tabelas 5–7 de 2010 e do desenho da Fase 3 (hierarquia de tipos -> classes e
DIT; ações -> casos de uso e métodos; predicados -> atributos e associações). Não foram
ajustadas para aproximar os valores de 2010.

  Classes              tipos declarados, exceto `object`. Sem `:types`, os "predicados de
                       tipo": predicados unários que nenhuma ação altera e que aparecem como
                       guarda de parâmetro nas pré-condições.
  Generalização        pares filho -> pai na hierarquia de tipos, exceto pai `object`.
  Hierarquias          tipos que têm subtipos, exceto `object`.
  DIT Máximo           maior profundidade na hierarquia de tipos; filhos de `object` = 0.
  Atributos            predicados de aridade 0 ou 1, exceto predicados de tipo.
  Associações          predicados de aridade 2 ou mais.
  Métodos              ações.
  Casos de Uso         ações.
  Ações (estados)      ações.
  Atores               tipos distintos do primeiro parâmetro das ações (sem `:types`, o
                       predicado de tipo que guarda o primeiro parâmetro).
  Casos de Uso/Atores  atores ÷ casos de uso, como 2010 calculou (achado G1).

Sem correspondente no PDDL, não extraídas: Agregação, HAgg Máximo e as quatro métricas
do diagrama de estados além de "ações" (estados, ações de entrada, ações de saída,
transições). A agregação e as máquinas de estados são decisões do modelador em UML.P.

Uso: python experimentos/extratores/metricas_2010_pddl.py
Requer os benchmarks em experimentos/benchmarks/ipc/pddl-instances (ver README.md desta pasta).
Saídas: experimentos/extratores/metricas-2010-pddl/{metricas.csv, comparacao.csv, resumo.csv}.
"""
import csv
import re
import statistics
import sys
from collections import defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
BENCH = RAIZ / "experimentos/benchmarks/ipc/pddl-instances"
SAIDA = RAIZ / "experimentos/extratores/metricas-2010-pddl"
sys.path.insert(0, str(RAIZ / "experimentos/analise"))
import nivel2  # noqa: E402

# Pathways tem um arquivo de domínio por instância; usa-se o da primeira instância
ARQUIVO_DOMINIO = {"pathways": "domains/domain-1.pddl"}
NAO_EXTRAIDAS = {"Número total de Agregação", "HAgg Máximo", "Número total de estados",
                 "Número total de ações de entrada", "Número total de ações de saída",
                 "Número total de transições"}


# ---------------------------------------------------------------- leitura do PDDL
def sexp(texto):
    texto = re.sub(r";[^\n]*", "", texto).lower()
    fichas = re.findall(r"\(|\)|[^\s()]+", texto)
    pilha = [[]]
    for f in fichas:
        if f == "(":
            pilha.append([])
        elif f == ")":
            x = pilha.pop()
            pilha[-1].append(x)
        else:
            pilha[-1].append(f)
    return pilha[0][0]


def lista_tipada(itens):
    """[a b - t c] -> [(a, t), (b, t), (c, 'object')]"""
    out, pend, i = [], [], 0
    while i < len(itens):
        if itens[i] == "-":
            tipo = itens[i + 1]
            tipo = tipo[1] if isinstance(tipo, list) else tipo  # (either ...) -> primeiro
            out += [(n, tipo) for n in pend]
            pend, i = [], i + 2
        else:
            pend.append(itens[i])
            i += 1
    return out + [(n, "object") for n in pend]


def atomos(expr, dentro_de_not=False):
    """Átomos (nome, argumentos) de uma fórmula, com a polaridade."""
    if not isinstance(expr, list) or not expr:
        return []
    cab = expr[0]
    if cab == "not":
        return atomos(expr[1], not dentro_de_not)
    if cab in ("and", "or", "imply", "forall", "exists", "when", "preference"):
        corpo = expr[2:] if cab in ("forall", "exists") else expr[1:]
        return [a for e in corpo for a in atomos(e, dentro_de_not)]
    if cab in ("=", "increase", "decrease", "assign"):
        return []
    return [(cab, expr[1:], not dentro_de_not)]


def ler_dominio(caminho):
    arvore = sexp(caminho.read_text(encoding="utf-8", errors="replace"))
    d = {"tipos": [], "predicados": {}, "acoes": []}
    for sec in arvore[2:]:
        if not isinstance(sec, list) or not sec:
            continue
        if sec[0] == ":types":
            d["tipos"] = lista_tipada(sec[1:])
        elif sec[0] == ":predicates":
            for p in sec[1:]:
                d["predicados"][p[0]] = len(lista_tipada(p[1:]))
        elif sec[0] == ":action":
            campos = dict(zip(sec[2::2], sec[3::2]))
            d["acoes"].append({"nome": sec[1],
                               "parametros": lista_tipada(campos.get(":parameters", [])),
                               "pre": atomos(campos.get(":precondition", [])),
                               "efe": atomos(campos.get(":effect", []))})
    return d


# ---------------------------------------------------------------- regras
def predicados_de_tipo(d):
    alterados = {nome for a in d["acoes"] for (nome, _args, _pol) in a["efe"]}
    guardas = {nome for a in d["acoes"] for (nome, args, pol) in a["pre"]
               if pol and len(args) == 1 and args[0].startswith("?")}
    return {p for p, ar in d["predicados"].items() if ar == 1 and p not in alterados and p in guardas}


def metricas(d):
    tipado = bool(d["tipos"])
    ptipo = set() if tipado else predicados_de_tipo(d)
    if tipado:
        pai = {t: p for t, p in d["tipos"] if t != "object"}
        classes = set(pai)
        gen = sum(1 for p in pai.values() if p != "object")
        hier = len({p for p in pai.values() if p != "object"})

        def prof(t):
            n = 0
            while pai.get(t, "object") != "object":
                t, n = pai[t], n + 1
            return n
        dit = max((prof(t) for t in classes), default=0)
    else:
        classes, gen, hier, dit = ptipo, 0, 0, 0
    atrib = sum(1 for p, ar in d["predicados"].items() if ar <= 1 and p not in ptipo)
    assoc = sum(1 for ar in d["predicados"].values() if ar >= 2)
    acoes = len(d["acoes"])
    atores = set()
    for a in d["acoes"]:
        if not a["parametros"]:
            continue
        nome, tipo = a["parametros"][0]
        if not tipado:
            guardas = [p for (p, args, pol) in a["pre"] if pol and p in ptipo and args == [nome]]
            tipo = guardas[0] if guardas else "object"
        atores.add(tipo)
    return {
        "Número de Atores": len(atores),
        "Número de Casos de Uso": acoes,
        "Número de Casos de Uso por Atores": round(len(atores) / acoes, 2) if acoes else 0,
        "Número total de Classes": len(classes),
        "Número total de Atributos": atrib,
        "Número total de Métodos": acoes,
        "Número total de Associações": assoc,
        "Número total de Generalização": gen,
        "Número total de Hierarquias": hier,
        "DIT Máximo": dit,
        "Número total de ações": acoes,
    }


# ---------------------------------------------------------------- comparação
def classes_extremos(valores, papel):
    """Discretização aplicada em 2010 (achado G23): menor valor do treino = Baixo, maior =
    Alto, o resto Médio; validação comparada com os extremos do treino."""
    treino = [v for d, v in valores.items() if papel[d] == "treino"]
    lo, hi = min(treino), max(treino)
    return {d: "Baixo" if v <= lo else "Alto" if v >= hi else "Médio" for d, v in valores.items()}


def main():
    if not BENCH.exists():
        sys.exit(f"Benchmarks ausentes em {BENCH}; ver experimentos/extratores/README.md")
    mapa = {r["dominio"]: r for r in csv.DictReader((RAIZ / "data/2010/benchmarks_ipc_mapa_final.csv").open(encoding="utf-8"))}
    publicado = list(csv.DictReader((RAIZ / "data/2010/metricas_dominios.csv").open(encoding="utf-8")))
    papel = {r["dominio"]: r["papel"] for r in publicado}
    pub = {(r["dominio"], r["metrica"]): (float(r["valor_corrigido"] or r["valor"]), r["classe"]) for r in publicado}

    extraido, linhas_m = {}, []
    for dom, r in sorted(mapa.items()):
        arq = BENCH / f"ipc-{r['ipc']}/domains/{r['variante_repositorio']}" / ARQUIVO_DOMINIO.get(dom, "domain.pddl")
        m = metricas(ler_dominio(arq))
        extraido[dom] = m
        for k, v in m.items():
            linhas_m.append({"dominio": dom, "arquivo": str(arq.relative_to(BENCH)), "metrica": k, "valor": v})

    comparacao, resumo = [], []
    for metrica in sorted({k for (_d, k) in pub}):
        if metrica in NAO_EXTRAIDAS:
            resumo.append({"metrica": metrica, "extraida": "não", "iguais": "", "spearman": "",
                           "classe_igual": "", "classe_igual_treino": ""})
            continue
        doms = sorted(extraido)
        ext = {d: float(extraido[d][metrica]) for d in doms}
        cls = classes_extremos(ext, papel)
        for d in doms:
            v, c = pub[(d, metrica)]
            comparacao.append({"dominio": d, "papel": papel[d], "metrica": metrica, "valor_2010": v,
                               "valor_pddl": ext[d], "igual": v == ext[d],
                               "classe_2010": c, "classe_pddl": cls[d], "classe_igual": c == cls[d]})
        linhas = [c for c in comparacao if c["metrica"] == metrica]
        rho = nivel2.spearman([c["valor_2010"] for c in linhas], [c["valor_pddl"] for c in linhas])
        resumo.append({"metrica": metrica, "extraida": "sim",
                       "iguais": f"{sum(c['igual'] for c in linhas)}/{len(linhas)}",
                       "spearman": "" if rho != rho else round(rho, 2),
                       "classe_igual": f"{sum(c['classe_igual'] for c in linhas)}/{len(linhas)}",
                       "classe_igual_treino": f"{sum(c['classe_igual'] for c in linhas if c['papel'] == 'treino')}/10"})

    SAIDA.mkdir(parents=True, exist_ok=True)
    for nome, linhas in (("metricas.csv", linhas_m), ("comparacao.csv", comparacao), ("resumo.csv", resumo)):
        with (SAIDA / nome).open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(linhas[0]), lineterminator="\n")
            w.writeheader()
            w.writerows(linhas)
    for r in resumo:
        print(r)


if __name__ == "__main__":
    main()
