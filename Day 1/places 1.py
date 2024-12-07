with open('input') as file:
    lines = [line.rstrip() for line in file]

sum = 0
leftList = []
rightList = []
for line in lines:
    left, right = line.split('   ')
    leftList.append(int(left))
    rightList.append(int(right))

leftList.sort()
rightList.sort()

zipped = zip(leftList, rightList)
for l, r in zipped:
    sum += abs(l - r)

print(sum)