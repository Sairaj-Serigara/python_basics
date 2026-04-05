#  time.time()--->It returns the current time in seconds since the “epoch.”
# The epoch is the starting point for time measurement in most computer systems.
# It’s defined as:
# January 1, 1970, 00:00:00 UTC (Coordinated Universal Time)

# time.time() → gives current time in seconds since epoch.

import time

def usingwhile():
    i=0
    while i<50:
        i=i+1
        print(i)

def usingforloop():
    i=0
    for i in range(50):
        print(i)

x=time.time()
usingwhile()
print("time taken",time.time()-x)
y=time.time()
usingforloop()
print("time taken",time.time()-y)
