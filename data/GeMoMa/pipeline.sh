#!/bin/bash
jar=$(eval "ls GeMoMa-*.jar")

# This script allows to run the complete GeMoMa pipeline multithreaded from the command line. 
# The final prediction is located in ${out}/filtered_predictions.gff.
#
# A simple example without RNA-seq using tblastn is
# ./pipeline.sh tblastn tests/gemoma/target-fragment.fasta tests/gemoma/ref-annotation.gff tests/gemoma/ref-fragment.fasta 1 results/sw-pipeline

#parameters
if [ "$1" == "tblastn" ]
then
	tblastn=true;
else 
	tblastn=false;
fi
target_genome=$2
ref_annotation=$3
ref_genome=$4
threads=$5
out=$6

if [ $# -ne 6 ]; then
	lib=$7;
	reads=$8;
	echo "GeMoMa using RNA-seq data: library type=" $lib "mapped reads=" $reads
	time java -jar $jar CLI GeMoMaPipeline threads=$threads t=$target_genome s=own a=$ref_annotation g=$ref_genome tblastn=${tblastn} outdir=$out r=MAPPED ERE.s=$lib ERE.m=$reads ERE.c=true AnnotationFinalizer.r=NO
else 
	echo "GeMoMa without RNA-seq data"
	time java -jar $jar CLI GeMoMaPipeline threads=$threads t=$target_genome s=own a=$ref_annotation g=$ref_genome tblastn=${tblastn} outdir=$out AnnotationFinalizer.r=NO
fi