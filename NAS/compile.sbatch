
module load openmpi

for exe in cd ep is ft mg sp
do
  for c in A B C D E F
  do
    make $exe CLASS=$c VERBOSE=1
  done
done

