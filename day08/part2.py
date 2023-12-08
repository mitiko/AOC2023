#!/usr/bin/python3

import math

read_sample = 0
filename = ["input.txt", "sample.txt"][read_sample]
[ops, lines] = open(filename).read().split('\n\n')
lines = lines.split('\n')
left = {}
right = {}
all_nodes = []
for line in lines:
    node = line.split('=')[0].strip()
    all_nodes.append(node)
    [left[node], right[node]] = [x.strip('() ') for x in line.split('=')[1].split(',')]

count = 0
nodes = [x for x in all_nodes if x[2] == 'A']

def c1(node):
    count = 0
    while True:
        for op in ops:
            count += 1
            if op == 'L':
                node = left[node]
            if op == 'R':
                node = right[node]
            if node[2] == 'Z':
                return (count, node)

data = [c1(x) for x in nodes]
data = [(c, c1(n)[0]) for c, n in data]
assert all([x == y for x,y in data])
nums = [x for x, _ in data]
res = 1
for num in nums:
    res = math.lcm(res, num)
print(res)