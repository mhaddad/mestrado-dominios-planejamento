"""Extrai contabilizacao_problemas.ods (nº de problemas resolvidos por planejador x domínio).

Saída: data/2010/problemas_resolvidos.csv
  dominio, planejador, total_problemas, resolvidos, pct_planilha, celula_vazia
`celula_vazia` = True quando a planilha não tem valor de 'n' (não dá para distinguir
'não executado' de 'zero resolvidos'; a dissertação trata como 0%).
Também compara pct com eficiencia_completa_pct do dataset e imprime divergências.
"""
import csv
import warnings
from pathlib import Path

import pandas as pd

warnings.filterwarnings("ignore")
RAIZ = Path(__file__).resolve().parents[3]
ODS = RAIZ / "acervo-2010/planejadores_analise_resultados/contabilizacao_problemas.ods"
DADOS = RAIZ / "data/2010"

PLANEJADORES = ["Blackbox", "IPP", "FF", "R", "LPG", "Fast Downward", "YAHSP", "SGPlan", "SATPlan", "MaxPlan"]
DOMINIOS = ["blocksworld", "depots", "driverlog", "gripper", "logistics", "mystery",
            "pathways", "pipesworld", "satellite", "tpp", "storage"]  # ordem das linhas da planilha


def main():
    d = pd.read_excel(ODS, sheet_name="Planilha1", header=None, engine="odf")
    linhas = []
    for i, dom in enumerate(DOMINIOS):
        r = d.iloc[2 + i]
        total = int(r[1])
        for j, pl in enumerate(PLANEJADORES):
            n, pct = r[2 + 2 * j], r[3 + 2 * j]
            vazio = pd.isna(n)
            resolvidos = 0 if vazio else int(n)
            pct_v = (0.0 if pd.isna(pct) else float(pct))
            linhas.append([dom, pl, total, resolvidos, round(pct_v, 2), vazio])
    with open(DADOS / "problemas_resolvidos.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["dominio", "planejador", "total_problemas", "resolvidos", "pct_planilha", "celula_vazia"])
        w.writerows(linhas)
    print(f"problemas_resolvidos.csv: {len(linhas)} linhas")

    # conferência interna: resolvidos/total x pct da planilha x tabela 14/15 da dissertação
    ef = {(r["dominio"], r["planejador"]): r for r in csv.DictReader(open(DADOS / "eficiencia_planejadores.csv", encoding="utf-8"))}
    dif = []
    for dom, pl, tot, res, pct, vazio in linhas:
        if dom == "storage":
            continue  # domínio de validação: sem eficiência nas Tabelas 14/15
        doc = float(ef[(dom, pl)]["eficiencia_completa_pct"])
        if abs(round(100 * res / tot) - doc) > 1 or abs(round(pct) - doc) > 1:
            dif.append((dom, pl, res, tot, pct, doc))
    print(f"divergências planilha x dissertação (treino, tolerância 1 p.p.): {len(dif)}")
    for x in dif:
        print("  ", x)


if __name__ == "__main__":
    main()
