import gffutils
#Create database
db = gffutils.FeatureDB("yeast.db")
#print all types of features in the gff 
for type in db.featuretypes():print type 
#print all gene names that have introns
for intron in db.features_of_type("intron"): print intron["Name"]
#What fraction of genes have introns? 
total_genes =  db.count_features_of_type("gene")
print total_genes
genes_w_introns = db.count_features_of_type("intron")
print genes_w_introns
intron_frac = float(genes_w_introns)/(total_genes)
print "The fraction of genes that have introns is ", intron_frac  

#compute length of every gene and write to an output file 
lengths = open ('yeast_gene_lengths.txt','w') 
for mRNA in db.features_of_type("mRNA"):
    CDS_length = db.children_bp(mRNA, child_featuretype = 'CDS')
    lengths.write("%s\t%d\n" %(mRNA["Name"], CDS_length)) 

lengths.close()

