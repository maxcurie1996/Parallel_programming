#https://youtu.be/x58W9A2lnQc

from numba import vectorize
import numpy as np
import time

n=100
run_times=200

@vectorize
#multiplication function
def vector_matmul_element(vector1,vector2):
    return vector1*vector2

# @vectorize
def vector_matmul(matrix1,matrix2):
    (m11,m12)=np.shape(matrix1)
    (m21,m22)=np.shape(matrix1)
    return_mat=np.zeros((m11,m22))
    for i in range(m11):
        for j in range(m22):
            return_mat[i,j]=np.sum(vector_matmul_element(matrix1[i,:],matrix2[:,j]))
    return return_mat


a=np.random.rand(n,n)

print('*******with jit vector*********')
start=time.time()
for i in range(run_times):
    c1=vector_matmul(a,a)

end=time.time()
print(f"Runtime of the program is {end - start} s")

print('*******not jit*********')
start=time.time()
for i in range(run_times):
    c2=np.matmul(a,a)

end=time.time()
print(f"Runtime of the program is {end - start} s")

print(c1)
print(c2)
print(abs(c1-c2))