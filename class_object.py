class person():
    name="Sai"
    age=20
    role="data scientist"
    def info(self):
        print(f"{self.name} is a {self.role}")

a=person()    #creating object
b=person()
c=person()
b.name="prithesh"
b.role="HR"
# a.name="sairaj"
# a.role="python developer"
# print(a.name,a.role)
a.info()
b.info()

