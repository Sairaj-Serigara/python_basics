
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    @classmethod
    def from_str(cls):
        return cls(str.split("-")[0],int(str.split("-")[1]))
str="me-50000"
e=Employee("Sairaj",50000)
print(e.name)
print(e.salary)

#if we have given a string like this we can follow below steps for one or two objects but for many objects we have to create a class method
# str="Sairaj-50000"
# e1=Employee(str.split("-")[0],str.split("-")[1])
# print(e1.name)
# print(e1.salary)

e2=Employee.from_str()
print(e2.name)
print(e2.salary)