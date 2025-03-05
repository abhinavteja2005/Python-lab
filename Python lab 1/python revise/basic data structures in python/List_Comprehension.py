"""
    List Comprehension= A concise way to create lists in Python 
                        Compact and easier to read than tradiotional loops
                        [expression for value in iterable if condition]
"""

# list = [exression for value in iterable if condition]
doubles = [x * 2 for x in range(1, 11)]
print(doubles)

numbers = [1, -2, 3, -4, 5, -6, 8, -7]
positive_numbers = [x for x in numbers if x >= 0]
negative_numbers = [x for x in numbers if x < 0]
even_numbers = [x for x in numbers if x % 2 == 0]
odd_numbers = [x for x in numbers if x % 2 == 1]

print(f"odd_numbers : {odd_numbers}")
print(f"even_numbers : {even_numbers}")
print(f"positive_numbers : {positive_numbers}")
print(f"negative_numbers : {negative_numbers}")
