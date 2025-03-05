# If-else statement
number = int(input("Enter a number: "))  # User enters: 10
if number > 0:
    print("The number is positive")
elif number == 0:
    print("The number is zero")
else:
    print("The number is negative")

# Check for even or odd
if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

# For loop
for i in range(5):  # Range generates numbers from 0 to 4
    print(f"Iteration {i}")  # Output: Iteration 0, Iteration 1, ...

# While loop
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1  # Increment count by 1

# Loop with break and continue
for i in range(1, 10):
    if i % 2 == 0:
        continue  # Skip even numbers
    if i > 7:
        break  # Stop the loop when i > 7
    print(i)  # Output: 1, 3, 5, 7

# achieving similar to do while loop
# Emulating a do-while loop (of C) in Python
while True:
    value = int(input("Enter a number (enter -1 to stop): "))
    if value == -1:  # Exit condition
        break
    print(f"You entered: {value}")
