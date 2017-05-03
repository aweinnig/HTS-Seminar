amtools view -bS output.sam > output.bammport samtools
#Map a yeast RNAseq experiment 

#Map the reads using bowtie2 to the yeast genome, ending up with an indexed bam file 
#bowtie2 -x/path/to/index --un /path/to/unmpapped/fastq -1 /path/to/reads_1.fastq -2/path/to/reads_2.fastq -S/path/to/output.sam
bowtie2-build YeastGenome.fa index 
#bowtie2 -x 

#convert sam file into bam file, sort the bam file, index the sorted bam file 
#samtools view -bS output.sam > output.bam
#samtools sort output.bam -o output.sorted.bam 
#samtools index output.sorted.bam 


#Did you get decent mapping statistics (what frac of reads mapped?) 
