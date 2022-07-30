import random

name = input("Please enter all of your names separated by a comma\n")
names = name.split(",")
rand_guy = random.randint(0, len(names)-1)
print(f"{names[rand_guy]} is going to buy the meal today!")