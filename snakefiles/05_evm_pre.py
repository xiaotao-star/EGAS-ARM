configfile: "config.yaml"
rule partition_EVM_input:
    input:
        # input_fa = "data/genome/c_elegans.fa",
        input_fa = config["data"]["genome"],
        genome_pro_gff = "02_homology_Annotation/genome_pro.gff",
        genome_rna_gff =  "03_trans_Annotation/transAnnota/genome_rna.gff",
        genome_ab_gff = "04_de_novo_Annotation/genome_ab.gff"
    output:
        "05_evm/partitions_list.out"
    priority: 2
    shell:
        "mkdir -p 05_evm && cd 05_evm && " \
        "partition_EVM_inputs.pl " \
        "--genome   ../{input.input_fa} " \
        "--gene_predictions  ../{input.genome_ab_gff} " \
        "--protein_alignments   ../{input.genome_pro_gff} " \
        "--transcript_alignments ../{input.genome_rna_gff} " \
        "--segmentSize 200000 --overlapSize 100000 --partition_listing  ../{output}" \

rule write_EVM_commands:
    input:
        input_fa = config["data"]["genome"],
        partitions_list_out = "05_evm/partitions_list.out",
        genome_pro_gff = "02_homology_Annotation/genome_pro.gff",
        genome_rna_gff =  "03_trans_Annotation/transAnnota/genome_rna.gff",
        genome_ab_gff = "04_de_novo_Annotation/genome_ab.gff"
    output:
        "05_evm/01_commands.list"
    priority: 2
    shell:
        "cd 05_evm && " \
        "write_EVM_commands.pl " \
        "--genome   ../{input.input_fa} " \
        "--weights  $(pwd)/../data/weight.txt " \
        "--gene_predictions  ../{input.genome_ab_gff} " \
        "--protein_alignments   ../{input.genome_pro_gff} " \
        "--transcript_alignments ../{input.genome_rna_gff} " \
        "--output_file_name evm.out " \
        "--partitions partitions_list.out > ../{output} && " \
        "echo 'hava done write_EVM_commands'  > 00_evm.out.txt "

rule all:
    input:
        ############05_evm_pre###########################
        "05_evm/01_commands.list"

