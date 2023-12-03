#!/usr/bin/python3

read_sample = 0
filename = ["input.txt", "sample.txt"][read_sample]
lines = open(filename).read().split('\n')

def is_digit(x): return x in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
def is_symbol(x): return x in ['%', '/', '=', '-', '@', '&', '+', '#', '$', '*']

y_max = len(lines) - 1
x_max = len(lines[0]) - 1

s = 0
for i, line in enumerate(lines):
    num = 0
    marker = False
    for j, x in enumerate(line):
        if is_digit(x):
            num = 10 * num + int(x)
            # check left, right, top, bottom
            l = False if j == 0 else is_symbol(line[j-1])
            r = False if j == x_max else is_symbol(line[j+1])
            t = False if i == 0 else is_symbol(lines[i-1][j])
            b = False if i == y_max else is_symbol(lines[i+1][j])

            lt = False if (j == 0 or i == 0) else is_symbol(lines[i-1][j-1])
            rt = False if (j == x_max or i == 0) else is_symbol(lines[i-1][j+1])
            lb = False if (j == 0 or i == y_max) else is_symbol(lines[i+1][j-1])
            rb = False if (j == x_max or i == y_max) else is_symbol(lines[i+1][j+1])
            if l or r or t or b or lt or rt or lb or rb:
                marker = True

        if not is_digit(x):
            if marker:
                # print('adding', num)
                s += num
            marker = False
            num = 0
    if marker:
        s += num
    marker = False
    num = 0

print(s)
