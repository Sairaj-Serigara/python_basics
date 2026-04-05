def greet(name):
    def wrapper(*args,**kwargs):
        print("Hello sairaj")
        name(*args,**kwargs)
        print("Bye sairaj")
    return wrapper

@greet
def hello():
    print("namaste")

@greet
def add(a,b):
    print(a+b)

hello()
add(1,2)