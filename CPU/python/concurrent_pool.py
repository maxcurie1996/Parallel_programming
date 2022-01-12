import concurrent.futures as future
import time 
import numpy as np

n=10

def f(x):
    time.sleep(0.2)
    return x*x

if __name__ == '__main__':    

    print('**************************')
    print('******no paraellel********')
    start=time.time()
    for i in range(n):
        print( 'no paraellel'+str(f(i)) )
    end=time.time()
    print(f"Runtime of the program is {end - start} s")

    #*************Method 1************************ 
    print('***********************************')
    print('*********paraellel method 1********')
    start=time.time()
    with future.ProcessPoolExecutor() as executor:
        results = [executor.submit(f,i) for i in range(n)]

    for result0 in future.as_completed(results):
        print( 'paraellel'+str(result0.result()) )

    end=time.time()
    print(f"Runtime of the program is {end - start} s")

    #*************Method 2************************ 
    print('***********************************')
    print('*********paraellel method 2********')
    start=time.time()
    with future.ProcessPoolExecutor() as executor:
        results = executor.map(f, np.arange(n))

    for result0 in results:
        print( 'paraellel'+str(result0) )

    end=time.time()
    print(f"Runtime of the program is {end - start} s")


