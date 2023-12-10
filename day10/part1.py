#!/usr/bin/python3

from collections import defaultdict

read_sample = 0
filename = ["input.txt", "sample.txt"][read_sample]
grid = [list(x) for x in open(filename).read().split('\n')]
edges = defaultdict(list) # start -> [next]

for y in range(len(grid)):
    for x, tile in enumerate(grid[y]):
        if tile == '|': edges[(x, y)] = [(x, y - 1), (x, y + 1)]
        if tile == '-': edges[(x, y)] = [(x - 1, y), (x + 1, y)]
        if tile == '7': edges[(x, y)] = [(x, y + 1), (x - 1, y)]
        if tile == 'F': edges[(x, y)] = [(x, y + 1), (x + 1, y)]
        if tile == 'J': edges[(x, y)] = [(x, y - 1), (x - 1, y)]
        if tile == 'L': edges[(x, y)] = [(x, y - 1), (x + 1, y)]
        if tile == 'S':
            start = (x, y)
            if grid[y - 1][x] in ['|', '7', 'F']:
                edges[(x, y)].append((x, y - 1))
            if grid[y + 1][x] in ['|', 'J', 'L']:
                edges[(x, y)].append((x, y + 1))
            if grid[y][x - 1] in ['-', 'F', 'L']:
                edges[(x, y)].append((x - 1, y))
            if grid[y][x + 1] in ['-', 'J', '7']:
                edges[(x, y)].append((x + 1, y))

# BFS with distance
nodes = [(start, 0)]
seen = set()
distance = {}

while len(nodes) > 0:
    node, steps = nodes[0]
    nodes = nodes[1:]
    # if seen, check the smallest distance
    if node not in seen:
        distance[node] = steps
    elif node in seen and steps <= distance[node]:
        distance[node] = steps
    elif node in seen:
        continue
    # append all new nodes
    for next_node in edges[node]:
        nodes.append((next_node, steps + 1))
    seen.add(node)

# for y in range(len(grid)):
#     for x, tile in enumerate(grid[y]):
#         d = '.' if (x, y) not in distance else distance[(x, y)]
#         print(d, end=' ')
#     print()

# 6749 is too low
m = max(distance.values())
print(m)