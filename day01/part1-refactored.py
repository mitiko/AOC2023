#!/usr/bin/python3

import re

read_sample = 0
filename = ["input.txt", "sample.txt"][read_sample]
lines = open(filename).readlines()

s = 0
for line in lines:
    m = re.findall('\d', line)
    s += int(m[0]) * 10 + int(m[-1])
print(s)
