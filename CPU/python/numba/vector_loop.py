#https://youtu.be/x58W9A2lnQc

from numba import jit
from numba import vectorize

import numpy as np
import time

n=10000
run_times=2000
def even_odd(A):
    B=np.zeros(len(A))
    for i in range(len(A)):
        if A[i]%2==0:
            B[i]=0
        else:
            B[i]=0
    return B

@vectorize
def vector_even_odd(a):
    if a%2==0:
        return 0
    else:
        return 1

jitted_even_odd=jit(nopython=True)(even_odd)

A=np.array(np.random.rand(n),dtype=int)


print('*******not jit*********')
start=time.time()
for i in range(run_times):
    even_odd(A)
end=time.time()
print(f"Runtime of the program is {end - start} s")

print('*******with jit*********')
start=time.time()
for i in range(run_times):
    jitted_even_odd(A)
end=time.time()
print(f"Runtime of the program is {end - start} s")

print('*******with vector*********')
start=time.time()
for i in range(run_times):
    vector_even_odd(A)
end=time.time()
print(f"Runtime of the program is {end - start} s")


