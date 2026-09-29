#Inheritance 

class Parent:

    def m1(self):
        print("In Parent class method m1")

    def m2(self):
        print("In Parent class method m2")


class Child(Parent):
    def m1(self):
        super().m1()
        print("In Child Class methom m1 from Parent Class")

    def m3(self):
        print("In Child class Method m3")


c=Child()
c.m1()
c.m2()
c.m3()