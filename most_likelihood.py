import numpy as np
import matplotlib.pyplot as plt

N=10
x=np.linspace(0,2*np.pi,N)
mean=0
std=.05
y=np.sin(x)
y+=np.random.normal(mean,std,N)
y=np.reshape(y,(len(x),1))
x=np.column_stack((np.ones(len(x)),x))
# Maximum likelihood weight estimate is same as the weight that minimizes cost function for linear regression independent of Beta.
w=np.matmul(np.matmul(np.linalg.inv(np.matmul(np.transpose(x),x)),np.transpose(x)),y)#W is independent of Beta
#by using maximum likelihood to determine the precision parameter Beta of the guassian conditional distribution
print w
