from collections import deque


def search(r, c, hMap):
    visited = {(r, c)}
    q = deque([(r, c)])
    maxR = len(hMap) - 1
    maxC = len(hMap[0]) - 1

    while q:
        r, c = q.popleft()
        for adjR, adjC in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= adjR <= maxR and 0 <= adjC <= maxC:
                    if hMap[adjR][adjC] < 9 and (adjR, adjC) not in visited:
                        visited.add((adjR, adjC))
                        q.append((adjR, adjC))

    return len(visited)


with open("input.txt") as file:
    heights =[list(map(int, list(line))) for line in file.read().split("\n")]

maxR = len(heights) - 1
maxC = len(heights[0]) - 1

risk = 0

lowPoints = []
for r in range(maxR + 1):
    for c in range(maxC + 1):
        up = heights[r - 1][c] if r > 0 else 10
        down = heights[r + 1][c] if r < maxR else 10
        left = heights[r][c - 1] if c > 0 else 10
        right = heights[r][c + 1] if c < maxC else 10

        pos = heights[r][c]
        if pos < up and pos < down and pos < left and pos < right:
            lowPoints.append((r, c))


sizes = []
for r, c in lowPoints:
    sizes.append(search(r, c, heights))

sizes = sorted(sizes, reverse=True)

print(sizes[0] * sizes[1] * sizes[2])
# %%
