marks=[45,23,90,12,32,47]

i=0
# for mark in marks:
#     print(mark)
#     if i==3:
#         print("lll")
#     i+=1


for i,mark in enumerate(marks):
    print(mark)
    if i==3:
        print("lllll")

#both are same
#enumerate is used to print objs and index in list,string,tuple


for i,mark in enumerate(marks,start=1):#starts from index 1
    print(i,mark)

s="gello"
for index, c in enumerate(s):
    print(index,c)