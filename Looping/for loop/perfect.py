# Find Perfect Number

num= int(input("Enter a Number :"))
sum = 0
for i in range(1 ,num):
    if num % i == 0:
        sum += i
print(sum)
if sum == num:
    print("This is perfect")
else:
    print ("Not Perfect ")
    