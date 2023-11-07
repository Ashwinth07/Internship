n = int(input("Enter a number greater than 2: "))
li = []

# adding
for i in range(n):
    li.append(i)

print("After adding elements:", li)

# accessing
print("Element at index 0:", li[0])

# slicing
print("Slice from index 0 to 2:", li[0:2])

# modifying
li[0] = 12
print("After modifying first element:", li)

# extending
another_list = [7, 8, 9]
li.extend(another_list)
print("After extending with [7, 8, 9]:", li)

# inserting
li.insert(2, 15)
print("After inserting 15 at index 2:", li)

# removing
# 5 ways
last_element = li.pop()
print("Popped last element:", last_element)

removed_element = li.pop(1)
print("Popped element at index 1:", removed_element)

# if li.remove(4):
#     print("Removed element 4:", li)

my_list = [x for x in li if x != 3]
print("List after removing 3:", my_list)

# Finding
# index = li.index(5)
# print("Index of element 5:", index)

# Counting
count = li.count(2)
print("Count of element 2:", count)

# Sorting
li.sort()
print("Sorted list:", li)

# Reversing
li.reverse()
print("Reversed list:", li)
