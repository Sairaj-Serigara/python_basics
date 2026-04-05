class employee:
    def __init__(self,name):
        self.name=name

    def printname(self):
        print(self.name)

class info(employee):
    def __init__(self,name,age):
        employee.__init__(self,name)
        self.age=age

    def printage(self):
        print(self.age)

obj=employee("sairaj")
obj.printname()

obj1=info("harry",20)
obj1.printname()
obj1.printage()