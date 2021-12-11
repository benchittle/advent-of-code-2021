with open("input.txt") as file:
    heights =[list(map(int, list(line))) for line in file.read().split("\n")]

print(heights)

maxR = len(heights) - 1
maxC = len(heights[0]) - 1

risk = 0

for r in range(maxR + 1):
    for c in range(maxC + 1):
        up = heights[r - 1][c] if r > 0 else 10
        down = heights[r + 1][c] if r < maxR else 10
        left = heights[r][c - 1] if c > 0 else 10
        right = heights[r][c + 1] if c < maxC else 10

        pos = heights[r][c]
        if pos < up and pos < down and pos < left and pos < right:
            risk += pos + 1

print(risk)