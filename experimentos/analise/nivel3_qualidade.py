"""R-22: qualidade dos planos do Nível 3 (EXP-05), medida pelo número de ações.

Os planos são considerados corretos, sem VAL (decisão do autor, 27/09/2026). Para cada execução
resolvida, lê o tamanho do plano (número de ações) no log bruto, no formato de cada planejador.
Escore de qualidade no estilo da IPC: em cada problema, menor plano encontrado por qualquer
planejador ÷ plano do planejador (0 se não resolveu); somado por domínio e dividido pelo número
de problemas (0 a 1). LPG-TD: média das 3 sementes.

Entrada: experimentos/execucoes/nivel3-2010-gcp.csv e os brutos (fora do git) em
experimentos/execucoes/brutos/gcp/ e brutos/gcp-tpp/ (TPP refeito).
Uso: python3 experimentos/analise/nivel3_qualidade.py
Saída: experimentos/analise/nivel3/planos.csv (por execução) e qualidade.csv (por par).
"""
import csv
import re
import statistics
import sys
from collections import defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ / "experimentos/planejadores"))
import calibrar_2010 as C  # noqa: E402

BRUTOS = RAIZ / "experimentos/execucoes/brutos"
SAIDA = RAIZ / "experimentos/analise/nivel3"
NOME_2010 = {"sattelite": "satellite", "logistic": "logistics"}
ACAO = re.compile(r"^\s*[\d.]+:\s*\(", re.M)


def pasta(pl, dom):
    if dom == "tpp" and pl in C.STRIPS_TPP:
        return BRUTOS / "gcp-tpp/nivel3/brutos"
    return BRUTOS / "gcp/nivel3/brutos"


def tamanho(pl, texto, soln):
    """Número de ações do plano, ou None se não achar o plano."""
    if pl == "Blackbox":
        m = re.search(r"Begin plan\n(.*?)End plan", texto, re.S)
        return len(re.findall(r"^\d+ \(", m.group(1), re.M)) if m else None
    if pl == "IPP":
        m = re.search(r"found plan as follows:\s*\n(.*?)\n\s*\n", texto, re.S)
        return len([l for l in m.group(1).splitlines() if l.strip()]) if m else None
    if pl == "FF":
        m = re.search(r"found legal plan as follows\s*\n(.*?)\n\s*\n", texto, re.S)
        return len(re.findall(r"^\s*(?:step\s+)?\d+: \S", m.group(1), re.M)) if m else None
    if pl == "Fast Downward":
        m = re.search(r"Plan length: (\d+) step", texto)
        return int(m.group(1)) if m else None
    if pl in ("SATPlan", "MaxPlan"):
        return len(ACAO.findall(soln)) if soln else None
    if pl == "R":
        m = re.search(r"^[^,\s]+,[\d.]+,\d+,(\(.*)$", texto, re.M)
        return m.group(1).count("(") if m else None
    if pl == "LPG":
        # O LPG-TD nem sempre imprime o plano (-noout), mas sempre o resumo "Actions: N".
        m = re.search(r"^Actions:\s+(\d+)", texto, re.M)
        return int(m.group(1)) if m else None
    n = len(ACAO.findall(texto))  # YAHSP, SGPlan
    return n or None


def main():
    planos, faltou = [], []
    with (RAIZ / "experimentos/execucoes/nivel3-2010-gcp.csv").open(encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r["situacao"] != "resolvido":
                continue
            pl, dom = r["planejador"], r["dominio"]
            base = pasta(pl, dom) / C.CHAVE[pl] / dom / (r["problema"] + (f".s{r['semente']}" if r["semente"] else ""))
            texto = Path(f"{base}.log").read_text(errors="replace")
            soln = Path(f"{base}.soln").read_text(errors="replace") if Path(f"{base}.soln").exists() else ""
            n = tamanho(pl, texto, soln)
            if n is None:
                faltou.append((pl, dom, r["problema"], r["semente"]))
                continue
            planos.append({"planejador": pl, "dominio": NOME_2010.get(dom, dom), "problema": r["problema"],
                           "semente": r["semente"], "acoes": n})
    melhor = {}
    for p in planos:
        k = (p["dominio"], p["problema"])
        melhor[k] = min(melhor.get(k, p["acoes"]), p["acoes"])
    problemas = defaultdict(set)
    with (RAIZ / "experimentos/execucoes/nivel3-2010-gcp.csv").open(encoding="utf-8") as f:
        for r in csv.DictReader(f):
            problemas[(r["planejador"], NOME_2010.get(r["dominio"], r["dominio"]))].add(r["problema"])
    escore = defaultdict(lambda: defaultdict(float))  # (pl, dom) -> semente -> soma
    razoes = defaultdict(list)
    for p in planos:
        q = melhor[(p["dominio"], p["problema"])] / p["acoes"] if p["acoes"] else 1.0
        escore[(p["planejador"], p["dominio"])][p["semente"]] += q
        razoes[(p["planejador"], p["dominio"])].append(q)
    linhas = []
    for (pl, dom), probs in sorted(problemas.items()):
        sementes = escore.get((pl, dom), {"": 0.0})
        linhas.append({"planejador": pl, "dominio": dom, "problemas": len(probs),
                       "planos_lidos": len(razoes[(pl, dom)]),
                       "escore_qualidade": round(statistics.mean(sementes.values()) / len(probs), 3),
                       "qualidade_media_dos_resolvidos": round(statistics.mean(razoes[(pl, dom)]), 3)
                       if razoes[(pl, dom)] else ""})
    SAIDA.mkdir(parents=True, exist_ok=True)
    for arq, ls in (("planos.csv", planos), ("qualidade.csv", linhas)):
        with (SAIDA / arq).open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(ls[0]), lineterminator="\n")
            w.writeheader()
            w.writerows(ls)
    print(f"planos lidos: {len(planos)}; resolvidos sem plano legível: {len(faltou)}")
    for x in faltou[:20]:
        print("  sem plano legível:", x)
    por_pl = defaultdict(list)
    for l in linhas:
        por_pl[l["planejador"]].append(l)
    print("planejador      escore médio (10 dom.)  qualidade média dos resolvidos")
    for pl, ls in sorted(por_pl.items(), key=lambda kv: -statistics.mean(l["escore_qualidade"] for l in kv[1])):
        qs = [l["qualidade_media_dos_resolvidos"] for l in ls if l["qualidade_media_dos_resolvidos"] != ""]
        print(f"{pl:15} {statistics.mean(l['escore_qualidade'] for l in ls):.3f}                   "
              f"{statistics.mean(qs):.3f}")


if __name__ == "__main__":
    main()
