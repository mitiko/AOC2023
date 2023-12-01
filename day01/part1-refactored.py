#!/usr/bin/python3

import re
input = open("input.txt").readlines()

s = 0
for line in input:
    m = re.findall('\d', line)
    s += int(m[0]) * 10 + int(m[-1])
print(s)
