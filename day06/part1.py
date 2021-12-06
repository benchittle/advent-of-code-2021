
with open("sample.txt") as file:
    cycles = list(map(int, file.read().split(",")))

#cycles = [6]
length = len(cycles)
for d in range(80):
    for i in range(length):
        cycles[i] -= 1
        if cycles[i] == -1:
            cycles[i] = 6
            cycles.append(8)
    length = len(cycles)

print(len(cycles))
    