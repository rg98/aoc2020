#!/usr/bin/env python3.9
import copy

def last_time(n, numbers):
    _first = None
    _next = None
    for i, num in enumerate(reversed(numbers)):
        if num == n:
            if _first == None:
                _first = i
            else:
                _next = i
                return (_first, _next)

    return (0, None)

# Read instructions
with open('in2.txt', 'r') as fd:
    numbers = fd.read()[:-1].split(',')

numbers = list(map(lambda x: int(x), numbers))

l = len(numbers)
for i in range(l, 20):
    idx = last_time(numbers[-1], numbers)
    if idx[1] == None:
        numbers.append(idx[0])
    else:
        numbers.append(idx[1] - idx[0])

print(f"numbers: {numbers}")
