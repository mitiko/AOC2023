#!/usr/bin/python3

import math

read_sample = 0
filename = ["input.txt", "sample.txt"][read_sample]
[ops, commands] = open(filename).read().split('\n\n')
left, right = {}, {}
for line in commands.split('\n'):
    [node, next] = [x.strip() for x in line.split('=')]
    [left[node], right[node]] = [x.strip('() ') for x in next.split(',')]
nodes = [x for x in (set(left.keys()) | set(right.keys())) if x[2] == 'A']
def cycle(node):
    count = 0
    while True:
        for op in ops:
            count += 1
            node = (left if op == 'L' else right)[node]
            if node[2] == 'Z':
                return (count, node)

data = [cycle(x) for x in nodes]
data = [(count, cycle(end_node)[0]) for count, end_node in data]
assert all([x == y for x, y in data]) # distance A -> Z = distance Z -> Z
nums = [x for x, _ in data]
print(math.lcm(*nums))
