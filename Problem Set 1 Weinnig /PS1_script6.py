#Question 6
def double (numinput):
	output = 2*numinput
	return output

def half (numinput):
	output = float(numinput)/2
	return output
print "Enter numbers, one at a time. When you are ready to quit, type quit."
while True:
	print "Input number"
	x = raw_input()
	if x == "quit":
		break
	if int(x)%2 == 0:
		print "Your number is even and half of your number is ", half(int(x)) 
	else: 
		print "Your number is odd and double of your number is ", double(int(x))


