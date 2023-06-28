# EGAS-ARM
## introduction

EGAS-ARM：It is a workflow based on AMR using Snakemake to realize eukaryotic genome annotation process. In the process of eukaryotic genome annotation, the six main steps of data preprocessing, repetitive sequence annotation, de novo prediction annotation, transcriptome annotation, homologous annotation, and result integration were designed and implemented, using well-known methods in the field of genetics Snakemake workflow is written and implemented, including codes such as python scripts and perl scripts.

## Software installation and preparation

1. Install the required software according to the   **SoftwareInstallation ** directory .

2. Download Caenorhabditis elegans data via Baidu SkyDrive:

   and the downloaded data corresponds to the EGAS-ARM directory

## Quick Start

1. install EGAS-ARM:

   ```
   git clone https://github.com/xiaotao-star/EGAS-ARM.git
   ```

2. Modify the **config.yaml** file:

   ```
   cd EGAS-ARM && vim  config.yaml 
   ```

3. run EGAS-ARM:

   ```
   sh GenomeAnnotation.sh
   ```

4. After running EGAS-ARM finished successfully. There are directories with 01_ to 05_ prefix and busco directory.

   The final Annotation file in **05_evm** directories.

## Catalog  Structure

- **scripts:**  Script files for this workflow
- **snakefiles:** Subworkflow files for this workflow
- **SoftwareInstallation:** Source code installation of all software related to this workflow (gcc and BiSheng)
- **data:** Input files and partial output files for the example
- **lib:** About some database files (busco) and training models
- **configs:** Some configuration files about the workflow software, such as: PASA and Augustus

## Citations



