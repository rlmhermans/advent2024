from collections import defaultdict

with open("input") as file:
    lines = [line.rstrip() for line in file]

width = len(lines[0])
antinodes = set()
antennas = defaultdict(list)
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c != '.': antennas[c].append((y, x))

for positions in antennas.values():
    for current in positions:
        antinodes.add(current)
        for pos in positions:
            if not pos == current:
                curr_y, curr_x = current
                pos_y, pos_x = pos
                delta_y = pos_y - curr_y 
                delta_x = pos_x - curr_x
                
                edge_one_reached = False
                edge_two_reached = False
                mul = 1
                while not (edge_one_reached and edge_two_reached):
                    new_y = curr_y - (mul*delta_y)
                    new_x = curr_x - (mul*delta_x)

                    if new_y > -1 and new_x > -1 and new_y < width and new_x < width:
                        antinodes.add((new_y, new_x))
                    else: edge_one_reached = True

                    new_y = pos_y + (mul*delta_y)
                    new_x = pos_x + (mul*delta_x)

                    if new_y > -1 and new_x > -1 and new_y < width and new_x < width:
                        antinodes.add((new_y, new_x))
                    else: edge_two_reached = True

                    mul += 1

print(len(antinodes))