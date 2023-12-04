#!/usr/bin/python3

read_sample = 0
filename = ["input.txt", "sample.txt"][read_sample]
lines = open(filename).read().split('\n')

s = 0
for line in lines:
    [card, data] = line.split(':')
    [winning, numbers] = data.split('|')
    w = {int(x) for x in winning.split()}
    count = 0
    for num in [int(x) for x in numbers.split()]:
        if num in w:
            count += 1
    if count > 0:
        s += 1 << (count - 1)

print(s)
