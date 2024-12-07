from collections import defaultdict

with open('input') as file:
    lines = [line.rstrip() for line in file]

sum = 0
leftList = []
rightDict = defaultdict(int)
for line in lines:
    left, right = line.split('   ')
    leftList.append(int(left))
    rightDict[int(right)] += 1

for l in leftList:
    sum += (l * rightDict[l])

print(sum)