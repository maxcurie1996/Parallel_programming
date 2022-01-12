import multiprocessing
import time 
#learnt from: https://youtu.be/fKl2JW_qrso

n=10

def f(x):
    time.sleep(0.2)
    return x*x

#https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/
if __name__ == '__main__':
    print('**************************')
    print('******no paraellel********')
    start=time.time()
    for i in range(n):
        print(f(i))
        
    end=time.time()
    print(f"Runtime of the program is {end - start} s")

    print('**************************')
    print('*********paraellel********')
    start=time.time()
    processes=[]
    for i in range(n):
        p=multiprocessing.Process(target=f,args=[2])
        p.start()
        print(i)
        processes.append(p)

    for process in processes:
        process.join()
    end=time.time()
    print(f"Runtime of the program is {end - start} s")
    

