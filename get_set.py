# Getter → a method (or property) to read the value of a private attribute.
# Setter → a method (or property) to update/change the value of a private attribute

# If you just make variables public, anyone can change them in any way (even with wrong values).
# Getters and setters let you control access to your class variables
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):          # getter
        return self._name

    @name.setter             # setter must use same name "name"
    def name(self, new_name):
        self._name = new_name


p = Person("Sairaj")
print(p.name)    # calls getter → Sairaj

p.name = "Devadiga"  # calls setter
print(p.name)    # getter again → Devadiga
