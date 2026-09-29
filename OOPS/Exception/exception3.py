import math

try:

    num = int(input("Enter a number: "))
    
  
    result = math.factorial(num)
    

    print(f"The factorial of {num} is {result}")
    
except ValueError:
    
    print("Value Error")