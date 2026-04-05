from enum import nonmember

a=3
b=3

print(a==b)  #compares the value
print(a is b) #compares the location
print("\n")
#Here value of a is consatant that is 3 and value of b is also 3...hence python stores the value of both in same location


a=[5,2,8]
b=[5,2,8]
print(a==b)
print(a is b)
print("\n")

#holds good for string tuple etc

a=None
b=None
print(a==b)
print(a is b)
print(a is None)
