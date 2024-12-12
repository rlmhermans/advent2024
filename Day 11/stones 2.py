from functools import cache

with open('input') as file:
    input = file.readline()
    
@cache
def solve(blinks, stone):
    if blinks == 0: 
        return 1
    
    length = len(str(stone))

    if stone == 0:
        return solve(blinks - 1, 1)

    elif length % 2 == 0:
        left, right = int(str(stone)[:int(length/2)]), int(str(stone)[int(length/2):])
        sum = solve(blinks - 1, left)
        sum += solve(blinks - 1, right)
        return sum

    else: return solve(blinks - 1, stone * 2024)

sum = 0
for i in list(map(int,input.split())):
    sum += solve(75, i)

print(sum)
