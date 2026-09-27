"""Resultados por instância da IPC 2018, trilhas clássicas ótima, satisficing e agile (Fase 4B).

Fonte: `ipc2018-classical.bitbucket.io/results/{optimal,satisficing,agile}-results.tar.bz2`,
baixados por `levantar_fontes.py` para brutos/2018/. Cada arquivo tem o `properties` (JSON do
downward lab, uma entrada por execução), o `planner_names.py` (número da equipe -> nome do
planejador) e o relatório final em HTML.

O `properties` tem execuções em 14 domínios: os 10 do placar oficial mais as formulações
alternativas de caldera e organic-synthesis (`caldera`, `caldera-split`, `organic-synthesis`,
`organic-synthesis-split`), cujo resultado oficial é o `-combined`. Na ótima, o placar usa
petri-net-alignment em vez de flashfill. A coluna `oficial` marca os domínios que o relatório
final usa em cada trilha.

Validação: para cada trilha e algoritmo, as somas de coverage, da nota da trilha e das contagens
de erro nos domínios oficiais têm de reproduzir a tabela Summary do relatório final.

Uso: python data/ipc-2011-2023/scripts/ipc2018.py
Saída: data/ipc-2011-2023/ipc2018_resultados.csv
"""

import ast
import collections
import csv
import html
import json
import re
import tarfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
BRUTOS = RAIZ / "brutos" / "2018"
SAIDA = RAIZ / "ipc2018_resultados.csv"
TRILHAS = {"optimal": ("seq-opt", "opt", "coverage"),
           "satisficing": ("seq-sat", "sat", "sat_score"),
           "agile": ("seq-agl", "agl", "agl_score")}


def ler(tar, nome):
    return tar.extractfile(nome).read().decode("utf-8")


def nomes_planejadores(texto):
    m = re.search(r"TEAM_ID_TO_PLANNER_NAME\s*=\s*(\{.*?\})", texto, re.S)
    return ast.literal_eval(m.group(1))


def resumo_oficial(texto):
    """Tabela Summary do relatório: {linha: {algoritmo: valor}} e os domínios do relatório."""
    i = texto.find('id="summary"')
    tabela = texto[i:texto.find("</table>", i)]
    limpa = lambda c: html.unescape(re.sub(r"<[^>]+>", "", c)).strip()
    linhas = re.findall(r"<tr>(.*?)</tr>", tabela, re.S)
    algoritmos = [limpa(c) for c in re.findall(r"<t[hd][^>]*>(.*?)</t[hd]>", linhas[0], re.S)][1:]
    resumo = {}
    for linha in linhas[1:]:
        celulas = [limpa(c) for c in re.findall(r"<td[^>]*>(.*?)</td>", linha, re.S)]
        resumo[celulas[0]] = dict(zip(algoritmos, celulas[1:]))
    dominios = set(re.findall(r'id="coverage-([a-z\-]+)"', texto))
    return resumo, dominios


def main():
    linhas = []
    for arquivo, (trilha, sufixo, nota) in TRILHAS.items():
        with tarfile.open(BRUTOS / f"{arquivo}-results.tar.bz2") as tar:
            props = json.loads(ler(tar, f"{arquivo}-results/properties"))
            nomes = nomes_planejadores(ler(tar, f"{arquivo}-results/planner_names.py"))
            resumo, oficiais = resumo_oficial(ler(tar, f"{arquivo}-results/final-report-{sufixo}.html"))
        somas = collections.defaultdict(lambda: collections.Counter())
        for p in props.values():
            if p["track"] != trilha:
                raise SystemExit(f"execução fora da trilha {trilha}: {p['id']}")
            base = "baseline" in p["algorithm"]
            equipe = p["team_id"]
            planejador = (re.search(r"baseline-(.+?)-team0", p["algorithm"]).group(1) if base
                          else nomes[equipe])
            oficial = p["domain"] in oficiais
            erro = p.get("error", "")
            valor_nota = p.get(nota) or 0
            if oficial:
                s = somas[p["algorithm"]]
                s["coverage"] += p["coverage"]
                s["nota"] += valor_nota
                s[f"error-{erro}"] += 1
            linhas.append({
                "trilha": trilha, "dominio": p["domain"], "dominio_original": p.get("original_domain", p["domain"]),
                "oficial": "sim" if oficial else "não", "problema": p["problem"],
                "algoritmo": p["algorithm"], "equipe": equipe, "planejador": planejador,
                "linha_de_base": "sim" if base else "não", "cobertura": p["coverage"],
                "custo": "" if p.get("cost") is None else p["cost"],
                "tempo_total_s": "" if p.get("total_time") is None else p["total_time"],
                "memoria_kib": "" if p.get("memory") is None else p["memory"],
                "erro": erro, "nota_trilha": f"{valor_nota:.4f}",
                "expansoes": "" if p.get("expansions") is None else p["expansions"],
            })
        # Validação contra a tabela Summary do relatório oficial.
        rotulo_nota = "coverage - Sum" if nota == "coverage" else f"{nota} - Sum"
        algoritmos = sorted(somas)
        if sorted(resumo[rotulo_nota]) != algoritmos:
            raise SystemExit(f"{trilha}: algoritmos diferentes do relatório")
        for alg in algoritmos:
            s = somas[alg]
            confere = [(float(resumo["coverage - Sum"][alg]), s["coverage"]),
                       (float(resumo[rotulo_nota][alg]), round(s["nota"], 2))]
            for rot, vals in resumo.items():
                if rot.startswith("error-") and rot.endswith(" - Sum"):
                    confere.append((float(vals[alg]), s[rot.removesuffix(" - Sum")]))
            for oficial, calculado in confere:
                if abs(oficial - calculado) > 0.011:
                    raise SystemExit(f"{trilha} {alg}: relatório {oficial} x calculado {calculado}")
        n_plan = sum(1 for a in algoritmos if "baseline" not in a)
        print(f"{trilha}: {len(props)} execuções; {len(oficiais)} domínios oficiais; "
              f"{n_plan} planejadores + {len(algoritmos) - n_plan} linhas de base; "
              "somas do relatório reproduzidas")
        ordem = sorted(algoritmos, key=lambda a: -somas[a]["nota"])
        print("   " + ", ".join(f"{nomes.get(int(re.search(r'team(\d+)', a).group(1)), a)} "
                                f"{somas[a]['nota']:.2f}" for a in ordem[:4]) + " ...")

    linhas.sort(key=lambda l: (l["trilha"], l["dominio"], l["problema"], l["algoritmo"]))
    with SAIDA.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(linhas[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(linhas)
    print(f"{len(linhas)} linhas -> {SAIDA.name}")


if __name__ == "__main__":
    main()
