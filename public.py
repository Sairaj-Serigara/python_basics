#ther is no public privsye protected in python .for convention these are used as private public protected

# class employee:
#     def __init__(self):
#         self.name="Sairj"
#     def s(self):
#         print(self.name)
# a=employee()
# a.s()

class employee1:
    def __init__(self,name,age):
        self.name=name
        self.age=age
obj=employee1("Sairaj",20)
print(obj.name)
print(obj.age)