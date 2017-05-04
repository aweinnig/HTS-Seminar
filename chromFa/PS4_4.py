#Problem Set 4, Question 4 
from scipy.special import binom 
import pysam

#opening fasta file 
FastaFile = open("YeastGenome.fa") 

#reading in the yeast reference geno
def read_fasta(FastaFile):
	fastaDict = {}
	for line in FastaFile: 
		if line[0] == ">":
			chromName = line.strip()[1:]
			fastaDict[chromName] =[]
		else: 
			fastaDict[chromName].append(line.strip())
	for chrom in fastaDict:
		fastaDict[chrom] = ''.join(fastaDict[chrom])
	return fastaDict 

#parse reference genome 
refGenome = read_fasta(FastaFile) 

#open output file 
outputFile = open('yeast_genome_likelihoods.txt','w')

#seperate function to compute genotype likelihoods
def compute_genotype_likelihood(n, alt_num, e=0.01):
	#computing n will make the code cleaner 
	n = alt_num + ref_num 
	#use binom from scipy.special 
	GLref = binom(n,alt_num)*e**alt_num*(1.0-e)**ref_num 
	GLalt = binom(n,alt_num)*(1.0-e)**alt_num*e**ref_num 
	return GLref, GLalt

#loop over all positions with coverage 

bamfile = pysam.AlignmentFile("output.sorted.bam")
for pileupcolumn in bamfile.pileup():
	#need to get chromosome and position to check the reference genome
	chrom = pileupcolumn.reference_name
	pos = pileupcolumn.pos
	#get the reference genome 
	ref_allele = refGenome[chrom][pos]
	#get the total coverage at this site 
	n = pileupcolumn.n
	#skip the site if coverage is too high 
	if n > 100: continue
	#number of reference alleles seen 
	ref_num = 0 
	#create a dictionary to hold all other possible alleles 
	alt_alleles = {}
	#loop over the reads at that position 
	for pileupread in pileupcolumn.pileups: 
		#skip sites that are indels 
		if pileupread.is_del or pileupread.is_refskip: continue 
		#get the nucleotide from that read  
		read = (pileupread.alignment.query_sequence[pileupread.query_position])
		#if it's not the reference allele, need to add to dictionary ir increment
		if read != ref_allele: 
			if read in alt_alleles: 
				#if it's in the dicitonary, increment 
				alt_alleles[read] += 1 
			else: 
				#if it's not, add one 
				alt_alleles[read] = 1 
		else: 
			#the allele is ref, so count it as one more time seeing ref 
			ref_num += 1 
	#go through and get the alterante allele that's seen the most times 
	#start with seeing 0 
	alt_num = 0 
	#before starting, no alternative allele yet 
	alt_allele = ''
	#loop over all the possilbe alternative alleles 
	for allele in alt_alleles: 
		if alt_alleles[allele] > alt_num:
			#if this allele is seen more than any other, it is the alternative allele 
			alt_num = alt_alleles[allele] 
			alt_allele = allele 
	if alt_num > 0: 
		#if there are more than 0 alt reads, then this is a potenitally variable site, so compute GLs and print
		GLref, GLalt = compute_genotype_likelihood(ref_num, alt_num) 
		outputFile.write("%s\t%d\t%s\t%s\t%f\t%f\n"%(chrom, pos, ref_allele, alt_allele, GLref, GLalt))


bamfile.close()
