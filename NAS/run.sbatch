#!/usr/bin/env bash
#SBATCH -o run.out
#SBATCH -e run.err
#SBATCH -t 08:59:00
#SBATCH -p risc5
#SBATCH -N 1
#SBATCH --mail-user=pdiehl@cct.lsu.edu
#SBATCH --exclusive
#SBATCH -c 64

module load openmpi

for exe in cd ep is ft mg sp
do
  for c in A B C D 
  do
    mpirun -np 4 --oversubscribe ./bin/$exe.$c.x
  done
done

