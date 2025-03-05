"""
    1. Using default arguments or variable-length arguments (*args, **kwargs) for functions.
    2. Overloading operators by defining magic methods (__add__, __eq__, etc.) for custom classes.
    3. Using functools.singledispatch to overload functions based on argument types.
"""

# Default arguments
def add(a, b=0):
    return a + b

print(add(5))    # Outputs: 5
print(add(5, 3)) # Outputs: 8


# args
def add(*args):
    return sum(args)

print(add(1, 2))        # Outputs: 3
print(add(1, 2, 3, 4))  # Outputs: 10

# kwargs
def info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

info(name="Alice", age=30)  # Outputs: name: Alice age: 30

# Magic methods
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(3, 4)

p3 = p1 + p2  # This calls the __add__ method
print(p3)      # Outputs: Point(4, 6)

"""
Few more magic methods
    1. __sub__(self, other) for - (subtraction)
    2. __mul__(self, other) for * (multiplication)
    3. __truediv__(self, other) for / (division)
    4. __eq__(self, other) for == (equality)
    5. __lt__(self, other) for < (less than)
    6. __len__(self) for len() (length of an object)
"""

# singledispatch
from functools import singledispatch

@singledispatch
def print_type(arg):
    print("Unknown type")

@print_type.register(int)
def _(arg):
    print(f"Integer: {arg}")

@print_type.register(str)
def _(arg):
    print(f"String: {arg}")

print_type(10)    # Outputs: Integer: 10
print_type("Hi")  # Outputs: String: Hi
print_type([1, 2, 3])  # Outputs: Unknown type
