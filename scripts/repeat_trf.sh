#!/bin/bash

if [ -f "01_rep_mask/repTrf/genome.fa.trf.gff" ]
then
  echo "Nothing to be done, have created genome.fa.trf.gff"
  exit
fi	

if [ -n "$1" ]
then
    echo "start running $1 repeat_trf ..."
else
    echo "error!!!,please input genome,for example: /data/genome/c_elegans.fa"
fi
mkdir -p 01_rep_mask/repTrf
trf $1  2 7 7 80 10 50 2000 -d  -h 
mv *.dat  01_rep_mask/repTrf

perl scripts/ConvertTrf2Gff.pl  01_rep_mask/repTrf/*.2.7.7.80.10.50.2000.dat   01_rep_mask/repTrf/genome.fa.trf.gff
