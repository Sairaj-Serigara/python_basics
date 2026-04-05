#protected is used to describe a member of class that is accessed by class itself or subclass
# _ is used for protected


class Employee:
    def __init__(self,name):
        self._name=name

    def funcname(self):
        print(self._name)


class Info(Employee):
    def __init__(self,name,age):
        Employee.__init__(self,name)
        self.age=age

    def printage(self):
        print(self.age)


obj=Employee("John")
obj.funcname()
obj1=Info("sairaj",20)
obj1.funcname()
obj1.printage()