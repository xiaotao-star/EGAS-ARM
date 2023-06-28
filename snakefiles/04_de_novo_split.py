configfile: "config.yaml"
rule split_genome:
    input:
        rep_softmasked = "01_rep_mask/merge_all/rep_merge_all_cut_gff.softmasked"
    output:
        rep_softmasked_split = "data/split_repAnno/rep_merge_all_cut_gff.softmasked.out",
        rep_hardmasked_split_state = "data/split_repAnno/rep_split_state"
    priority: 10
    shell:
        "mkdir  -p data/split_repAnno && " \
        "seqkit seq -w0 {input}  > {output.rep_softmasked_split} && " \
        "perl  scripts/split_genome.pl 5000000  {output.rep_softmasked_split} && " \
        "mv Split-*.fa data/split_repAnno/  && echo 'have done' > {output.rep_hardmasked_split_state}"
rule all:
    input:
        "data/split_repAnno/rep_split_state"
