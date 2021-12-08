with open("input.txt") as file:
    data = file.read().split("\n")

total = 0
for line in data:
    line = line.split(" | ")
    digitStrings = list(map(set, line[0].split(" "))) # Strings to the left of |
    outputStrings = list(map(set, line[1].split(" "))) # String to the right of |

    # Numbers 0-9 as keys mapped to their
    mapping = {i:None for i in range(10)}

    for s in digitStrings:
        if len(s) == 2:
            mapping[1] = s
        elif len(s) == 3:
            mapping[7] = s
        elif len(s) == 7:
            mapping[8] = s
        elif len(s) == 4:
            mapping[4] = s

    # Take away the letters common to the strings for 7 and 1 to get the
    # character corresponding to 'a' in the default 7-seg display
    a = mapping[7].difference(mapping[1]).pop()
    
    b = ""
    c = ""
    e = ""
    f = ""
    # Since b is the only character to appear 6 times in the (default) 
    # digitStrings, we can determine which character corresponds to b. Similar 
    # applies for the characters c, e, and f.
    for letter in "abcdefg":
        count = 0
        for s in digitStrings:
            if letter in s:
                count += 1

        if count == 6:
            b = letter
        elif count == 8 and letter != a:
            c = letter
        elif count == 4:
            e = letter
        elif count == 9:
            f = letter

    # Removing now known characters from some known strings yields the 
    # remaining characters, d and g
    d = mapping[4].difference(set(b + c + f)).pop()
    g = mapping[8].difference(set(a + b + c + d + e + f)).pop()

    # Build the remaining mappings
    mapping[0] = set(a + b + c + e + f + g)
    mapping[2] = set(a + c + d + e + g)
    mapping[3] = set(a + c + d + f + g)
    mapping[5] = set(a + b + d + f + g)
    mapping[6] = set(a + b + d + e + f + g)
    mapping[9] = set(a + b + c + d + f + g)

    # Build the value of the output number in num using the known mappings
    num = 0
    for i in outputStrings:
        for k, v in mapping.items():
            if v == i:
                num = 10 * num + k
    total += num

print(total)
    
