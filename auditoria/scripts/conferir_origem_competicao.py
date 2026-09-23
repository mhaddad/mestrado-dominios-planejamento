"""Confere a origem dos pares planejador × domínio que 2010 marca como "competição".

Para cada par com origem_do_dado == "competicao" em data/2010/eficiencia_planejadores.csv:
1. verifica se o planejador participou de alguma IPC que usou o domínio (listas abaixo,
   tiradas dos relatórios oficiais de cada competição);
2. procura log de execução própria de 2010 no acervo e, se houver, conta os planos.

Fontes das listas:
- IPC 1998: McDermott (2000), AI Magazine 21(2), DOI 10.1609/aimag.v21i2.1506.
- IPC 2000: Bacchus (2001), AI Magazine 22(3), DOI 10.1609/aimag.v22i3.1571, Tabela 1.
- IPC 2002: Long e Fox (2003), JAIR 20, DOI 10.1613/jair.1240, Figura 1 e Apêndice A.
- IPC 2004: Hoffmann e Edelkamp (2005), JAIR 24, DOI 10.1613/jair.1677, Tabela 1 e seção 2.
- IPC 2006: https://ipc06.icaps-conference.org/deterministic/results.html e IPC5-results.tgz
  (pastas de resultados por planejador e domínio).

Saída: auditoria/extracao/conferencia-origem-competicao.csv
Uso: python auditoria/scripts/conferir_origem_competicao.py
"""
import csv
import os
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
LOGS = RAIZ / "acervo-2010/planejadores_analise_resultados/comp/planners/resultados"
SAIDA = RAIZ / "auditoria/extracao/conferencia-origem-competicao.csv"

# Domínios de 2010 presentes em cada IPC (só os que importam aqui).
DOMINIOS = {
    1998: {"gripper", "logistics", "mystery"},
    2000: {"blocksworld", "logistics"},
    2002: {"depots", "driverlog", "satellite"},
    2004: {"pipesworld", "satellite"},
    2006: {"pathways", "pipesworld", "tpp"},
}
# Planejadores de 2010 que participaram de cada IPC. Na IPC 2006, o Fast Downward de 2004
# rodou como referência (pasta downward.ipc04 dos resultados oficiais).
PARTICIPANTES = {
    1998: {"Blackbox", "IPP"},
    2000: {"Blackbox", "IPP", "FF", "R"},
    2002: {"FF", "LPG"},
    2004: {"Fast Downward", "YAHSP", "SGPlan", "LPG", "SATPlan"},
    2006: {"SGPlan", "SATPlan", "MaxPlan", "Fast Downward"},
}
PASTA = {"Blackbox": "blackbox", "IPP": "ipp", "FF": "ff", "R": "r", "LPG": "lpg",
         "Fast Downward": "fastdownward", "YAHSP": "yahsp", "SGPlan": "sgplan",
         "SATPlan": "satplan", "MaxPlan": "maxplan"}
ALIAS = {"logistics": "logistic", "pathways": "pathway"}
# Como contar um plano em cada formato de log.
PLANO = {"r": lambda texto: len([l for l in texto.splitlines() if l.strip()]),
         "fastdownward": lambda texto: len(re.findall(r"Solution found", texto))}


def main() -> None:
    saida = []
    with (RAIZ / "data/2010/eficiencia_planejadores.csv").open(encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r["origem_do_dado"] != "competicao":
                continue
            dom, pl = r["dominio"], r["planejador"]
            ipcs = [ano for ano in DOMINIOS if dom in DOMINIOS[ano] and pl in PARTICIPANTES[ano]]
            pasta = LOGS / PASTA[pl]
            logs = [f for f in os.listdir(pasta) if ALIAS.get(dom, dom) in f.lower()] if pasta.is_dir() else []
            planos = ""
            if logs and PASTA[pl] in PLANO:
                planos = str(PLANO[PASTA[pl]]((pasta / logs[0]).read_text(errors="replace")))
            saida.append({
                "dominio": dom, "planejador": pl, "eficiencia_pct": r["eficiencia_competicao_pct"],
                "ipc_compativel": ";".join(map(str, ipcs)) or "nenhuma",
                "log_execucao_propria": ";".join(logs), "planos_no_log": planos,
                "origem_provavel": "competicao" if ipcs and not logs else "execucao_propria",
            })
    with SAIDA.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(saida[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(saida)
    erradas = [s for s in saida if s["origem_provavel"] != "competicao"]
    print(f"{len(saida)} pares marcados como competição; {len(erradas)} com origem provável em execução própria")
    for s in erradas:
        print(f"  {s['dominio']} × {s['planejador']}: {s['eficiencia_pct']}%, IPC compatível: {s['ipc_compativel']}, "
              f"log: {s['log_execucao_propria']}, planos: {s['planos_no_log']}")


if __name__ == "__main__":
    main()
