configfile: "config.yaml"

#========01=================
rule parallel_EVM:
    input:
        "05_evm/01_commands.list"
    output:
        "05_evm/01_commands.txt"
    threads:
        config["cpus"]
    priority: 1
    shell:
        "cd 05_evm && " \
        "parallel -j {threads} < ../{input} && " \
        "echo 'hava done parallel' > ../{output}"
rule all:
    input:
        ############05_evm_merger###########################
        "05_evm/01_commands.txt"


