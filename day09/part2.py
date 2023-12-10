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
    a = sum([x[0] for i, x in enumerate(diffs) if i % 2 == 0])
    b = sum([x[0] for i, x in enumerate(diffs) if i % 2 == 1])
    return a - b

# A - X = 0 -> X = A
# B - Y = X -> Y = B - A
# C - Z = Y -> Z = C - B + A
# D - T = Z -> T = D - C + B - A

s = 0
for line in lines:
    nums = [int(x) for x in line.split()]
    s += calc(nums)

print(s)
