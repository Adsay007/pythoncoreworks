
""" 
Need to add import functools !!!
reduce = Combine into one.
Use it when you want to merge every item in a list together to get a single final answer.

Syntax: functools.reduce(function, iterable, initializer)

Input: A list of 5 items.

Output: One single value.

Analogy: Crushing all the cars on the assembly line into one giant cube of metal. """

from functools import reduce

numbers = [1, 2, 3, 4, 5]
words = ['Python', 'is', 'awesome']

# Sum of all numbers in a list
print("Sum:", reduce(lambda x, y: x + y, numbers))

# Product of all numbers in a list
print("Product:", reduce(lambda x, y: x * y, numbers))

# Find the maximum number in a list
print("Max number:", reduce(lambda x, y: x if x > y else y, numbers))

# Combine a list of strings into a single sentence
print("Sentence:", reduce(lambda x, y: x + ' ' + y, words))