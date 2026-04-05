for i in range (5):
    print(i)
else:
    print("out of range")


for i in range(6):
    print(i)
    if i==3:
        break

else:
    print("out of range")   # else will  ot be executed cuz loop ended there