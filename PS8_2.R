library(tximport)
library(DESeq2)
library(data.table)

#create named list of files 
files = c("/Users/AlexisWeinnig/Desktop/sequencing_class/WT_1/abundance.tsv",
         "/Users/AlexisWeinnig/Desktop/sequencing_class/WT_2/abundance.tsv",
         "/Users/AlexisWeinnig/Desktop/sequencing_class/WT_3/abundance.tsv",
         "/Users/AlexisWeinnig/Desktop/sequencing_class/WT_4/abundance.tsv",
         "/Users/AlexisWeinnig/Desktop/sequencing_class/WT_5/abundance.tsv",
         "/Users/AlexisWeinnig/Desktop/sequencing_class/SNF2_1/abundance.tsv",
         "/Users/AlexisWeinnig/Desktop/sequencing_class/SNF2_2/abundance.tsv",
         "/Users/AlexisWeinnig/Desktop/sequencing_class/SNF2_3/abundance.tsv",
         "/Users/AlexisWeinnig/Desktop/sequencing_class/SNF2_4/abundance.tsv",
         "/Users/AlexisWeinnig/Desktop/sequencing_class/SNF2_5/abundance.tsv")
names(files) = c("WT1","WT2","WT3","WT4","WT5","SNF2_1","SNF2_2","SNF2_3","SNF2_4","SNF2_5")
files 


#use tximport to read in the kallisto files 
txdat = tximport(files, type = "kallisto", txOut=TRUE)

#Generate condtion matrix 
coldata = data.frame(condition=c("WT","WT","WT","WT","WT",
                                   "SNF2","SNF2","SNF2","SNF2","SNF2"))
rownames(coldata) = names(files)
coldata

#turn it into a DESeq2 object, tells it to group samples by the 'condition' column of condmatrix
dds = DESeqDataSetFromTximport(txdat, colData= coldata, design=~ condition)
#run differential expression 
dds = DESeq(dds)
#summarize results 
res = results(dds)
res
plotMA(res)
plotDispEsts(dds)

res$padj
res$pvalue

sum(res$pvalue < .05, na.rm = TRUE)
sum(res$padj < .05, na.rm = TRUE)
