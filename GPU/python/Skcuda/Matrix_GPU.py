import skcuda # pip install scikit-cuda
import numpy as np

import pycuda.gpuarray as gpuarray


n=5
a=np.random.rand(n)
print(a)
a_gpu=gpuarray.to_gpu(a)
print(a)
print(a_gpu)
skcuda.linalg.init()
b_gpu=skcuda.linalg.inv(a_gpu)
print(b_gpu)
b=get_cuda(b_gpu)
