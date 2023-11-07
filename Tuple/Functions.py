n=int(input())
my_tuple=()
for i in range(n):
    my_tuple += (int(input()),)

# Accessing 
print("Element at index 0:", my_tuple[0])

# Slicing
print("Slice from index 0 to 2:", my_tuple[0:3])

# Concatenating
another_tuple = (6, 7, 8)
concatenated_tuple = my_tuple + another_tuple

# length
length = len(my_tuple)

# Counting occurrences
count_of_3 = my_tuple.count(3)

# Finding index
index_of_4 = my_tuple.index(4)

# Creating new tuple with modified elements
modified_tuple = tuple(x*2 for x in my_tuple)

# Displaying results
print("Original Tuple:", my_tuple)
print("Concatenated Tuple:", concatenated_tuple)
print("Length of Tuple:", length)
print("Count of '3' in Tuple:", count_of_3)
print("Index of '4' in Tuple:", index_of_4)
print("Modified Tuple:", modified_tuple)

#For Updating and Changing the values
my_tuple = (1, 2, 3, 4, 5)

# Removing elements (creating a new tuple)
element_to_remove = 3
new_tuple = tuple(x for x in my_tuple if x != element_to_remove)

# Updating elements (creating a new tuple)
element_to_update = 4
new_value = 10
updated_tuple = tuple(new_value if x == element_to_update else x for x in my_tuple)

# Displaying results
print("Original Tuple:", my_tuple)
print("Tuple after removing element", element_to_remove, ":", new_tuple)
print("Tuple after updating element", element_to_update, ":", updated_tuple)

