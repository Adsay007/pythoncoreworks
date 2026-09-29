""" 
filter = Select specific items.
Use it when you want to weed out items you don't need based on a True/False test.

Syntax: filter(function, iterable)

Input: A list of 5 items.

Output: A smaller list containing only the items that passed the test.

Analogy: Pulling only the defective cars off the assembly line. """

#Bool Output Map Vs Filter
l =[1,2,3,4,5,6,7,8,9]

print("Bool Map:" ,list(map(lambda x:x%2==0,l)))
print("Bool Filter:" ,list(filter(lambda x:x%2==0,l)))

# Print even values greater than 50
l1 = [23,45,67,12,89,70]

print("Even Greater than 50 :", list(filter(lambda x:x%2==0 and x>50,l1)))

#Filter the color length is greater than 5
#Filter Colour containing letter N
l2=["red","green","blue","yellow","orange"]

print("Colour:" ,list(filter(lambda x:len(x) > 5,l2 )))

print("Colour with Letter N :" ,list(filter(lambda x: 'n' in x,l2 )))
