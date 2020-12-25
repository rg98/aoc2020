#!/usr/bin/env python3.9

from collections import deque

def move(current, cups):
    # Get current cup
    current_cup = cups[current]
    # Remove three cups behind current
    left = (current+1) % len(cups)
    right = (current+3) % len(cups)
    if left > right:
        keep = list(cups)[left:]
        keep.extend(list(cups)[:right+1])
    else:
        keep = list(cups)[left:right+1]
    # print('keep:', keep, 'left:', left, 'right:', right)
    for cup in keep:
        cups.remove(cup)
    # Select destination (current - 1 or next lower if not available 
    # begin from the highest cup)
    dest = None
    try:
        dest = cups.index(current_cup-1)
    except ValueError:
        available = list(reversed(sorted(list(filter(lambda x: x <= current_cup-1, cups)))))
        # print('lower available:', available)
        if len(available) > 0:
            dest = available[0]
        else:
            available = list(reversed(sorted(list(filter(lambda x: x > current_cup, cups)))))
            # print('higher available:', available)
            if len(available) > 0:
                dest = available[0]
        dest = cups.index(dest) 
    for cup in keep:
        dest += 1
        dest = dest % len(cups)
        cups.insert(dest, cup)
    while cups[current] != current_cup:
        cups.rotate(-1)

# Read decks
cups = deque()
with open('in.txt', 'r') as fd:
    line = fd.readline()
    for cup in line[:-1]:
        cups.append(int(cup))

current = 0
for _ in range(100):
    # print('before:', cups)
    move(current, cups)
    # print('after :',cups)
    current = (current + 1) % len(cups)
    # print()

while cups[0] != 1:
    cups.rotate()

print(list(cups)[1:])
