factorial_number  = int(input("Please Enter an Integer to Calculate its Factorial\n"))
res = 1
i = 0
while factorial_number > 1:
    res *= factorial_number
    factorial_number -= 1

print(res)