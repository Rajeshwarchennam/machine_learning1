import numpy as np
import matplotlib.pyplot as plt
# Number of training samples
N = 10
# Generate equispaced floats in the interval [0, 2*Pi]
x = np.linspace(0, 2*np.pi, N)
# Generate noise
mean = 0
std = 0.05
# Generate some numbers from the sine function
y = np.sin(x)
# Add noise
y += np.random.normal(mean, std, N)
y=np.reshape(y,(len(x),1))
x=np.column_stack((np.ones(len(x)),x))
w=np.matmul(np.matmul(np.linalg.inv(np.matmul(np.transpose(x),x)),np.transpose(x)),y)
# Number of test samples
N_test = 100
# Generate equispaced floats in the interval [0, 2*pi]
x_test = np.linspace(0, 2*np.pi, N_test)
x_test += np.random.normal(mean, std, N_test)
x_test=np.column_stack((np.ones(len(x_test)),x_test))
plt.scatter(x_test[:,1],np.matmul(x_test,w),c='g',label='test_data')
plt.scatter(x[:,1],y,c='r',label='trained_data')
plt.show()
