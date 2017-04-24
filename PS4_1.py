import numpy
#Question 1a
FastaFile = open("my_short_genome.fa")


def parse_fasta(fastaFile): 
	#initiate an empty dictionary 
	fastaDict = {} 
	for line in fastaFile: 
		if line[0] == ">":
			#if the first character is >, then we know its a chromosome name 
			chromosomeName = line.strip()[1:]
			fastaDict[chromosomeName] = []
		else: 
			#otherwise its the sequence, so we assign it to that entry in the dicitonary 
			fastaDict[chromosomeName].append(line.strip())
	for chrom in fastaDict: 
		fastaDict[chrom] = ''.join(fastaDict[chrom])
	return fastaDict

chromdictionary = parse_fasta(FastaFile)
print chromdictionary 
# for all the items in the dictionary add a '$' at the end and then sort the list lexicographically
list_of_keys = chromdictionary.keys()
print list_of_keys
sequences = []
for key in list_of_keys:
	#adding '$' at the end of each sequence 
	seq = chromdictionary[key] + '$'
	sequences.append(seq)
print sequences 
#generating a list of all suffixes and sorting them
newsequences = []
count = 0
for chromosome in sequences:
	count += 1 
	chromsequences = []
	for x in range(len(chromosome)):
		chromsequences.append(chromosome[x:]+ chromosome[:x])
	chromsequences = sorted(chromsequences)
	finalCharList = []
	for i in chromsequences: #take final character of each line and output into seperate file for each chromosome
		finalChar = i[-1:]
		finalCharList.append(finalChar)
	finalCharStr = ''.join(finalCharList)
	newsequences.append(chromsequences)
	OutputFile = open("BWT_chromosome.txt%s" % (count), "w")
	OutputFile.write(finalCharStr)
print newsequences

#Question 1b 
#generate a checkpointed suffix array 


#FastaFile = open("my_genome.fa")

 
