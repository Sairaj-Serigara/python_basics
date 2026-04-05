x=10
print(x)

def fun():
    print("hello")
    global x
    x=5
    print(x)


fun()
print(x)