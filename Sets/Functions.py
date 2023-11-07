n1=int(input("Enter no the set1 Elements"))
set1=set()
set2=set()
for i in range(n1):
    set1.add(int(input()))
print("Original Set 1:", set1)
n2=int(input("Enter no the set1 Elements"))
for i in range(n2):
    set2.add(int(input()))
print("Original Set 2:", set2)
# Adding 
set1.add(6)
set2.add(9)

# Removing
set1.remove(3)
set2.discard(7)

# Union
union_set = set1.union(set2)

# Intersection
intersection_set = set1.intersection(set2)

# Difference
difference_set = set1.difference(set2)

# Symmetric difference
symmetric_difference_set = set1.symmetric_difference(set2)

# Checking Disjoint Sets
disjoint = set1.isdisjoint(set2)

# Checking Subsets and Supersets
subset = set1.issubset(set2)
superset = set1.issuperset(set2)

# CheckingEquality
equal = set1 == set2

# Removing Common Elements (in-place)
set1.intersection_update(set2)

# Adding Elements from Another Set (in-place)
set1.update(set2)

# Discarding Elements Not in Another Set (in-place)
set1.difference_update(set2)

# Removing Duplicate Elements
my_list = [1, 2, 3, 2, 1, 4, 5, 4]
unique_set = set(my_list)


# Displaying results
print("Original Set 1:", set1)
print("Original Set 2:", set2)
print("Union of Sets:", union_set)
print("Intersection of Sets:", intersection_set)
print("Difference of Sets:", difference_set)
print("Symmetric Difference of Sets:", symmetric_difference_set)
print("Are the sets disjoint?", disjoint)
print("Is Set 1 a subset of Set 2?", subset)
print("Is Set 1 a superset of Set 2?", superset)
print("Are Set 1 and Set 2 equal?", equal)
print("Set 1 after intersection update with Set 2:", set1)
print("Unique elements from the list:", unique_set)
