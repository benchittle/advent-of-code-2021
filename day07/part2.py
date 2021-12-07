
with open("input.txt") as file:
    positions = list(map(int, file.read().split(",")))

minX = min(positions)
maxX = max(positions)

# Initialize minTotal to the fuel required to move to minX
# (can't use 0 because then there's nothing smaller!)
minTotal = 0
for p in positions:
    steps = abs(p - minX)
    minTotal += steps * (steps + 1) // 2

total = 0
for i in range(minX + 1, maxX + 1):
    lastTotal = total
    total = 0
    for p in positions:
        steps = abs(p - i)
        total += (steps * (steps + 1)) // 2

    if total < minTotal:
        minTotal = total


print(minTotal)
