# Function definition
def greet(name):
    """Function to greet a user"""
    print(f"Hello, {name}!")

# Calling the function
greet("Alice")  # Output: Hello, Alice!

# Function with return value
def add(x, y):
    """Function to add two numbers and return the result"""
    return x + y

result = add(5, 3)
print("Sum:", result)  # Output: Sum: 8

#default arguments

def net_price(list_price, discount = 0, tax = 0.05):
    return list_price * (1 - discount/100) * (1 + tax)

price = 500
dis = 25
print(net_price(price, dis))
# here discount and tax are set as default, i.e they can be either included in the function call or not, if not included their 
# default value will be used for computing it and always default arguments should be at the end
# you can't define a function as net_price(discount = 0, list_price, tax = 0.05)

# keyword arguments
# an argument preceded by an identifier helps with readability and order of arguments doesn't matter
# but always positional arguments should preceed keyword arguments

def hello(greeting, first, last, title = "Noob"):
    print(f"{greeting} {title} {first} {last}")

hello("Good morning", last = "teja", title = "The Great", first = "Abhinav")

#arbitary arguments
# *args : allows you to pass multiple non key arguments,  a tuple named args is created which stores these values
# * is the unpacking operator

def add(*nums):
    total = 0
    for num in nums:
        total += num
    return total

print(add(1, 2, 3, 4, 5))

# **kwargs : allows you to pass multiple keyword-arguments

def print_address(**kwargs):
    #a dictionary is created which has variables as keys
    for key in kwargs.keys():
        print(key)

    for value in kwargs.values():
        print(value)
    
    for key, value in kwargs.items():
        print(f"{key} : {value}")

print_address(street = "123 street", city = "Detroit", state = "MI", zip = "54321")

"""
The order is as follows:
    1. Positional arguments (non-default arguments).
    2. Default arguments (keyword arguments with default values).
    3. *args (variable-length positional arguments).
    4. **kwargs (variable-length keyword arguments).
"""

def example(pos1, pos2, default1=10, default2=20, *args, **kwargs):
    print(pos1, pos2, default1, default2, args, kwargs)

example(1, 2, 30, 40, 50, 60, key1="value1", key2="value2")