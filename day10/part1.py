from collections import deque

with open("input.txt") as file:
    data = file.read().split("\n")

counts = {")" : 0, "]" : 0, "}" : 0, ">" : 0}
pairs = {"}" : "{", "]" : "[", ")" : "(", ">" : "<"}

for line in data:
    stack = deque()
    for c in line:
        if c in pairs.values():
            stack.appendleft(c)
        elif pairs[c] != stack.popleft():
            counts[c] += 1
            break

print(counts[")"] * 3 + counts["]"] * 57 + counts["}"] * 1197 + counts[">"] * 25137)
