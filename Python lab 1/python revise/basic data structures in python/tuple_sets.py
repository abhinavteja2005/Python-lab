# Tuples: Immutable, ordered collections in Python.
# Used when data shouldn't change, like coordinates or constants.

# Creating a tuple
my_tuple = (1, 2, 3, 2, 2)

# 1. count() - Count occurrences of a value
count_of_2 = my_tuple.count(2)  # Count occurrences of 2
print("Count of 2:", count_of_2)  # Output: 3

# 2. index() - Find the first index of a value
index_of_3 = my_tuple.index(3)  # Find the first occurrence of 3
print("Index of 3:", index_of_3)  # Output: 2

# Operations on Tuples
# 3. Concatenation
t1 = (1, 2)
t2 = (3, 4)
concatenated = t1 + t2  # Combine two tuples
print("Concatenated Tuple:", concatenated)  # Output: (1, 2, 3, 4)

# 4. Repetition
repeated = t1 * 3  # Repeat the tuple
print("Repeated Tuple:", repeated)  # Output: (1, 2, 1, 2, 1, 2)

# 5. Slicing
sliced = my_tuple[1:4]  # Extract a portion of the tuple
print("Sliced Tuple:", sliced)  # Output: (2, 3, 2)

# 6. Membership Testing
print("Is 2 in tuple?", 2 in my_tuple)  # Output: True
print("Is 5 not in tuple?", 5 not in my_tuple)  # Output: True

# Sets: Unordered collections of unique elements in Python.
# Used for fast membership tests and removing duplicates.

# Creating a set
my_set = {1, 2, 3, 4}

# 1. add() - Add an element to the set
my_set.add(5)
print("After adding 5:", my_set)  # Output: {1, 2, 3, 4, 5}

# 2. remove() - Remove an element (throws error if not present)
my_set.remove(3)
print("After removing 3:", my_set)  # Output: {1, 2, 4, 5}

# 3. discard() - Remove an element (no error if not present)
my_set.discard(10)  # Does nothing as 10 is not in the set
print("After discarding 10:", my_set)  # Output: {1, 2, 4, 5}

# 4. pop() - Remove and return an arbitrary element
popped_element = my_set.pop()
print("Popped element:", popped_element)
print("After pop:", my_set)

# 5. union() - Combine two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print("Union:", union_set)  # Output: {1, 2, 3, 4, 5}

# 6. intersection() - Elements common to both sets
intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)  # Output: {3}

# 7. difference() - Elements in set1 but not in set2
difference_set = set1.difference(set2)
print("Difference:", difference_set)  # Output: {1, 2}

# 8. symmetric_difference() - Elements in either set but not both
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric Difference:", symmetric_difference_set)  # Output: {1, 2, 4, 5}

# 9. Membership Testing
print("Is 4 in set1?", 4 in set1)  # Output: False
print("Is 2 in set1?", 2 in set1)  # Output: True
