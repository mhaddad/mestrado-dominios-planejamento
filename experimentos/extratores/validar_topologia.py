"""Validação do extrator de topologia (topologia_sas.py) contra Hoffmann (2011), Tabela 3 (Fase 4B).

Critérios fixados antes de rodar (27/09/2026):
  1. O resultado básico (grafo de suporte acíclico, transições inversíveis, sem efeitos colaterais)
     vale em todas as tarefas do Logistics e em nenhuma tarefa dos outros domínios. Fonte: "of the
     considered benchmarks, it applies only in Logistics" (Hoffmann, 2011, p. 157).
  2. Taxa de sucesso da sondagem (SP) por domínio: correlação de Spearman >= 0,7 com a coluna SP,
     R = 10, da Tabela 3.
  3. Taxa de becos sem saída (DE) por domínio: correlação de Spearman >= 0,7 com a coluna DE da
     Tabela 3 (R = 1000).
Se algum critério falhar, as medidas correspondentes não entram na análise da 4B sem nova decisão.

Tabela 3 transcrita do PDF do artigo (JAIR 41, p. 184; https://doi.org/10.1613/jair.3276),
colunas "R = 10, SP" e "DE". Domínios da tabela sem pasta correspondente no downward-benchmarks
ficam de fora: Blocks-NoArm, Ferry, Hanoi, Simple-TSP, Tyreworld. Din-Phil e Opt-Tele têm axiomas
na tradução do Fast Downward e ficam de fora se o extrator os recusar.

Instâncias: até 10 por domínio, espaçadas na lista ordenada de problemas da pasta; 10 estados
amostrados por instância (Hoffmann usa todas as instâncias; o artigo mostra que R = 10 e R = 1000
dão taxas próximas).

Uso: uv run --no-project --with numpy --with networkx --with scipy python experimentos/extratores/validar_topologia.py
Saídas: experimentos/extratores/topologia-validacao/{tarefas.csv, dominios.csv}
"""

import csv
import zlib
import os
import sys
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

from scipy.stats import spearmanr

sys.path.insert(0, str(Path(__file__).resolve().parent))
import topologia_sas as T  # noqa: E402

RAIZ = Path(__file__).resolve().parents[2]
DB = RAIZ / "experimentos/ferramentas/planner-museum/benchmarks/downward-benchmarks"
SAIDA = Path(__file__).resolve().parent / "topologia-validacao"

# domínio da Tabela 3 -> (pasta do downward-benchmarks, SP com R = 10, DE com R = 1000)
TABELA3 = {
    "Airport": ("airport", 2.0, 97.0), "Blocks-Arm": ("blocks", 94.5, 0), "Depots": ("depot", 99.1, 0),
    "Din-Phil": ("philosophers", 23.1, 77.2), "Driverlog": ("driverlog", 100, 0),
    "Elevators": ("elevators-sat08-strips", 100, 0), "Freecell": ("freecell", 62.8, 35.4),
    "Grid": ("grid", 92.0, 0), "Gripper": ("gripper", 100, 0), "Logistics": ("logistics00", 100, 0),
    "Miconic": ("miconic", 100, 0), "Movie": ("movie", 100, 0), "Mprime": ("mprime", 76.3, 7.2),
    "Mystery": ("mystery", 43.9, 46.8), "Opt-Tele": ("optical-telegraphs", 2.9, 98.3),
    "Pipes-NoTank": ("pipesworld-notankage", 97.4, 0), "Pipes-Tank": ("pipesworld-tankage", 90.0, 8.7),
    "PSR": ("psr-small", 69.8, 0), "Rovers": ("rovers", 99.5, 0), "Satellite": ("satellite", 100, 0),
    "Transport": ("transport-sat08-strips", 93.0, 0), "Zenotravel": ("zenotravel", 99.5, 0),
    "Openstacks": ("openstacks-sat08-strips", 21.3, 79.1), "Parc-Printer": ("parcprinter-08-strips", 8.3, 93.0),
    "Pathways": ("pathways", 6.0, 95.3), "Peg-Sol": ("pegsol-08-strips", 22.7, 75.2),
    "Scanalyzer": ("scanalyzer-08-strips", 99.7, 0), "Sokoban": ("sokoban-sat08-strips", 38.3, 54.2),
    "Storage": ("storage", 96.3, 0), "TPP": ("tpp", 67.0, 34.5), "Trucks": ("trucks-strips", 3.1, 97.3),
    "Woodworking": ("woodworking-sat08-strips", 14.3, 84.6),
}
INSTANCIAS, AMOSTRAS = 10, 10


def dominio_de(pasta, prob):
    cands = [pasta / f"domain_{prob.name}", pasta / f"domain-{prob.name}", pasta / f"{prob.stem}-domain.pddl",
             pasta / f"{prob.stem.split('-')[0]}-domain.pddl", pasta / "domain.pddl"]
    return next(c for c in cands if c.exists())


def tarefas():
    for nome, (pasta, _sp, _de) in TABELA3.items():
        p = DB / pasta
        probs = sorted(x for x in p.glob("*.pddl") if not x.name.startswith("domain") and not x.stem.endswith("-domain"))
        passo = max(1, len(probs) // INSTANCIAS)
        for prob in probs[::passo][:INSTANCIAS]:
            yield nome, prob


def rodar(args):
    nome, prob = args
    txt, st = T.traduzir(dominio_de(prob.parent, prob), prob, 300)
    base = {"dominio": nome, "problema": prob.name}
    if txt is None:
        return {**base, "status": st}
    return {**base, **T.analisar(txt, amostras=AMOSTRAS, semente=zlib.crc32(prob.name.encode()))}


def main():
    SAIDA.mkdir(parents=True, exist_ok=True)
    lista = list(tarefas())
    linhas = []
    with ProcessPoolExecutor(max(1, (os.cpu_count() or 2) - 2)) as ex:
        for f in as_completed([ex.submit(rodar, t) for t in lista]):
            linhas.append(f.result())
    campos = ["dominio", "problema", "status", "variaveis", "operadores", "axiomas", "basico", "frac_inversiveis",
              "hff_s0", "hff_custo_s0", "amostras", "de_taxa", "sp_taxa", "sp_limite", "sp_dist_media", "tempo_s"]
    linhas.sort(key=lambda l: (l["dominio"], l["problema"]))
    with (SAIDA / "tarefas.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=campos, lineterminator="\n", extrasaction="ignore")
        w.writeheader()
        w.writerows(linhas)
    dom = []
    for nome, (pasta, sp_h, de_h) in TABELA3.items():
        ok = [l for l in linhas if l["dominio"] == nome and l.get("amostras")]
        n = sum(l["amostras"] for l in ok)
        if not n:
            dom.append({"dominio": nome, "pasta": pasta, "tarefas": 0, "sp_hoffmann": sp_h, "de_hoffmann": de_h,
                        "obs": ";".join(sorted({l["status"] for l in linhas if l["dominio"] == nome}))})
            continue
        dom.append({"dominio": nome, "pasta": pasta, "tarefas": len(ok), "amostras": n,
                    "sp": round(100 * sum(l["sp_taxa"] * l["amostras"] for l in ok) / n, 1),
                    "de": round(100 * sum(l["de_taxa"] * l["amostras"] for l in ok) / n, 1),
                    "sp_hoffmann": sp_h, "de_hoffmann": de_h,
                    "basico_tarefas": sum(1 for l in ok if l["basico"]),
                    "sp_limite": sum(l["sp_limite"] for l in ok), "obs": ""})
    with (SAIDA / "dominios.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["dominio", "pasta", "tarefas", "amostras", "sp", "sp_hoffmann", "de",
                                          "de_hoffmann", "basico_tarefas", "sp_limite", "obs"],
                           lineterminator="\n", extrasaction="ignore")
        w.writeheader()
        w.writerows(dom)
    val = [d for d in dom if d.get("tarefas")]
    rho_sp = spearmanr([d["sp"] for d in val], [d["sp_hoffmann"] for d in val]).statistic
    rho_de = spearmanr([d["de"] for d in val], [d["de_hoffmann"] for d in val]).statistic
    basico_ok = all((d["basico_tarefas"] == d["tarefas"]) if d["dominio"] == "Logistics" else d["basico_tarefas"] == 0
                    for d in val)
    for d in dom:
        print(d)
    print(f"\n{len(val)} domínios com dados; {len(lista)} tarefas")
    print(f"Critério 1 (básico só no Logistics): {'OK' if basico_ok else 'FALHOU'}")
    print(f"Critério 2 (Spearman SP): {rho_sp:.3f} {'OK' if rho_sp >= 0.7 else 'FALHOU'}")
    print(f"Critério 3 (Spearman DE): {rho_de:.3f} {'OK' if rho_de >= 0.7 else 'FALHOU'}")


if __name__ == "__main__":
    main()
