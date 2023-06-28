
rule ConvertFormat_GeMoMa:
    input:
        state = "02_homology_Annotation/result.fa_state"
    output:
        genome_pro_gff = "02_homology_Annotation/genome_pro.gff"
    shell:
        "cat {input} && " \
        "perl scripts/ConvertFormat_GeMoMa.pl  02_homology_Annotation/final_annotation.gff  GeMoMa &&" \
        "mv 02_homology_Annotation/final_annotation.gff_pro.gff  {output}"
rule all:
    input:
        "02_homology_Annotation/genome_pro.gff"






