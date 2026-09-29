# --- Problem 3: Maximum Salary and Minimum Age (List Comprehension Method) ---
# Given list 'l' containing employee data: [Name, Age, Salary]
l = [['arun', 23, 30000],
     ['amal', 25, 50000],
     ['anu', 27, 40000]]

# max() - Extract the salary (index 2) from each item 'i' in the list and find the highest
maximum_salary = max([i[2] for i in l])

# min() - Extract the age (index 1) from each item 'i' in the list and find the lowest
minimum_age = min([i[1] for i in l])

# Print the results with descriptive text
print("Maximum salary:", maximum_salary)
print("Minimum age:", minimum_age)