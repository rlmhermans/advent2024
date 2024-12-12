with open('test') as file:
    input = file.readline()

stones = list(map(int, input.split()))
blinks = 25

for _ in range(blinks):
    skip = False

    for idx, s in enumerate(stones):
        if skip: 
            skip = False
            continue

        if s == 0: 
            stones[idx] = 1
            continue

        ss = str(s)
        l = len(ss)
        if l % 2 == 0: 
            left, right = ss[:int(l/2)], ss[int(l/2):]
            stones[idx] = int(right)
            stones.insert(idx, int(left))
            skip = True
            continue

        stones[idx] = s * 2024

print(len(stones))