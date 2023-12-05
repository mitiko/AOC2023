#!/usr/bin/python3

read_sample = 0
filename = ["input.txt", "sample.txt"][read_sample]
maps = open(filename).read().split('\n\n')

seeds = [int(x) for x in maps[0].split(':')[1].split()]
seeds = [(a, b) for [a, b] in zip(seeds[0::2], seeds[1::2])]
maps = [x.split('\n')[1:] for x in maps[1:]]

def convert(start, r, dest, src, range):
    start_r1 = start
    end_r1 = start + r - 1
    start_r2 = src
    end_r2 = src + range - 1
    diff = dest - src # to add

    if start_r1 < start_r2:
        if end_r1 < start_r2:
            return ([(start_r1, r)], [])
        if end_r1 >= start_r2 and end_r1 <= end_r2:
            return ([(start_r1, start_r2 - start_r1)], [(diff + start_r2, end_r1 - start_r2 + 1)])
        if end_r1 > end_r2:
            return ([(start_r1, start_r2 - start_r1), (end_r2 + 1, end_r1 - end_r2)], [(diff + start_r2, end_r2 - start_r2 + 1)])
    if start_r1 >= start_r2 and start_r1 <= end_r2:
        if end_r1 <= end_r2:
            return ([], [(diff + start_r1, r)])
        if end_r1 > end_r2:
            return ([(end_r2 + 1, end_r1 - end_r2)], [(diff + start_r1, end_r2 - start_r1 + 1)])
    if start_r1 >= end_r2:
        return ([(start, r)], [])

inter = [list() for _ in range(len(maps) + 1)]
inter[0] = seeds

for level, m in enumerate(maps):
    convs = [[int(y) for y in x.split()] for x in m]
    for [dest, src, range] in convs:
        rem = []
        for (s, r) in inter[level]:
            (remaining, converted) = convert(s, r, dest, src, range)
            inter[level + 1].extend(converted)
            rem.extend(remaining)
        inter[level] = rem
    inter[level + 1].extend(inter[level])

result = 10 ** 100
for (s, r) in inter[-1]:
    result = min(result, s)

print(result)
