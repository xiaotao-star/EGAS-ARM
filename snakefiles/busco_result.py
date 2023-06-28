configfile: "config.yaml"
rule split_genome:
    input:
        "05_evm/05_gffread_proteins.txt"
    output:
        state = "busco/state"
    params:
        cpus = config["cpus"],
        TargetGenome = config["TargetGenome"]，
        busco_lib=config["busco_lib"]
    shell:
        "busco -f -i  05_evm/{params.TargetGenome}_proteins.fa -o busco -m prot -c  {params.cpus} --offline -l {params.busco_lib}  && " \
        "echo 'have done' > {output}"

rule all:
    input:
        "busco/state"







