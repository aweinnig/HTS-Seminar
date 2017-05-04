# Create a 4 coumn file (with column names) to be read into R 

import gffutils 
import pysam 

#load the database and sorted bamfiles 
db = gffutils.FeatureDB("yeast.db")
BY = pysam.AlignmentFile("outputBY.sorted.bam")
RM = pysam.AlignmentFile("outputRM.sorted.bam") 

#open output file 
two_gene_counts = open ("two_yeast_counts.txt","w")

two_gene_counts.write("gene_name\tgene_length\tBY_expression\tRM_expression\n")
#Loop over all the gene using gffutils, just like in problem 1 
for mRNA in db.features_of_type("mRNA"): 
    if mRNA.chrom == "chrmt": continue
    gene_length = db.children_bp(mRNA, child_featuretype = "CDS")
    #Get expression counts 
    countBY = BY.count(mRNA.chrom, mRNA.start, mRNA.stop)  
    countRM = RM.count(mRNA.chrom, mRNA.start, mRNA.stop) 
    two_gene_counts.write("%s\t%d\t%d\t%d\n" %(mRNA["Name"], gene_length, countBY, countRM))

two_gene_counts.close()
