import numpy as np
import matplotlib.pyplot as plt
def power(x,n):
    y=1
    for i in range(n):
        y=y*x
    return y
def polybasis(x,m):
    l=len(x)
    X=x
    if m>1:
        for i in range(2,m+1):
            y=power(X,i)
            x=np.column_stack((x,y))
    z=np.column_stack((np.ones(l),x))
    return z
N=100
x=np.linspace(0,2*np.pi,N)
mean=0
y=np.sin(x)
std=.05
y+=np.random.normal(mean,std,N)
y=np.reshape(y,(len(x),1))
#maximizing the posterior distribution is equivalent to minimizing the regularized sum-of-squares error function
print "value of alpha:"
alpha=(input ())# alpha is the precision of distribution of weights
print "value of beta:"
beta=(input ())# beta corresponds to the inverse variance of the distribution of labels
Lambda=alpha/beta#to maximize the posterior distribution ,we need to minimize regularized sum-of-squares error function with lambda=alpha/beta
print "input M value"
M=(input())
x=polybasis(x,M)
I=np.identity(M+1)
w=np.matmul(np.matmul(np.linalg.inv(np.matmul(np.transpose(x),x)+Lambda*I),np.transpose(x)),y)
print w
