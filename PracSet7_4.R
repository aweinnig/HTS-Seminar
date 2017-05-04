#Read in the table using fread 
library(data.table)
counts = fread("~/Desktop/sequencing_class/two_yeast_counts.txt")
counts

#4d - Using data.table syntax, compute the log fold change of every gene in ONE LINE. NB: log fold-change means log2(BY_expression/RM_expression) i.e. how many factors of 2 you need to get from the RM expression level to the BY expression level. 
log_fold <- counts[, .(gene_name,log_fold = log2(BY_expression/RM_expression))]
head(log_fold) # Alot of NaNs because a lot of the RM expression values are 0 so dividing by 0

#4e - Filter out the "bad" rows and redo d 
log_fold_filtered <- counts[with(counts, RM_expression > 0 & BY_expression > 0), .(gene_name, log_fold = log2(BY_expression/RM_expression))]
head(log_fold_filtered)
#Update the data table by removing RM_expression and BM_expression rows with value = 0
counts_filtered <- counts[with(counts, RM_expression > 0 & BY_expression > 0), .(gene_name, gene_length, BY_expression, RM_expression)]

#4f Add pseudo-counts to every gene: 
counts_pseudo <- counts[, .(gene_name, gene_length, BY_pseudo = BY_expression + 1, RM_pseudo = RM_expression +1)]
#add information as a new column to the data.table "counts" 
counts_pseudo <- counts[, BY_pseudo := BY_expression +1]
counts_pseudo

#4g Re-compute the log-fold change using pseudo-counted data: 
log_fold_pseudo <- counts_pseudo[, .(gene_name, log_fold = log2(BY_pseudo/RM_pseudo))]
head(log_fold_filtered)

#4h Compute FPKM values for every gene: 
FPKM <- counts_filtered[, .(gene_name, FPKM_BY = BY_expression/(gene_length*sum(BY_expression)*(10^9)), FPKM_RM = RM_expression/(gene_length*sum(RM_expression)*(10^9)))]
head(FPKM)

#4i Compute the log-fold change of the FPKM values
log_fold_FPKM <- FPKM[, .(gene_name, log_fold_FPKM = log2(FPKM_BY/FPKM_RM))]
head(log_fold_FPKM)