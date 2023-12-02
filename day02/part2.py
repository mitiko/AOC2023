#!/usr/bin/python3

import re
read_sample = 0

filename = ["input.txt", "sample.txt"][read_sample]
lines = open(filename).read().strip().split('\n')

s = 0
for line in lines:
    [game, data] = line.split(':')
    game_id = int(re.findall('\d+', game)[0])
    # print(game_id)
    samples = data.strip().split(';')
    possible = True
    min_red, min_green, min_blue = 0, 0, 0
    for sample in [x.strip() for x in samples]:
        red, green, blue = 0, 0, 0
        dd1 = [x.strip() for x in sample.split(',')]
        for dd in dd1:
            count = int(re.findall('\d+', dd)[0])
            if dd.endswith('red'):
                red = count
            if dd.endswith('green'):
                green = count
            if dd.endswith('blue'):
                blue = count
        min_red = max(min_red, red)
        min_green = max(min_green, green)
        min_blue = max(min_blue, blue)

    power = min_red * min_green * min_blue
    s += power

print(s)