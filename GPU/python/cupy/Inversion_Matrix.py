#conda install -c conda-forge cupy cudatoolkit=11.0
#install microsoft visual c++
import cupy as cp
import numpy as np
import time 

n=1000
run_times=100

a=np.random.rand(n,n)
print(a)
a_gpu=cp.asarray(a)
print(a)
print(a_gpu)

print('*******With GPU*******')
start=time.time()
for i in range(run_times):
	b_gpu=cp.linalg.inv(a_gpu)
end=time.time()
print(f"Runtime of the program is {end - start} s")


b=cp.asnumpy(b_gpu)

print('*******Without GPU*******')
start=time.time()
for i in range(run_times):
	a_inv=np.linalg.inv(a)
end=time.time()
print(f"Runtime of the program is {end - start} s")