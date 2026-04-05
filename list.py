marks=[1,2,3,"Sai",True]
# print(marks)
# print(marks[-3])
# print(marks[len(marks)-3])
# print(5-3)

if "Sai" in marks:
    print("yes")
else:
    print("no")
if 3 in marks:
    print("yes")
else:
    print("no")


#same thing applies for string
if "Sa" in "Sai":
    print("yes")
else:
    print("no")

list2=[i for i in range(4)]#list comprehension
print(list2)
list3=[i*i for i in range(10) if i%2==0]
print(list3)
