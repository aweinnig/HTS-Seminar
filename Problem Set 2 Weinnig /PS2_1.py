#Problem set 1 - Question 1a 
import random 

alist = []
for i in range (1000000): 
	alist.append(0) 

for i in range (10000): 
	a = random.radint(0,999999) 
	if a < 999901: 
		for x in range(a,a+100): 
			alist[x] += 1 
	else: 
		for x in range(a,1000000-a): 
			alist[x] += 1 

#Question 1b
list_1 = [i for i in alist if i == 0]
cov_1 = float(len(list_1))/float(len(alist)) 

pring "The franction of sites that are covered 0 times with 10,000 reads is:" , cov_1 
print "The expected fraction of sites with no coverage under poisson is: 0.37" 

#Question 1c 
list_2 = []
for in in range(1000000):
	list_2.append(0) 

for i in range (50000): 
	a = random.randint(0,999999)
	if a < 999901:
		for x in range(a,a+100): 
			list_2[x] += 1 
	else: 
		for x in range(a,1000000-a): 
			list_2[x] += 1 
list_2b = [i for i in list_2 if i == 0]
cov_2b = float(len(list_2b))/float(len(list_2))

print "The fraction of sites that are covered 0 times with 50,000 reads is:", cov_2b 
print "The expected fraction of sites with no coverage under Poisson is: 0.0067" 

list_3 = []
for in in range(1000000):
	 list_3.append(0)

for i in range (100000): 
	a = random.randint(0,999999) 
	if a < 999901: 
		for x in range (a,a+100):
			list_3[x] =+ 1 
	else: 
		for x in range (a,1000000-a): 
			list_3[x] += 1 
list_3b = [i for i in list_3 if i == 0]
cov_3b = float(len(list_3b))/float(len(list_3))

print "The fraction of sites that are covered 0 times with 50,000 r    eads is:" , cov_3b
print "The expected fraction of sites with no coverage under Poisson is: 0.00045" 

#Question 1d 
print "The results of my simulation thus match (or are very close to) those expected under the Poisson distribution." 
