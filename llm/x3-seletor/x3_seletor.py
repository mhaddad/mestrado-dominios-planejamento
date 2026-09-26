"""X3 (Fase 4): LLM como seletor de planejador, condição anônima (llm/x3-seletor/protocolo.md).

Para cada domínio do EXP-12 e cada modelo, envia ao OpenRouter o prompt de
llm/prompts/x3-anonimo-v1.md com o domínio e a instância p01 do Autoscale e o catálogo dos 29
planejadores do Planner Museum, anônimos (P01–P29, em ordem sorteada com semente fixa, porque a
ordem original é cronológica) e descritos só pelas técnicas da taxonomia 4D. Grava cada resposta
bruta em llm/registros/x3/<rodada>/ e, com `avaliar`, calcula as medidas do EXP-12.

Uso:
  python llm/x3-seletor/x3_seletor.py rodar --rodada teste --dominios blocksworld floortile rovers
  python llm/x3-seletor/x3_seletor.py rodar --rodada principal
  python llm/x3-seletor/x3_seletor.py avaliar --rodada principal [--pontuacao grupo|exata]
  python llm/x3-seletor/x3_seletor.py rodar --rodada nomes --condicao nomes

Condições (protocolo): "anonimo" (P01–P29 descritos só por técnicas) e "nomes" (os mesmos códigos,
ordem e descrições, mais nome do planejador e edição da IPC).

Chave: OPENROUTER_API_KEY no .env da raiz (fora do git). Trava de orçamento: antes de cada
chamada, lê o uso da chave no OpenRouter e para se passar de TETO_USD.
"""
import argparse
import csv
import json
import random
import re
import sys
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ / "experimentos/analise"))
AUTOSCALE = RAIZ / "experimentos/ferramentas/planner-museum/benchmarks/autoscale-unit-cost"
PROMPTS = {"anonimo": RAIZ / "llm/prompts/x3-anonimo-v1.md", "nomes": RAIZ / "llm/prompts/x3-nomes-v1.md"}
REGISTROS = RAIZ / "llm/registros/x3"
MODELOS = ["anthropic/claude-sonnet-5", "openai/gpt-6-sol", "google/gemini-3.1-pro-preview",
           "deepseek/deepseek-v4-pro-0813"]
# max_tokens: 8000 na rodada de teste; 16000 a partir da principal (o DeepSeek esgotou 8000 no raciocínio)
CONFIG = {"reasoning": {"effort": "medium"}, "max_tokens": 16000, "usage": {"include": True}}
TETO_USD = 9.50
LIMITE_ARQUIVO = 40_000  # caracteres; acima disso o arquivo é truncado (protocolo)
SEMENTE_CATALOGO = 2026
INGLES = {
    "Busca progressiva no espaço de estados": "forward (progression) state-space search",
    "Busca em grafo de planejamento": "planning-graph search / plan extraction",
    "Compilação para SAT/CSP": "compilation to SAT/CSP",
    "Decomposição recursiva por metas": "recursive goal decomposition (means-ends, recursive STRIPS)",
    "Busca local": "local search",
    "Busca no espaço de planos parciais": "search in the space of partial plans",
    "Decomposição/particionamento": "decomposition/partitioning into subproblems",
    "Busca por largura/novidade": "width-based / novelty search",
    "Busca simbólica (BDD)": "symbolic search (BDDs)",
    "Busca desacoplada (topologia em estrela)": "decoupled search (star-topology factoring)",
    "Sem heurística": "no heuristic",
    "Heurísticas de relaxação": "delete-relaxation heuristics",
    "Grafo causal": "causal-graph heuristic",
    "Landmarks": "landmarks",
    "Relaxação parcial (red-black)": "partial delete relaxation (red-black)",
    "Heurística de SAT para planejamento": "planning-specific SAT solver heuristic",
    "Contagem de metas": "goal counting",
    "Avaliação heurística da vizinhança": "heuristic evaluation of neighbouring partial plans",
    "Proposicional / STRIPS clássico": "propositional STRIPS",
    "STRIPS/ADL estendido (grafo de planos)": "STRIPS/ADL over a planning graph",
    "Grafos de ação": "action graphs",
    "Proposicional traduzido em SAT/CNF": "propositional encoding in SAT/CNF",
    "Variáveis multivaloradas": "multi-valued (finite-domain) variables",
    "Simbólica (BDD)": "symbolic (BDD) state sets",
    "Lifted (sem aterramento)": "lifted (no grounding)",
    "Planejador único": "single planner",
    "Planejador único com componente plugável": "single planner with a pluggable SAT solver",
    "Portfólio": "portfolio of several planner configurations",
}
DIMENSAO = {"D1": "search", "D2": "heuristic", "D3": "representation", "D4": "architecture"}


def catalogo(condicao="anonimo"):
    """Devolve (texto do catálogo, código -> sigla, código -> códigos com a mesma descrição).
    Ordem sorteada com semente fixa."""
    tec, nome = {}, {}
    with (RAIZ / "auditoria/taxonomia/planejadores_museu_4d.csv").open(encoding="utf-8") as f:
        for r in csv.DictReader(f):
            tec.setdefault(r["sigla"], {}).setdefault(r["dimensao"], []).append(INGLES[r["valor"]])
            nome[r["sigla"]] = f"{r['planejador']} (IPC {r['ipc']})"
    siglas = sorted(tec)
    random.Random(SEMENTE_CATALOGO).shuffle(siglas)
    codigo = {f"P{i + 1:02d}": s for i, s in enumerate(siglas)}
    linhas, descr = [], {}
    for c, s in codigo.items():
        partes = [f"{DIMENSAO[d]}: {' + '.join(tec[s][d]) if d in tec[s] else 'not specified'}" for d in DIMENSAO]
        descr[c] = "; ".join(partes)
        linhas.append(f"{c}: " + (f"{nome[s]}; " if condicao == "nomes" else "") + descr[c])
    iguais = {c: [c2 for c2 in codigo if descr[c2] == descr[c]] for c in codigo}
    return "\n".join(linhas), codigo, iguais


def ler(arq):
    t = arq.read_text(encoding="utf-8", errors="replace")
    if len(t) > LIMITE_ARQUIVO:
        return t[:LIMITE_ARQUIVO] + f"\n; [TRUNCATED: file has {len(t)} characters; first {LIMITE_ARQUIVO} shown]", True
    return t, False


def montar_prompt(dominio, texto_catalogo, condicao):
    md = PROMPTS[condicao].read_text(encoding="utf-8")
    sistema, usuario = re.findall(r"```\n(.*?)```", md, re.S)
    pasta = AUTOSCALE / dominio
    arq_dom = pasta / "domain.pddl" if (pasta / "domain.pddl").exists() else pasta / "domain-p01.pddl"
    dom, t1 = ler(arq_dom)
    inst, t2 = ler(pasta / "p01.pddl")
    usuario = usuario.replace("{catalogo}", texto_catalogo).replace("{dominio}", dom).replace("{instancia}", inst)
    return sistema.strip(), usuario, t1 or t2


def chave():
    for l in (RAIZ / ".env").read_text().splitlines():
        if l.startswith("OPENROUTER_API_KEY="):
            return l.split("=", 1)[1].strip()
    sys.exit("OPENROUTER_API_KEY ausente no .env")


def http(url, corpo=None, k=None, tempo=600):
    req = urllib.request.Request(url, data=json.dumps(corpo).encode() if corpo else None,
                                 headers={"Authorization": f"Bearer {k}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=tempo) as r:
        return json.loads(r.read())


def uso_da_chave(k):
    return float(http("https://openrouter.ai/api/v1/key", k=k)["data"]["usage"])


def extrair_escolha(texto):
    achados = re.findall(r"\{[^{}]*\"planner\"[^{}]*\}", texto or "", re.S)
    if not achados:
        return None, None
    try:
        j = json.loads(achados[-1])
        return str(j.get("planner", "")).strip().upper(), j.get("reason")
    except json.JSONDecodeError:
        m = re.search(r"P\d{2}", achados[-1])
        return (m.group(0) if m else None), None


def chamar(k, modelo, dominio, rodada, texto_catalogo, condicao):
    destino = REGISTROS / rodada / modelo.replace("/", "__") / f"{dominio}.json"
    if destino.exists():
        return "já registrado"
    if uso_da_chave(k) >= TETO_USD:
        return "teto atingido"
    sistema, usuario, truncado = montar_prompt(dominio, texto_catalogo, condicao)
    corpo = {"model": modelo, "messages": [{"role": "system", "content": sistema}, {"role": "user", "content": usuario}],
             **CONFIG}
    inicio = time.time()
    for tentativa in range(3):
        try:
            resp = http("https://openrouter.ai/api/v1/chat/completions", corpo, k)
            break
        except Exception as e:  # noqa: BLE001
            erro = repr(e)
            time.sleep(10 * (tentativa + 1))
    else:
        return f"erro de rede, sem registro (rodar de novo tenta outra vez): {erro[:120]}"
    texto = (resp.get("choices") or [{}])[0].get("message", {}).get("content") if "choices" in resp else None
    escolha, razao = extrair_escolha(texto)
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(json.dumps({
        "modelo_pedido": modelo, "modelo_respondeu": resp.get("model"), "provedor": resp.get("provider"),
        "dominio": dominio, "data_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "config": CONFIG, "condicao": condicao, "prompt": PROMPTS[condicao].name, "semente_catalogo": SEMENTE_CATALOGO, "truncado": truncado,
        "segundos": round(time.time() - inicio, 1), "uso": resp.get("usage"), "escolha": escolha, "razao": razao,
        "resposta": texto, "bruto": resp}, ensure_ascii=False, indent=1), encoding="utf-8")
    return f"{escolha} (US$ {((resp.get('usage') or {}).get('cost') or 0):.4f})"


def rodar(a):
    import nivel4_publicados as N
    _p, cob, _pddl, sas = N.carregar()
    doms = a.dominios or sorted(d for d in cob if cob[d].max() > 0 and d in sas)
    k = chave()
    texto_catalogo, _codigo, _iguais = catalogo(a.condicao)
    print(f"uso da chave antes: US$ {uso_da_chave(k):.4f}; {len(doms)} domínios × {len(MODELOS)} modelos")

    def por_modelo(modelo):
        for d in doms:
            r = chamar(k, modelo, d, a.rodada, texto_catalogo, a.condicao)
            print(f"{modelo:36s} {d:26s} {r}", flush=True)
            if r == "teto atingido":
                return
    with ThreadPoolExecutor(len(MODELOS)) as ex:
        list(ex.map(por_modelo, MODELOS))
    print(f"uso da chave depois: US$ {uso_da_chave(k):.4f}")


def avaliar(a):
    import numpy as np
    from scipy.stats import wilcoxon
    import nivel4_publicados as N
    planejadores, cob, _pddl, sas = N.carregar()
    doms = sorted(d for d in cob if cob[d].max() > 0 and d in sas)
    _t, codigo, iguais = catalogo()
    Y = np.array([cob[d] for d in doms])
    melhor = Y.max(axis=1)
    sbs = [int(np.argmax(Y[[k for k in range(len(doms)) if k != i]].sum(axis=0))) for i in range(len(doms))]
    perda_sbs = melhor - Y[np.arange(len(doms)), sbs]
    linhas, resumo = [], []
    for modelo in MODELOS:
        pasta = REGISTROS / a.rodada / modelo.replace("/", "__")
        perdas, custo, invalidas = [], 0.0, 0
        for i, d in enumerate(doms):
            arq = pasta / f"{d}.json"
            if not arq.exists():
                perdas.append(np.nan)
                continue
            r = json.loads(arq.read_text(encoding="utf-8"))
            custo += float((r.get("uso") or {}).get("cost") or 0)
            sigla = codigo.get(r["escolha"] or "")
            if sigla is None:
                invalidas += 1
                cobertura = float(Y[i].mean())  # resposta inválida: cobertura esperada de uma escolha ao acaso
                grupo = []
            elif a.pontuacao == "exata":
                grupo = [sigla]
                cobertura = float(Y[i, planejadores.index(sigla)])
            else:
                # descrições idênticas não se distinguem: vale a cobertura média do grupo (protocolo)
                grupo = [codigo[c] for c in iguais[r["escolha"]]]
                cobertura = float(np.mean([Y[i, planejadores.index(g)] for g in grupo]))
            p = float(melhor[i] - cobertura)
            perdas.append(p)
            linhas.append({"modelo": modelo, "dominio": d, "codigo": r["escolha"], "planejador": sigla or "",
                           "grupo_de_descricao_igual": " ".join(grupo), "cobertura": round(cobertura, 2),
                           "melhor": int(melhor[i]), "perda": round(p, 2), "razao": r.get("razao") or ""})
        perdas = np.array(perdas)
        ok = ~np.isnan(perdas)
        dif = perda_sbs[ok] - perdas[ok]
        resumo.append({"modelo": modelo, "dominios": int(ok.sum()), "respostas_invalidas": invalidas,
                       "perda_total": round(float(perdas[ok].sum()), 1),
                       "perda_total_sbs_mesmos_dominios": round(float(perda_sbs[ok].sum()), 1),
                       "dominios_perda_zero": int((perdas[ok] == 0).sum()),
                       "wilcoxon_p_vs_sbs": round(float(wilcoxon(dif).pvalue), 3) if ok.sum() > 5 and np.any(dif != 0) else "",
                       "custo_usd": round(custo, 4)})
    saida = RAIZ / "llm/x3-seletor/resultados" / f"{a.rodada}-{a.pontuacao}"
    saida.mkdir(parents=True, exist_ok=True)
    for nome, ls in (("escolhas.csv", linhas), ("resumo.csv", resumo)):
        if ls:
            with (saida / nome).open("w", encoding="utf-8", newline="") as f:
                w = csv.DictWriter(f, fieldnames=list(ls[0]), lineterminator="\n")
                w.writeheader()
                w.writerows(ls)
    for r in resumo:
        print(r)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("acao", choices=("rodar", "avaliar", "catalogo"))
    ap.add_argument("--rodada", default="teste")
    ap.add_argument("--dominios", nargs="*")
    ap.add_argument("--condicao", choices=("anonimo", "nomes"), default="anonimo")
    ap.add_argument("--pontuacao", choices=("grupo", "exata"), default="grupo",
                    help="grupo: média dos planejadores de descrição igual (condição anônima); exata: o planejador escolhido")
    a = ap.parse_args()
    if a.acao == "catalogo":
        texto, codigo, iguais = catalogo(a.condicao)
        print(texto)
        print(codigo)
        print({c: g for c, g in iguais.items() if len(g) > 1})
    else:
        {"rodar": rodar, "avaliar": avaliar}[a.acao](a)


if __name__ == "__main__":
    main()
