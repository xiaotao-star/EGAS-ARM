#!/bin/bash

# This script runs 4 tests for GeMoMa. There is a single parameter that states whether "tblastn" or "mmseqs" should be used as search algorithm.

data=tests/gemoma/
search=$1

echo "GeMoMa test using "${search}" as search alogorithm"

sep() {
	echo "";
	echo "#############################################################################";
	echo "";
}

#without
sep
./run.sh ${search} ${data}/target-fragment.fasta ${data}/ref-annotation.gff ${data}/ref-fragment.fasta results/without-${search}/

#with
sep
./run.sh ${search} ${data}/target-fragment.fasta ${data}/ref-annotation.gff ${data}/ref-fragment.fasta results/with-${search}/ FR_UNSTRANDED ${data}/target-accepted_hits.bam

#pipeline without
sep
./pipeline.sh ${search} ${data}/target-fragment.fasta ${data}/ref-annotation.gff ${data}/ref-fragment.fasta 4 results/without-${search}_pipeline/

#pipeline with
sep
./pipeline.sh ${search} ${data}/target-fragment.fasta ${data}/ref-annotation.gff ${data}/ref-fragment.fasta 4 results/with-${search}_pipeline/ FR_UNSTRANDED ${data}/target-accepted_hits.bam

echo ""
sep

ls -l results/*/final*.gff

#sep
#
#echo "difference without RNA-seq:"
#diff <(grep -v "^#" results/without-${search}/final_annotation.gff) <(grep -v "^#" results/without-${search}_pipeline/final_annotation.gff)
#
#sep
#
#echo "difference with RNA-seq:"
#diff <(grep -v "^#" results/with-${search}/final_annotation.gff) <(grep -v "^#" results/with-${search}_pipeline/final_annotation.gff)
