# EGAS-ARM
## introduction

EGAS-ARM：It is a workflow based on AMR using Snakemake to realize eukaryotic genome annotation process. In the process of eukaryotic genome annotation, the six main steps of data preprocessing, repetitive sequence annotation, de novo prediction annotation, transcriptome annotation, homologous annotation, and result integration were designed and implemented, using well-known methods in the field of genetics Snakemake workflow is written and implemented, including codes such as python scripts and perl scripts.

## Quick Start

```
1. git clone https://github.com/xiaotao-star/EGAS-ARM.git
2. cd EGAS-ARM
3. sh startAnnotation.sh 
```

## Catalog  Structure

- **scripts:**  Script files for this workflow
- **snakefiles:** Subworkflow files for this workflow
- **SoftwareInstallation:** Source code installation of all software related to this workflow (gcc and BiSheng)
- **data:** Input files and partial output files for the example
- **lib: **About some database files (busco) and training models
- **configs:** Some configuration files about the workflow software, such as: PASA and Augustus

## Citations



