#Question 4 
#Try to divide 5/7  
divide=5/7
print divide
#Get 0, python only does integer division so you have to use float to make it use decimals 

dividetwo = float(5)/float(7)
print "5 divided by 7 is " , dividetwo

#Make a list of length 5. Try to access element 5. What happens? Why? 
list5 = [4,3,6,7,3]
len(list5)
#list5[5]
#Prints the error "IndexError: list index out of range" because the access starts at 0 so there is only 4 other elements that are accessible 

#Make a dictionary. Try to access an element that doesn't exist. 
fakeDic = {"sleep":8,"eat":2,"read":5,"walk":2}
#print fakeDic["run"]
#Prints the error "NameError: name 'run' is not defined"

#Make a dictionary. Try to use a list as a key. What happens? 
listDic = {"list":list5,"pen":5, "bread":6}
print listDic["list"]
#Works to call the list 
