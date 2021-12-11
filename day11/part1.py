from collections import deque
from pprint import pprint

with open("input.txt") as file:
    levels = [list(map(int, line)) for line in file.read().split("\n")]


# Return the 9 neighbour coordinates around the given (i, j) coord
def getAdj(i, j, size):
    for iAdj in range(i - 1, i + 2):
        for jAdj in range(j - 1, j + 2):
            if 0 <= iAdj < size and 0 <= jAdj < size and (iAdj != i or jAdj != j):
                yield (iAdj, jAdj)
   
    
count = 0
for cycle in range(100):
    q = deque()
    # First increase all levels by 1. Any octo that bursts is set to 0 and its
    # neighbours are added to a queue to check later.
    for i in range(len(levels)):
        for j in range(len(levels[0])):
            levels[i][j] += 1
            if levels[i][j] > 9:
                count += 1
                levels[i][j] = 0
                q.extend(getAdj(i, j, len(levels)))

    # Go through the queue and increase any octo's energy if it didn't already
    # burst (level > 0). If a new octo bursts, add its neighbours to the end of
    # the queue and set its level to 0.
    while q:
        i, j = q.popleft()
        if levels[i][j] > 0:
            levels[i][j] += 1
            if levels[i][j] > 9:
                count += 1
                levels[i][j] = 0
                for iAdj, jAdj in getAdj(i, j, len(levels)):
                    q.append((iAdj, jAdj))

print(count)


