disk = open('input').readline()

def index_of_last(arr, c):
    for idx, r in enumerate(list(reversed(arr))):
        if r == c: return len(arr) - 1 - idx

def decode(disk):
    contents = []
    current = 0

    for idx, x in enumerate(disk):
        contents.append((int(x), str(current))) if idx % 2 == 0 else contents.append((int(x), '.'))
        
        if idx % 2 == 0: current += 1
    
    return contents

def print_result(l):  
    result = ""
    for (space, char) in list(reversed(l)):
        for _ in range(space):
            result += char
        
    print(result)

reverse_decoded = list(reversed(decode(disk)))

for idx, pair in enumerate(reverse_decoded):
    needed_space, c = pair
    if c != '.': 
        space_idx = -1
        for temp_idx, r in enumerate(list(reversed(reverse_decoded))):
            target_space, target_c = r
            space_idx = len(reverse_decoded) - 1 - temp_idx
            if target_c == '.' and target_space >= needed_space:  
                break
        
        if space_idx != -1 and space_idx > idx:
            space_left = target_space - needed_space
            reverse_decoded[space_idx] = (needed_space, c)
            if space_left > 0: 
                reverse_decoded.insert(space_idx, (space_left, '.'))
            reverse_decoded[idx] = (needed_space, '.')

sum = 0
index = -1
for (space, char) in list(reversed(reverse_decoded)):
    for _ in range(space):
        index += 1
        if char != '.': sum += index * int(char)

print(sum)