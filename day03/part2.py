#!/usr/bin/python3

read_sample = 0
filename = ["input.txt", "sample.txt"][read_sample]
lines = open(filename).read().split('\n')

y_max = len(lines) - 1
x_max = len(lines[0]) - 1

def flatten(x): return [item for sublist in x for item in sublist]
def is_digit(x): return x in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
def is_symbol(x): return x in ['%', '/', '=', '-', '@', '&', '+', '#', '$', '*']

def parse_int(line, t):
    start = -1 # actually incorrect if end == x_max, but whatevs
    end = t
    while is_digit(line[t]):
        start = t
        t -= 1
        if t < 0:
            break
    t = end
    while is_digit(line[t]):
        end = t
        t += 1
        if t > x_max:
            break
    rg = line[start:end+1]
    return 0 if rg == '' else int(rg)

s = 0
for i, line in enumerate(lines):
    num = 0
    marker = False
    for j, x in enumerate(line):
        if x != '*':
            continue
        l = 0 if j == 0 else parse_int(line, j-1)
        r = 0 if j == x_max else parse_int(line, j+1)

        tl = 0 if i == 0 or j == 0 else parse_int(lines[i-1], j-1)
        tm = 0 if i == 0 else parse_int(lines[i-1], j)
        tr = 0 if i == 0 or j == x_max else parse_int(lines[i-1], j+1)
        bl = 0 if i == y_max or j == 0 else parse_int(lines[i+1], j-1)
        bm = 0 if i == y_max else parse_int(lines[i+1], j)
        br = 0 if i == y_max or j == x_max else parse_int(lines[i+1], j+1)

        adj = [l, r]
        if tl != 0 and tr != 0 and tm == 0:
            adj.extend([tl, tr])
        elif tl != 0:
            adj.append(tl)
        elif tm != 0:
            adj.append(tm)
        elif tr != 0:
            adj.append(tr)

        if bl != 0 and br != 0 and bm == 0:
            adj.extend([bl, br])
        elif bl != 0:
            adj.append(bl)
        elif bm != 0:
            adj.append(bm)
        elif br != 0:
            adj.append(br)

        adj = [x for x in adj if x != 0]
        # print('____adj', adj)
        if len(adj) != 2:
            continue
        # print('adding:', adj[0], adj[1])
        s += adj[0] * adj[1]

print(s)
