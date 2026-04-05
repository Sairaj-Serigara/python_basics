#default argument
def average(a=2,b=8):
    print((a+b)/2)

average(5,5) #neglets 2,2
average(b=3)       #takes A by  defaul  and b as

#Required argument
def average2(a,b,c=9):
    return ((a+b+c)/3)
c=average2(4,5)  # a,b are the required argument
print(c)

#variable length argument
def average3(*numbers):
    sum=0
    for i in numbers:#for more multiple numbers
        sum=sum+i
        print(sum)
average3(3,4,2)
