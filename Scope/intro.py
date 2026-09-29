""" Scope means where a variable can be accessed 
LEGB rule - L for Local , E for enclosing etc so this is the order it checks for variable

there are - global , local ,nonlocal/enclosing , built in

>Global - declared inside a main part of program 
>Local - declared inside a block of code or function
>Nonlocal/enclosing - dclared inside a nested function
>Builtin - all the names declared in python built in library
 """

x=20 #Global

print("Outside :",x)

def a():
    print("Inside :",x)

a()
######
#Local
def b():
    z=30 #Local
    print("Inside :",z)
    

b()

#print("Outside :",z)

#Nonlocal/enclosing

def outer():
    w=33 #nonlocal
    def inner():
       print("inner =",w)
    inner()
    print("outer =",w)

outer()
