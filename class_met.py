#classmethod is used to change the class variables rather than instances
class Employee:
    company="Apple"
    def show(self):
        print(f"name is {self.name} and company is {self.company}")

    @classmethod
    def change_comp(something,new_comp):
        something.company=new_comp

obj=Employee()
obj.name="sai"
obj.show()
obj.change_comp("tesla")
obj.show()
print(Employee.company)  #here actually company is not changed to change it we should use classmethod decorator


#simple code for decorators
# class Employee:
#     company_name = "Realme"
#
#     @classmethods
#     def change_company(cls, new_name):
#         cls.company_name = new_name
