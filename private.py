#ther is such thing called privayr in python,as in other language
#but can be considered private by using__

class employee:
    def __init__(self):
        self.__name="sairaj"    #becomes private after using __

obj=employee()
# print(obj.__name)   throws error
print(obj._employee__name)    #this is name mangling