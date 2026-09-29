# Check whether a number is negative or positive or zero

num= int(input("Enter a Number : "))

if num > 0:
    print(f"{num} is Positive")
elif num == 0:
    print(f"{num} is Zero")

else:
    print(f"{num} is Negative")
