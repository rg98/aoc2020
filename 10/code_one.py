#!/usr/bin/env python3.9
import copy
  
def count_diff(numbers):
    numbers.append(0)
    numbers.sort()
    numbers.append(numbers[-1]+3)
    differences = {1: 0, 3: 0}
    _n = numbers[0]
    for n in numbers[1:]:
        differences[n-_n] += 1
        _n = n
    return differences

# Read program
numbers = []
with open('in.txt', 'r') as fd:
    for line in fd:
        num = int(line[:-1])
        numbers.append(num)

diffs = count_diff(numbers)
print(diffs[1] * diffs[3])
