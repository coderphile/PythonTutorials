row1 = ['💀', '💀', '💀']
row2 = ['💀', '💀', '💀']
row3 = ['💀', '💀', '💀']

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}\n")

value = input("Where do you want to place the treasure?\n")
horizontal = int(value[0])-1
vertical = int(value[1])-1

map[vertical][horizontal] = "X"
print(f"{row1}\n{row2}\n{row3}\n")
