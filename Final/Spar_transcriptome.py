#Producing transcriptome from S paradoxus genome 

#Reading genome reference fasta files
def read_fasta(fastaFile): 
    #create empty dictionary 
    fastaDict = {}
    #iterate through every line in the file 
    chromNum = 0 
    for line in fastaFile: 
        #if it has a > at the start, it is the name of the sequence 
        if line[0] =='>':
            chromNum += 1 
            chromName = chromNum 
            #create newly seen sequence names with empty lists 
            #so that we can append every line as it comes in 
            fastaDict[chromName] = []
        else: 
            #append all the lines that belong to that chromosome 
            fastaDict[chromName].append(line.strip())
    #merge all the lines together 
    #loop over every chromosome and merge all of its lines 
    for chrom in fastaDict: 
            fastaDict[chrom] = ''.join(fastaDict[chrom])
    return fastaDict 

#parse S par reference genome 
x = open("S_paradoxus.fa")
S_par_GenomeDict = read_fasta(x) 
output = open("Spar_transcriptome.fa","w") 

#Change names of chromosomes and names of genes 
S_par_genes = open("S_paradoxus_genes.bed")
for line in S_par_genes: 
    line = line.strip().split() 
    if line[0] == "Spar_1":
        line.insert(0,1)
    if line[0] == "Spar_2":
        line.insert(0,2)
    if line[0] == "Spar_3": 
        line.insert(0,3)
    if line[0] == "Spar_4":
        line.insert(0,4)
    if line[0] == "Spar_5":
        line.insert(0,5) 
    if line[0] == "Spar_6":
        line.insert(0,6)
    if line[0] == "Spar_7":
        line.insert(0,7)
    if line[0] == "Spar_8":
        line.insert(0,8)
    if line[0] == "Spar_9":
        line.insert(0,9)
    if line[0] == "Spar_10":
        line.insert(0,10) 
    if line[0] == "Spar_11":
        line.insert(0,11)
    if line[0] == "Spar_12":
        line.insert(0,12) 
    if line[0] == "Spar_13":
        line.insert(0,13) 
    if line[0] == "Spar_14":
        line.insert(0,14)
    if line[0] == "Spar_15":
        line.insert(0,15)
    if line[0] == "Spar_16":
        line.insert(0,16)
    stop = line[4].find('.')
    if stop == -1: 
        gene_name = line[4]
    else: 
        gene_name = line[4][:stop]
    #gene sequence is from the number at line 2 until the number at line 3 (+1)
    gene_seq = S_par_GenomeDict[line[0]][int(line[2]):(int(line[3])+1)]
    #generate outputfile with gene names and gene sequences (aka transcriptome) 
    output.write(">%s\n%s\n" %(gene_name, gene_seq)) 

x.close()
output.close() 
