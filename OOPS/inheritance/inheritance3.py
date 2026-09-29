
class Company:
    def __init__(self):
        self.cmpnyname = input("Enter Company Name : ")
        self.location = input("Enter Location : ")
    def display_company(self):
        print(f"Company name : {self.cmpnyname}")

class Employee(Company):
    def __init__(self):
        super().__init__()
        self.empid = int(input("Enter Employee Id : "))
        self.name = input("Enter Name : ")
        self.designation = input("Enter Designation : ")
        self.salary = int(input("Enter Salary : "))

    def display_details(self):
        super().display_company()
        print(f"Employee Name : {self.name}, Employee id : {self.empid}")
        print(f"Employee Designation : {self.designation}, Employee Salary : {self.salary}")

    def update_salary(self):
        self.salary *= 1.1

        
s=Employee()
s.display_details()
s.update_salary()
s.display_details()