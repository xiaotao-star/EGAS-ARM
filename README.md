# EGAS-ARM
## introduction

EGAS-ARM：It is a workflow based on AMR using Snakemake to realize eukaryotic genome annotation process. In the process of eukaryotic genome annotation, the six main steps of data preprocessing, repetitive sequence annotation, de novo prediction annotation, transcriptome annotation, homologous annotation, and result integration were designed and implemented, using well-known methods in the field of genetics Snakemake workflow is written and implemented, including codes such as python scripts and perl scripts.

## Catalog  Structure

- **scripts:**  Script files for this workflow
- **snakefiles:** Subworkflow files for this workflow
- **SoftwareInstallation:** Source code installation of all software related to this workflow 
- **data:** Input files and partial output files for the example
- **lib:** About some busco database files
- **configs:** Some configuration files about the workflow software, such as: PASA and Augustus

## Software installation and preparation

1. Install the required software according to the   **SoftwareInstallation ** directory .

2. Download Caenorhabditis elegans data via Baidu SkyDrive: 

   链接：https://pan.baidu.com/s/1yRHazt0_6U02UdW_k72Edw 
   提取码：oqgk   

   The downloaded data corresponds to the EGAS-ARM directory.

## Quick Start

1. install EGAS-ARM:

   ```
   git clone https://github.com/xiaotao-star/EGAS-ARM.git
   ```

2. modify the **config.yaml** file:

   ```
   cd EGAS-ARM && vim  config.yaml 
   ```

3. run EGAS-ARM:

   ```
   sh GenomeAnnotation.sh
   ```

4. After running EGAS-ARM finished successfully and there are directories with 01_ to 05_ prefix and busco directory. The final Annotation file in **05_evm** directories.

   

## Citations

1. Holt C, Yandell M. MAKER2: an annotation pipeline and genome-database management tool for second-generation genome projects [J]. BMC bioinformatics, 2011, 12(1):1-14.
2. Brůna T, Hoff KJ, Lomsadze A, et al. BRAKER2: automatic eukaryotic genome annotation with GeneMark-EP+ and AUGUSTUS supported by a protein database [J]. NAR genomics and bioinformatics, 2021, 3(1):lqaa108.
3. Köster J, Rahmann S. Snakemake—a scalable bioinformatics workflow engine [J]. Bioinformatics, 2012, 28(19):2520-2.
4. Seppey M, Manni M, Zdobnov EM. BUSCO: assessing genome assembly and annotation completeness [J]. Gene prediction: methods and protocols, 2019:227-45.
5. Xia J, Cheng C, Zhou X, et al. Kunpeng 920: The first 7-nm chiplet-based 64-Core ARM SoC for cloud services [J]. IEEE Micro, 2021, 41(5):67-75.
6. Hoff KJ, Lange S, Lomsadze A, et al. BRAKER1: unsupervised RNA-Seq-based genome annotation with GeneMark-ET and AUGUSTUS [J]. Bioinformatics, 2016, 32(5):767-9.
7. Yandell M, Ence D. A beginner's guide to eukaryotic genome annotation [J]. Nature Reviews Genetics, 2012, 13(5):329-42.



