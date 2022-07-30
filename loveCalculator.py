your_name = input("what is your name?\n")
their_name = input("what is their name?\n")

combined_name = your_name + their_name

lower_case_str = combined_name.lower()

t = lower_case_str.count("t")
r = lower_case_str.count("r")
u = lower_case_str.count("u")
e = lower_case_str.count("e")

true = t + r + u + e

l = lower_case_str.count("l")
o = lower_case_str.count("o")
v = lower_case_str.count("v")
e = lower_case_str.count("e")

love = l + o + v + e

num = str(true) + str(love)

print(num)