# Problem 1: Dictionary of Number Occurrences ---
# Given list

number_list = [11, 34, 78, 23, 90, 65]

# Find the largest and smallest directly (no sorting needed for these)
largest_num = max(number_list)
smallest_num = min(number_list)

# Now sort the list to easily grab the positional items
number_list.sort()
# The list is now: [11, 23, 34, 65, 78, 90]

# Grab the second items from the front and back
second_smallest = number_list[1]
second_largest = number_list[-2]

print("Largest number:", largest_num)
print("Second largest number:", second_largest)
print("Smallest number:", smallest_num)
print("Second smallest number:", second_smallest)