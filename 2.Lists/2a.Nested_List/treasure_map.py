row1 = ["o", "o", "o"]
row2 = ["o", "o", "o"]
row3 = ["o", "o", "o"]

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? (eg:13) ")

horizontal = int(position[0])
vertical = int(position[1])
map[horizontal-1][vertical-1] = "X"

print(f"{row1}\n{row2}\n{row3}")
