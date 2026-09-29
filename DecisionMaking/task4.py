"""
If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird 
If n is even and in the inclusive range of 6 to 20, print Weird 
If n is even and greater than 20, print Not Weird

"""

num= int(input("Enter a Number : "))

if num % 2 == 0:
    if num >= 2 and num <=5:
        print("Even and in range of 2 and 5")
    elif num >= 6 and num <=20:
            print("Even and in range of 6 and 20")
    elif num >20:
         print("Greater than 20")
else: 
     print(f"{num} is odd")


num1= int(input("Enter a Number : "))

if num1 % 2 != 0:
    print(f"{num1} is odd")
elif num1 >= 2 and num1 <=5:
        print("Even and in range of 2 and 5")
elif num1 >= 6 and num1 <=20:
        print("Even and in range of 6 and 20")
elif num1 >20:
        print("Greater than 20")
