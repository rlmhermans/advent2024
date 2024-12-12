from collections import defaultdict

with open('test') as file:
    input = file.readline()

blinks = 75
solved = {'0': '1'}
stones = defaultdict(int)

for i in input.split():
    stones[i] = 1

for blink in range(blinks):
    for k, v in stones.copy().items():
        if v == 0: continue
        stones[k] = stones[k] - v

        if k in solved:    
            stones[solved[k]] = stones[solved[k]] + v
        
        else:
            stone_long = []
            for stone in k.split():
                if stone in solved:
                    stones[solved[stone]] = stones[solved[stone]] + 1
                    stone_long.append(solved[stone])

                else:
                    l = len(stone)

                    if l % 2 == 0: 
                        newstone = stone[:int(l/2)] + ' ' + str(int(stone[int(l/2):]))

                    else:
                        n = int(stone)
                        newstone = str(n * 2024)
                    
                    stones[newstone] = stones[newstone] + v
                    solved[stone] = newstone
                    stone_long.append(newstone)

            solved[k] = " ".join(stone_long)

result = []
for k, v in stones.items():
    for _ in range(v):
        result += k.split()

print(len(result)) 