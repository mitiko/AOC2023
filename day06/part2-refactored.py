#!/usr/bin/python3

import math

read_sample = 0
filename = ["input.txt", "sample.txt"][read_sample]
lines = open(filename).read().split('\n')

[time, distance] = [int(''.join(lines[i].split(':')[1].split())) for i in range(2)]
def is_faster(speed): return speed * (time - speed) > distance
def binary_search(lo, hi, test):
    while hi > lo:
        mid = lo + (hi - lo) // 2
        if test(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo

guess = round(math.sqrt(distance))
start = binary_search(1, guess, is_faster)
end = binary_search(guess, distance, lambda x: not is_faster(x))
print(end - start)
