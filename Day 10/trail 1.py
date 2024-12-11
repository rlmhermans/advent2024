import numpy as np

with open('input') as file:
    lines = file.read().splitlines()

transformed = []
for line in lines:
    transformed.append(list(map(int, line))) 
    
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
m = np.array(transformed)
m = np.pad(m, 1, mode="constant", constant_values=-1)

def follow(current, y, x, summits):
    if current == 9: 
        summits.add((y, x))
        return summits
    else: 
        current += 1
        for d in directions:
            dy, dx = d
            next_y, next_x = y + dy, x + dx
            if m[next_y, next_x] == current:
                summits.update(follow(current, next_y, next_x, summits))
        return summits

sum = 0
for y in range(len(m)):
    for x in range(len(m)):
        if m[y, x] == 0:
            sum += len(follow(0, y, x, set()))

print(sum)