# break
for i in range(12):
    if i==10:#here since we ahve used i+1 we get 5x10=50 at 9th iteration ,so breaking at i=10
        break
    print("5 X",i+1,"=",5*(i+1))



#continue
for i in range(12):
    if i==10:
        continue
    print("5 X",i+1,"=",5*(i+1))

