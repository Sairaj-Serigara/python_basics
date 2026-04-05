class Student():
    def __init__(self,name,usn):
        self._name = name
        self._usn = usn
    def show(self):
        print(f"student name is {self._name} usn is {self._usn}")

class studentdetails(Student):
    def marks(self,m1):
        print(f"marks is {m1} ")
obj=Student("sairaj",129)
obj.show()
obj1=studentdetails("sairaj",130)
obj1.show()
obj1.marks(99)