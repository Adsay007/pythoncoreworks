from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self):
        self.name = input("Enter Name : ")
        self.age = int(input("Enter Age : "))
        self.empid = int(input("Enter Empid : "))

    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self):
        super().__init__() 
        self.monthlysalary = int(input("Enter Monthly Salary : "))

    def calculate_salary(self):
        print("Full-Time Salary :", self.monthlysalary)

class PartTimeEmployee(Employee):
    def __init__(self):
        super().__init__()
        self.rate = int(input("Enter Rate : "))
        self.hours = int(input("Enter Working Hours : "))

    def calculate_salary(self):
        print("Part-Time Salary :", self.rate * self.hours)



femp = FullTimeEmployee()
femp.calculate_salary()


pemp = PartTimeEmployee()
pemp.calculate_salary()