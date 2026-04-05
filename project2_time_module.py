import time
# Time=time.strftime("%H:%M:%S")
# print(Time)
hour=int(time.strftime('%H'))
print(hour)
min=time.strftime("%M")
print(min)
sec=time.strftime("%S")
print(sec)


#if hour is not cinverted into int it will shoe error cuz strftime returns string
if(hour>=0 and hour<12):
    print("gm")
elif(hour>=12 and hour<5):
    print("good after noon")
else:
    print("good night")