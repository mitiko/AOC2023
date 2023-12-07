#!/usr/bin/python3

from functools import cmp_to_key

read_sample = 0
filename = ["input.txt", "sample.txt"][read_sample]
lines = open(filename).read().split('\n')

values = {
    'A': 12,
    'K': 11,
    'Q': 10,
    'T': 9,
    '9': 8,
    '8': 7,
    '7': 6,
    '6': 5,
    '5': 4,
    '4': 3,
    '3': 2,
    '2': 1,
    'J': 0,
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

faces = [k for k,v in values.items() if k != 'J']
mm = {}
def get_type(hand):
    if hand in mm:
        return mm[hand]
    # try all combinations of jokers
    cards = list(hand)
    cards.sort(key=lambda c: values[c])
    joker_count = cards.count('J')
    if joker_count == 4 or joker_count == 5:
        return 'Five of a kind'
    # if joker_count == 3:
    #     if len(set(cards)) == 2:
    #         return 'Five of a kind'
    #     else:
    #         return 'Four of a kind'
    t = get_orig_type(cards)
    if joker_count == 0:
        return t
    for j1 in faces:
        cards[0] = j1
        if cards[1] != 'J':
            t2 = get_orig_type(cards)
            t = t2 if types[t2] > types[t] else t
            cards[0] = 'J'
            continue
        for j2 in faces:
            cards[1] = j2
            if cards[2] != 'J':
                t2 = get_orig_type(cards)
                t = t2 if types[t2] > types[t] else t
                cards[1] = 'J'
                continue
            for j3 in faces:
                cards[2] = j3
                assert cards[3] != 'J'
                t2 = get_orig_type(cards)
                t = t2 if types[t2] > types[t] else t
                cards[2] = 'J'
            cards[1] = 'J'
        cards[0] = 'J'
    mm[hand] = t
    return t

def get_orig_type(cards):
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
# more than 251161833
