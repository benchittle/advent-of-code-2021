with open("input.txt") as file:
    data = file.read().split("\n")

count = 0
for line in data:
    line = line.split(" | ")
    digits = list(map(set, line[0].split(" ")))
    outputs = list(map(set, line[1].split(" ")))

    mapping = {i:None for i in range(10)}

    for d in digits:
        if len(d) == 2:
            mapping[1] = d
        elif len(d) == 3:
            mapping[7] = d
        elif len(d) == 7:
            mapping[8] = d
        elif len(d) == 4:
            mapping[4] = d

    for i in outputs:
        count += (i in [mapping[1], mapping[4], mapping[7], mapping[8]])

print(count)
    


