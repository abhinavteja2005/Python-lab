# Printing to the console
print("Hello, World!")  # Output: Hello, World!

# Printing multiple values
print("The sum of", 5, "and", 3, "is", 5 + 3)  # Output: The sum of 5 and 3 is 8

# Formatting output using f-strings
name = "Alice"
age = 25
print(f"{name} is {age} years old")  # Output: Alice is 25 years old

# Input from the user (always returns a string)
name = input("Enter your name: ")  # User enters: John
print("Hello, " + name)  # Output: Hello, John

# Convert input to integer or float
age = int(input("Enter your age: "))  # User enters: 30
height = float(input("Enter your height in meters: "))  # User enters: 1.75
print(f"You are {age} years old and {height} meters tall")

# Input three integers from the user
# Prompt the user to enter values
x, y, z = map(int, input("Enter the values (space-separated): ").split())

# Print the values to verify
print(f"The values entered are: x = {x}, y = {y}, z = {z}")

# Printing values on the same line

# Example 1: Using the end parameter
print("This is", end=" ")
print("on the same line.")  # Output: This is on the same line.

# Example 2: Printing variables on the same line
x, y, z = 10, 20, 30
print("Values are:", end=" ")
print(x, y, z)  # Output: Values are: 10 20 30

# Example 3: Custom separator between values
print(x, y, z, sep=", ")  # Output: 10, 20, 30
