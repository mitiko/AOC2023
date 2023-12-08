#!/usr/bin/python3

read_sample = 0
filename = ["input.txt", "sample.txt"][read_sample]
[ops, commands] = open(filename).read().split('\n\n')
left, right = {}, {}
for line in commands.split('\n'):
    [node, next] = [x.strip() for x in line.split('=')]
    [left[node], right[node]] = [x.strip('() ') for x in next.split(',')]

count, node = 0, 'AAA'
while True:
    for op in ops:
        count += 1
        node = (left if op == 'L' else right)[node]
        if node == 'ZZZ':
            print(count)
            exit(0)
