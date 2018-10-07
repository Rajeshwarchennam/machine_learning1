import numpy as np
from random import random
from random import seed
def activate(weights, inputs):
	activation = weights[-1]
	for i in range(len(weights)-1):
		activation += weights[i] * inputs[i]
	return activation
def checking_output(network, row):
	inputs = row
	for layer in network:
		new_inputs = []
		for node in layer:
			activation = activate(node['weights'], inputs)
			node['output'] = 1.0 / (1.0 + np.exp(-activation))
			new_inputs.append(node['output'])
		inputs = new_inputs
	return inputs
def back_propagation(network,expected):
    for i in reversed(range(len(network))):
        layer =network[i]
        errors=list()
        if (i== len(network)-1):
            for j in range(len(layer)):
                node=layer[j]
                errors.append(expected[j]-node['output'])
        else:
            for j in range(len(layer)):
                error=0.0
                for node in network[i+1]:
                    error+=(node['weights'][j]*node['delta'])
                errors.append(error)
        for j in range(len(layer)):
            node=layer[j]
            node['delta']=errors[j]*node['output'] * (1.0 - node['output'])
def update_weights(network,row,l_rate):
    for i in range(len(network)):
        inputs=row
        if i!=0:
            inputs=[node['output'] for node in network[i-1]]
        for node in network[i]:
            for j in range(len(inputs)):
                node['weights'][j]+=l_rate*node['delta']*inputs[j]
            node['weights'][-1]+=l_rate*node['delta']
def process(network,row,expected,l_rate):
    out=checking_output(network, row)
    back_propagation(network,expected)
    update_weights(network,row,l_rate)

input_nodes =2
hidden_nodes =2
output_nodes =1
seed(1)
network1=list()
hidden_layer=[{'weights':[random() for i in range(input_nodes + 1)]} for i in range(hidden_nodes)]
network1.append(hidden_layer)
output_layer=[{'weights':[random() for i in range(hidden_nodes+ 1)]} for i in range(output_nodes)]
network1.append(output_layer)
network2=list()
hidden_layer=[{'weights':[random() for i in range(input_nodes + 1)]} for i in range(hidden_nodes)]
network2.append(hidden_layer)
output_layer=[{'weights':[random() for i in range(hidden_nodes+ 1)]} for i in range(output_nodes)]
network2.append(output_layer)
network3=list()
hidden_layer=[{'weights':[random() for i in range(input_nodes + 1)]} for i in range(hidden_nodes)]
network3.append(hidden_layer)
output_layer=[{'weights':[random() for i in range(hidden_nodes+ 1)]} for i in range(output_nodes)]
network3.append(output_layer)

l_rate=.5

mean=0
std=0.05
row1=[0,0]
row2=[1,0]
row3=[0,1]
row4=[1,1]
for i in range(10000):#training xor gate
    expected1=[0]+np.random.normal(mean,std,1)
    expected2=[1]+np.random.normal(mean,std,1)
    expected3=[1]+np.random.normal(mean,std,1)
    expected4=[0]+np.random.normal(mean,std,1)
    process(network1,row1,expected1,l_rate)
    process(network1,row2,expected2,l_rate)
    process(network1,row3,expected3,l_rate)
    process(network1,row4,expected4,l_rate)
for i in range(10000):# training and gate
    expected1=[0]+np.random.normal(mean,std,1)
    expected2=[0]+np.random.normal(mean,std,1)
    expected3=[0]+np.random.normal(mean,std,1)
    expected4=[1]+np.random.normal(mean,std,1)
    process(network2,row1,expected1,l_rate)
    process(network2,row2,expected2,l_rate)
    process(network2,row3,expected3,l_rate)
    process(network2,row4,expected4,l_rate)
for i in range(10000):# training or gate
    expected1=[0]+np.random.normal(mean,std,1)
    expected2=[1]+np.random.normal(mean,std,1)
    expected3=[1]+np.random.normal(mean,std,1)
    expected4=[1]+np.random.normal(mean,std,1)
    process(network3,row1,expected1,l_rate)
    process(network3,row2,expected2,l_rate)
    process(network3,row3,expected3,l_rate)
    process(network3,row4,expected4,l_rate)
print("select gate to test")
print ("1)xor")
print("2)and")
print("3)or")
selection=input()
print("give inputs one by one")
a=input()
b=input()
row=[a,b]
if(selection==1):
    output=checking_output(network1,row)
if(selection==2):
    output=checking_output(network2,row)
if(selection==3):
    output=checking_output(network3,row)
a=output[0]
if(a>0.5):
	print 1
if(a<0.5):
	print 0
