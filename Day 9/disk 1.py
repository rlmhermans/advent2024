disk = open('input').readline()

def index_of_last(arr, c):
    for idx, r in enumerate(list(reversed(arr))):
        if r == c: return len(arr) - 1 - idx

def decode(disk):
    contents = []
    current = 0

    for idx, x in enumerate(disk):
        for _ in range(int(x)):
            contents.append(str(current)) if idx % 2 == 0 else contents.append('.')
        
        if idx % 2 == 0: current += 1
    
    return contents

reverse_decoded = list(reversed(decode(disk)))
spaces = len([x for x in reverse_decoded if x == '.'])
match_list = ['.' for _ in range(spaces)]

for idx, c in enumerate(reverse_decoded):
    if c != '.': 
        last_space = index_of_last(reverse_decoded, '.')
        reverse_decoded[last_space] = c
        reverse_decoded[idx] = '.'

    if match_list == reverse_decoded[0:spaces]: break

sum = 0
for idx, r in enumerate(list(reversed(reverse_decoded))):
    if r != '.': sum += idx * int(r)

print(sum)