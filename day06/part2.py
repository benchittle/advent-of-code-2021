from collections import OrderedDict
from os import stat

with open("sample.txt") as file:
    cycles = (map(int, file.read().split(",")))



states = [0 for i in range(9)]
for i in cycles:
    states[i] += 1

print(states)
DAYS = 256
for d in range(DAYS):
    ready = states[0]
    for i in range(1, 9):
        states[i - 1] = states[i]
    
    states[8] = ready
    states[6] += ready

    print(states)

print(sum(states))

