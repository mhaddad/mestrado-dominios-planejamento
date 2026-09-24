#!/usr/bin/env bash
# Teste de fumaça dos 10 planejadores de 2010 na máquina da Fase 3 (OrbStack).
#
# Uso, no macOS, a partir da raiz do repositório:
#   orb -m fase3-amd64 bash experimentos/planejadores/teste_2010.sh [domínio] [problema] [limite_s]
# Padrão: driverlog pfile1 120
#
# O acervo é somente leitura: os planejadores são copiados para ~/fase3/planners-2010
# e rodam de lá (vários escrevem arquivos temporários no diretório corrente).
# As linhas de comando são as dos scripts finais de 2010 (acervo-2010/.../comp/planners/scripts/),
# com caminhos trocados; os binários também vêm de scripts/<planejador>/ quando existem
# (só o IPP difere do binário da pasta principal). Ajustes necessários, registrados aqui:
#   - R: r.execute e bin/* chamam /local/bin/tclsh e /usr/local/bin/pl; na cópia,
#     passam a usar /usr/bin/tclsh e o SWI-Prolog 3.2.9 do próprio acervo.
#   - Fast Downward: translate.py é chamado com python2.
set -uo pipefail
RAIZ="$(cd "$(dirname "$0")/../.." && pwd)"
ACERVO="$RAIZ/acervo-2010/planejadores_analise_resultados/comp"
DOM="${1:-driverlog}"; PROB="${2:-pfile1}"; LIM="${3:-120}"
D="$ACERVO/$DOM/domain.pddl"; P="$ACERVO/$DOM/$PROB"
W="$HOME/fase3/planners-2010"; L="$HOME/fase3/teste-2010/$DOM-$PROB"
mkdir -p "$L"

if [ ! -d "$W" ]; then
  mkdir -p "$(dirname "$W")"
  cp -a "$ACERVO/planners" "$W"
  # R: caminhos e interpretadores da cópia
  sed -i "1s|.*|#!/usr/bin/tclsh|" "$W/r/r.execute" "$W/r/bin/pddl2lower" "$W/r/bin/pl2pddl"
  sed -i "s|^set PL .*|set PL $W/r/pl-3.2.9/src/pl|; s|^set BIN .*|set BIN $W/r/bin|" "$W/r/r.execute"
  # SatPlan: os resolvedores ficam no mesmo diretório do binário
  chmod +x "$W"/*/* "$W"/* 2>/dev/null || true
fi

roda() {  # nome, diretório, comando...
  local nome="$1" dir="$2"; shift 2
  ( cd "$dir" && /usr/bin/time -f "TEMPO=%e s MEMORIA=%M KB" timeout "$LIM" "$@" ) > "$L/$nome.log" 2>&1
  local rc=$?
  printf "%-14s saída=%-3s %s\n" "$nome" "$rc" "$(grep -o 'TEMPO=.*' "$L/$nome.log" | tail -1)"
}

echo "== $DOM / $PROB, limite ${LIM}s"
roda blackbox      "$W/scripts/blackbox"  ./blackbox -o "$D" -f "$P"
roda ipp           "$W/scripts/ipp"       ./ipp -o "$D" -f "$P"
roda ff            "$W/scripts/ff"        ./ff -p "$(dirname "$D")/" -o domain.pddl -f "$(basename "$P")"
roda lpg-td        "$W/scripts/lpg"       ./lpg-td-1.0 -o "$D" -f "$P" -speed -noout
roda yahsp         "$W/scripts/yahsp"     ./yahsp "$D" "$P"
roda sgplan6       "$W"                   ./sgplan6 -o "$D" -f "$P"
roda satplan       "$W/satplan"           ./satplan -domain "$D" -problem "$P"
roda maxplan       "$W/scripts/maxplan"   ./maxplan -o "$D" -f "$P"
roda fastdownward  "$W/fastdownward"      bash -c "python2 translate/translate.py '$D' '$P' && ./preprocess/preprocess < output.sas && ./search/search cCfF < output"
roda r             "$W/r"                 tclsh ./r.execute "$ACERVO/$DOM" "$PROB"
echo "Logs em $L"
