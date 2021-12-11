from collections import deque

with open("input.txt") as file:
    data = file.read().split("\n")

scores = {"(" : 1, "[" : 2, "{" : 3, "<" : 4}
pairs = {"}" : "{", "]" : "[", ")" : "(", ">" : "<"}

totals = []
for i, line in enumerate(data):
    stack = deque()
    for c in line:
        if c in pairs.values():
            stack.appendleft(c)
        elif pairs[c] != stack.popleft():
            break
    else:
        total = 0
        while stack:
            total = 5 * total + scores[stack.popleft()]
        totals.append(total)

print(sorted(totals)[len(totals) // 2])