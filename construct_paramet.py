#parameterised constructor
class person:
    def __init__(self,n,a):
        self.name=n
        self.age=a
        print("hello")
    def info(self):
            print(f"{self.name} is {self.age} years old")
a=person("sai",22)
b=person("sacchu",40)
a.info()
b.info()
print("\n")

#default constructor
class car:
    def __init__(self):
        print("Car contains four wheels")
obj=car()
