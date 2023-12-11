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

def pprint(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            print(m[i][j], end=' ')
        print()

def expand(m):
    n = []
    for row in m:
        if all([x == '.' for x in row]):
            n.append(row.copy()) # very important to copy
        n.append(row)
    return n

galaxies = [list(line) for line in lines]
galaxies = trans(expand(trans(expand(galaxies))))

galaxy_locations = []
for y in range(len(galaxies)):
    for x, spot in enumerate(galaxies[y]):
        if spot == '#':
            galaxy_locations.append((x, y))

def distance(a, b):
    (x, y) = a
    (nx, ny) = b
    return abs(x - nx) + abs(y - ny)

s = 0
for i, g1 in enumerate(galaxy_locations):
    for g2 in galaxy_locations[i:]:
        s += distance(g1, g2)

print(s)
