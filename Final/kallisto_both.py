#Use Kallisto to quanitfy boththe mRNAseq and the ribosomal profiling data 
import os 

S_cer_mRNA_samples = ["Scer_RNA_seq_1.fastq.gz","Scer_RNA_seq_2.fastq.gz"]

for sample in S_cer_mRNA_samples: 
    command = "kallisto quant -i Scer_transcriptome.idx -o Scer_mRNA_ouputs%s --single -l 180 -s 20 %s" % (S_cer_mRNA_samples.index(sample),sample)
    print "currently running: %s" %command 
    os.system(command)

S_cer_rRNA_samples = ["Scer_ribo_seq_1.fastq.gz","Scer_ribo_seq_2.fastq.gz"]

for sample in S_cer_rRNA_samples: 
    command = "kallisto quant -i Scer_transcriptome.idx -o Scer_rRNA_outputs%s --single -l 180 -s 20 %s" % (S_cer_rRNA_samples.index(sample),sample)
    print "currently running: %s" %command 
    os.system(command) 

S_par_mRNA_samples = ["Spar_RNA_seq_1.fastq.gz","Spar_RNA_seq_2.fastq.gz"]

for sample in S_par_mRNA_samples: 
    command = "kallisto quant -i Spar_transcriptome.idx -o Spar_mRNA_outputs%s --single -l 180 -s 20 %s" % (S_par_mRNA_samples.index(sample),sample)
    print "currently running: %s" %command 
    os.system(command) 

S_par_rRNA_samples = ["Spar_ribo_seq_1.fastq.gz","Spar_ribo_seq_2.fastq.gz"]

for sample in S_par_rRNA_samples: 
    command = "kallisto quant -i Spar_transcriptome.idx -o Spar_rRNA_outputs%s --single -l 180 -s 20 %s" % (S_par_rRNA_samples.index(sample),sample)
    print "currently running: %s" %command
    os.system(command) 

