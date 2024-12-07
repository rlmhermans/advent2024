from collections import defaultdict

with open("input") as file:
    rules, instructions = file.read().split('\n\n')

rules = rules.split()
instructions = instructions.split()

ruleset = defaultdict(set)
for r in rules:
    b, a = r.split('|')
    ruleset[b].add(a)

invalids = []
for instruction in instructions:
    instruction = instruction.split(',')
    correct = True
    for id, n in enumerate(instruction):
        if n in ruleset:
            earlier = set(instruction[:id])
            if not earlier.isdisjoint(ruleset[n]): correct = False

    if not correct: invalids.append(instruction)

valids = []
for pages in invalids:
    for id, page in enumerate(pages):
        earliest = 100
        for post in ruleset[page]:
            if post in pages:
                idx = list.index(pages, post)
                earliest = min(earliest, idx)
        if earliest != 100 and earliest < id:
            pages.remove(page)
            pages.insert(earliest, page)
    
    valids.append(pages)
    
sum = 0
for pages in valids:
    sum += int(pages[int(len(pages)/2)])

print(sum)