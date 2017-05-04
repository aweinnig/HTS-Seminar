#1a get the length of a vector or list
vector1 = c(9,5,2,0)
vector1 
length(vector1)
list1 = list(9,5,2,0)
length(list1)

#1b creating a range 
range1 = seq(1,10)
range1 

#1c initialize a vector of all 0s 
zerovector = rep(0,10)
zerovector 

#2a make 2 vectors 
v1 = c(3,6,7,3,1) 
v2 = c(6,3,0,6,1)

#2b v1 + v2, v1 * v2, v1 – v2, and v1/v2 
v1 + v2 #9 9 7 9 2
v1 * v2 #18 18  0 18  1
v1 - v2 #-3  3  7 -3  0
v1/v2 #0.5 2.0 Inf 0.5 1.0 - the 0 in v2 creates the infinity issue

#2c other mathmatical operations 
log(100) #4.60517
3**89 #2.909321e+42
sqrt(489) #22.11334

#3a matrix multiplication 
v1%*%v2

#3b make a matrix. Create a matrix m with 2 rows and 2 columns, first row is 3, 6; second row is 7, 1. Also create a vector v = c(3,1).
m = matrix(c(3,7,6,1), nrow=2, ncol=2)
m
v=c(3,1)
v 
m%*%v 

install.packages(data.table)