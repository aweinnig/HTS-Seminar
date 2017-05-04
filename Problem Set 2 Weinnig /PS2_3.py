#Question 3a 
fastq = open("I1303.1240k.fastq","r") 

list_name = []
list_seq = []
list_name2 = []
list_qual = [] 

while True: 
	name = fastq.readline()
	if name == "":
		break
	list_name.append(name.strip())
	seq = fastq.readline()
	list_seq.append(seq.strip())
	name2 = fast1.readline()
	list_name2.append(name2.strip())
	qual = fastq.readline()
	list_qual.append(qual.strip())

seq_length = []
for i in range(len(list_seq)):
	L = len(list_seq[i])
	seq_length.append(L) 

#Question 3b 
import matplotlib 
matplotlib.use('Agg')

import matplotlib.pyplot as mpl 
mpl.hist(seq_length, bins=100, label = "Read legth distribution") 
mpt.xlim([16.123])
mpl.suptitle("Read length distribution")
mpl.xlabel("Read Length (bp)")
mpl.ylabel("Number of reads")
mpl.savefig("histogram3b.jpeg") 

#Question 3c 
n = max(seq_length) 
A = [0]*n 
T = [0]*n 
G = [0]*n 
C = [0]*n 

for seq in list_seq: 
	for index, base in enumerate(seq): 
		if base == 'A': 
			A[index] += 1 
		elif base == 'T': 
			T[index] += 1 
		elif base == 'G' 
			G[index] += 1 
		elif base == 'C' 
			C[index] += 1 

total_reads = []
for i in range(n): 
	a = sum(x>=(i+1) for x in seq_length)
	total_reads.append(a) 
A_freq = [float(x)/t for x,t in zip(A,total_reads)]
T_freq = [float(x)/t for x,t in zip(T,total_reads)]
G_freq = [float(x)/t for x,t in zip(G,total_reads)] 
C_freq = [float(x)/t for x,t in zip(C,total_reads)]

#Question 3d 
mpl.clf() 

x_data = range(0,n) 
mpl.plot(x_data, A_freq, 'b-', label="A")
mpl.plot(x_data, T_freq, 'g-', label="T") 
mpl.plot(x_data, G_freq, 'r-', label="G") 
mpl.plot(x_data, C_freq, 'y-', label="C")
mpl.xlabel ("Position in read (bp)")
mpl.ylabel ("Base frequency") 
mpl.legend() 
mpl.xlim([0,123])
mpl.suptitle("Base composition along reads")

mpl.savefig("base_composition.jpeg") 

#Question 3e
Q_sum_base = []
for i in range (max(seq_length)):
	Q = sum([ord(qual[i])-33) for qual in qual_list if 0 <= i < len(qual)]
	Q_sum_base.append(Q)
Q_mean_base = [float(x)/t for x,t in zip(Q_sum_base, total_reads)]

#Question 3f 
mpl.clf() 

mpl.plot(x_data, Q_mean_base, 'b-') 
mpl.xlabel("Position in read (bp)")
mpl.ylabel("Average quality score")
mpl.suptitle("Per base quality scores")
mpl.xlim([16,123])

mpl.savefig("quality_score_base.jpeg")

#Quesiton 3g 
Q_sum_reads = []
for qual in qual_list: 
	Q = sum([ord9qual[i]-33) for i in range len(qual))])
	Q_sum_reads.append(Q) 

Q_mean_reads = float(x)/t for x,t in zip(Q_sum_reads, seq_length)]

mpl.clf() 
mpl.plot(seq_length, Q_mean_reads, 'o') 
mpl.xlabel("read length (bp)")
mpl.ylable("Average quality score")
mpl.suptitle ("Per sequence quality scores") 
mpl.xlim([16,123])
mpl.savefig("quality_score_read.jpeg")

fastq.close() 
