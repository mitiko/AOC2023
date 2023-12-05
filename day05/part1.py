#!/usr/bin/python3

read_sample = 0
filename = ["input.txt", "sample.txt"][read_sample]
maps = open(filename).read().split('\n\n')

seeds = [int(x) for x in maps[0].split(':')[1].split()]
maps = [x.split('\n')[1:] for x in maps[1:]]

def convert(x, dest, src, range):
    if x < src or x > src + range - 1:
        return None
    return x + dest - src

result = 10 ** 100
for seed in seeds:
    t = seed
    for m in maps:
        convs = [[int(y) for y in x.split()] for x in m]
        out = None
        for [dest, src, range] in convs:
            out = convert(t, dest, src, range)
            if out is not None:
                break
        t = t if out is None else out
    result = min(result, t)

print(result)
