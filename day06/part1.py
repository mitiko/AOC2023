#!/usr/bin/python3

read_sample = 0
filename = ["input.txt", "sample.txt"][read_sample]
lines = open(filename).read().split('\n')

times = [int(x) for x in lines[0].split(':')[1].split()]
distances = [int(x) for x in lines[1].split(':')[1].split()]
print(times)
print(distances)

s = 1
for i in range(3 if read_sample else 4):
    t = times[i]
    goal = distances[i]
    count = 0
    for hold in range(t):
        rem_t = t - hold
        assert rem_t >= 0
        speed = hold
        d = speed * rem_t
        if d > goal:
            # print(i, '->', hold, d, goal)
            count +=        1
    # print(i, count)
    s *= count

print(s)
