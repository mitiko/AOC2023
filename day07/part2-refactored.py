#!/usr/bin/python3

from functools import cmp_to_key

read_sample = 0
filename = ["input.txt", "sample.txt"][read_sample]
lines = open(filename).read().split('\n')

values = { 'A': 12, 'K': 11, 'Q': 10, 'T': 9, 'J': 0 }
values.update({ str(x+1): x for x in range(1, 9) })

faces = [k for k in values.keys() if k != 'J']
mm = {}
def get_type(hand):
    if hand in mm: return mm[hand]
    cards = sorted(hand, key=lambda c: values[c])
    joker_count = cards.count('J')
    t = get_orig_type(cards)
    if joker_count == 4 or joker_count == 5: return 5
    if joker_count == 0: return t
    for j1 in faces:
        for j2 in faces:
            for j3 in faces:
                cards[0] = j1
                cards[1] = j2 if cards[1] == 'J' else cards[1]
                cards[2] = j3 if cards[2] == 'J' else cards[2]
                t = max(t, get_orig_type(cards))
                cards[:joker_count] = ['J'] * joker_count
    mm[hand] = t
    return t

def get_orig_type(cards):
    uniq_cards = len(set(cards))
    if uniq_cards == 1: return 5
    if uniq_cards == 2: return 4 if cards.count(cards[0]) in [1, 4] else 3.5
    if uniq_cards == 3: return 2 if 2 in [cards.count(cards[x]) for x in range(2)] else 3
    if uniq_cards == 4: return 1
    if uniq_cards == 5: return 0

def compare(x1, x2):
    (h1, _), (h2, _) = x1, x2
    t1, t2 = get_type(h1), get_type(h2)
    if t1 != t2: return [1, -1][t1 < t2]
    c1, c2 = [values[x] for x in h1], [values[x] for x in h2]
    for i in range(5):
        if c1[i] != c2[i]: return [1, -1][c1[i] < c2[i]]
    return 0

data = [(x.split()[0], int(x.split()[1])) for x in lines]
data.sort(key=cmp_to_key(compare))
s = sum([(i + 1) * bid for i, (_, bid) in enumerate(data)])
print(s)