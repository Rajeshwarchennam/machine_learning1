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
print "the value of lambda:"
Lambda=(input())
print "the value of M is"
M=(input())
x=polybasis(x,M)
I=np.identity(M+1)
w=np.matmul(np.matmul(np.linalg.inv(np.matmul(np.transpose(x),x)+Lambda*I),np.transpose(x)),y)
# Number of test samples
N_test = 100
# Generate equispaced floats in the interval [0, 2*pi]
x_test = np.linspace(0, 2*np.pi, N_test)
x_test += np.random.normal(mean, std, N_test)
x_test=polybasis(x_test,M)
plt.scatter(x_test[:,1],np.matmul(x_test,w),c='g',label='test_data')
plt.scatter(x[:,1],y,c='r',label='trained_data')
plt.show()
