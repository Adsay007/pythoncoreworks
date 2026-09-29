# set() - Create an empty set or convert a sequence into a set
my_list = [1, 2, 2, 3] # Notice the duplicate 2
new_set = set(my_list)
print("set():", new_set) # Sets automatically remove duplicates -> {1, 2, 3}

# len() - Get the number of items in a set
len_set = {1, 2, 3, 4, 5}
set_length = len(len_set)
print("len():", set_length)

# add(element) - Add a single new element to the set
add_set = {1, 2}
add_set.add(3)
print("add():", add_set)

# update(seq) - Add multiple elements from a sequence (like a list) to the set
update_set = {1, 2}
update_set.update([3, 4, 5])
print("update():", update_set)

# remove(element) - Delete a single element (throws an error if the item doesn't exist)
remove_set = {1, 2, 3}
remove_set.remove(2)
print("remove():", remove_set)

# discard(element) - Delete a single element (does NOT throw an error if the item doesn't exist)
discard_set = {1, 2, 3}
discard_set.discard(2)
print("discard():", discard_set)

# pop() - Remove and return a random element (since sets are unordered)
pop_set = {1, 2, 3}
popped_item = pop_set.pop()
print("pop():", pop_set, "(popped:", popped_item, ")")

# union() - Combine all elements from two sets (duplicates are ignored)
set_a = {1, 2, 3}
set_b = {3, 4, 5}
union_set = set_a.union(set_b)
print("union():", union_set) # -> {1, 2, 3, 4, 5}

# intersection() - Keep ONLY the elements that are in BOTH sets
set_c = {1, 2, 3}
set_d = {3, 4, 5}
intersect_set = set_c.intersection(set_d)
print("intersection():", intersect_set) # -> {3}

# difference() - Keep elements in the first set that are NOT in the second set
set_e = {1, 2, 3}
set_f = {3, 4, 5}
diff_set = set_e.difference(set_f)
print("difference():", diff_set) # -> {1, 2}

# symmetric_difference() - Keep all elements EXCEPT the ones they share
set_g = {1, 2, 3}
set_h = {3, 4, 5}
sym_diff_set = set_g.symmetric_difference(set_h)
print("symmetric_difference():", sym_diff_set) # -> {1, 2, 4, 5}