with open("test") as file:
    lines = [line.rstrip() for line in file]

def calc(target, current, numbers):
    if numbers == []:
        return current == target
    else:
        head, *tail = numbers
        valid1 = calc(target, head + current, tail)
        valid2 = calc(target, head * current, tail)
        
        return valid1 or valid2

sum = 0
for line in lines:
    target, numbers = line.split(': ')
    target = int(target)
    numbers = list(map(int, numbers.split(' ')))

    if calc(target, 0, numbers): sum += target

print(sum)