from collections import Counter

def rasterizeHorizontal(line):
    points = []
    y = line[0][1]
    x1, x2 = line[0][0], line[1][0]
    xMin, xMax = (x1, x2) if x1 < x2 else (x2, x1)
    for x in range(xMin, xMax + 1):
        points.append((x, y))

    return points

def rasterizeVertical(line):
    points = []
    x = line[0][0]
    y1, y2 = line[0][1], line[1][1]
    yMin, yMax = (y1, y2) if y1 < y2 else (y2, y1)
    for y in range(yMin, yMax + 1):
        points.append((x, y))

    return points

def rasterizeDiagonal(line):
    points = []
    x1, x2 = line[0][0], line[1][0]
    xMin = x1 if x1 < x2 else x2
    y1, y2 = line[0][1], line[1][1]
    yMin = y1 if y1 < y2 else y2

    for p in zip(range(x1, x2, 1 if xMin == x1 else -1), range(y1, y2, 1 if yMin == y1 else -1)):
        points.append(p)
    points.append((x2, y2))
    return points


with open("input.txt") as file:
    lines = [[[int(n) for n in pair.split(",")] for pair in s.split(" -> ")] for s in file.read().split("\n")]

vertical = [line for line in lines if line[0][0] == line[1][0]]
horizontal = [line for line in lines if line[0][1] == line[1][1]]

diagonals = [line for line in lines if line[0][0] != line[1][0] and line[0][1] != line[1][1]]

points = []
for line in vertical:
    points += rasterizeVertical(line)

for line in horizontal:
    points += rasterizeHorizontal(line)

for line in diagonals:
    points += rasterizeDiagonal(line)

total = 0
pointCounts = Counter(points)
for coord, count in pointCounts.items():
    if count >= 2:
        total += 1

print(total)

