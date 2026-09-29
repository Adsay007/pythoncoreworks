def add():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result:", a + b)

def sub():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result:", a - b)

def mul():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result:", a * b)

def div():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    if b != 0:
        print("Result:", a / b)
    else:
        print("Error: Cannot divide by zero")

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