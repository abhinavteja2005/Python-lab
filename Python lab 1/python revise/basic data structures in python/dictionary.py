# Creating a dictionary
my_dict = {"name": "Alice", "age": 25, "city": "New York"}

# Accessing values using keys
print("Name:", my_dict["name"])  # Output: Alice
print("Age:", my_dict["age"])    # Output: 25

# Modifying values
my_dict["age"] = 26
print("Updated age:", my_dict["age"])  # Output: 26

# Adding new key-value pairs
my_dict["profession"] = "Engineer"
print("Updated dictionary:", my_dict)
# Output: {'name': 'Alice', 'age': 26, 'city': 'New York', 'profession': 'Engineer'}

# Removing a key-value pair
del my_dict["city"]
print("After deletion:", my_dict)
# Output: {'name': 'Alice', 'age': 26, 'profession': 'Engineer'}

# Using the get() method (safe way to access values)
print("City:", my_dict.get("city", "Not Found"))  # Output: Not Found

# Checking if a key exists
if "age" in my_dict:
    print("Age exists:", my_dict["age"])  # Output: 26
else:
    print("Age not found")

# Iterating through a dictionary
for key, value in my_dict.items():
    print(f"{key}: {value}")
# Output:
# name: Alice
# age: 26
# profession: Engineer

# Nested dictionaries
nested_dict = {"person": {"name": "Bob", "age": 50}, "city": "London"}
print("Nested Dictionary:", nested_dict)
print("Nested person's name:", nested_dict["person"]["name"])  # Output: Bob
