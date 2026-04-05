#tuple cannot be changed like list like tup[0]=999  IMMUTABLE
tup=(1,2,"Sai",True)
tup1=(1)
tup2=(1,)
print(tup,tup1,tup2)
print(type(tup),type(tup1),type(tup2))

if "Sai" in tup:
    print("yes")
else:
    print("no")


tup3=tup[2:4]
print(tup3)

print(tup[0:3])