#pip install cupy
#install microsoft visual c++
import cupy 
import numpy as np

n=5

a=np.random.rand(n)
print(a)
a_gpu=cupy.array(a)
print(a)
print(a_gpu)
b_gpu=cupy.linalg.inv(a_gpu)
print(b_gpu)
b=cupy.asnumpy(b_gpu)
