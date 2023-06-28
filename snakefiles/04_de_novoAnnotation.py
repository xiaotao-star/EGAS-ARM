configfile: "config.yaml"

rule augustus:
    input:
        hardmasked =  "data/split_repAnno/Split-{sample}.fa",
        AUGUSTUS_CONFIG_PATH = config["AUGUSTUS_CONFIG_PATH"]
    output:
        "04_de_novo_Annotation/{sample}_rep_all_cut.gff.hardmasked.out"
    params:
        species = config["species_au"]
    shell:
        "augustus --softmasking=1  --AUGUSTUS_CONFIG_PATH={input.AUGUSTUS_CONFIG_PATH} " \
        "--species={params.species} {input.hardmasked} " \
        "--UTR=off > {output}"

rule de_novo_Annotation_ConvertFormat:
    input:
         "04_de_novo_Annotation/{sample}_rep_all_cut.gff.hardmasked.out"
    output:
        "04_de_novo_Annotation/{sample}_genome_ab.gff"
    shell:
        "perl scripts/ConvertFormat_augustus.pl  {input}  {output} && " \
        "cat {output} >> 04_de_novo_Annotation/genome_ab.gff"

#rule all:
#     input:
#         expand("04_de_novo_Annotation/{sample}_genome_ab.gff", sample=config["SplitNumbers"])

