import numpy as np

#tutorial on cython: https://youtu.be/mXuEoqK4bEc
def for_loop(n):
    sum0=0.+0j
    for i in range(n):
        for j in range(n):
            sum0=sum0+0.2+0.5j
    return sum0


cpdef complex for_loop_def_type(int n):
    cdef complex sum0=0
    cdef int i
    cdef int j
    for i in range(n):
        for j in range(n):
            sum0=sum0+0.2+0.5j
    return sum0

cpdef complex for_loop_def_loop_type(int n):
    sum0=0
    cdef int i
    cdef int j
    for i in range(n):
        for j in range(n):
            sum0=sum0+0.2+0.5j
    return sum0