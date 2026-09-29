class Person:
    def __init__(self): #__init__ used to create and initialize object attributes and prop
        self.name = input("Enter Name : ")
        self.age = int(input("Enter Age :"))

    def show(self): #Self represents current object
        print(f"Name : {self.name} Age :{self.age}")

p1 =Person() # creates object of class person , it will call __init__ automatically


p1.show()
