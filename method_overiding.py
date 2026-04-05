class Square:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def area(self):
        return self.x*self.y

class circle(Square):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14*self.radius*self.radius

sqobj=Square(5,3)
print(sqobj.area())


# class Parent:
#     def greet(self):
#         print("Hello from Parent")
#
# class Child(Parent):
#     def greet(self):  # <-- same method name as in Parent
#         print("Hello from Child")  # <-- overrides Parent version
#
# # Using it
# p = Parent()
# p.greet()   # Hello from Parent
#
# c = Child()
# c.greet()   # Hello from Child  (overridden method is called)
#
#
# cir=circle(2)
# print(cir.area())

'''
Here, Child.greet() overrides Parent.greet() because:
Same name (greet)
Same parameters (none in this case)
Happens in a subclass (Child inherits Parent)
'''