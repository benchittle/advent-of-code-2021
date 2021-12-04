
with open("sample.txt") as file:
    data = file.read().split("\n")

gamma = []

for c in range(len(data[0])):
    col = []
    for row in data:
        col.append(row[c])

    ones = col.count("1")
    zeros = len(col) - ones
    if zeros > ones:
        gamma.append('0')
    else:
        gamma.append('1')


epsilon = ['1' if i == '0' else '0' for i in gamma]

print(gamma)
print(epsilon)

g = int("".join(gamma), 2)
e = int("".join(epsilon), 2)

print(g * e)







