import time
t=time.localtime()
formated_time=time.strftime("%y-%m-%d ,%H:%M:%S",t)
print(formated_time)