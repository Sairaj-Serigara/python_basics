#dir is used to check the methods available in the list or tuple etc

x=(1,3,4)
print(dir(x))

# print(x.__add__)
print("\n")

#__dict__
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

obj=person("sai",20)
print(obj.__dict__)
print("\n")

#help is used to get help documentation for help object including description of this attribute and method

print(help(person))