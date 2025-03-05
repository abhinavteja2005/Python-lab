import random

low = 1
high = 100
number = random.randint(low, high) # lower limit is set as low and higher limit
print(number)

# to print random double between 0 and 1
num = random.random()
print(num)

# to choose a random item from a list
options = ["rock", "paper", "scissors"]
option = random.choice(options)
print(option)

# to rearrange the items in a list
cards = ['A', 'K', 'Q', 'J','2', '3', '4', '5', '6', '7', '8', '9', '10']
random.shuffle(cards)
print(cards)