# --- Problem 1: Remove duplicates (Using set) ---
l_1 = [1, 1, 2, 3, 3, 4]

# Converting to a set automatically removes duplicates, 
# then we convert it back to a list.
unique_list_1 = list(set(l_1))
print("Problem 1 (Using set):", unique_list_1)


# --- Problem 2: Remove duplicates without set() (Preserve order) ---
l_2 = [1, 1, 2, 3, 3, 4]
unique_list_2 = []

# Loop through original list and only add items if they aren't already in the new list
for item in l_2:
    if item not in unique_list_2:
        unique_list_2.append(item)

print("Problem 2 (Without set, ordered):", unique_list_2)


# --- Problem 3: Find common elements (Using intersection) ---
l1 = [13, 27, 30, 42, 57]
l2 = [13, 57, 89, 33, 80]

# Convert both lists to sets, find the intersection, and convert back to a list
common_elements = list(set(l1).intersection(set(l2)))

print("Problem 3 (Common elements):", common_elements)