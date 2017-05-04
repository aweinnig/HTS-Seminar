#Question 2 

y=input ("Enter a number, please.")
z=input ("Enter another number, please.")
w=input ("Enter a thind number, please.")
u=input ("Enter one last number, please.")
mylist = [y,z,w,u]
print "This list of numbers is" , mylist
numsum = sum(list(mylist))
print "The sum of this list of number is", (numsum)
newlist = [(y*z),(w*u)]
print "The new list of numbers is", newlist
