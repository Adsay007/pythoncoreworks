# Find strong number 

number = 144
temp = number

sum = 0
while (number > 0):
    digit = number % 10
    fact = 1
    for i in range (1,digit+1):
        fact *= i
    sum += fact
    number //= 10

print ("Strong " if temp == sum else " Not Strong")
