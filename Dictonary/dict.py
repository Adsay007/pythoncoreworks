# dict() - Create a dictionary using keyword arguments
new_dict = dict(name="arun", age=23)
print("dict():", new_dict)

# len() - Get the number of key-value pairs in the dictionary
len_dict = {'name': 'arun', 'age': 23}
dict_length = len(len_dict)
print("len():", dict_length)

# keys() - Get a list-like view of all the keys
keys_dict = {'name': 'arun', 'age': 23}
all_keys = keys_dict.keys()
print("keys():", all_keys)

# values() - Get a list-like view of all the values
values_dict = {'name': 'arun', 'age': 23}
all_values = values_dict.values()
print("values():", all_values)

# items() - Get a list-like view of all key-value pairs as tuples
items_dict = {'name': 'arun', 'age': 23}
all_items = items_dict.items()
print("items():", all_items)

# get(keyname) - Safely get the value for a key (returns None if key doesn't exist)
get_dict = {'name': 'arun', 'age': 23}
name_value = get_dict.get('name')
print("get():", name_value)

# pop(keyname) - Remove a specific key and return its value
pop_dict = {'name': 'arun', 'age': 23, 'city': 'Trivandrum'}
removed_age = pop_dict.pop('age')
print("pop():", pop_dict, "(popped value:", removed_age, ")")

# popitem() - Remove and return the last inserted key-value pair as a tuple
popitem_dict = {'name': 'arun', 'age': 23}
removed_item = popitem_dict.popitem()
print("popitem():", popitem_dict, "(popped item:", removed_item, ")")

# update(dictionary) - Add new key-value pairs or update existing ones
update_dict = {'name': 'arun', 'age': 23}
update_dict.update({'city': 'Trivandrum', 'age': 24})
print("update():", update_dict)

# copy() - Make a duplicate of the dictionary
original_dict = {'name': 'arun', 'age': 23}
copied_dict = original_dict.copy()
print("copy():", copied_dict)

# clear() - Empty the entire dictionary
clear_dict = {'name': 'arun', 'age': 23}
clear_dict.clear()
print("clear():", clear_dict)