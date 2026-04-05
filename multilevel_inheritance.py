class Animal:
    def __init__(self,breed):
        self.breed =breed

    def showdetails(self):
        print(f"breed is {self.breed}")

class Dog(Animal):
    def __init__(self,breed,name):
        super().__init__(breed)
        self.name = name

    def showdetails(self):
        # Animal.showdetails(self)
        super().showdetails()
        print(f"Dog is {self.name}")


class Cat(Dog):
    def __init__(self,cate,breed,name):
        super().__init__(breed,name)
        self.cate = cate
    def showdetails(self):
        super().showdetails()
        print(f"Cat is {self.cate}")

obj=Cat("something","persian","tom")
obj.showdetails()