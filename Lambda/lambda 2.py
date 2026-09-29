# create a new list of squares 
l=[1,2,3,4]
print("List:",list(map(lambda x:x**2,l)))
print("Tuple:",tuple(map(lambda x:x**2,l)))
print("Set:",set(map(lambda x:x**2,l)))

# create a new list of cubes
l1 = [1, 2, 3, 4]
print("Cubes:", list(map(lambda x: x**3, l1)))

# create a new list of square roots
l2 = [25, 36, 81, 100]
print("Square roots:", list(map(lambda x: x**0.5, l2)))

# Add 10 to each element in the given sequence
l3 = [23, 78, 12, 56]
print("Plus 10:", list(map(lambda x: x + 10, l3)))


colors = ['red', 'green', 'blue', 'yellow', 'black']

# create a new list of lengths
print("Lengths:", list(map(lambda x: len(x), colors)))

# create a new list of first characters
print("First chars:", list(map(lambda x: x[0], colors)))

# create a new list of last characters
print("Last chars:", list(map(lambda x: x[-1], colors)))

# create a new list of reverse of each elemnt
print("Reversed strings:", list(map(lambda x: x[::-1], colors)))


# given a list of dictionaries
l4 = [{'empid':100,'name':'arun','salary':20000,'email':'arun@gmail.com'},
      {'empid':101,'name':'amal','salary':25000,'email':'amal@gmail.com'},
      {'empid':102,'name':'anu','salary':30000,'email':'anu@gmail.com'}]

# create a new list of emails
print("Emails:", list(map(lambda x: x['email'], l4)))