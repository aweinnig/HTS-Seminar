#Question 7
def products (inputlist):
	firstprod = inputlist[0]
	lastprod = inputlist[-1]
	finalprod = firstprod*lastprod
	return finalprod
numlist = []	
print "Enter 5 numbers, one at a time."
for i in range(5):
	print "Input number" 
	number = int(raw_input())
	numlist.append(number)

print "This list of numbers is ", numlist
print "The product of the first and last numbers you input is ", products(numlist)
