#!/bin/bash

cpus=$(cat /proc/cpuinfo | grep processor | wc -l)

### 00 split_genome for parallel running
echo "=============00 split genome...==============="
snakemake -s snakefiles/00_split_genome.py -p --cores 1 all

#### 01 start repeat_trf to avoid a bug in snakemake shell,for example: sh scripts/repeat_trf.sh  /path/to/genome.fa
echo "=============01 start repeat_trf...==============="
sh scripts/repeat_trf.sh data/genome/c_elegans.fa

#### 01 start repeat_mask, repeat_pro, repeat_mod ,to parallel run repeat_pro
echo "==============01 start repeat_pro...=============="
snakemake -s snakefiles/01_repeat_pro.py -p --cores $cpus all

#### 01 merge repeatAnnotation all gffs
echo "==============01 start repeat_Annotation...========"
snakemake -s snakefiles/01_repeatAnnotation.py -p --cores $cpus all

#### parallel running 02_homo_Annotationo,03_trans_Annotation，04_de_novo_Annotation to reduce running time
echo "=============start  02_homo_Annotationo,03_trans_Annotation，04_de_novo_Annotationrepeat_Annotation...========"
snakemake -s snakefiles/04_de_novo_split.py -p --cores 1 all
snakemake -s snakefiles/02_homo_Annotation.py -p --cores $cpus all
snakemake -s snakefiles/02_homo_Annotation_ConvertFormat.py -p --cores 1 all

echo "=============05 start evm merge...========"
#### 05 evm results
snakemake -s snakefiles/05_evm_pre.py -p --cores $cpus all
snakemake -s snakefiles/05_evm_parallel.py -p --cores $cpus all
snakemake -s snakefiles/05_evm_merge.py -p --cores 1 all

####busco evaluation
#echo "============busco evaluation... ============="
#snakemake -s snakefiles/busco_result.py -p --cores $cpus all
