class Employee:
    def __init__(self):
        self.empid= int(input("Enter Empid : "))
        self.name= input("Enter Name : ")
        self.age= int(input("Enter Age : "))
        self.place= input("Enter Place : ")
        self.salary= int(input("Enter Salary : "))
        self.designation= input("Enter Designation : ")

    def getsalary(self):
        print ("Salary : ",self.salary )

    def personaldetails(self):
        print("Name :",self.name)
        print("Age :",self.age)
        print("Place :",self.place)

p1=Employee()

p1.getsalary()
p1.personaldetails()




