#!/bin/bash

##get data
#mkdir NCBI
#cd NCBI
#wget -c https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/001/735/GCF_000001735.4_TAIR10.1/GCF_000001735.4_TAIR10.1_genomic.fna.gz
#wget -c https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/001/735/GCF_000001735.4_TAIR10.1/GCF_000001735.4_TAIR10.1_genomic.gff.gz
#wget -c https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/004/255/GCF_000004255.2_v.1.0/GCF_000004255.2_v.1.0_genomic.fna.gz
#wget -c https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/004/255/GCF_000004255.2_v.1.0/GCF_000004255.2_v.1.0_genomic.gff.gz
#cd ..

##run pipeline
#java -Xms200G -Xmx400G -jar GeMoMa-1.8.jar CLI GeMoMaPipeline threads=20 AnnotationFinalizer.r=NO p=false o=true t=NCBI/GCF_000004255.2_v.1.0_genomic.fna.gz GAF.a="iAA>=0.8" i=thaliana a=NCBI/GCF_000001735.4_TAIR10.1_genomic.gff.gz g=NCBI/GCF_000001735.4_TAIR10.1_genomic.fna.gz outdir=output/

##create syntheny plot
#Rscript synplot.r output/reference_gene_table.tabular 5 output/test lyrata

##run Analyzer
#java -jar GeMoMa-1.8.jar CLI Analyzer t=NCBI/GCF_000004255.2_v.1.0_genomic.gff.gz n="test" p=output/final_annotation.gff w=YES outdir=output/
#Rscript analyze.r output/Comparison_0.tabular

##run BUSCO
java -jar GeMoMa-1.8.jar CLI Extractor Ambiguity=AMBIGUOUS p=true outdir=output/ g=NCBI/GCF_000004255.2_v.1.0_genomic.fna.gz a=output/final_annotation.gff
busco -i output/proteins.fasta -l embryophyta_odb10 -o busco -m proteins
java -jar GeMoMa-1.8.jar CLI BUSCORecomputer b=busco/run_embryophyta_odb10/full_table.tsv i=output/assignment.tabular outdir=output/



