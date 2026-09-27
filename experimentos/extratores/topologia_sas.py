"""Propriedades de topologia de busca de uma tarefa SAS+, na linha de Hoffmann (2011) (Fase 4B).

Fonte do método: Hoffmann, J. Analyzing Search Topology Without Running Any Search. JAIR 41,
2011 (`hoffmann2011analyzing`), seções 3, 4 e 8.1–8.2 e Tabela 3. Não é o TorchLight: é a
alternativa por busca que o próprio artigo chama de search probing (SP) e mostra ser competitiva
com a análise (III) do TorchLight nos benchmarks, mais a taxa de becos sem saída reconhecidos (DE)
e o "resultado básico" da seção 1.

Medidas por tarefa:
  basico            o resultado básico: grafo de suporte acíclico, toda transição inversível e
                    nenhum operador com efeito colateral (mais de uma variável afetada) =>
                    nenhum mínimo local sob h+ (seção 1 e fim da seção 3). Inversível, como na
                    seção 4: a transição (c, c') de x é inversível se existe (c', c) em DTG_x
                    cujas condições estão contidas nas de (c, c').
  frac_inversiveis  fração das transições dos DTGs que são inversíveis nesse sentido
  hff_s0            hFF no estado inicial (plano relaxado do FF, custo unitário)
  hff_custo_s0      soma dos custos dos operadores desse plano relaxado
  amostras          número de estados amostrados
  de_taxa           fração dos estados amostrados sem plano relaxado (beco sem saída
                    reconhecido; coluna DE da Tabela 3)
  sp_taxa           fração dos estados amostrados em que a sondagem acha um estado com hFF menor
                    (coluna SP da Tabela 3); becos sem saída contam como fracasso, como na tabela
  sp_limite         quantas sondagens pararam no limite de tempo ou de avaliações (contadas como
                    fracasso, como o SP1s do artigo)
  sp_dist_media     profundidade média da saída encontrada

Amostragem (seção 8.1): R passeios aleatórios a partir do estado inicial, cada um com comprimento
sorteado uniformemente entre 0 e 5·hFF(s0). Sondagem (seção 8.2): uma iteração do Enforced
Hill-Climbing do FF, isto é, busca em largura por um estado com hFF menor, com poda por helpful
actions e só por caminhos monótonos (estados com hFF igual ao do estado de partida).

Tarefas com axiomas (variáveis derivadas) não são analisadas (status "axiomas").
"""

import random
import time
from collections import deque

import numpy as np

INF = float("inf")


class Tarefa:
    """Tarefa SAS+ lida da saída do tradutor do Fast Downward (formato versão 3)."""

    def __init__(self, texto):
        linhas = [l.strip() for l in texto.split("\n")]
        pos = 0

        def prox():
            nonlocal pos
            pos += 1
            return linhas[pos - 1]

        self.dominios, self.camadas, self.ops, self.custos = [], [], [], []
        self.goal, self.axiomas, self.usa_custo = [], 0, False
        while pos < len(linhas):
            l = prox()
            if l == "begin_metric":
                self.usa_custo = prox() == "1"
            elif l == "begin_variable":
                prox()
                self.camadas.append(int(prox()))
                k = int(prox())
                pos += k
                self.dominios.append(k)
            elif l == "begin_state":
                self.s0 = np.array([int(prox()) for _ in self.dominios], dtype=np.int32)
            elif l == "begin_goal":
                self.goal = [tuple(map(int, prox().split())) for _ in range(int(prox()))]
            elif l == "begin_operator":
                prox()
                prevail = [tuple(map(int, prox().split())) for _ in range(int(prox()))]
                efeitos = []
                for _ in range(int(prox())):
                    x = list(map(int, prox().split()))
                    nc = x[0]
                    conds = [(x[1 + 2 * i], x[2 + 2 * i]) for i in range(nc)]
                    v, pre, post = x[1 + 2 * nc:4 + 2 * nc]
                    efeitos.append((conds, v, pre, post))
                custo = int(prox())
                self.ops.append((prevail, efeitos))
                self.custos.append(custo if self.usa_custo else 1)
            elif l == "begin_rule":
                self.axiomas += 1
        self._compilar()

    def _compilar(self):
        n = len(self.dominios)
        self.base = np.concatenate([[0], np.cumsum(self.dominios)]).astype(np.int64)
        fato = lambda v, c: int(self.base[v] + c)
        self.nfatos = int(self.base[-1])
        # Pré-condição de cada operador: prevail + valores anteriores das variáveis afetadas.
        self.pre_op = []
        for prevail, efeitos in self.ops:
            pre = dict(prevail)
            for _c, v, p, _q in efeitos:
                if p != -1:
                    pre[v] = p
            self.pre_op.append(sorted(pre.items()))
        pv, pval, pidx = [], [], []
        for k, pre in enumerate(self.pre_op):
            for v, c in pre:
                pv.append(v)
                pval.append(c)
                pidx.append(k)
        self._pv = np.array(pv, dtype=np.int64)
        self._pval = np.array(pval, dtype=np.int32)
        self._pidx = np.array(pidx, dtype=np.int64)
        # Unidades relaxadas: uma por (operador, efeito), com as condições do efeito somadas.
        self.u_op, self.u_pre, self.u_add = [], [], []
        for k, (prevail, efeitos) in enumerate(self.ops):
            base_pre = [fato(v, c) for v, c in self.pre_op[k]]
            for conds, v, _p, q in efeitos:
                self.u_op.append(k)
                self.u_pre.append(sorted(set(base_pre + [fato(cv, cc) for cv, cc in conds])))
                self.u_add.append(fato(v, q))
        self.consumidores = [[] for _ in range(self.nfatos)]
        for u, pre in enumerate(self.u_pre):
            for f in pre:
                self.consumidores[f].append(u)
        self.produtores = [[] for _ in range(self.nfatos)]
        for u, f in enumerate(self.u_add):
            self.produtores[f].append(u)
        self.goal_fatos = [fato(v, c) for v, c in self.goal]
        self.n = n

    # ---------------------------------------------------------------- busca
    def aplicaveis(self, s):
        if len(self._pv) == 0:
            return np.arange(len(self.ops))
        falhas = s[self._pv] != self._pval
        ruins = np.bincount(self._pidx[falhas], minlength=len(self.ops))
        return np.flatnonzero(ruins == 0)

    def aplicar(self, s, k):
        t = s.copy()
        for conds, v, _p, q in self.ops[k][1]:
            if all(s[cv] == cc for cv, cc in conds):
                t[v] = q
        return t

    def meta(self, s):
        return all(s[v] == c for v, c in self.goal)

    # ------------------------------------------------------------- relaxação
    def hff(self, s, com_helpful=False):
        """hFF do FF (grafo de planejamento relaxado, custo unitário). Devolve (h, custo, helpful)."""
        nivel_f = {}
        faltam = [len(p) for p in self.u_pre]
        camada = [int(self.base[v] + c) for v, c in enumerate(s)]
        for f in camada:
            nivel_f[f] = 0
        nivel_u = {}
        prontas = [u for u, p in enumerate(self.u_pre) if not p]
        for f in camada:
            for u in self.consumidores[f]:
                faltam[u] -= 1
                if faltam[u] == 0:
                    prontas.append(u)
        metas = set(self.goal_fatos)
        i = 0
        while not metas.issubset(nivel_f):
            if not prontas:
                return INF, INF, []
            novos = []
            for u in prontas:
                nivel_u.setdefault(u, i)
                f = self.u_add[u]
                if f not in nivel_f:
                    nivel_f[f] = i + 1
                    novos.append(f)
            prontas = []
            for f in novos:
                for u in self.consumidores[f]:
                    faltam[u] -= 1
                    if faltam[u] == 0:
                        prontas.append(u)
            i += 1
        # Extração do plano relaxado, das camadas altas para as baixas (FF).
        porcamada = {}
        for g in metas:
            porcamada.setdefault(nivel_f[g], set()).add(g)
        escolhidos, g1 = set(), set()
        for c in range(max(porcamada), 0, -1):
            for g in list(porcamada.get(c, ())):
                if c == 1:
                    g1.add(g)
                melhor, dif = None, INF
                for u in self.produtores[g]:
                    if nivel_u.get(u) == c - 1:
                        d = sum(nivel_f[p] for p in self.u_pre[u])
                        if d < dif:
                            melhor, dif = u, d
                escolhidos.add(melhor)
                for p in self.u_pre[melhor]:
                    lp = nivel_f[p]
                    if lp > 0:
                        porcamada.setdefault(lp, set()).add(p)
        ops = {self.u_op[u] for u in escolhidos}
        h = len(ops)
        custo = sum(self.custos[k] for k in ops)
        helpful = []
        if com_helpful and g1:
            for k in self.aplicaveis(s):
                for conds, v, _p, q in self.ops[k][1]:
                    if int(self.base[v] + q) in g1 and all(s[cv] == cc for cv, cc in conds):
                        helpful.append(int(k))
                        break
        return h, custo, helpful

    # ------------------------------------------------------------ estrutura
    def criterio_basico(self):
        """(basico, frac_inversiveis) conforme Hoffmann (2011), seções 1, 3 e 4."""
        trans = {}  # (v, c, c') -> lista de conjuntos de condições
        suporte = set()
        efeito_colateral = False
        for k, (prevail, efeitos) in enumerate(self.ops):
            vars_ef = {v for _c, v, _p, _q in efeitos}
            if len(vars_ef) > 1:
                efeito_colateral = True
            for conds, v, p, q in efeitos:
                fora = frozenset((pv, pc) for pv, pc in self.pre_op[k] if pv != v) | frozenset(
                    (cv, cc) for cv, cc in conds if cv != v)
                for u, _ in fora:
                    suporte.add((u, v))
                origens = [p] if p != -1 else [c for c in range(self.dominios[v]) if c != q]
                for c in origens:
                    if c != q:
                        trans.setdefault((v, c, q), []).append(fora)
        total = inv = 0
        for (v, c, q), lista in trans.items():
            inversas = trans.get((v, q, c), [])
            for cond in lista:
                total += 1
                if any(ci <= cond for ci in inversas):
                    inv += 1
        # Grafo de suporte acíclico (sem contar laços)?
        adj = {}
        for u, v in suporte:
            if u != v:
                adj.setdefault(u, set()).add(v)
        cor = {}

        def ciclo(x):
            cor[x] = 1
            for y in adj.get(x, ()):
                if cor.get(y) == 1 or (y not in cor and ciclo(y)):
                    return True
            cor[x] = 2
            return False

        import sys
        sys.setrecursionlimit(max(10000, 4 * self.n))
        aciclico = not any(ciclo(x) for x in list(adj) if x not in cor)
        frac = inv / total if total else 1.0
        return (aciclico and inv == total and not efeito_colateral), round(frac, 4)


def traduzir(dom, prob, limite_s):
    """Texto SAS+ do tradutor do Fast Downward da Fase 3 (mesmo ajuste do features_sas), ou o motivo da falha."""
    import os
    import subprocess
    import sys
    import tempfile
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import features_sas
    dom, prob = Path(dom).resolve(), Path(prob).resolve()
    with tempfile.TemporaryDirectory() as tmp:
        sas, copia = Path(tmp) / "output.sas", Path(tmp) / "problema.pddl"
        if features_sas.sem_constantes_duplicadas(dom, prob, copia):
            prob = copia
        try:
            r = subprocess.run([sys.executable, "-m", "fast_downward.translate", str(dom), str(prob),
                                "--sas-file", str(sas)], cwd=tmp,
                               env={**os.environ, "PYTHONPATH": str(features_sas.FD)},
                               capture_output=True, text=True, timeout=limite_s)
        except subprocess.TimeoutExpired:
            return None, f"tempo esgotado na tradução ({limite_s} s)"
        if r.returncode != 0 or not sas.exists():
            return None, f"falha do tradutor ({r.returncode})"
        return sas.read_text(), "ok"


def sondar(tarefa, s, h, limite_s, limite_aval):
    """Uma iteração do EHC do FF a partir de s: (sucesso, profundidade, bateu_limite)."""
    if h == 0:
        return True, 0, False
    inicio = time.time()
    vistos = {s.tobytes()}
    fila = deque([(s, 0)])
    aval = 0
    while fila:
        x, d = fila.popleft()
        _hx, _cx, helpful = tarefa.hff(x, com_helpful=True)
        for k in helpful:
            y = tarefa.aplicar(x, k)
            chave = y.tobytes()
            if chave in vistos:
                continue
            vistos.add(chave)
            hy, _c, _h = tarefa.hff(y)
            aval += 1
            if hy < h:
                return True, d + 1, False
            if hy == h:
                fila.append((y, d + 1))
            if aval >= limite_aval or time.time() - inicio > limite_s:
                return False, None, True
    return False, None, False


def analisar(texto_sas, amostras=10, semente=2010, limite_sonda_s=2.0, limite_sonda_aval=500,
             limite_total_s=120.0):
    inicio = time.time()
    t = Tarefa(texto_sas)
    r = {"variaveis": t.n, "operadores": len(t.ops), "axiomas": t.axiomas}
    if t.axiomas:
        return {**r, "status": "axiomas"}
    r["basico"], r["frac_inversiveis"] = t.criterio_basico()
    h0, c0, _ = t.hff(t.s0)
    r["hff_s0"], r["hff_custo_s0"] = (h0, c0) if h0 < INF else ("inf", "inf")
    if h0 == INF:
        return {**r, "status": "s0 sem plano relaxado"}
    rng = random.Random(semente)
    de = sp = lim = feitos = 0
    dists = []
    for _ in range(amostras):
        if time.time() - inicio > limite_total_s:
            break
        s = t.s0
        for _p in range(rng.randint(0, 5 * h0)):
            ap = t.aplicaveis(s)
            if len(ap) == 0:
                break
            s = t.aplicar(s, int(ap[rng.randrange(len(ap))]))
        h, _c, _ = t.hff(s)
        feitos += 1
        if h == INF:
            de += 1
            continue
        ok, d, bateu = sondar(t, s, h, limite_sonda_s, limite_sonda_aval)
        sp += ok
        lim += bateu
        if ok:
            dists.append(d)
    r.update(amostras=feitos, de_taxa=round(de / feitos, 4) if feitos else "",
             sp_taxa=round(sp / feitos, 4) if feitos else "", sp_limite=lim,
             sp_dist_media=round(sum(dists) / len(dists), 3) if dists else "",
             tempo_s=round(time.time() - inicio, 1),
             status="ok" if feitos == amostras else f"parcial ({feitos}/{amostras}, tempo)")
    return r
