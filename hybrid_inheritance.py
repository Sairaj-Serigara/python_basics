# A combination of two or more types of inheritance (like multiple + hierarchical together).
# Base class
class Animal:
    def breathe(self):
        print("All animals breathe")

# Child class 1
class Mammal(Animal):  # Single inheritance
    def feed(self):
        print("Mammals feed milk")

# Child class 2
class Bird(Animal):  # Hierarchical inheritance
    def fly(self):
        print("Birds can fly")

# Child class 3 (inherits from two classes → Multiple inheritance)
class Bat(Mammal, Bird):
    def special(self):
        print("Bat is a mammal but can fly")


# Example usage
b = Bat()
b.breathe()   # From Animal
b.feed()      # From Mammal
b.fly()       # From Bird
b.special()   # From Bat
