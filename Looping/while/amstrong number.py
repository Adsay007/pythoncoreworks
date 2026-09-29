# Find if a number is Amstrong 

i = int(input("Enter a Number : "))
temp1 = i
temp = i 
sum = 0
count = 0

while (i > 0):
    i= i // 10 
    count += 1

while (temp1 > 0):
    digit = temp1 % 10
    sum += digit ** count 
    temp1 //= 10

if temp == sum :
    print("Amstrong")
else:
    print(" Not Amstrong")


