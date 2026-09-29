
class Person:
    def __init__(self,n,a): #__init__ used as initializer to set up starting attributes of a new obj
        self.name = n
        self.age = a

    def show(self): #Self represents current object
        print(self.name,self.age)

p1 =Person("arun",26) # creates object of class person , it will call __init__ automatically
p2 =Person("amal",30)
p3 =Person("riya",40)

p1.show()
p2.show()
p3.show()