import numba
from numba import jit, cuda
import numpy as np
# to measure exec time
from timeit import default_timer as timer  
 
n_loop=10000000
# normal function to run on cpu
def func(a):                               
    for i in range(n_loop):
        a[i]+= 1     
 
# function optimized to run on gpu
#@jit(target ="cuda") 
#@numba.njit(target='cuda')
@jit(nopython=True)
def func2(a):
    for i in range(n=n_loop):
        a[i]+= 1
        

n = n_loop                           
a = np.ones(n, dtype = np.float64)
b = np.ones(n, dtype = np.float64)
 
start = timer()
func(a)
print("without GPU:", timer()-start)   
 
start = timer()
func2(a)
print("with GPU:", timer()-start)