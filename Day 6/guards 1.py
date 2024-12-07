with open("input") as file:
    lines = [list(line.rstrip()) for line in file]

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
start = '^'
current = 0

visited = set()
for idx, line in enumerate(lines):
    if start in line: 
        y, x = idx, line.index(start)
        visited.add((y,x))
        line[x] = '.'

try:
    while True:
        dy, dx = directions[current]
        next_y, next_x = y + dy, x + dx
        if next_y < 0 or next_x < 0: raise IndexError 
        if '.' == lines[next_y][next_x]:
            visited.add((next_y, next_x))
            y, x = next_y, next_x
        elif '#' == lines[next_y][next_x]:
            current = (current + 1) % 4

except IndexError:
    print(len(visited))