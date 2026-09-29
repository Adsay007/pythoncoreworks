
class Person:
    def __init__(self):
        self.name = input("Enter Name : ")
        self.age = int(input("Enter Age : "))
    def show(self):
        print(self.name , self.age)
class Student(Person):
    def __init__(self):
        super().__init__()
        self.rollno = int(input("Enter Rollno : "))
        self.course = input("Enter Course : ")
        self.mark = int(input("Enter Mark : "))

    def show(self):
        super().show()
        print(f"Roll No : {self.rollno}, Mark : {self.mark}, Course : {self.course}")

    def updatemark(self):
        self.mark = int(input("Enter new Mark : "))


s=Student()
s.show()
s.updatemark()
s.show()