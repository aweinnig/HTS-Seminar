#PS6, Question 4 - Find differential expression between two yeast strains 

import gffutils 
import pysam 
import numpy as np 
import scipy.stats as st 
#load the database and sorted bamfiles 
db = gffutils.FeatureDB("yeast.db") 
BY = pysam.AlignmentFile("outputBY.sorted.bam") 
RM = pysam.AlignmentFile("outputRM.sorted.bam") 
#open output file 
two_yeast_DE = open ("two_yeast_DE.txt","w") 

gene_name = []
BYgene_read_count = []
RMgene_read_count = []
BYtotal_read_count = 0.0
RMtotal_read_count = 0.0

#Loop over all the genes using gffutils
for mRNA in db.features_of_type("mRNA"):
    if mRNA.chrom == "chrmt": continue 
    gene_name.append(mRNA["Name"])
    #Quantify expression for each gene for the two diff strands 
    countBY = BY.count(mRNA.chrom, mRNA.start, mRNA.stop) 
    BYgene_read_count.append(countBY) 
    BYtotal_read_count += countBY
    countRM = RM.count(mRNA.chrom, mRNA.start, mRNA.stop) 
    RMgene_read_count.append(countRM)
    RMtotal_read_count += countRM

#compute p-value for if gene is differnetially expressed 
for i in range (len(gene_name)):
    #compute the lambda for the null hypothesis
    lambda_null = (float(BYgene_read_count[i])/BYtotal_read_count + float(RMgene_read_count[i])/RMtotal_read_count)/2
    #compute the lambdas for each experiment seperatly 
    lambda_BY = float(BYgene_read_count[i])/BYtotal_read_count 
    lambda_RM = float(RMgene_read_count[i])/RMtotal_read_count
    #compute the probablitity of the data under the null 
    prob_data_null = st.poisson.pmf(BYgene_read_count[i],BYtotal_read_count*lambda_null)*st.poisson.pmf(RMgene_read_count[i], RMtotal_read_count*lambda_null)
    #compute the probablility of the data under the alt 
    prob_data_alt = st.poisson.pmf(BYgene_read_count[i],BYtotal_read_count*lambda_BY)*st.poisson.pmf(RMgene_read_count[i], RMtotal_read_count*lambda_RM)
    #compute the LRT 
    LRT = 2*(np.log(prob_data_alt) - np.log(prob_data_null))
    #compute the p-value 
    p_value = st.chi2.sf(LRT, df=1)
  #  print lambda_null, lambda_BY, lambda_RM, prob_data_null, prob_data_alt
 #   print BYtotal_read_count, RMtotal_read_count
#    raw_input()

    #Output mRNA name, counts in BY, counts in RM, a p-value for if that gene is differentially expressed 
    two_yeast_DE.write("%s\t%d\t%d\t%f\n" %(gene_name[i],BYgene_read_count[i], RMgene_read_count[i],p_value))

two_yeast_DE.close()
