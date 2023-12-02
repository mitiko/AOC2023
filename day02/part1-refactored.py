#!/usr/bin/python3

read_sample = 0
filename = ["input.txt", "sample.txt"][read_sample]
lines = open(filename).read().strip().split('\n')

def parse(sample: str):
    colors = [x.strip() for x in sample.split(',')]
    d = {'red': 0, 'blue': 0, 'green': 0 }
    d.update({x.split()[1]: int(x.split()[0]) for x in colors})
    return d

def fits(cmap): return not (cmap['red'] > 12 or cmap['green'] > 13 or cmap['blue'] > 14)

s = 0
for line in lines:
    [game, data] = line.split(':')
    game_id = int(game.split()[1])
    samples = [x.strip() for x in data.strip().split(';')]
    if all([fits(parse(sample)) for sample in samples]):
        s += game_id
print(s)
