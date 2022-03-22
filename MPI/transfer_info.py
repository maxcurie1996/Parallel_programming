# -*- coding: utf-8 -*-
"""
Created on 10/25/2021

@author: maxcurie
"""

import numpy as np
from mpi4py import MPI

from MPI_tools import task_dis

comm=MPI.COMM_WORLD
rank=comm.Get_rank()
size=comm.Get_size()
print('size='+str(size))

print('*******rank='+str(rank)+'*************')

if rank==0:
    total_task_list=np.random.rand(1000)
    task_list = task_dis(size-1,total_task_list)
    for i in range(size-1):
        comm.send(task_list[i],dest=i+1) #sending the data
    print('**********rank=0 waiting****************')

elif rank!=0:
    task_list_rank=comm.recv(source=0)  #recieve the data
    for i in task_list_rank:
        print(i**2)