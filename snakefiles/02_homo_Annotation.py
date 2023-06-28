configfile: "config.yaml"

include: "04_de_novoAnnotation.py"
include: "03_trans_Annotation.py"

rule homology_Annotation:
    input:
        target_genome = config["data"]["genome"],
        ref_genome = config["data"]["ref_genome"]["ref_genomic_fna"],
        ref_gff=  config["data"]["ref_genome"]["ref_genomic_gff"]
    threads: config["cpus"]
    output:
        state = "02_homology_Annotation/result.fa_state"
    shell:
        # "mkdir 02_homology_Annotation && " \
        "java -Xms200g -Xmx200g -jar   data/GeMoMa/GeMoMa-1.9.jar CLI GeMoMaPipeline threads={threads} " \
        "s=own  t={input.target_genome}  a={input.ref_gff}  g={input.ref_genome} " \
        "outdir=02_homology_Annotation AnnotationFinalizer.r=NO   tblastn=false && " \
        "echo 'hava done homology_Annotation' > {output.state} "

rule all:
    input:
        "02_homology_Annotation/result.fa_state",
        # 04_de_novo_Annotation
        expand("04_de_novo_Annotation/{sample}_genome_ab.gff", sample=config["SplitNumbers"]),

        "03_trans_Annotation/transAnnota/annota_state",
        "03_trans_Annotation/transAnnota/genome_rna.gff"







