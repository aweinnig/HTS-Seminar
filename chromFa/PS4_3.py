#Problem Set 4, Question 4 
import matplotlib.pyplot as plt 
import pysam
#open the sorted bam file
bamfile = pysam.AlignmentFile("output.sorted.bam", "rb")

#open empty lists to fill with things
qualityList = []
strands = []
for read in bamfile.fetch():
	#get the mapping quality of the reads 
	quality = read.mapping_quality
	qualityList.append(quality)
	#get the strand tha the read maps to
	strand = read.is_reverse
	strands.append(strand)
bamfile.close()
#histogram of mapping qualities 
plt.hist(qualityList)
#saving the histogram
plt.savefig("mappingqualityHist.pdf")

#compute the proportion of reads that are + strand 
forwardStrand = 0.0
reverseStrand = 0.0
for strand in strands: 
	if strand == False: forwardStrand += 1
	if strand == True: reverseStrand += 1
fraction_of_forward = forwardStrand/len(strands)
fraction_of_reverse = reverseStrand/len(strands)
print "%f of reads are on the forward strand"%(fraction_of_forward)
print "%f of reads are on the reverse strand"%(fraction_of_reverse)
