# Lambda Functions in Python
# Lambda functions are small, anonymous (nameless) functions defined with the `lambda` keyword.
# Syntax: lambda arguments: expression
# They're used for quick operations where a full function definition is unnecessary.

# Example of a regular function vs a lambda function:

# Regular function to compute square
def square_function(x):
    return x ** 2

# Lambda equivalent
square_lambda = lambda x: x ** 2

# Both give the same result
print("Square using regular function:", square_function(5))  # Output: 25
print("Square using lambda function:", square_lambda(5))    # Output: 25

# Lambda functions are commonly used with built-in functions like sort, filter, map, and reduce.

# -----------------------------------------------------------------------------------------

# **Sorting with and without Lambda**
# Sort a list of tuples by the second element

# Without lambda function (using a regular function)
def sort_by_second(tuple):
    return tuple[1]

pairs = [(1, 'b'), (3, 'a'), (2, 'c')]
pairs.sort(key=sort_by_second)  # Using the regular function
print("Sorted by second element (regular function):", pairs)

# With lambda function
pairs = [(1, 'b'), (3, 'a'), (2, 'c')]  # Reset list
pairs.sort(key=lambda x: x[1])  # Inline function for sorting
print("Sorted by second element (lambda):", pairs)

# -----------------------------------------------------------------------------------------

# **Filter with and without Lambda**
# Filter out even numbers from a list

nums = [1, 2, 3, 4, 5, 6]

# Without lambda function (using a regular function)
def is_even(num):
    return num % 2 == 0

evens = list(filter(is_even, nums))
print("Even numbers (regular function):", evens)  # Output: [2, 4, 6]

# With lambda function
evens = list(filter(lambda x: x % 2 == 0, nums))
print("Even numbers (lambda):", evens)  # Output: [2, 4, 6]

# -----------------------------------------------------------------------------------------

# **Map with and without Lambda**
# Double each number in a list

# Without lambda function (using a regular function)
def double(num):
    return num * 2

doubles = list(map(double, nums))
print("Doubled numbers (regular function):", doubles)  # Output: [2, 4, 6, 8, 10, 12]

# With lambda function
doubles = list(map(lambda x: x * 2, nums))
print("Doubled numbers (lambda):", doubles)  # Output: [2, 4, 6, 8, 10, 12]

# -----------------------------------------------------------------------------------------

# **Reduce with and without Lambda**
# Sum up all numbers in a list

from functools import reduce

# Without lambda function (using a regular function)
def add(x, y):
    return x + y

sum_result = reduce(add, nums)
print("Sum of numbers (regular function):", sum_result)  # Output: 21

# With lambda function
sum_result = reduce(lambda x, y: x + y, nums)
print("Sum of numbers (lambda):", sum_result)  # Output: 21

# -----------------------------------------------------------------------------------------

# Summary:
# - **sort()**: Used for sorting a collection. The `key` parameter can take a function to specify custom sorting.
# - **filter()**: Filters elements based on a condition. Returns an iterator.
# - **map()**: Transforms each element in a collection using a function.
# - **reduce()**: Applies a function cumulatively to elements in a collection to reduce it to a single value.

# Lambda functions make code more concise when used with these operations, 
# but for more complex logic, regular functions are preferred for readability.
