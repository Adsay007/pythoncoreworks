class Student:
    def __init__(self):
        self.roll=int(input("Enter Roll No : "))
        self.name=input("Enter Name : ")
        self.mark=int(input("Enter Total Mark : "))

    def studentdetails(self):
         print("\n")
         print(f"Roll Number : {self.roll}")
         print(f"Student Name : {self.name}")
         print(f"Total Mark : {self.mark}")
        
l=[]

while(1):
    # Main Menu
    print("\nMenu")
    print("1.Add Student Details")
    print("2.Update Mark")
    print("3.Display All Students Details")
    print("4.Search Student by Roll No")
    print("5.Delete Student Detail ")
    print("6.Exit\n")

    ch = int(input("Enter your choice: "))
    
    if ch == 1:
        new = Student() 
        for i in l:
            if i.roll == new.roll:
                print("Student Exists")
                break
        else:
            l += [new]
               
    elif ch == 2:
        s = int(input("Enter roll no to update mark: "))
        for i in l:
            if i.roll == s:
                print(f"Current Mark : {i.mark}")
                i.mark = int(input("Enter New Total Mark : "))
                break
        else:
            print("Student Doesnt Exist")  

    elif ch == 3:
        for i in l:
            i.studentdetails()

    elif ch == 4:
        roll1 = int(input("Enter Roll No : "))
        for i in l:
            if i.roll == roll1:
                i.studentdetails()
                break
        else:
            print("Student Doesnt Exist")
            
    elif ch == 5:
        roll2 = int(input("Enter roll no to delete: "))
        for i in l:
            if i.roll == roll2:
                l.remove(i)
                break
        else:
            print("Student doesnt exist")

    else:
        exit()