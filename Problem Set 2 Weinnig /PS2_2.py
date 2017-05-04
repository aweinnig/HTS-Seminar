#Question 2a 
def fasta_dict(x): 
	names = [] 
	sequences = [] 
	for line in x: 
		line = line.strip()
		if line.startswith(">"): 
			contig = line[1:]
			contig = contig.replace("_"," ")
			names.append(contig) 
		else: 
			sequences.append(line) 
	dictionary = dict(zip(names, sequences))
	return dictionary 
#Question 2b 
genome = open("test.fasta") 
genome_dict = fasta_dict(genome) 

def compute_N(x,Dict1): 
	dic_sorted = sorted(Dict1, key=lambda k:len(Dict1[k]))
	L_list = []
	for i in range (len(dic_sorted)):
		L = (len(Dict1[dic_sorted[i]]))
		L_times_L = [L]*L
		L_list.extend(L_times_L)
	xn = float(len(L_list)*x) 
	if isinstance(xn, int) == True: 
		xn = int(xn)
		quantile = float(float(L_list[xn] + L_list[xn+1])/float(2)
	else: 
		xn = int(xn) +1 
		quantile = L_list[xn] 

	return x, quantile 

#Question 2c 
Output1 = open(Nx_output.txt","w")

def frange(start,stop,step=1.0): 
	while start < stop
		yield start 
		start += step 
for i in frange (0.05, 1.00, 0.05): 
	result = computer_N(i, Genome_dic) 
	Output1.write("For x = %s, N(x) = %s.\n" %result) 

Genome.close()
Output1.close() 
