#great video: https://youtu.be/x58W9A2lnQc

import numpy as np 
import numba as nb 
import time 

n=5

def maxt_inv(n):
    a=np.random.rand(n,n)
    b=np.linalg.inv(a)
    return b

jitted_maxt_inv = nb.njit()(maxt_inv)


print('*********numpy*************')
start=time.time()
maxt_inv(n)
end=time.time()
print(f"Runtime of the program is {end - start} s")

print('*********numba*************')
start=time.time()
jitted_maxt_inv(n)
end=time.time()
print(f"Runtime of the program is {end - start} s")