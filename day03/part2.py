
with open("input.txt") as file:
    data = file.read().split("\n")

o2 = data[:]
co2 = data[:]

final_o2 = []
final_co2 = []

for c in range(len(data[0])):
    new_o2 = []
    new_co2 = []

    o2_col = [row[c] for row in o2]
    co2_col = [row[c] for row in co2]

    o2_ones = o2_col.count("1")
    o2_zeros = len(o2_col) - o2_ones

    co2_ones = co2_col.count("1")
    co2_zeros = len(co2_col) - co2_ones

    msb = '1' if o2_ones >= o2_zeros else '0'
    lsb = str(1 - int(msb))

    for row in o2:
        if row[c] == msb:
            new_o2.append(row)
    
    for row in co2:
        if row[c] == lsb:
            new_co2.append(row)
    
    o2 = new_o2[:]
    co2 = new_co2[:]

    if len(o2) == 1:
        final_o2 = o2[:]
    if len(co2) == 1:
        final_co2 = co2[:]

print(int("".join(final_co2), 2) * int("".join(final_o2), 2))
