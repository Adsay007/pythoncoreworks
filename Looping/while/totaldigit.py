#get the count of digist given 

i = int(input("Enter a number : "))

count = 0

while(i > 0):
    i = i // 10
    count += 1

print(count)

# Count of even digits 

p = int(input("Enter a number : "))

count1 = 0

while(p > 0):
    even = p % 10
    if even % 2 == 0:
         count1 += 1
 
    p = p // 10
   

print(count1)

# Count of even digits and odd digits 

p2 = int(input("Enter a number : "))

counteven = 0
countodd = 0

while(p2 > 0):
    digits = p2 % 10
    if digits % 2 == 0:
         counteven += 1
    else:
        countodd += 1
 
    p2 = p2 // 10
   

print(f"Even = {counteven} , Odd = {countodd}")
