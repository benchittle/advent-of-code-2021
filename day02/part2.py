with open("input.txt") as file:
    data = file.read().split("\n")

aim = 0
hor = 0
depth = 0

for line in data:
    direction, amount = line.split(" ")

    if direction == "forward":
        hor += int(amount)
        depth -= int(amount) * aim
    elif direction == "up":
        aim += int(amount)
    else:
        aim -= int(amount)

print(hor * direction)

