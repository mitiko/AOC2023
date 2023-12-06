#!/usr/bin/python3

import math

read_sample = 0
filename = ["input.txt", "sample.txt"][read_sample]
lines = open(filename).read().split('\n')

t = int(''.join(lines[0].split(':')[1].split()))
goal = int(''.join(lines[1].split(':')[1].split()))

# can we do a binary search?
guess = round(math.sqrt(goal))
print(guess)

def calc(hold): return 1 if hold * (t - hold) > goal else 0
def calc1(hold): return hold * (t - hold) > goal

lo = 1
hi = guess + 1
assert calc1(hi)

while hi > lo:
    mid = lo + (hi - lo) // 2
    if calc1(mid):
        hi = mid
    else:
        lo = mid + 1

assert lo == hi
start = lo
# print('start', start)

lo = guess
hi = goal
while hi > lo:
    mid = lo + (hi - lo) // 2
    if calc1(mid):
        lo = mid + 1
    else:
        hi = mid

assert lo == hi
end = lo
# print('end', end)
count = end - start
# for hold in range(t):
#     count += calc(hold)

# print("answer:", count)
print(count)
