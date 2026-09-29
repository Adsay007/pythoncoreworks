#Lis Functions

# len() - Get the number of items in a list
len_list = [10, 20, 30]
list_length = len(len_list)
print(list_length)

# list(seq) - Convert a sequence (like a string) into a list
my_string = "ABC"
string_to_list = list(my_string)
print(string_to_list)

# append(element) - Add one item to the end
append_list = [10, 20]
append_list.append(30)
print(append_list)

# extend(seq) - Add multiple items to the end
extend_list = [10, 20]
extend_list.extend([30, 40])
print(extend_list)

# index() - Find the position of an item
index_list = [10, 20, 30]
position = index_list.index(20)
print(position)

# count() - Count how many times an item appears
count_list = [10, 20, 10, 30]
total_tens = count_list.count(10)
print(total_tens)

# remove(element) - Delete the first matching item
remove_list = [10, 20, 30]
remove_list.remove(20)
print(remove_list)

# pop() - Remove the very last item
pop_list = [10, 20, 30]
pop_list.pop()
print(pop_list)

# pop(index) - Remove an item at a specific position
pop_index_list = [10, 20, 30]
pop_index_list.pop(0)
print(pop_index_list)

# insert(index, element) - Put an item at a specific position
insert_list = [10, 20, 30, 40, 50, 60]
insert_list.insert(2, 70)
print(insert_list)

# copy() - Make a duplicate of the list
original_list = [10, 20, 30]
copied_list = original_list.copy()
print(copied_list)

# clear() - Empty the entire list
clear_list = [10, 20, 30]
clear_list.clear()
print(clear_list)

# sort() - Put items in order (smallest to largest)
sort_list = [30, 10, 20]
sort_list.sort()
print(sort_list)

# reverse() - Flip the list backwards
reverse_list = [10, 20, 30]
reverse_list.reverse()
print(reverse_list)

# max() - Find the largest item in a list
my_list = [10, 50, 20, 30]
largest_item = max(my_list)
print(largest_item)

# min() - Find the smallest item in a list
my_list = [10, 50, 20, 30]
smallest_item = min(my_list)
print(smallest_item)