import re

with open('input') as file:
    lines = [line.rstrip() for line in file]

sum = 0
for l in lines:
    results = re.findall('mul\(\d{1,3},\d{1,3}\)', l)

    for r in results:
        x, y = re.findall('\d{1,3}', r)
        sum += int(x) * int(y)

print(sum)

