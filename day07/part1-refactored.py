#!/usr/bin/python3

from functools import cmp_to_key

read_sample = 0
filename = ["input.txt", "sample.txt"][read_sample]
lines = open(filename).read().split('\n')

values = { 'A': 12,'K': 11,'Q': 10,'J': 9, 'T': 8 }
values.update({str(x+2): x for x in range(8)})

def get_type(cards):
    uniq_cards = len(set(cards))
    if uniq_cards == 1: return 5
    if uniq_cards == 2: return 4 if cards.count(cards[0]) in [1, 4] else 3.5
    if uniq_cards == 3: return 2 if 2 in [cards.count(cards[x]) for x in range(2)] else 3
    if uniq_cards == 4: return 1
    if uniq_cards == 5: return 0

def compare(x1, x2):
    (h1, _), (h2, _) = x1, x2
    t1, t2 = get_type(list(h1)), get_type(list(h2))
    if t1 != t2: return [1, -1][t1 < t2]
    c1, c2 = [values[x] for x in h1], [values[x] for x in h2]
    for i in range(5):
        if c1[i] != c2[i]: return [1, -1][c1[i] < c2[i]]
    return 0

data = [(x.split()[0], int(x.split()[1])) for x in lines]
data.sort(key=cmp_to_key(compare))
s = sum([(i + 1) * bid for i, (_, bid) in enumerate(data)])
print(s)
