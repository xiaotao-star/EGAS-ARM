configfile: "config.yaml"
#========02=================
rule recombine_EVM_partial:
    input:
        commands_txt = "05_evm/01_commands.txt",
        partitions_list_out = "05_evm/partitions_list.out"
    output:
        "05_evm/02_recombine_EVM.txt"
    priority: 1
    shell:
        "cat {input.commands_txt} && cd 05_evm && " \
        "recombine_EVM_partial_outputs.pl " \
        "--partitions ../{input.partitions_list_out} " \
        "--output_file_name  evm.out && " \
        "echo 'have done recombine_EVM' > ../{output} "

#=========03=================
rule convert_EVM_outputs:
    input:
        partitions_list_out = "05_evm/partitions_list.out",
        genome = config["data"]["genome"],
        recombine_EVM_txt = "05_evm/02_recombine_EVM.txt"
    output:
        "05_evm/03_convert_EVM_outputs.txt"
    priority: 1
    shell:
        "cat {input.recombine_EVM_txt} &&  cd 05_evm && " \
        "convert_EVM_outputs_to_GFF3.pl " \
        "--partitions ../{input.partitions_list_out} " \
        "--output evm.out " \
        "--genome   ../{input.genome} && " \
        "echo 'have done convert_EVM_outputs' >  ../{output}"

#=========04=================
rule merge_EVM:
    input:
        EVM_outputs_txt  = "05_evm/03_convert_EVM_outputs.txt"
    output:
        "05_evm/04_merge_EVM_all_gff.txt"
    priority: 0
    shell:
        "cat {input.EVM_outputs_txt} && cd 05_evm && " \
        "cat $(find .  -name 'evm.out.gff3') > genome_EVM.all.gff && " \
        "echo 'have done EVM' > ../{output} "

rule gffread_proteins:
    input:
        merge_EVM_all_gff_txt = "05_evm/04_merge_EVM_all_gff.txt",
        target_genome = config["data"]["genome"]
    output:
        "05_evm/05_gffread_proteins.txt"
    params:
        TargetGenome = config["TargetGenome"]
    shell:
        """
        cat {input.merge_EVM_all_gff_txt} &&
        gffread 05_evm/genome_EVM.all.gff  -g {input.target_genome}  -y  05_evm/{params.TargetGenome}_proteins.fa && \
        echo 'have done gffread_proteins ' > {output}
        """

rule all:
    input:
        ############05_evm_merger###########################
        "05_evm/05_gffread_proteins.txt"

