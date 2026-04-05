class Employee:
    company_name="realme" #class variable(applies to whole class
    no_employee=0
    def __init__(self,name):
        self.name=name  #instance variable
        self.raise_amnt=0.02
        Employee.no_employee+=1

    def display(self):
        print(f"Name of the employee is {self.name} and the rase in salary in {self.company_name} is {self.raise_amnt} and number of employee is {self.no_employee}")

emp1=Employee("John")
emp1.raise_amnt=0.5
emp1.company_name="apple"
emp1.display()
Employee.company_name="samsung"
emp2=Employee("Jane")
emp2.display()