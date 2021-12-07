
with open("input.txt") as file:
    positions = list(map(int, file.read().split(",")))

minX = min(positions)
maxX = max(positions)

minTotal = sum(positions)
for i in range(minX, maxX + 1):
    total = 0
    for p in positions:
        total += abs(p - i)

    if total < minTotal:
        minTotal = total

print(minTotal)