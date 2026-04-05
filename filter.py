l=[5,5,3,2,1,5,4,5]
def greter(x):
    return x>2
l1=list(filter(greter,l))
print(l1)