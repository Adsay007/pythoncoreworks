#Given a list

l=[23,45,67,12,90,78]
max=l[0]
min =l[0]
for i in l:
    if (i>max):
        max=i
    elif(i<min):
        min=i

print("max :",max)
print("min :",min)