#!/usr/bin/python3

from functools import cmp_to_key

read_sample = 0
filename = ["input.txt", "sample.txt"][read_sample]
lines = open(filename).read().split('\n')

values = {
    'A': 12,
    'K': 11,
    'Q': 10,
    'J': 9,
    'T': 8,
    '9': 7,
    '8': 6,
    '7': 5,
    '6': 4,
    '5': 3,
    '4': 2,
    '3': 1,
    '2': 0,
}
types = {
    'Five of a kind': 6,
    'Four of a kind': 5,
    'Full house': 4,
    'Three of a kind': 3,
    'Two pair': 2,
    'One pair': 1,
    'High card': 0,
}

def get_type(hand):
    cards = list(hand)
    uniq_cards = len(set(cards))
    if uniq_cards == 1:
        return 'Five of a kind'
    if uniq_cards == 2:
        c = cards.count(cards[0])
        return 'Four of a kind' if c == 1 or c == 4 else 'Full house'
    if uniq_cards == 3:
        # three of a kind 1 + 1 + 3
        # two pair        2 + 2 + 1
        c1 = cards.count(cards[0])
        if c1 == 1:
            c2 = cards.count(cards[1])
            if c2 == 1 or c2 == 3:
                return 'Three of a kind'
            elif c2 == 2:
                return 'Two pair'
            else:
                raise 'Error (1)'
        else:
            if c1 == 3:
                return 'Three of a kind'
            if c1 == 2:
                return 'Two pair'
            else:
                raise 'Error (2)'
    if uniq_cards == 4:
        return 'One pair'
    if uniq_cards == 5:
        return 'High card'

def compare(x1, x2):
    (h1, _), (h2, _) = x1, x2
    t1, t2 = types[get_type(h1)], types[get_type(h2)]
    if t1 < t2:
        return -1
    elif t1 > t2:
        return 1
    else:
        c1, c2 = [values[x] for x in h1], [values[x] for x in h2]
        for i in range(5):
            if c1[i] < c2[i]:
                return -1
            if c1[i] > c2[i]:
                return 1
        return 0

data = [(x.split()[0], int(x.split()[1])) for x in lines]
data.sort(key=cmp_to_key(compare))
s = 0
for i, (_, bid) in enumerate(data):
    s += (i + 1) * bid

print(s)
