#!/usr/bin/python3

import re

read_sample = 0
filename = ["input.txt", "sample.txt"][read_sample]
lines = open(filename).read().strip().split('\n')

max_red = 12
max_green = 13
max_blue = 14

s = 0
for line in lines:
    [game, data] = line.split(':')
    game_id = int(re.findall('\d+', game)[0])
    # print(game_id)
    samples = data.strip().split(';')
    possible = True
    for sample in [x.strip() for x in samples]:
        red, green, blue = 0, 0, 0
        dd1 = [x.strip() for x in sample.split(',')]
        for dd in dd1:
            count = int(re.findall('\d+', dd)[0])
            # print('dd:', dd, 'count:', count)
            if dd.endswith('red'):
                red = count
            if dd.endswith('green'):
                green = count
            if dd.endswith('blue'):
                blue = count
            # print('dd:', dd, 'count:', count, 'red:', red, 'blue:', blue, 'green:', green)
        if red > max_red or green > max_green or blue > max_blue:
            possible = False
            break

    if possible:
        # print(game_id)
        s += game_id

print(s)