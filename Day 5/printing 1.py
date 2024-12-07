from collections import defaultdict

with open("input") as file:
    rules, instructions = file.read().split('\n\n')

rules = rules.split()
instructions = instructions.split()

rd = defaultdict(set)
for r in rules:
    b, a = r.split('|')
    rd[b].add(a)

valid = []
for i in instructions:
    i = i.split(',')
    correct = True
    for id, n in enumerate(i):
        if n in rd:
            earlier = set(i[:id])
            if not earlier.isdisjoint(rd[n]): correct = False

    if correct: valid.append(i)

sum = 0
for v in valid:
    sum += int(v[int(len(v)/2)])

print(sum)