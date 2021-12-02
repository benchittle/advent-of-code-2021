
with open("input.txt") as file:
    data = file.read().split("\n")

hor = 0
depth = 0

for line in data:
    direction, amount = line.split(" ")

    if direction == "forward":
        hor += int(amount)
    elif direction == "up":
        depth -= int(amount)
    else:
        depth += int(amount)

print(hor * depth)