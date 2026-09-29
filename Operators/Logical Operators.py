# Logical Operators - and , or , not

number = int(input("enter the number: ")) 

if number % 3 == 0 and number % 5 == 0:
    print(" Divisible by 3 and 5")

elif number % 3 == 0 or number % 5 == 0:
    print(" Divisible either by 3 or 5")

else:
    print("Not Divisble by 3 and 5")
    
"""
#condition1
num = 15

num % 3 == 0 and num % 5 == 0
#  True      and    True  >> True 

#condition2
num = 9

num % 3 == 0 and num % 5 == 0
#  True      and    False  >> False 

#condition3
num = 7

num % 3 == 0 and num % 5 == 0
#  False     and    False  >> False 

condition1   condition2   And Output  Or Output

True           True        True         True

False          False       False        False

True           False       False        True

False          True        False        True
"""


