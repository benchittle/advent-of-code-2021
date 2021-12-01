import pandas as pd

with open("input.txt") as file:
    data = list(map(int, file.read().split("\n")[:-1]))

# Cheeky overkill use of Pandas for this
s = pd.Series(data)
rolling_sum = s.rolling(window=3).sum()

print(sum(rolling_sum > rolling_sum.shift(1)))

