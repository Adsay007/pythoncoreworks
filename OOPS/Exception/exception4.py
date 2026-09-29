def add():
 try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result:", a + b)
 except:
     print("Value Error")

def sub():
 try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result:", a - b)
 except:
    print("Value Error")

def mul():
 try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result:", a * b)
 except:
    print("Value Error")

def div():
 try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
   
    print("Result:", a / b)
 except ZeroDivisionError:
    print("Zero Divison Error")
 except ValueError:
    print("Value Error")
   

# Main Menu
print("Menu driven")
print("1.Add")
print("2.Sub")
print("3.Mul")
print("4.Div")
print("5.Exit")

ch = int(input("Enter your choice: "))

if ch == 1:
    add()
elif ch == 2:
    sub()
elif ch == 3:
    mul()
elif ch == 4:
    div()
else:
    exit()