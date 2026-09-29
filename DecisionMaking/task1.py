#Ask user to enter a number below 20 , if higher print Too High otherwise Print Thank You 

num= int(input("Enter a Number below 20 : "))

if num < 20:
    print (f"Thank You")
else:
    print (f"{num} is Too High")