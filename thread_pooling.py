import time
from concurrent.futures import ThreadPoolExecutor

def func(seconds):
    print(f"sleep for {seconds} seconds")
    time.sleep(seconds)
    return seconds



def threadpoolexecutor():
    with ThreadPoolExecutor() as executor:
        # method 1
        # future1=executor.submit(func,4)
        # future2=executor.submit(func,3)
        # future3=executor.submit(func,1)
        #
        # print(future1.result())
        # print(future2.result())
        # print(future3.result())

        # method 2
        l=[4,3,1]
        results=executor.map(func,l)
        for r in results:
            print(r)
threadpoolexecutor()