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

# BFS doesn't preserve flow
assert len(edges[start]) == 2
flow = defaultdict(list) # node -> directions (up, down, left, right)
in_loop = set()

prev, node = start, edges[start][0]
switch = False
while True:
    in_loop.add(prev)
    in_loop.add(start)
    (x, y) = prev
    (nx, ny) = node
    direction = ''
    if nx == x - 1: direction = 'left'
    if nx == x + 1: direction = 'right'
    if ny == y - 1: direction = 'up'
    if ny == y + 1: direction = 'down'
    flow[node] = [direction]
    if direction not in flow[prev]:
        flow[prev].append(direction)

    # exit on the second time this condition is met
    if prev == start:
        if switch: break
        switch = True

    next_nodes = edges[node]
    assert len(next_nodes) == 2
    assert prev in next_nodes
    prev, node = node, [x for x in next_nodes if x != prev][0]
    # prev, node = node, [x for x in edges[node] if x != prev][0]

from termcolor import colored
# for y in range(len(grid)):
#     for x, tile in enumerate(grid[y]):
#         c = 'black'
#         if 'right' in flow[(x, y)]:
#             c = 'red'
#         if 'left' in flow[(x, y)]:
#             c = 'blue'
#         if 'up' in flow[(x, y)]:
#             c = 'green'
#         if 'down' in flow[(x, y)]:
#             c = 'yellow'
#         print(colored(tile, c), end=' ')
#     print()

counts = [0, 0]
max_y = len(grid) # exclusive
max_x = len(grid[0]) # exclusive
for y in range(len(grid)):
    for x, tile in enumerate(grid[y]):
        if (x, y) in in_loop:
            if read_sample == 1: print(tile, end=' ')
            continue
        f_up, f_down, f_right, f_left = [], [], [], []
        for i in reversed(range(0, x)):
            if (i, y) in flow:
                f_left = flow[(i, y)]
                break
        for i in range(x + 1, max_x):
            if (i, y) in flow:
                f_right = flow[(i, y)]
                break
        for i in reversed(range(0, y)):
            if (x, i) in flow:
                f_up = flow[(x, i)]
                break
        for i in range(y, max_y):
            if (x, i) in flow:
                f_down = flow[(x, i)]
                break
        clock = -1
        if 'down' in f_right or 'up' in f_left or 'left' in f_down or 'right' in f_up:
            clock = 0
        elif 'up' in f_right or 'down' in f_left or 'right' in f_down or 'left' in f_up:
            clock = 1

        if clock >= 0:
            counts[clock] += 1
        c = { -1: 'black', 0: 'red', 1: 'blue' }[clock]
        if read_sample == 1: print(colored('x', c), end=' ')
        # print(f_up, f_down, f_right, f_left)

        if len(f_up) == 0 or len(f_down) == 0 or len(f_right) == 0 or len(f_left) == 0:
            if clock != -1:
                inside_clock = 1 - clock
    if read_sample == 1: print()

print(counts[inside_clock])
