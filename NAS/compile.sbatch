#!/usr/bin/env bash
#SBATCH -o compile.out
#SBATCH -e compile.err
#SBATCH -t 00:09:00
#SBATCH -p risc5
#SBATCH -N 1
#SBATCH --mail-user=pdiehl@cct.lsu.edu
#SBATCH --exclusive
#SBATCH -c 64

module load openmpi

for exe in cg ep is ft mg sp
do
  for c in A B C D E F
  do
    make $exe CLASS=$c VERBOSE=1
  done
done

