import time
from ctypes import *

def my_add(num):
    result = 0
    
    for i in range(num + 1):
        result = result + i

    print("Python from 1 to",num,"accumulation =>",result)



def main():
    num = int(input("input integer:"))

    start_time = time.time()
    result = cdll.LoadLibrary("./c_dll.so")
    result.my_add(num)
    end_time = time.time()
    print("C total time: %s"%(end_time-start_time))

    start_time = time.time()
    my_add(num)
    end_time = time.time()
    print("Python total time: %s"%(end_time-start_time))
    
if __name__ == "__main__":
    main()
