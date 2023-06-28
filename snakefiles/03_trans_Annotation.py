configfile: "config.yaml"
##############step 1###############
rule trans_build:
    input:
        config["data"]["genome"]
    output:
       build_state =  "03_trans_Annotation/build/state"
    threads: 15
    shell:
        "hisat2-build -p {threads} {input} ref_genomic_index &&" \
        "mkdir -p 03_trans_Annotation/build &&" \
        "mv ref_genomic_index.* 03_trans_Annotation/build &&" \
        "echo 'have done' > {output.build_state} "

###############step 2###############
rule trans_comparison:
    input:
        build_state = "03_trans_Annotation/build/state",
        read1 = config["data"]["RNA-seq"]["read1"],
        read2 = config["data"]["RNA-seq"]["read2"]
    output:
        stringtie_gtf = "03_trans_Annotation/comparison/ref_genomic_comparison_stringtie.gtf"
    threads: 25
    shell:
        ## for connect last result
        "cat {input.build_state} && " \ 
        "hisat2 -x 03_trans_Annotation/build/ref_genomic_index   -p {threads}  -X 500 --dta  --fr  --min-intronlen 20  --max-intronlen 600000 " \    
        "-1  {input.read1}   -2  {input.read2}  -S 03_trans_Annotation/comparison/reads.sam && " \
        "samtools view -bS  03_trans_Annotation/comparison/reads.sam   | samtools sort  -o   03_trans_Annotation/comparison/reads.bam && " \
        "stringtie  03_trans_Annotation/comparison/reads.bam     -p {threads}   -o  {output.stringtie_gtf} " \
        # "stringtie  --merge -p {threads}  03_trans_Annotation/comparison/ref_genomic_comparison.gtf -o  {output}"

###############step 3#########################
rule trans_gffread:
    input:
        stringtie_gtf = "03_trans_Annotation/comparison/ref_genomic_comparison_stringtie.gtf",
        # ref_genome = "data/ref_genome/ref_genomic.fna"
        ref_genome = config["data"]["genome"]
    output:
        stringtie_transcript_fa = "03_trans_Annotation/gffread/stringtie_transcript.fa"
    shell:
        "gffread  {input.stringtie_gtf}   -g {input.ref_genome}   -w {output.stringtie_transcript_fa}"

##############Trans Annotation#######################
rule trans_annotation:
    input:
        stringtie_transcript_fa = "03_trans_Annotation/gffread/stringtie_transcript.fa",
        RunPASA_config = config["RunPASA_config"],
        # c_elegans_fa = "data/genome/c_elegans.fa"
        genome_fa = config["data"]["genome"]
    threads:
        config["cpus"]
    output:
        trans_annotation_state = "03_trans_Annotation/transAnnota/annota_state",
        genome_rna_gff = "03_trans_Annotation/transAnnota/genome_rna.gff"
    shell:
        "mkdir -p 03_trans_Annotation/transAnnota && cd 03_trans_Annotation/transAnnota && " \
        "Launch_PASA_pipeline.pl " \
        "--TRANSDECODER -c {input.RunPASA_config} -C -r -R " \
        "-g ../../{input.genome_fa} " \
        "-t ../../{input.stringtie_transcript_fa} " \
        "--ALIGNERS blat --CPU {threads} && " \
        "pasa_asmbls_to_training_set.dbi " \
        "--pasa_transcripts_fasta database.sqlite.assemblies.fasta " \
        "--pasa_transcripts_gff3 database.sqlite.pasa_assemblies.gff3 >  pasa_asmbls_to_training_set.log && " \
        "cp database.sqlite.pasa_assemblies.gff3  ../../{output.genome_rna_gff} && " \
        "echo 'have done trans_annotation' > ../../{output.trans_annotation_state}"

# rule all:
#     input:
#         "03_trans_Annotation/transAnnota/annota_state",
#         "03_trans_Annotation/transAnnota/genome_rna.gff"

