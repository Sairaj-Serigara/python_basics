class Father:
    def skills(self):
        print("Father: Cooking")

class Mother:
    def skills(self):
        print("Mother: Dancing")

class Child(Father, Mother):  # Multiple inheritance
    def skills(self):
        # Call both parents' methods
        Father.skills(self)   # Call Father's method
        Mother.skills(self)   # Call Mother's method
        print("Child: Singing")


# Create object of Child
c = Child()
c.skills()




# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
# 
#
# class Mammal:
#     def __init__(self, name, fur_color):
#         self.name = name
#         self.fur_color = fur_color
#
#
# class Dog(Animal, Mammal):
#     def __init__(self, name, breed, fur_color):
#         super().__init__(name, "Dog")   # Calls Animal first (MRO order)
#         self.fur_color = fur_color      # Add Mammal’s attribute manually
#         self.breed = breed
#
#     def make_sound(self):
#         print("Bark!")
#
#
# # Example
# d = Dog("Tommy", "Labrador", "Brown")
# print(d.name)       # Tommy
# print(d.species)    # Dog
# print(d.breed)      # Labrador
# print(d.fur_color)  # Brown
# d.make_sound()      # Bark!
