with open("input") as file:
    lines = [line.rstrip() for line in file]

def calc(target, current, numbers):
    if numbers == []:
        return current == target
    else:
        head, *tail = numbers
        sum_path = calc(target, head + current, tail)
        mul_path = calc(target, head * current, tail)
        concat_path = calc(target, int('' + str(current) + str(head)), tail)
        
        return sum_path or mul_path or concat_path

sum = 0
for line in lines:
    target, numbers = line.split(': ')
    target = int(target)
    numbers = list(map(int, numbers.split(' ')))

    if calc(target, 0, numbers): sum += target

print(sum)