#!/usr/bin/python3

read_sample = 0
filename = ["input.txt", "sample.txt"][read_sample]
lines = open(filename).readlines()

import re
ss = re.compile("(one|two|three|four|five|six|seven|eight|nine|\d)")
ssr = re.compile("(eno|owt|eerht|ruof|evif|xis|neves|thgie|enin|\d)")

ddm = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
}
ddmr = {
    "eno": 1,
    "owt": 2,
    "eerht": 3,
    "ruof": 4,
    "evif": 5,
    "xis": 6,
    "neves": 7,
    "thgie": 8,
    "enin": 9,
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
}

s = 0
for line in lines:
    mm = re.findall(ss,line)
    mmr = re.findall(ssr,line[::-1])
    d1 = ddm[mm[0]]
    d2 = ddmr[mmr[0]]
    d = d1 * 10 + d2
    s += d
print(s)