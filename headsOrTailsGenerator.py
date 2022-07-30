import random
randInt = random.randint(1,10)
heads = False
tails = False
if randInt % 2 == 0:
    heads = True
else:
    tails = True

getInput = input("Please Type Heads or Tails\n")

getInput = getInput.lower()

if getInput == "heads":
    if heads == True:
        print("It is Heads, You Won!")
    else:
        print("Tails, You Lost!")
elif getInput == "tails":
    if tails == True:
        print("It is Tails, You Won!")
    else:
        print("Heads, You Lost!")
else:
    print("Please Enter Heads or Tails")