from functools import reduce

l=[1,2,3,4,5]
def sum(x,y):
    return x+y
l1=reduce(sum,l)
print(l1)