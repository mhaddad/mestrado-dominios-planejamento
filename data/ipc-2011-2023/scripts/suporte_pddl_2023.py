"""Suporte declarado a recursos do PDDL pelos planejadores da IPC 2023 (Fase 4B).

Cada entrada da IPC 2023 é uma receita `Apptainer.<nome>` na branch
`ipc2023-classical` de um repositório `ipc2023-classical/plannerN`. As regras da
competição exigiam nove rótulos `Supports...` em cada receita, com yes, no ou
partially. O script lê os rótulos e o campo Tracks de todas as receitas.

Serve para separar "não resolveu" de "não suporta" na análise da cobertura.

Uso: python data/ipc-2011-2023/scripts/suporte_pddl_2023.py
Saída: data/ipc-2011-2023/suporte_pddl_2023.csv
"""

import csv
import json
import re
import urllib.request
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
BRUTOS = RAIZ / "brutos" / "2023" / "apptainer"
SAIDA = RAIZ / "suporte_pddl_2023.csv"

ORG = "ipc2023-classical"
BRANCH = "ipc2023-classical"
# Repositórios de planejadores listados em https://ipc2023-classical.github.io/
REPOS = [f"planner{n}" for n in
         [1, 2, 3, 4, 7, 8, 10, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 28, 29, 30, 32, 34]]
RECURSOS = [
    "DerivedPredicates", "UniversallyQuantifiedPreconditions",
    "ExistentiallyQuantifiedPreconditions", "UniversallyQuantifiedEffects",
    "NegativePreconditions", "EqualityPreconditions", "InequalityPreconditions",
    "ConditionalEffects", "ImplyPreconditions",
]


def ler_url(url):
    with urllib.request.urlopen(url) as r:
        return r.read().decode("utf-8", errors="replace")


def receitas(repo):
    cache = BRUTOS / f"{repo}.json"
    if not cache.exists():
        BRUTOS.mkdir(parents=True, exist_ok=True)
        cache.write_text(ler_url(f"https://api.github.com/repos/{ORG}/{repo}/git/trees/{BRANCH}"))
    arvore = json.loads(cache.read_text())["tree"]
    for item in arvore:
        if item["path"].startswith("Apptainer."):
            destino = BRUTOS / f"{repo}.{item['path']}"
            if not destino.exists():
                destino.write_text(ler_url(
                    f"https://raw.githubusercontent.com/{ORG}/{repo}/{BRANCH}/{item['path']}"))
            yield item["path"], destino.read_text()


def valor(texto, rotulo):
    m = re.search(rf"^\s*{rotulo}\s+(.*)$", texto, flags=re.M)
    if not m:
        return "ausente"
    v = m.group(1).strip()
    for chave in ("yes", "no", "partial"):
        if v.lower().startswith(chave):
            return {"yes": "sim", "no": "não", "partial": "parcial"}[chave]
    return v


def main():
    linhas = []
    for repo in REPOS:
        for arquivo, texto in receitas(repo):
            linha = {
                "repositorio": repo,
                "entrada": arquivo.removeprefix("Apptainer."),
                "nome": valor(texto, "Name"),
                "trilhas": valor(texto, "Tracks"),
            }
            for recurso in RECURSOS:
                linha[recurso] = valor(texto, "Supports" + recurso)
            linhas.append(linha)
    with SAIDA.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(linhas[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(linhas)
    print(f"{len(linhas)} receitas -> {SAIDA}")
    for recurso in RECURSOS:
        contagem = {}
        for l in linhas:
            contagem[l[recurso]] = contagem.get(l[recurso], 0) + 1
        print(f"{recurso:38s} {contagem}")


if __name__ == "__main__":
    main()
