import cython_function 
import time 
import numpy as np

loop_time=1
matrix_size=20

a=np.random.rand(20,20) 

def matrix_add(m):
    for i in range(m):
        b=a+a 
    return b

print('****************************')
print('*********python*************')
start=time.time()
sum0=matrix_add(loop_time)
#print(sum0)
end=time.time()
print(f"Runtime of the program is {end - start} s")

print('****************************')
print('*********Cython************')
start=time.time()
sum0=cython_function.matrix_add(loop_time)
#print(sum0)
end=time.time()
print(f"Runtime of the program is {end - start} s")

print('****************************')
print('*Cython with type definition*')
start=time.time()
sum0=cython_function.matrix_add_def_type(loop_time)
#print(sum0)
end=time.time()
print(f"Runtime of the program is {end - start} s")


if 1==0: 
    a=np.random.rand(20,20)  
    #print(repr(a))
    print(np.shape(a))
    b=''
    for i in repr(a):
        if i=='[':
            b=b+'{'
        elif i==']':
            b=b+'}'
        else:
            b=b+i
    print(str(b))
