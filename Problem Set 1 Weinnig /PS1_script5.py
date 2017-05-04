#Question 5 - redo question number 2 but use a for loop
numlist = []
print "Enter 4 numbers, one at a time." 
for i in range(4):
	print "Input number" 
	number = int(raw_input())
	numlist.append(number)
print "This list of numbers is ", numlist
numsum = sum(list(numlist))
print "The sum of this list of number is", (numsum)
newlist = [(numlist[0]*numlist[1]),(numlist[2]*numlist[3])]
print "The new list of numbers is", newlist

#Question 5b - Redo problem 2, but allow the user to specify an arbitrarily long sequence of numbers hint: you might ask the user to input a special character if they want to stop inputting characters
numlist2 = []
print "Enter numbers, one at a time. When you are ready to quit, type 0."
while True:
	print "Input number"
	numb = (raw_input())
	numlist2.append(numb)
	if numb == "0":
		break
print "This list of numbers is", numlist2 
numsum2 = sum(int(numb))
print "The sum of this list of numbers is", numsum2

