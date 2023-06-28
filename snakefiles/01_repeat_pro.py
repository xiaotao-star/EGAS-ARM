configfile: "config.yaml"
rule repeat_pro:
    input:
        "data/split_genome/Split-{sample}.fa"
    output:
        "01_rep_mask/repPro/Split-{sample}.fa.annot.gff"
    priority: 5
    shell:
        "mkdir -p 01_rep_mask/repPro && " \
        "RepeatProteinMask -engine ncbi -noLowSimple -pvalue 1e-04  {input} && " \
        "cp  -r data/split_genome/Split-{wildcards.sample}.fa.*   01_rep_mask/repPro/  && " \
        "perl scripts/ConvertRepeatMasker2gff.pl " \
        "01_rep_mask/repPro/Split-{wildcards.sample}.fa.annot {output}  TP && " \
        "cat {output} >> 01_rep_mask/repPro/genome.fa.annot.gff "
rule all:
    input:
        expand("01_rep_mask/repPro/Split-{sample}.fa.annot.gff", sample=config["SplitNumbers"])






