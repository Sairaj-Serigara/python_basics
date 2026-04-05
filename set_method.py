s1={2,3,1,4}
s2={9,2,3,5,1,4}
print(s1.union(s2)) #store s2 in s1
print(s1.intersection(s2))
s1.update(s2)
print(s1)
# symmetric difference which is not common in both
s3=s1.symmetric_difference(s2)
print(s3)

#difference means only present in main set but not in both
s4=s1.difference(s2)

#disjoint :no element in common
print(s1.isdisjoint(s2))

#super set:all elements are in common
print(s1.issuperset(s2))

print(s1.issubset(s2))

s1.add(5)
print(s1)

s1.update(s2)

s1.remove(5)
print(s1)
#if element not present in the set remove raises erroe,but discard dont rises error
s1.discard(5)

#pop removes any random elelment
s5=s1.pop()
print(s5)
print(s1)

#del:delets entire set
del s5
# print(s5)

# clear:delets only elelments in the set
s4.clear()
print(s4)

if 2 in s1:
    print("present")
else:
    print("absent")