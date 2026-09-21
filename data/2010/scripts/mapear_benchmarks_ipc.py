"""Identifica de qual IPC e variante vieram os problemas PDDL usados em 2010.

Compara os arquivos de `acervo-2010/.../comp/<dominio>/` com as instâncias do repositório
https://github.com/potassco/pddl-instances (IPCs 1998 a 2008) em duas camadas:
  - "identico":    texto igual após normalizar (sem comentários, minúsculas, espaços colapsados)
  - "equivalente": texto diferente, mesmo conteúdo semântico (mesmos objetos, mesmos átomos em
                   :init e :goal, ignorando ordem e o nome do problema). Só é tentado quando não há
                   correspondência idêntica.

Uso:
  git clone https://github.com/potassco/pddl-instances.git <pasta>
  git -C <pasta> checkout cf19edf7c53d1540ddbb396c642595e0926ee552     # commit analisado
  python mapear_benchmarks_ipc.py <pasta>

Saídas em data/2010/:
  benchmarks_ipc_instancias.csv  um registro por problema do acervo
  benchmarks_ipc.csv             um registro por (domínio, variante do repositório) com cobertura
  benchmarks_ipc_mapa_final.csv  a variante escolhida para cada um dos 13 domínios, com a base da escolha
"""
import csv
import hashlib
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[3]
COMP = RAIZ / "acervo-2010/planejadores_analise_resultados/comp"
SAIDA = RAIZ / "data/2010"
ANOS = ["1998", "2000", "2002", "2004", "2006", "2008"]

# domínio (slug do dataset) -> (pasta no acervo, regex dos arquivos de problema, regex do arquivo de domínio)
ACERVO = {
    "blocksworld": ("blocksworld", r"probBLOCKS-\d+-\d+\.pddl$", r"domain\.pddl$"),
    "depots": ("depots", r"pfile\d+$", r"domain\.pddl$"),
    "driverlog": ("driverlog", r"pfile\d+$", r"domain\.pddl$"),
    "gripper": ("gripper", r"pfile\d+\.pddl$", r"domain\.pddl$"),
    "logistics": ("logistic", r"probLOGISTICS-\d+-\d+\.pddl$", r"domain\.pddl$"),
    "mystery": ("mystery", r"pfile\d+$", r"domain\.pddl$"),
    "pathways": ("pathways", r"^p\d+\.pddl$", r"^domain_p\d+\.pddl$"),
    "pipesworld": ("pipesworld", r"^p\d+\.pddl$", r"domain\.pddl$"),
    "satellite": ("sattelite", r"P\d+_PFILE\d+\.PDDL$", r"domain\.pddl$"),
    "tpp": ("tpp", r"^p\d+\.pddl$", r"domain\.pddl$"),
    "storage": ("storage", r"^p\d+\.pddl$", r"domain\.pddl$"),
    # subpastas com a versão compilada para STRIPS (chave = domínio#strips)
    "pathways#strips": ("pathways/Strips", r"^p\d+\.pddl$", r"^domain_p\d+\.pddl$"),
    "pipesworld#strips": ("pipesworld/Strips", r"^p\d+\.pddl$", r"^domain_p\d+\.pddl$"),
    "tpp#strips": ("tpp/Strips", r"^p\d+\.pddl$", r"^domain_p\d+\.pddl$"),
}
# Escolha final por domínio: (ipc, variante, base, observação).
# base = identico | equivalente  -> comprovado por comparação de conteúdo com o acervo
#      = confirmado_pelo_autor   -> Zeno-travel e Elevator não têm PDDL no acervo (ver observação)
ESCOLHA = {
    "blocksworld": ("2000", "blocks-strips-typed", "identico", ""),
    "depots": ("2002", "depots-strips-automatic", "identico", ""),
    "driverlog": ("2002", "driverlog-strips-automatic", "identico", ""),
    "gripper": ("1998", "gripper-round-1-strips", "equivalente",
                "19 de 20 equivalentes; pfile1 (2 bolas) gerado localmente, sem par na IPC"),
    "logistics": ("2000", "logistics-strips-typed", "identico", "domínio equivalente: só muda a ordem de :types"),
    "mystery": ("1998", "mystery-round-1-strips", "identico", ""),
    "pathways": ("2006", "pathways-propositional", "identico", "a pasta Strips/ = pathways-propositional-strips"),
    "pipesworld": ("2004", "pipesworld-tankage-nontemporal-strips", "identico",
                   "idêntico a 2006 pipesworld-propositional; a edição de origem não se distingue pelos arquivos"),
    "satellite": ("2004", "satellite-strips", "identico", "domínio idêntico ao de 2004; problemas também em 2002"),
    "tpp": ("2006", "tpp-propositional", "identico", "a pasta Strips/ = tpp-propositional-strips"),
    "storage": ("2006", "storage-propositional", "identico", ""),
    "zenotravel": ("2002", "zenotravel-strips-automatic", "confirmado_pelo_autor",
                   "autor confirmou 'strips' (21/09/2026). 'automatic' é inferência: todos os domínios de 2002 do acervo "
                   "usam a variante automatic e os planejadores são independentes de domínio; o domínio é igual ao "
                   "hand-coded, só mudam as instâncias. Instâncias usadas: conjunto de 20, a confirmar"),
    "elevator": ("2000", "elevator-strips-simple-typed", "confirmado_pelo_autor",
                 "autor confirmou 'strips-simple' (21/09/2026). 'typed' é inferência: Blocks World e Logistics de 2000 "
                 "usam a variante typed e o modelo itSIMPLE é tipado. Subconjunto de instâncias (de 150): a confirmar"),
}
# prefixo do nome da variante no repositório -> domínio
PREFIXOS = {"blocks": "blocksworld", "depots": "depots", "driverlog": "driverlog", "gripper": "gripper",
            "logistics": "logistics", "mystery": "mystery", "pathways": "pathways", "pipesworld": "pipesworld",
            "satellite": "satellite", "tpp": "tpp", "storage": "storage", "zenotravel": "zenotravel",
            "elevator": "elevator"}


def norm(texto):
    texto = re.sub(r";[^\n]*", "", texto)
    return re.sub(r"\s+", " ", texto.lower()).strip()


def canon(texto):
    """Forma canônica semântica de um problema PDDL (ordem e nome do problema ignorados)."""
    t = re.sub(r"\s+", " ", re.sub(r";[^\n]*", "", texto.lower()))
    t = re.sub(r"\(define \(problem [^)]*\)", "", t)
    objs = re.search(r"\(:objects(.*?)\)", t)
    objetos = tuple(sorted(objs.group(1).split())) if objs else ()
    i, g = t.find("(:init"), t.find("(:goal")
    init = tuple(sorted(set(re.findall(r"\([^()]*\)", t[i:g])))) if i >= 0 and g >= 0 else ()
    meta = t[g:] if g >= 0 else t
    meta_atomos = tuple(sorted(set(re.findall(r"\([^()]*\)", meta))))
    conectivos = tuple(sorted(set(re.findall(r"\((and|or|not|forall|exists|imply|when)\b", meta))))
    return hashlib.sha1(repr((objetos, init, meta_atomos, conectivos)).encode()).hexdigest()


def hc(p):
    return canon(p.read_text(encoding="latin-1", errors="replace"))


def h(p):
    return hashlib.sha1(norm(p.read_text(encoding="latin-1", errors="replace")).encode()).hexdigest()


def dominio_da_variante(nome):
    for pref, dom in PREFIXOS.items():
        if nome.startswith(pref):
            return dom
    return None


def indexa_repo(repo):
    """hash -> [(ano, variante, tipo, id)] ; e {(dominio, ano, variante): n_instancias}"""
    idx = defaultdict(list)
    sem = defaultdict(list)   # índice semântico (só problemas)
    tam = {}
    for ano in ANOS:
        for var in sorted((repo / f"ipc-{ano}/domains").iterdir()):
            dom = dominio_da_variante(var.name)
            if not dom:
                continue
            inst = sorted((var / "instances").glob("*.pddl"))
            tam[(dom, ano, var.name)] = len(inst)
            for f in inst:
                idx[h(f)].append((ano, var.name, "problema", f.stem))
                sem[hc(f)].append((ano, var.name, "problema", f.stem))
            for f in list(var.glob("domain.pddl")) + list((var / "domains").glob("*.pddl")):
                if f.stat().st_size < 5_000_000:
                    idx[h(f)].append((ano, var.name, "dominio", f.stem))
    return idx, sem, tam


def main(repo):
    repo = Path(repo)
    idx, sem, tam = indexa_repo(repo)
    inst_rows = []
    por_var = defaultdict(set)      # (chave, ano, var) -> arquivos do acervo com correspondência idêntica
    por_var_eq = defaultdict(set)   # idem, equivalência semântica
    dom_ok = defaultdict(set)       # chave -> {(ano, var)} cujo domínio é idêntico
    n_acervo = Counter()
    for chave, (pasta, rp, rd) in ACERVO.items():
        base = COMP / pasta
        arqs = sorted((f for f in base.iterdir() if f.is_file() and re.search(rp, f.name)),
                      key=lambda f: [int(x) for x in re.findall(r"\d+", f.name)])
        n_acervo[chave] = len(arqs)
        for f in arqs:
            m = [x for x in idx.get(h(f), []) if x[2] == "problema"]
            tipo = "identico"
            if m:
                for ano, var, _, i in m:
                    por_var[(chave, ano, var)].add(f.name)
            else:
                m = list(sem.get(hc(f), []))
                tipo = "equivalente" if m else "nenhuma"
                for ano, var, _, i in m:
                    por_var_eq[(chave, ano, var)].add(f.name)
            inst_rows.append([chave, f.name, tipo, ";".join(sorted({f"{a}:{v}" for a, v, _, _ in m})),
                              ";".join(sorted({i for *_, i in m}))])
        for f in sorted(f for f in base.iterdir() if f.is_file() and re.search(rd, f.name) and f.stat().st_size < 5_000_000):
            for ano, var, t, _ in idx.get(h(f), []):
                if t == "dominio":
                    dom_ok[chave].add((ano, var))

    with open(SAIDA / "benchmarks_ipc_instancias.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["dominio", "arquivo_acervo", "correspondencia", "ipc_e_variantes", "instancias_do_repositorio"])
        w.writerows(inst_rows)

    linhas = []
    for chave in ACERVO:
        base = chave.split("#")[0]
        for (dom, ano, var), n_rep in sorted(tam.items()):
            if dom != base:
                continue
            ident = len(por_var.get((chave, ano, var), ()))
            equiv = len(por_var_eq.get((chave, ano, var), ()))
            if ident + equiv == 0:
                continue
            na = n_acervo[chave]
            linhas.append([chave, ano, var, na, n_rep, ident, equiv, round((ident + equiv) / na, 2),
                           (ano, var) in dom_ok[chave]])
    for (dom, ano, var), n_rep in sorted(tam.items()):   # domínios sem PDDL no acervo: só lista as variantes
        if dom in ("zenotravel", "elevator"):
            linhas.append([dom, ano, var, "", n_rep, "", "", "", ""])
    with open(SAIDA / "benchmarks_ipc.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["dominio", "ipc", "variante_repositorio", "problemas_no_acervo", "instancias_na_variante",
                    "problemas_identicos", "problemas_equivalentes", "fracao_do_acervo_coberta",
                    "arquivo_de_dominio_identico"])
        w.writerows(linhas)

    # mapa final
    usadas = defaultdict(set)
    for chave, arq, tipo, _, ids in inst_rows:
        for i in ids.split(";"):
            if i:
                usadas[chave].add(int(re.findall(r"\d+", i)[0]))
    with open(SAIDA / "benchmarks_ipc_mapa_final.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["dominio", "ipc", "variante_repositorio", "instancias_usadas", "instancias_no_conjunto",
                    "base_da_escolha", "observacao"])
        for dom, (ano, var, base, obs) in ESCOLHA.items():
            assert (dom, ano, var) in tam, f"variante inexistente no repositório: {dom} {ano} {var}"
            u = sorted(usadas.get(dom, ()))
            faixa = f"{u[0]}-{u[-1]}" if u else "a confirmar"
            w.writerow([dom, ano, var, faixa, tam[(dom, ano, var)], base, obs])

    print(f"{'entrada':18} {'acervo':>6}  id = idêntico, eq = equivalente, sem = sem correspondência")
    for chave in ACERVO:
        ids = {a for (d, *_), v in por_var.items() if d == chave for a in v}
        eqs = {a for (d, *_), v in por_var_eq.items() if d == chave for a in v}
        c = sorted(((len(v), k) for k, v in list(por_var.items()) + list(por_var_eq.items()) if k[0] == chave), reverse=True)
        top = "; ".join(f"{a}:{v} ({n})" for n, (_, a, v) in c[:2]) or "NENHUMA"
        print(f"{chave:18} {n_acervo[chave]:>6}  id={len(ids)} eq={len(eqs)} sem={n_acervo[chave]-len(ids)-len(eqs)} | {top}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
