#https://youtu.be/x58W9A2lnQc

from numba import jit
from numba import cuda
cuda.select_device(0)

@cuda.
def matmul(A, B, C):
    """Perform square matrix multiplication of C = A * B
    """
    i, j = cuda.grid(2)
    if i < C.shape[0] and j < C.shape[1]:
        tmp = 0.
        for k in range(A.shape[1]):
            tmp += A[i, k] * B[k, j]
        C[i, j] = tmp
    print(C)

jit()matmul(A, B, C)