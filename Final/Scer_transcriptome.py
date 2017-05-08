#Producing transcriptome from S cerevisiae genome 

#Reading genome reference fasta files 
def read_fasta(fastaFile): 
    #create empty dictionary 
    fastaDict = {}
    #iterate through every line in the file 
    chromNum = 0 
    for line in fastaFile: 
        #if it has a > at the start, it is the name of the sequence 
        if line[0] == '>': 
            chromNum += 1 
            chromName = chromNum 
            #create newly seen sequence names with empty lists 
            #so that we can append every line as it comes in 
            fastaDict[chromName] = []
        else: 
            #append all the lines that belong to that chromosome 
            fastaDict[chromName].append(line.strip())
    #merge all the lines together 
    #loop over every chromosome and merge all its lines 
    for chrom in fastaDict: 
        fastaDict[chrom] = ''.join(fastaDict[chrom])
    return fastaDict 

#parse S cer reference genome 
x = open("S_cerevisiae.fa")
S_cer_GenomeDict = read_fasta(x) 
output = open("Scer_transcriptome.fa","w") 

#Change names of chromosomes 
S_cer_genes = open("S_cerevisiae_genes.bed")
for line in S_cer_genes: 
    line = line.strip().split()
    if line[0] == "chrI":
        line.insert(0,1)
    if line[0] == "chrII":
        line.insert(0,2)
    if line[0] == "chrIII":
        line.insert(0,3)
    if line[0] == "chrIV":
        line.insert(0,4)
    if line[0] == "chrV":
        line.insert(0,5)
    if line[0] == "chrVI":
        line.insert(0,6)
    if line[0] == "chrVII":
        line.insert(0,7)
    if line[0] == "chrVIII":
        line.insert(0,8)
    if line[0] == "chrIX":
        line.insert(0,9)
    if line[0] == "chrX":
        line.insert(0,10) 
    if line[0] == "chrXI":
        line.insert(0,11)
    if line[0] == "chrXII":
        line.insert(0,12) 
    if line[0] == "chrXIII":
        line.insert(0,13)
    if line[0] == "chrXIV":
        line.insert(0,14) 
    if line[0] == "chrXV":
        line.insert(0,15) 
    if line[0] == "chrXVI":
        line.insert(0,16) 
    gene_name = line[4]
    gene_seq = S_cer_GenomeDict[line[0]][int(line[2]):(int(line[3])+1)]
    output.write(">%s\n%s\n" % (gene_name, gene_seq)) 

x.close()
output.close()
  
