#https://youtu.be/x58W9A2lnQc

from numba import jit
from numba import vectorize
import numpy as np
import time

n=10000
run_times=200

@vectorize
def vector_add(a,b):
    return a+b

def add(a,b):
    return a+b

a=np.random.rand(n,n)

print('*******with jit vector*********')
start=time.time()
for i in range(run_times):
    vector_add(a,a)
end=time.time()
print(f"Runtime of the program is {end - start} s")

print('*******not jit*********')
start=time.time()
for i in range(run_times):
    add(a,a)
end=time.time()
print(f"Runtime of the program is {end - start} s")
