#conda install -c conda-forge cupy cudatoolkit=11.0
#install microsoft visual c++
import cupy as cp
import numpy as np
import time 

n=5000
run_times=100

a_cpu=np.random.rand(n,n)
a_gpu=cp.asarray(a_cpu)
print(a_cpu)
print(a_gpu)

print('*******With GPU*******')
start=time.time()
for i in range(run_times):
	b_gpu=a_gpu+a_gpu
end=time.time()
print(f"Runtime of the program is {end - start} s")

b=cp.asnumpy(b_gpu)


print('*******Without GPU*******')
start=time.time()
for i in range(run_times):
	a=a_cpu+a_cpu
end=time.time()
print(f"Runtime of the program is {end - start} s")