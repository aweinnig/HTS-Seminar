#PS6, Question 3 - Quantify expression using gffutils and pysam 
 
import gffutils 
import pysam 
#load the database and sorted bamfile 
db = gffutils.FeatureDB("yeast.db")
bamfile = pysam.AlignmentFile("output.sorted.bam") 
#open output file 
gene_FPKM = open ('yeast_FPKM.txt','w')


gene_read_count = []
gene_name = []
total_read_count = 0.0
gene_length = []
#Loop over all the genes using gffutils, just like in problem 1
for mRNA in db.features_of_type("mRNA"):
    if mRNA.chrom == "chrmt": continue 
    gene_name.append(mRNA["Name"])
    #Quantify expression of each gene using pysam
    count = bamfile.count(mRNA.chrom,mRNA.start, mRNA.stop)
    gene_read_count.append(count)
    total_read_count += count
    CDS_length = db.children_bp(mRNA, child_featuretype = 'CDS')
    gene_length.append(CDS_length)
    #FPKM means you need to divide the counts of each gene by its length, and normalize by the total number of reads that map to genes (keep a counter of how many reads mapped to any gene
for i in range (len(gene_name)):
    FPKM = float(gene_read_count[i])/(gene_length[i]*total_read_count)*10**9
    #Output the FPKM for each gene into a file where one column is gene name and other is FPKM
    gene_FPKM.write("%s\t%d\n" %(gene_name[i],FPKM))

gene_FPKM.close()    



#Does a counter have to be after/within a dictionary? 
