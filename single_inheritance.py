class Animal:
    def __init__(self,breed):
        self.breed= breed

    def sound(self):
        print("Sounds made by animal")


class Cat(Animal):
    def __init__(self,name,breed):
        super().__init__(breed)
        self.name=name

    def sound(self):
        print("Mwowes")

ani=Animal("Persian")
ani.sound()
ca=Cat("Julian","persian")
ca.sound()
print(ca.name)
print(ca.breed)