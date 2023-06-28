configfile: "config.yaml"

rule repeat_mask:
    input:
        input_fa = config["data"]["genome"]
    output:
        genome_fa_out_gff = "01_rep_mask/repMask/genome.fa.out.gff"
    threads: 24
    params:
        species = config["TargetGenome"],
        species_rep = config["species_rep"]
    shell:
        "mkdir -p 01_rep_mask/repMask && " \
        "RepeatMasker -pa {threads} -species {params.species_rep} -q -no_is -norna -nolow  -dir 01_rep_mask/repMask {input.input_fa} && " \
        "perl scripts/ConvertRepeatMasker2gff.pl 01_rep_mask/repMask/{params.species}.fa.out {output.genome_fa_out_gff}  TE "

rule repeat_modeler:
    input:
        input_fa = config["data"]["genome"]
    output:
        genome_fa_out_gff  = "01_rep_mask/repMod/genome.fa.out.gff"
    threads: 24
    params:
        species = config["TargetGenome"]
    shell:
        "mkdir -p 01_rep_mask/repMod && " \
        "RepeatMasker -pa {threads}  -q -no_is -norna -nolow  -poly -dir 01_rep_mask/repMod -lib ./lib/consensi.fa.classified  {input.input_fa} && " \
        "perl scripts/ConvertRepeatMasker2gff.pl " \
        "01_rep_mask/repMod/{params.species}.fa.out   {output.genome_fa_out_gff}  Denovo " \

rule mergeAndcut_all:
    input:
        repMask_gff = "01_rep_mask/repMask/genome.fa.out.gff",
        repMod_gff =  "01_rep_mask/repMod/genome.fa.out.gff",
        repPro_gff = "01_rep_mask/repPro/genome.fa.annot.gff",
        repTrf_gff = "01_rep_mask/repTrf/genome.fa.trf.gff"
    output:
        rep_merge_all_cut_gff = "01_rep_mask/merge_all/rep_merge_all_cut.gff"
    shell:
        "mkdir -p 01_rep_mask/merge_all && " \
        "cat {input.repMask_gff} {input.repMod_gff} {input.repPro_gff} {input.repTrf_gff} >  01_rep_mask/merge_all/rep_merge_all.gff && " \
        "cut  -f 1,4,5 01_rep_mask/merge_all/rep_merge_all.gff > {output} "

rule bedtools:
    input:
        rep_merge_all_cut_gff = "01_rep_mask/merge_all/rep_merge_all_cut.gff",
        genome_fa = config["data"]["genome"]
    output:
        rep_merge_all_cut_gff_softmasked = "01_rep_mask/merge_all/rep_merge_all_cut_gff.softmasked"
    shell:
        "bedtools  maskfasta -soft -fi {input.genome_fa} -bed  {input.rep_merge_all_cut_gff}   -fo  01_rep_mask/merge_all/rep_merge_all_cut_gff.softmasked " \
        # "sed 'y/atcg/NNNN/'  01_rep_mask/merge_all/rep_merge_all_cut_gff.softmasked  > {output.rep_merge_all_cut_gff_hardmasked} "

rule all:
    input:
        "01_rep_mask/repMask/genome.fa.out.gff",
        "01_rep_mask/repMod/genome.fa.out.gff",
        "01_rep_mask/merge_all/rep_merge_all_cut_gff.softmasked"






