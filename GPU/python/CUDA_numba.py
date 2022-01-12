import numpy as np
from numba import cuda, float32
import time
 
@cuda.jit
def matmul(A, B, C):
    """Perform square matrix multiplication of C = A * B
    """
    i, j = cuda.grid(2)
    if i < C.shape[0] and j < C.shape[1]:
        tmp = 0.
        for k in range(A.shape[1]):
            tmp += A[i, k] * B[k, j]
        C[i, j] = tmp


import time 
start=time.time()

A, B, C
np
matmul(A, B, C)

end=time.time()
print(f"Runtime of the program is {end - start} s")