from multiprocessing import Pool
import time 

def f(x):
    time.sleep(1)
    return x*x
'''
print('**************************')
print('******no paraellel********')
start=time.time()
for i in range(4):
    f(i)
end=time.time()
print(f"Runtime of the program is {end - start} s")
'''

print('**************************')
print('*********paraellel********')
start=time.time()
with Pool(6) as p:
    print(p.map(f, [1, 2, 3, 4]))
end=time.time()
print(f"Runtime of the program is {end - start} s")


