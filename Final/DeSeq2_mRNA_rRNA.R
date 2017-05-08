#Use DeSeq2 for differnetial expression of mRNA 

library(DESeq2)
library(tximport)
library(GenomeInfoDb)
library(rhdf5)

#create named list of files 
mRNA_files = c("/Users/AlexisWeinnig/Desktop/sequencing_class/Final/Spar_mRNA_outputs0/abundance.tsv",
               "/Users/AlexisWeinnig/Desktop/sequencing_class/Final/Spar_mRNA_outputs1/abundance.tsv",
               "/Users/AlexisWeinnig/Desktop/sequencing_class/Final/Scer_mRNA_ouputs0/abundance.tsv",
               "/Users/AlexisWeinnig/Desktop/sequencing_class/Final/Scer_mRNA_ouputs1/abundance.tsv")
names(mRNA_files) = c("Spar_1","Spar_2","Scer_1","Scer_2")

#Read in the kallisto files using tximport 
txdat_mRNA = tximport(mRNA_files, type = "kallisto", txOut=TRUE)

#Create conditions matrix 
coldata_mRNA <- data.frame(condition = c("Spar", "Spar", "Scer", "Scer"))
rownames(coldata_mRNA) = names(mRNA_files)
coldata_mRNA

#Turn it into a DESeq2 object 
#Groups samples by the "condition" column of colData 
dds_mRNA <- DESeqDataSetFromTximport(txdat_mRNA, colData = coldata_mRNA, design =~ condition)

#Run differential expression 
dds_mRNA <- DESeq(dds_mRNA)

#Summarize results 
res_mRNA <- results(dds_mRNA)
res_mRNA
summary(res_mRNA)
res_mRNA_sig = subset(res_mRNA, padj < 0.1)
#head(res_mRNA_sig[order(res_mRNA_sig$log2FoldChange),])
write.csv(as.data.frame(res_mRNA_sig[order(res_mRNA_sig$log2FoldChange),]), file = "mRNAresults.csv")

#plotmA - shows the log 2 fold changes attributable to a given variable over the mean of normalized counts 
plotMA(res_mRNA_sig)

#plotDispEsts - visualizes DESeq2's dispersion estimates 
plotDispEsts(dds_mRNA)

#Calculate the sum of p-values 
nom_pvalue_nb_mRNA = sum(res_mRNA$pvalue < 0.1, na.rm = TRUE)
nom_pvalue_nb_mRNA

#Calculate sum of adjusted p-values 
false_discovery_nb_mRNA = sum(res_mRNA$padj < 0.1, na.rm = TRUE)
false_discovery_nb_mRNA

#Use DESeq2 for differential ribosomal occupancy, essentially treating the ribosomal profiling data as if it were mRNA seq data 
#Create list of files 
rRNA_files = c("/Users/AlexisWeinnig/Desktop/sequencing_class/Final/Spar_rRNA_outputs0/abundance.tsv",
               "/Users/AlexisWeinnig/Desktop/sequencing_class/Final/Spar_rRNA_outputs1/abundance.tsv",
               "/Users/AlexisWeinnig/Desktop/sequencing_class/Final/Scer_rRNA_outputs0/abundance.tsv",
               "/Users/AlexisWeinnig/Desktop/sequencing_class/Final/Scer_rRNA_outputs1/abundance.tsv")
names(rRNA_files) = c("Spar1", "Spar2", "Scer1", "Scer2")

#read in the kallisto files using tximport
txdat_rRNA = tximport(rRNA_files, type = "kallisto", txOut = TRUE)

#create the conditions matrix 
coldata_rRNA = data.frame(condition = c("Spar","Spar","Scer","Scer"))
rownames(coldata_rRNA) = names(rRNA_files)
coldata_rRNA

#Turn it into a DESeq2 object 
dds_rRNA = DESeqDataSetFromTximport(txdat_rRNA, colData = coldata_rRNA, design =~ condition)

#Run differential expression 
dds_rRNA = DESeq(dds_rRNA)

#Summarize results 
res_rRNA = results(dds_rRNA)
res_rRNA
summary(res_rRNA)
res_rRNA_sig = subset(res_rRNA, padj < 0.1)
#head(res_rRNA_sig[order(res_rRNA_sig$log2FoldChange),])
write.csv(as.data.frame(res_rRNA_sig[order(res_rRNA_sig$log2FoldChange),]), file = "rRNAresults.csv")

#MApot 
plotMA(res_rRNA_sig)

#Dispersion plot 
plotDispEsts(dds_rRNA)

#Calculate sum of p-value below 0.1 
nom_pvalue_nb_rRNA = sum(res_rRNA$pvalue < 0.1, na.rm = TRUE)
nom_pvalue_nb_rRNA

#Calculate the sum of adjusted p-values 
false_discovery_nb_rRNA = sum(res_rRNA$padj <0.1, na.rm = TRUE)
false_discovery_nb_rRNA

#Use DESeq2 to calcualte differential translational efficiency 
#translational efficiency = ribosomal occupancy (counts from ribosome prpfiling experiment) normalized by the mRNA abundance (counts from mRNA experiment)
#this disentangles whether degree of protein synthesis results from a few ribosomes working to make many mRNA, or its alot of ribosomes working to make a few mRNAs
trans_eff_files = c("/Users/AlexisWeinnig/Desktop/sequencing_class/Final/Spar_mRNA_outputs0/abundance.tsv",
                    "/Users/AlexisWeinnig/Desktop/sequencing_class/Final/Spar_mRNA_outputs1/abundance.tsv",
                    "/Users/AlexisWeinnig/Desktop/sequencing_class/Final/Scer_mRNA_ouputs0/abundance.tsv",
                    "/Users/AlexisWeinnig/Desktop/sequencing_class/Final/Scer_mRNA_ouputs1/abundance.tsv",
                    "/Users/AlexisWeinnig/Desktop/sequencing_class/Final/Spar_rRNA_outputs0/abundance.tsv",
                    "/Users/AlexisWeinnig/Desktop/sequencing_class/Final/Spar_rRNA_outputs1/abundance.tsv",
                    "/Users/AlexisWeinnig/Desktop/sequencing_class/Final/Scer_rRNA_outputs0/abundance.tsv",
                    "/Users/AlexisWeinnig/Desktop/sequencing_class/Final/Scer_rRNA_outputs1/abundance.tsv")
names(trans_eff_files) = c("SparmRNA1","SparmRNA2","ScermRNA1","ScermRNA2","SparrRNA1","SparrRNA2","ScerrRNA1","ScerrRNA2")

#Read in the kallisto files using tximport 
txdat_trans_eff = tximport(trans_eff_files, type = "kallisto", txOut = TRUE)

#Create the condition matrix 
coldata_trans_eff = data.frame(condition = c("Spar","Spar","Scer","Scer","Spar","Spar","Scer","Scer"), assay = c("mRNA","mRNA","mRNA","mRNA","rRNA","rRNA","rRNA","rRNA"))
rownames(coldata_trans_eff) = names(trans_eff_files)
coldata_trans_eff

#Turn it into a DESeq2 object 
dds_trans_eff = DESeqDataSetFromTximport(txdat_trans_eff, colData = coldata_trans_eff, design =~ assay + condition + assay:condition)

#Run differential expression 
#LRT = likelihood ratio test = comparing the normal hypothesis to the alternative hypothesis, Ha states that the two expression values are different; H0 states that they are the same, so to test it against the H0, we need to remove the interaction term 
dds_trans_eff = DESeq(dds_trans_eff, test = "LRT", reduced = ~assay + condition)

#Summarize results 
res_trans_eff = results(dds_trans_eff)
res_trans_eff
summary(res_trans_eff)
res_trans_eff_sig = subset(res_trans_eff, padj < 0.1)
#head(res_trans_eff_sig[order(res_trans_eff_sig$log2FoldChange),])
write.csv(as.data.frame(res_trans_eff_sig[order(res_trans_eff_sig$log2FoldChange),]), file = "trans_eff_results.csv")

#MA plot 
plotMA(res_trans_eff_sig)

#Dispersion plot 
plotDispEsts(dds_trans_eff)

#Caluclate the sum of p-value below 0.1
nom_pvalue_nb_trans_eff = sum(res_trans$pvalue <0.1, na.rm = TRUE)
nom_pvalue_nb_trans_eff

#Caluclate the sum of adjusted pvalues
false_discovery_nb_trans_eff = sum(res_trans$padj < 0.1, na.rm = TRUE)
false_discovery_nb_trans_eff

#Scatter plot showing log fold change in mRNA abundance between species bs. log fold change in translation efficiency 
plot(res_mRNA$log2FoldChange, res_trans_eff$log2FoldChange, main = "log fold change of mRNA abundance vs. log fold change in translation efficiency", xlab= "log fold change of mRNA", ylab = "log for change of translation efficiency")
plot(res_mRNA_sig$log2FoldChange, res_trans_eff_sig$log2FoldChange, main = "log fold change of mRNA abundance vs. log fold change in translation efficiency", xlab= "log fold change of mRNA", ylab = "log for change of translation efficiency")

#determining compnsatory evolution (mRNA up, TEdown or mRNAdown, TEup)
#or coordinated evolution (mRNA up, TE up or mRNA down, TE down)
mRNAup_TEdown_sig = length(which(res_mRNA_sig$log2FoldChange>0&res_trans_eff_sig$log2FoldChange<0))
mRNAup_TEdown = length(which(res_mRNA$log2FoldChange>0&res_trans_eff$log2FoldChange<0))
mRNAup_TEdown_sig
mRNAup_TEdown
mRNAdown_TEup_sig = length(which(res_mRNA_sig$log2FoldChange<0&res_trans_eff_sig$log2FoldChange>0))
mRNAdown_TEup = length(which(res_mRNA$log2FoldChange<0&res_trans_eff$log2FoldChange>0))
mRNAdown_TEup_sig
mRNAdown_TEup
mRNAup_TEup_sig = length(which(res_mRNA_sig$log2FoldChange>0&res_trans_eff_sig$log2FoldChange>0))
mRNAup_TEup = length(which(res_mRNA$log2FoldChange>0&res_trans_eff$log2FoldChange>0))
mRNAup_TEup_sig
mRNAup_TEup
mRNAdown_TEdown_sig = length(which(res_mRNA_sig$log2FoldChange<0&res_trans_eff_sig$log2FoldChange<0))
mRNAdown_TEdown = length(which(res_mRNA$log2FoldChange<0&res_trans_eff$log2FoldChange<0))
mRNAdown_TEdown_sig
mRNAdown_TEdown
