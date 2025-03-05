# Python Lists and Basic Operations

# Creating a list
my_list = [10, 20, 30, 40, 50]  # Initialize with elements
print("Initial list:", my_list)  # Output: [10, 20, 30, 40, 50]

# Accessing elements by index (0-based)
print("First element:", my_list[0])  # Output: 10
print("Last element:", my_list[-1])  # Output: 50

# Modifying elements
my_list[1] = 25  # Change the second element
print("After modification:", my_list)  # Output: [10, 25, 30, 40, 50]

# Adding elements
my_list.append(60)  # Add to the end
print("After appending:", my_list)  # Output: [10, 25, 30, 40, 50, 60]

# Inserting at a specific position
my_list.insert(2, 15)  # Insert 15 at index 2
print("After inserting:", my_list)  # Output: [10, 25, 15, 30, 40, 50, 60]

# Removing elements
my_list.remove(30)  # Remove the first occurrence of 30
print("After removing 30:", my_list)  # Output: [10, 25, 15, 40, 50, 60]

# Deleting by index
del my_list[2]  # Remove the element at index 2
print("After deleting index 2:", my_list)  # Output: [10, 25, 40, 50, 60]

# Slicing (sub-lists)
sub_list = my_list[1:4]  # Get elements from index 1 to 3 (exclusive)
print("Sub-list:", sub_list)  # Output: [25, 40, 50]

# Checking existence
print(40 in my_list)  # Output: True
print(100 in my_list)  # Output: False

# Length of the list
print("Length of list:", len(my_list))  # Output: 5

# Iterating over a list
for value in my_list:
    print("Value:", value)

# Extending lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)  # Append all elements of list2 to list1
print("After extending:", list1)  # Output: [1, 2, 3, 4, 5, 6]

# Sorting a list
unsorted_list = [5, 2, 9, 1, 7]
unsorted_list.sort()  # Sorts in ascending order
print("Sorted list:", unsorted_list)  # Output: [1, 2, 5, 7, 9]

# Reversing a list
unsorted_list.reverse()  # Reverses the order of elements
print("Reversed list:", unsorted_list)  # Output: [9, 7, 5, 2, 1]

# Copying a list
copied_list = my_list.copy()
print("Copied list:", copied_list)  # Output: [10, 25, 40, 50, 60]

# Clearing all elements
my_list.clear()
print("After clearing:", my_list)  # Output: []
