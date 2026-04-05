#super is used to refer the parent class ,it is usefull when class inherites from multiple class

class parentclass:
    def parentmethod(self):
        print("Parent method")

class childclass(parentclass):
    def parentmethod(self):
        print("hai")
        super().parentmethod()
    def childmethod(self):
        print("Child method")
        super().parentmethod()

obj=childclass()
obj.childmethod()
obj.parentmethod()
