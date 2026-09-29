"""
A lambda function is a small, anonymous function in Python. 
While standard functions are defined using the def keyword and given a name, 
lambda functions are defined in a single line using the lambda keyword 
and typically act as quick, throwaway operations.

The Syntax:
lambda arguments: expression

"""

# sum of 2 numbers
# Note: The correct Python syntax uses a colon ':' instead of an '=' after the variables
sum_two = lambda a, b: a + b
print("Sum of 5 and 3:", sum_two(5, 3))

# product of 3 numbers
product_three = lambda a, b, c: a * b * c
print("Product of 2, 3, and 4:", product_three(2, 3, 4))

# Cube of a number
cube = lambda x: x ** 3
print("Cube of 4:", cube(4))

# first letter of a string
first_letter = lambda s: s[0]
print("First letter of 'Python':", first_letter("Python"))

# length of a string
string_length = lambda s: len(s)
print("Length of 'Python':", string_length("Python"))

# reverse of a string
reverse_string = lambda s: s[::-1]
print("Reverse of 'Python':", reverse_string("Python"))

# name value from a dictionary
get_name = lambda d: d.get('name')
sample_dict = {'name': 'arun', 'age': 23}
print("Name from dictionary:", get_name(sample_dict))

# second element from a list
second_element = lambda l: l[1]
sample_list = [10, 20, 30, 40]
print("Second element from list:", second_element(sample_list))

# Add 10 to a number
add_ten = lambda x: x + 10
print("15 plus 10:", add_ten(15))