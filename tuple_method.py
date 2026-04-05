countries=("india","spain","russia","australia","america")
temp=list(countries)
temp.append("korea")
temp[1]="england"
temp=tuple(countries)
print(countries)
countries=tuple(temp)
print(countries)

#we can add two tuples directly
udupi=("hebri","mangalore")
udupi2=("kundapur",)
dist=udupi+udupi2
print(dist)

res=udupi.count("hebri")
print(res)
res1=udupi.index("hebri")
print(res1)

num=(1,4,5,3,8,9,3,3,5,6,6)
num_res=num.index(3,4,7)#index of 3 in the range of 3 to 7
print(num_res)
num1=print(len(num))
