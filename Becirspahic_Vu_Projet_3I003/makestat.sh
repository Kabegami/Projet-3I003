#! /bin/bash

longueur=50
max=$1
prog=$2

while [ $longueur -le $max ]; do
    #while [ $strat -le 5 ]; do
    echo -n "$longueur " >> "stats/$prog"
    python3.4 projet.py <<< "$longueur" | tail -n1 | cut -d':' -f2 >> "stats/$prog"
    longueur=$((longueur+50))
    echo $longueur
done

#gnuplot < makestat_cpu.txt
#gnuplot < makestat_coups.txt
