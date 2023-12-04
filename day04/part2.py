#!/usr/bin/python3

read_sample = 0
filename = ["input.txt", "sample.txt"][read_sample]
lines = open(filename).read().split('\n')

copies = [1] * (len(lines) + 2)
s = 0
for line in lines:
    [card, data] = line.split(':')
    card_id = int(card.split()[1])
    [winning, numbers] = data.split('|')
    w = {int(x) for x in winning.split()}
    count = 0
    for num in [int(x) for x in numbers.split()]:
        if num in w:
            count += 1
    for c in range(card_id + 1, card_id + count + 1):
        copies[c] += copies[card_id]
    s += copies[card_id]

print(s)
