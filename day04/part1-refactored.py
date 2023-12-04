#!/usr/bin/python3

read_sample = 0
filename = ["input.txt", "sample.txt"][read_sample]
lines = open(filename).read().split('\n')

s = 0
for line in lines:
    [winning, numbers] = line.split(':')[1].split('|')
    w = {int(x) for x in winning.split()}
    count = len([1 for x in numbers.split() if int(x) in w])
    if count > 0:
        s += 1 << (count - 1)
print(s)
