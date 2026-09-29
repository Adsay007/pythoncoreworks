from functools import reduce

#Q.Write Python Programs Using map(), filter(), or reduce()

# 1. Capitalize all names in a list
names = ['alin', 'arun', 'anu']
print(*map(str.capitalize, names)) 
# Output: Alin Arun Anu

# 2. Append "@gmail.com" to a list of usernames
users = ['user1', 'user2']
print(*map(lambda x: x + "@gmail.com", users)) 
# Output: user1@gmail.com user2@gmail.com

# 3. Filter out all empty strings from a list
words = ['hello', ' ', 'world', ' ', 'python']
print(*filter(lambda x: x.strip() != "", words)) 
# Output: hello world python

# 4. Filter names that start with the letter 'A'
names = ['Anu', 'Neenu', 'Arun', 'Ravi']
print(*filter(lambda x: x.startswith('A'), names)) 
# Output: Anu Arun

# 5. Concatenate all strings in a list
words = ['Python', 'is', 'fun']
print(reduce(lambda x, y: x + " " + y, words)) 
# Output: Python is fun

# 6. Multiply all numbers in a list
nums = [2, 3, 4]
print(reduce(lambda x, y: x * y, nums)) 
# Output: 24

# 7. Extract First Character of Each Word
words = ["apple", "banana", "cherry"]
print(*map(lambda x: x[0], words)) 
# Output: a b c

# 8. Add 10 to Each Number
nums = [5, 10, 15]
print(*map(lambda x: x + 10, nums)) 
# Output: 15 20 25

# 9. Given a List 
l = [12, -4, 78, -34, 90, 45, 16, 26, -2, -11, 3]

#Sum of positive even numbers
print(reduce(lambda x, y: x + y, filter(lambda x: x > 0 and x % 2 == 0, l), 0)),
# Output: 222

# #Sum of Positive Odd numbers
print(reduce(lambda x, y: x + y, filter(lambda x: x > 0 and x % 2 != 0, l), 0)),
#Output: 48 

# #Sum of Negative odd numbers
print(reduce(lambda x, y: x + y, filter(lambda x: x < 0 and x % 2 != 0, l), 0)),
#Output: -11

# #Sum of Negatve Even numbers
print(reduce(lambda x, y: x + y, filter(lambda x: x < 0 and x % 2 == 0, l), 0)),
#Output: -40

# #Count of Positive numbers
print(sum(map(lambda x: x > 0, l))),
#Output: 7

# #Count of negative numbers
print(sum(map(lambda x: x < 0, l))),
#Output: 4


# 10. Convert all Strings to Integers
nums = ["1", "2", "3", "4"]
print(*map(int, nums)) 
# Output: 1 2 3 4

# 11. Product Dictionary Operations
p = [{'name':'laptop','price':50000},
     {'name':'phone','price':20000},
     {'name':'watch','price':3000},
     {'name':'Tablet','price':25000}]

# Product names in Uppercase
print(*map(lambda x: x['name'].upper(), p)) 
# Output: LAPTOP PHONE WATCH TABLET

# Products with price > 10000 (Prints the raw dictionary items on one line)
print(*filter(lambda x: x['price'] > 10000, p)) 
# Output: {'name': 'laptop', 'price': 50000} {'name': 'phone', 'price': 20000} {'name': 'Tablet', 'price': 25000}

# Total price of all products
print(reduce(lambda acc, x: acc + x['price'], p, 0)) 
# Output: 98000