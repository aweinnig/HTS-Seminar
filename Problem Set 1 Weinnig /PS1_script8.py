#Question 8 
numfile= open('numbers.txt',"r")

def extremes (lineinput): 
	for i in range(len(lineinput)):
		lineinput[i] = int(lineinput[i])
	minimum = min(lineinput)
	maximum = max(lineinput)
	return minimum, maximum 
myLine = numfile.readlines() 
numfile.close()
numoutput = open('num_output_Weinnig.txt','w')
for line in myLine:
	myLineSplit = line.strip().split("\t")
	thismin,thismax = extremes(myLineSplit)
	numoutput.write("The minimimum of this line is %i and the maximum of this line is %i\n"%(thismin,thismax)) 
	print myLineSplit 
numoutput.close() 
