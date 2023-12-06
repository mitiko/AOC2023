#!/usr/bin/python3

read_sample = 0
filename = ["input.txt", "sample.txt"][read_sample]
lines = open(filename).read().split('\n')
data = [[int(x) for x in lines[i].split(':')[1].split()] for i in range(2)]

s = 1
for time, distance in zip(data[0], data[1]):
    count = 0
    for speed in range(time):
        count += speed * (time - speed) > distance
    s *= count

print(s)
