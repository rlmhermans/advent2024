import copy


with open("input") as file:
    lines = [list(line.rstrip()) for line in file]

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
start = '^'

for idx, line in enumerate(lines):
    if start in line: 
        start_y, start_x = idx, line.index(start)
        line[start_x] = '.'

def mazerunner(lines):
    visited = set()
    visited_with_dir = set()
    current = 0
    stuck = False
    try:
        y, x = start_y, start_x
        while not stuck:
            dy, dx = directions[current]
            next_y, next_x = y + dy, x + dx
            if next_y < 0 or next_x < 0: raise IndexError 
            if (next_y, next_x, current) in visited_with_dir:
                visited.clear()
                return visited
            if '.' == lines[next_y][next_x]:
                visited.add((next_y, next_x))
                visited_with_dir.add((next_y, next_x,current))
                y, x = next_y, next_x
            elif '#' == lines[next_y][next_x]:
                current = (current + 1) % 4

    except IndexError:
        return visited
    
visited = mazerunner(lines)

total = 0
for y, x in visited:
    lines_temp = copy.deepcopy(lines)
    lines_temp[y][x] = '#'
    
    new_visited = mazerunner(lines_temp)
    if len(new_visited) == 0: total += 1

print(total)