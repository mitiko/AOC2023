#!/usr/bin/python3

read_sample = 0
filename = ["input.txt", "sample.txt"][read_sample]
lines = open(filename).readlines()

s = 0
for line in lines:
    d1 = 0
    for ch in line:
        if ch in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            d1 = int(ch)
            break
    d2 = 0
    for ch in line[::-1]:
        if ch in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            d2 = int(ch)
            break
    d = d1 * 10 + d2
    s += d
print(s)