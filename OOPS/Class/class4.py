class Student:
    def __init__(self):
        self.rollno = int(input("Enter Roll No : "))
        self.name = input("Enter Name : ")
        self.mark1 = int(input("Enter Mark 1 : "))
        self.makrk2 = int(input("Enter Mark 2 : "))
        self.makr3 = int(input("Enter MArk 3 : "))
    def display(self):
        print(f"Roll No :{self.rollno} Total Mark : {self.mark1+ self.makrk2 + self.makr3}")


s1=Student()
s1.display()

s2=Student()
s2.display()