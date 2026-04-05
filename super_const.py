


class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class student(Employee):
    def __init__(self,name,age,usn):
        # self.name=name
        # self.age=age
        super().__init__(name,age)
        self.usn=usn

obj=Employee("sai",20)
obj2=student("harry",20,4)
print(obj2.name)
print(obj.name)
print(obj2.usn)