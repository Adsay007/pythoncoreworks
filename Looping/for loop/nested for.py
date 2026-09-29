# find the factorial from 2 to 6

for num in range (2,7):
    product=1
    for i in range (1 , num+1):
            product *= i

    print (f"Factorial of {num} is {product}")