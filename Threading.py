# With join() → main program waits for threads → guaranteed all thread output appears before continuing.
# Without join() → main program continues immediately → thread output may appear later or sometimes might be missed if the program ends.

import time
import threading

def fun(seconds):
    print(f"sleep for {seconds} seconds")
    time.sleep(seconds)

# normal method
# time1=time.perf_counter()
# fun(4)
# fun(3)
# fun(2)
# time2=time.perf_counter()

# same method using threading
time3=time.perf_counter()
t1=threading.Thread(target=fun,args=[4])
t2=threading.Thread(target=fun,args=[3])
t3=threading.Thread(target=fun,args=[1])

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
time4=time.perf_counter()

# print(time2-time1)
print(time4-time3)