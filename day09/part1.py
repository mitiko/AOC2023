#!/usr/bin/python3

read_sample = 0
filename = ["input.txt", "sample.txt"][read_sample]
lines = open(filename).read().split('\n')

def calc(nums):
    diffs = [nums]
    while True:
        diff = diffs[-1]
        if all([x == 0 for x in diff]):
            break
        diff = [diff[i] - diff[i-1] for i in range(1, len(diff))]
        diffs.append(diff)
    return sum([x[-1] for x in diffs])

s = 0
for line in lines:
    nums = [int(x) for x in line.split()]
    s += calc(nums)

print(s)
