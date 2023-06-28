configfile: "config.yaml"
rule split_genome:
    input:
        config["data"]["genome"]
    output:
        genome_split = "data/split_genome/genome_split",
        genome_split_state = "data/split_genome/genome_split_state"
    shell:
        "mkdir  -p data/split_genome && " \
        "seqkit seq -w0 {input}  > {output.genome_split} && " \
        "perl  scripts/split_genome.pl 5000000  {output.genome_split} && " \
        "mv Split-*.fa data/split_genome && echo 'have done' > {output.genome_split_state}"
rule all:
    input:
        "data/split_genome/genome_split_state"







