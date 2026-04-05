#decoratoe is a function that takes another function as argument and returns the new function that modifies the behaviour of the
# original function
# Decorators in Python are a powerful and elegant way to modify or enhance the behavior of functions or methods without changing
# their actual code.
# def my_decorator(fx):
#     def mfx():
#         print("good morning")
#         fx()
#         print("Thanks for using this application")
#     return mfx
# @my_decorator
# def hello():
#     print("Hello")
#
# hello()


def dec(decorator):
    def wrapper():
        print("wrapper function")
        decorator()
        print("wrapper end")
    return wrapper
@dec
def hello():    #here hello passes to dec(decorator).In 1 line hello=dec(hello),then executes wrapper then prints hello then ends
    print("hello world")

hello()

print("\n")

def deco1(func):
    def wrapper():
        print(">>> deco1 start")
        func()
        print(">>> deco1 end")
    return wrapper

def deco2(func):
    def wrapper():
        print("*** deco2 start ***")
        func()
        print("*** deco2 end ***")
    return wrapper

@deco1
def greet():
    print("Hi!")

@deco2
def farewell():
    print("Bye!")

greet()
farewell()
