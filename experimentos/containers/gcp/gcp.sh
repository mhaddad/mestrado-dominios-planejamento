#!/usr/bin/env bash
# Operação da VM da Fase 3 no Google Cloud (GCP): planejadores de 2010 em x86_64 nativo.
#
# Uso, no macOS, da raiz do repositório:
#   bash experimentos/containers/gcp/gcp.sh <etapa>
# Etapas, em ordem: criar | preparar | enviar | calibrar | rodar | variante | status | buscar | apagar
#
# Por que GCP: os binários de 2010 são ELF 32-bit i386 e rodam nativamente em x86_64 com as
# bibliotecas i386, sem a emulação QEMU do OrbStack (EXP-01, EXP-02). A VM é Spot (barata,
# pode ser interrompida): o executor retoma de onde parou.
#
# Criar a VM gasta créditos do projeto; só rode "criar" com autorização do autor.
set -euo pipefail

PROJETO="${PROJETO:-$(gcloud config get-value project 2>/dev/null)}"
ZONA="${ZONA:-us-central1-c}"    # a e b sem estoque de c2d Spot em 25/09/2026; cota do projeto: 12 vCPUs (avaliação)
TIPO="${TIPO:-c2d-standard-8}"   # 8 vCPUs, 32 GB, AMD EPYC; com 1 thread por núcleo = 4 núcleos
NOME="${NOME:-fase3-2010}"
PARALELOS="${PARALELOS:-4}"       # um por núcleo físico
RAIZ="$(cd "$(dirname "$0")/../../.." && pwd)"
REMOTO='~/repo'

ssh_vm() { gcloud compute ssh "$NOME" --zone "$ZONA" --project "$PROJETO" --command "$1"; }

case "${1:-}" in
  criar)
    gcloud compute instances create "$NOME" --project "$PROJETO" --zone "$ZONA" \
      --machine-type "$TIPO" --threads-per-core 1 \
      --provisioning-model SPOT --instance-termination-action STOP \
      --image-family ubuntu-2204-lts --image-project ubuntu-os-cloud \
      --boot-disk-size 30GB --boot-disk-type pd-balanced
    ;;
  preparar)
    gcloud compute scp "$RAIZ/experimentos/containers/orbstack/provisionar.sh" "$NOME:~/provisionar.sh" \
      --zone "$ZONA" --project "$PROJETO"
    ssh_vm "sudo bash ~/provisionar.sh && lscpu | grep -E 'Model name|^CPU\(s\)|Thread|Core'"
    ;;
  enviar)
    # Só o que os scripts usam: código, dados de 2010 e a pasta comp do acervo (não se altera o acervo)
    pacote="$(mktemp -d)/repo.tgz"
    tar -C "$RAIZ" -czf "$pacote" --exclude experimentos/execucoes/brutos \
      --exclude experimentos/benchmarks --exclude experimentos/ferramentas experimentos data/2010 \
      acervo-2010/planejadores_analise_resultados/comp
    gcloud compute scp "$pacote" "$NOME:~/repo.tgz" --zone "$ZONA" --project "$PROJETO"
    ssh_vm "mkdir -p $REMOTO && tar -C $REMOTO -xzf ~/repo.tgz && cd $REMOTO && \
      bash experimentos/planejadores/teste_2010.sh driverlog pfile1 120"
    ;;
  calibrar)
    ssh_vm "cd $REMOTO && setsid nohup python3 -u experimentos/planejadores/calibrar_2010.py $PARALELOS -gcp \
      > ~/calibracao.log 2>&1 < /dev/null &"
    ;;
  rodar)
    ssh_vm "cd $REMOTO && rm -f ~/fase3/nivel3/PARAR && mkdir -p ~/fase3/nivel3 && \
      setsid nohup python3 experimentos/execucoes/rodar_nivel3_2010.py --paralelos $PARALELOS \
      --fatores experimentos/execucoes/fatores-2010-gcp.csv \
      --resultados experimentos/execucoes/nivel3-2010-gcp.csv --por-ultimo R \
      >> ~/fase3/nivel3/execucao.log 2>&1 < /dev/null &"
    ;;
  variante)
    # Depois da rodada principal: Blackbox no Satellite com -M 8192, como em 2010 (achado G25)
    gcloud compute scp "$RAIZ/experimentos/execucoes/rodar_nivel3_2010.py" \
      "$NOME:$REMOTO/experimentos/execucoes/rodar_nivel3_2010.py" --zone "$ZONA" --project "$PROJETO"
    ssh_vm "cd $REMOTO && rm -f ~/fase3/nivel3/PARAR && \
      setsid nohup python3 experimentos/execucoes/rodar_nivel3_2010.py --paralelos $PARALELOS \
      --fatores experimentos/execucoes/fatores-2010-gcp.csv --variante blackbox-m8192 \
      --resultados experimentos/execucoes/nivel3-2010-gcp-blackbox-m8192.csv \
      >> ~/fase3/nivel3/variante.log 2>&1 < /dev/null &"
    ;;
  status)
    ssh_vm "tail -3 ~/calibracao.log 2>/dev/null; tail -2 ~/fase3/nivel3/execucao.log 2>/dev/null; \
      wc -l $REMOTO/experimentos/execucoes/nivel3-2010-gcp.csv 2>/dev/null; uptime"
    ;;
  buscar)
    for f in calibracao-2010-gcp.csv fatores-2010-gcp.csv nivel3-2010-gcp.csv nivel3-2010-gcp-blackbox-m8192.csv; do
      gcloud compute scp "$NOME:$REMOTO/experimentos/execucoes/$f" "$RAIZ/experimentos/execucoes/$f" \
        --zone "$ZONA" --project "$PROJETO" || true
    done
    ;;
  apagar)
    gcloud compute instances delete "$NOME" --zone "$ZONA" --project "$PROJETO" --quiet
    ;;
  *)
    sed -n '2,12p' "$0"; exit 1 ;;
esac
