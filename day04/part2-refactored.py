#!/usr/bin/python3

read_sample = 0
filename = ["input.txt", "sample.txt"][read_sample]
lines = open(filename).read().split('\n')

copies = [1] * len(lines)
s = 0
for i, line in enumerate(lines):
    [winning, numbers] = line.split(':')[1].split('|')
    w = {int(x) for x in winning.split()}
    count = len([1 for x in numbers.split() if int(x) in w])
    for c in range(i + 1, i + count + 1):
        copies[c] += copies[i]
    s += copies[i]
print(s)
