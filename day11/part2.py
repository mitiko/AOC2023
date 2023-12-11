#!/usr/bin/python3

read_sample = 0
filename = ["input.txt", "sample.txt"][read_sample]
lines = open(filename).read().split('\n')

def trans(m):
    n = [['_'] * len(m) for _ in range(len(m[0]))]
    for i in range(len(m)):
        for j in range(len(m[0])):
            n[j][i] = m[i][j]
    return n

galaxies = [list(line) for line in lines]
# store expansion rows & cols
expand_rows = set()
expand_cols = set()

for i, row in enumerate(galaxies):
    if all([x == '.' for x in row]):
        expand_rows.add(i)
for i, col in enumerate(trans(galaxies)):
    if all([x == '.' for x in col]):
        expand_cols.add(i)

galaxy_locations = []
for y in range(len(galaxies)):
    for x, spot in enumerate(galaxies[y]):
        if spot == '#':
            galaxy_locations.append((x, y))

def distance(a, b):
    (x, y) = a
    (nx, ny) = b
    x, nx = min(x, nx), max(x, nx)
    y, ny = min(y, ny), max(y, ny)
    add_rows = len([1 for t in expand_rows if t in range(y, ny)])
    add_cols = len([1 for t in expand_cols if t in range(x, nx)])
    expand_rate = 1000000
    # if they cross an expansion boundary, add many
    return abs(x - nx) + abs(y - ny) + (expand_rate - 1) * (add_rows + add_cols)

s = 0
for i, g1 in enumerate(galaxy_locations):
    for g2 in galaxy_locations[i:]:
        s += distance(g1, g2)

print(s)
