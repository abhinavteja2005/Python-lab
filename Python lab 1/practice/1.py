# practice problem from tutorial (line 39)

"""
a.  Write a program which will take the following lists and set to create a larger list, which should
    include all the elements in the lists list1 and list2 and set set3.
    Also, find the union, intersection and difference of the sets obtained from the list list1 and
    list2. Print all the sets you have obtained.
    list1 = [1, 2, 3, 4]
    list2 = [1, 4, 2, 3, 5]
    set3 = {'a', 'b', 'c'}
"""

list1 = [1,2,3,4]
list2 = [1, 4, 2, 3, 5]
set3 = {'a', 'b', 'c'}

list4 = list1 + list2 + list(set3)

print(list4)
set1 = set(list1)
set2 = set(list2)
set4 = set1 | set2
set5 = set1 & set2
set6 = set2 - set1


print(set1)
print(set2)
print(set3)
print(set4)
print(set5)
print(set6)

"""
b.  The following is a program which shows how to create a set given a list and can be updated.

    # Python program to demonstrate the use of update() method
    list1 = [1, 2, 3]
    list2 = [5, 6, 7]
    list3 = [10, 11, 12]
    # Lists converted to sets
    set1 = set(list2)
    set2 = set(list1)
    # Update method
    set1.update(set2)
    # Print the updated set
    print(set1)
    # List is passed as an parameter which gets automatically
    converted to a set
    set1.update(list3)
    print(set1)

    Consider another list, say list4 = [1, 3, 5, 7, 9, 11, 13] and update the list list3 with the elements
    from the list list4.    
"""

# Python program to demonstrate the use of update() method
list1 = [1, 2, 3]
list2 = [5, 6, 7]
list3 = [10, 11, 12]
list4 = [1, 3, 5, 7, 9, 11, 13]

# Lists converted to sets
set1 = set(list2)
set2 = set(list1)
set3 = set(list3)
set4 = set(list4)

# Update method: updating set3 with elements from set4
set3.update(set4)

# Print the updated set3 (which represents list3)
print(set3)

"""
c.  Given a set and a dictionary as below. Write a program which will include all the elements from
    the dictionary to set.
    Set1 = {1, 2, 3, 4, 5}
    myDict = {6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten'}
    Hint: Set1.update(myDict)
"""

Set1 = {1, 2, 3, 4, 5}
myDict = {6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten'}
Set1.update(myDict)
print(Set1)

"""
d.  The following program create a dictionary and then updating elemnets/ key values in it. Run
    the program and do the following tasks.

    # Creating an empty Dictionary
    Dict = {}
    # Adding elements one at a time
    Dict[0] = 'Apple'
    Dict[1] = 'Banana'
    Dict[2] = 'Mango'
    print("\nDictionary after adding 3 elements: ", Dict)
    # Adding set of values to a single Key
    Dict[3] = 'Orange', 'Cherry', 'Guava'
    print("\nDictionary after adding 3 elements: ")
    print(Dict)
    # Updating existing Key's Value
    Dict[2] = 'Water Mellon'
    print("\nUpdated key value: ")
    print(Dict)
"""

 # Creating an empty Dictionary
Dict = {}
# Adding elements one at a time
Dict[0] = 'Apple'
Dict[1] = 'Banana'
Dict[2] = 'Mango'
print("\nDictionary after adding 3 elements: ", Dict)
# Adding set of values to a single Key
Dict[3] = 'Orange', 'Cherry', 'Guava' # stored as a tuple
print("\nDictionary after adding 3 elements: ")
print(Dict)
# Updating existing Key's Value
Dict[2] = 'Water Mellon'
print("\nUpdated key value: ")
print(Dict)

""" to check how the values are stored
print(type(Dict[3]))

for value in Dict.values():
    print(type(value))
"""
Dict[4] = 'Pineapple'
print(Dict)
Dict.pop(1)
print(Dict)
Dict.pop(3)
print(Dict)