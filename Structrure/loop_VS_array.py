import time 
import numpy as np
#https://youtu.be/Qgevy75co8c
n=1000000
x=np.random.rand(n)

print('*************for loop**************')

start=time.time()
for i in range(n):
	a=x[i]+x[i]
end=time.time()
print(f"Runtime of the program is {end - start} s")


print('*************vector add**************')
start=time.time()
y=x+x
for i in range(n):
	a=y[i]
end=time.time()
print(f"Runtime of the program is {end - start} s")