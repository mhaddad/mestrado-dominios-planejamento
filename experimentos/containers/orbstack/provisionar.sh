#!/usr/bin/env bash
# Prepara a máquina da Fase 3 no OrbStack (Ubuntu 22.04 amd64).
#
# Uso, no macOS:
#   orb create --arch amd64 ubuntu:jammy fase3-amd64
#   orb -m fase3-amd64 -u root bash experimentos/containers/orbstack/provisionar.sh
#
# Por que 22.04: é a última LTS com o pacote python2, exigido pelo tradutor do
# Fast Downward de 2010. Por que amd64: os planejadores de 2010 são binários
# ELF 32-bit i386; neste Mac (Apple M4), o OrbStack executa x86_64 via Rosetta
# e i386 via QEMU (binfmt qemu-i386), por isso precisamos das bibliotecas i386.
set -euo pipefail
dpkg --add-architecture i386
apt-get update -qq
DEBIAN_FRONTEND=noninteractive apt-get install -y -qq \
  libc6:i386 libstdc++6:i386 libgcc-s1:i386 libncurses5:i386 libtinfo6:i386 zlib1g:i386 \
  python2 tcl file time perl curl
# SWI-Prolog 3.2.9 (usado pelo planejador R, binário i386 de 2010) precisa de
# libreadline.so.5, que saiu do Ubuntu depois do 20.04. Pacote oficial do 20.04:
RL=libreadline5_5.2+dfsg-3build3_i386.deb
curl -fsSL -o /tmp/$RL http://archive.ubuntu.com/ubuntu/pool/main/r/readline5/$RL
dpkg -i /tmp/$RL
# Registro do ambiente (vai para a saída; copie para o registro do experimento)
echo "== ambiente"
uname -m
grep -m1 "model name" /proc/cpuinfo
lsb_release -ds
python2 --version 2>&1
echo 'puts [info patchlevel]' | tclsh
ls /proc/sys/fs/binfmt_misc/ | tr '\n' ' '; echo
