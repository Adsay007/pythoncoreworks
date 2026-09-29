# Find Palindrome Number 

i = int(input("Enter a Number : "))
temp = i
reverse = 0

while (i > 0):
    digit = i % 10
    reverse = reverse * 10 + digit
    i //= 10 


print(reverse)

if reverse == temp :
    print("Palindrome")
else:
    print("Not Palindrome")