def cube(x):
    return x ** 3
l = [4, 5, 2, 4, 1]
# l1=[]
# for i in l:
#     l1.append(cube(i))
# print(list(l1))



l1=list(map(cube,l))
print(l1)


l2=list(map(lambda x:x*x*x,l))
print(l2)