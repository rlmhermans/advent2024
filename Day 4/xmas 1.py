import numpy as np

with open("input") as file:
    lines = [list(line.rstrip()) for line in file]

td = np.pad(lines, 3, mode="constant")
directions = [(-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1), (0, -1), (0, 1)]

sum = 0

for y in range(len(td)):
    for x in range(len(td[y])):
        if td[y, x] == "X":
            for dy, dx in directions:
                if td[y + dy, x + dx] == "M":
                    if td[y + 2 * dy, x + 2 * dx] == "A":
                        if td[y + 3 * dy, x + 3 * dx] == "S":
                            sum += 1

print(sum)
