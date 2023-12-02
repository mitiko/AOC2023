#!/usr/bin/python3

read_sample = 0
filename = ["input.txt", "sample.txt"][read_sample]
lines = open(filename).read().strip().split('\n')

def parse(sample: str):
    colors = [x.strip() for x in sample.split(',')]
    d = {'red': 0, 'blue': 0, 'green': 0 }
    d.update({x.split()[1]: int(x.split()[0]) for x in colors})
    return d

def maxc(cmap_a, cmap_b): return { k: max(cmap_a[k], cmap_b[k]) for k in cmap_a.keys() }

s = 0
for line in lines:
    samples = [x.strip() for x in line.split(':')[1].strip().split(';')]
    m = {'red': 0, 'blue': 0, 'green': 0 }
    for sample in samples:
        m = maxc(m, parse(sample))
    s += m['red'] * m['green'] * m['blue']
print(s)
