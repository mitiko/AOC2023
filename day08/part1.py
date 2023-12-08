#!/usr/bin/python3

read_sample = 0
filename = ["input.txt", "sample.txt"][read_sample]
[ops, lines] = open(filename).read().split('\n\n')
lines = lines.split('\n')
left = {}
right = {}
for line in lines:
    node = line.split('=')[0].strip()
    [left[node], right[node]] = [x.strip('() ') for x in line.split('=')[1].split(',')]

count = 0
node = 'AAA'
while True:
    for op in ops:
        count += 1
        if op == 'L':
            node = left[node]
        if op == 'R':
            node = right[node]
        if node == 'ZZZ':
            print(count)
            exit(0)
