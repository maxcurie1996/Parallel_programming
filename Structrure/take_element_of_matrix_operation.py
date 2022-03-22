import time 
import numpy as np

n=1000000
matrix_len=100
x=np.random.rand(matrix_len)
A=np.random.rand(matrix_len,matrix_len)
index=0

print('**********Do the whole matrix***********')
start=time.time()
for i in range(n):
	a1=np.matmul(A,x)[index]
end=time.time()
print(f"Runtime of the program is {end - start} s")

print('**********only calculate the sub-matrix***********')
start=time.time()

for i in range(n):
	a2=np.matmul(A[index,:],x)
end=time.time()
print(f"Runtime of the program is {end - start} s")

print(abs(a1-a2))