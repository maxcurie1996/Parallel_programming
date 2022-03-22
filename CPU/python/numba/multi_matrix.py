#https://youtu.be/x58W9A2lnQc

from numba import jit
import numpy as np
import time

n=1000
run_times=2000

def matmul(A, B):
    """Perform square matrix multiplication of C = A * B
    """
    return A*B

jitted_matmul=jit(nopython=True)(matmul)

a=np.random.rand(n,n)

print('*******with jit*********')
start=time.time()
for i in range(run_times):
    jitted_matmul(a,a)
end=time.time()
print(f"Runtime of the program is {end - start} s")

print('*******not jit*********')
start=time.time()
for i in range(run_times):
    matmul(a,a)
end=time.time()
print(f"Runtime of the program is {end - start} s")
