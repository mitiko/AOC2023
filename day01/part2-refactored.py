#!/usr/bin/python3

import re
input = open("input.txt").readlines()

d1 = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}
d2 = {k[::-1]: v for k, v in d1.items()}
r1 = re.compile(f"({'|'.join(d1.keys())}|\d)")
r2 = re.compile(f"({'|'.join(d2.keys())}|\d)")
d1.update({str(x): x for x in range(10)})
d2.update({str(x): x for x in range(10)})

s = 0
for line in input:
    x1 = d1[re.findall(r1, line)[0]]
    x2 = d2[re.findall(r2, line[::-1])[0]]
    s += x1 * 10 + x2
print(s)
