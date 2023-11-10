
my_dict = {}

# Adding elements
n = int(input("Enter no of key-value pairs to add: "))
for i in range(n):
    key = input(f"Enter key {i+1}: ")
    value = input(f"Enter value for {key}: ")
    my_dict[key] = value

# Accessing elements
access_key = input("Enter a key to access: ")
if access_key in my_dict:
    accessed_value = my_dict[access_key]
else:
    accessed_value = None

# Removing elements 
remove_key = input("Enter a key to remove: ")
if remove_key in my_dict:
    removed_value = my_dict.pop(remove_key)
else:
    removed_value = None

# Getting all keys, values
keys = my_dict.keys()
values = my_dict.values()

# Checking for key existence
check_key = input("Enter a key to check for existence: ")
key_exists = check_key in my_dict

# Creating second dictionary
another_dict = {}
m = int(input("Enter the number of key-value pairs for the second dictionary: "))
for i in range(m):
    key = input(f"Enter key {i+1} for the second dictionary: ")
    value = input(f"Enter value for {key} in the second dictionary: ")
    another_dict[key] = value

# Merging dictionaries
merged_dict = {**my_dict, **another_dict}

# Updating the original dictionary with second dictionary
my_dict.update(another_dict)

# Removing a key-value pair and getting the value
remove_key = input("Enter a key to remove and get the value: ")
removed_value = my_dict.pop(remove_key, None)

# Creating a shallow copy of the dictionary
new_dict = my_dict.copy()

# Clearing the entire dictionary
my_dict.clear()

# Displaying results
print("Original Dictionary:", my_dict)
print("Accessed Value:", accessed_value)
print("Removed Value:", removed_value)
print("Keys:", keys)
print("Values:", values)
print("Does the key exist?", key_exists)
print("Merged Dictionary:", merged_dict)
print("Updated Dictionary:", new_dict)
