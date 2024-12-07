import numpy as np

with open("input") as file:
    lines = [list(line.rstrip()) for line in file]

td = np.pad(lines, 3, mode="constant")
opp = {"M": "S", "S": "M"}
sum = 0

for y in range(len(td)):
    for x in range(len(td[y])):
        if td[y, x] == "A":
            lt = td[y - 1, x - 1]
            rt = td[y - 1, x + 1]
            lb = td[y + 1, x - 1]
            rb = td[y + 1, x + 1]

            if lt in opp and rb == opp[lt] and rt in opp and lb == opp[rt]:
                sum += 1

print(sum)
