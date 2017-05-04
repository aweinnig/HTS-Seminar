#Question 3 

a=raw_input ("Enter a name, please")
b=input("Enter " + a + "'s age.")
c=raw_input ("Enter another name, please.")
d=input("Enter "+c+ "'s age.")
e=raw_input ("Enter a third name, please.")
f=int(input("Enter "+e+ "'s age."))
friendDic = {a:b, c:d, e:f}

print a+ " is "+ str(friendDic[a])+  " years old. They will be " + str(friendDic[a]+5)+ " in 5 years."
print c+ " is "+ str(friendDic[c])+  " years old. They will be " + str(friendDic[c]+5)+ " in 5 years."
print e+ " is "+ str(friendDic[e])+  " years old. They will be " + str(friendDic[e]+5)+ " in 5 years."
