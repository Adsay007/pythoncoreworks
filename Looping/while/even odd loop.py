# get the sum of even numbers and produt of odd number from 1 to n

i=1
n=int(input("Enter a Number : "))
sum=0
product=1

while(i <= n):
    if i % 2 == 0:
        sum += i
    else:
        product *= i
    i += 1
print (f"Sum = {sum}")
print (f"Product = {product}")