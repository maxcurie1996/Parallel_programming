import cython_function 
import time 

def for_loop(n):
    sum0=0.
    for i in range(n):
        for j in range(n):
            sum0=sum0+0.2+0.5j
    return sum0

print('****************************')
print('*********python*************')
loop_time=10000
start=time.time()
sum0=for_loop(loop_time)
print(sum0)
end=time.time()
print(f"Runtime of the program is {end - start} s")

print('****************************')
print('*********Cython************')
start=time.time()
sum0=cython_function.for_loop(loop_time)
print(sum0)
end=time.time()
print(f"Runtime of the program is {end - start} s")

print('****************************')
print('*Cython with type definition*')
start=time.time()
sum0=cython_function.for_loop_def_type(loop_time)
print(sum0)
end=time.time()
print(f"Runtime of the program is {end - start} s")

print('****************************')
print('*Cython with only the loop index type definition*')
start=time.time()
sum0=cython_function.for_loop_def_loop_type(loop_time)
print(sum0)
end=time.time()
print(f"Runtime of the program is {end - start} s")

