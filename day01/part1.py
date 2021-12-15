with open("input.txt") as file:
    data = list(map(int, file.read().split("\n")[:-1]))

print(sum([1 for i, j in zip(data[:-1], data[1:]) if j > i]))