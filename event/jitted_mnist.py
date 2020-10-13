import os
import chainer
import numpy as np
import matplotlib.pyplot as pyplot
train,_ = chainer.datasets.get_mnist()

i = 2
y = train[i][0]
label = train[i][1]

num_time = 20
fr = 100 #Hz
dt = 1e-3

print("y : ",y)

y_fr = fr * np.repeat(np.expand_dims(y, 1), num_time, axis=1)
print("y_fr : ",y_fr)

print(np.random.rand(784, num_time).shape)
x = np.where(np.random.rand(784, num_time) < y_fr*dt, 1, 0)
print("x : ",x)