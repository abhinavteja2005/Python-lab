"""
    Membership operators: used to test whether a value or variable is found in a sequence
    (string, list, tuple, set, or dictionary)
    1. in
    2. not in
"""

word = "APPLE"

letter = input("Guess a letter in the secret word: ")

if letter not in word:
    print(f"{letter} was not found")
else:
    print(f"{letter} was found")

grades = {"Sandy" : "A", "Squidward" : "B", "Spongebob" : "C", "Patrick" : "D"}
student = input("Enter the name: ")

if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"grades of {student} is not found")

# to check whether a gmail is valid or not(simple one)

gmail = "dasariabhinavteja@gmail.cm"

if "gmail.com" in gmail:
    print("Correct")
else:
    print("Not Correct")