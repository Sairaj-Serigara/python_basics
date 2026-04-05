# One parent class, multiple child classes.
# Parent class
class Animal:
    def sound(self):
        print("Animals make sounds")

# Child classes inheriting from Animal
class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")


# Example usage
d = Dog()
c = Cat()

d.sound()   # Dog barks
c.sound()   # Cat meows
