# Define the two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Method 1: Using the extend() method
list1.extend(list2)

# Method 2: Using the append() method in a loop
for item in list2:
    list1.append(item)

# Method 3: Using the list() and map() functions
list1 = list(map(lambda x: x, list1)) + list(map(lambda x: x, list2))

# Print the concatenated list
print(list1)
