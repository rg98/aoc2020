#!/usr/bin/env python3.9
import copy
  
def count_combinations(numbers):
    numbers.append(0)
    numbers.sort()
    numbers.append(numbers[-1]+3)

    # Cound numbers of consecutive differences of one
    cc_count = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    cc_factor = {1: 1, 2: 2, 3: 4, 4: 7, 5: 12}
    count = 0
    _n = numbers[0]
    threes = 0
    for n in numbers[1:]:
        if n - _n == 1:
            count += 1
        else:
            if n - _n == 3:
                threes += 1
            if count > 0:
                cc_count[count] += 1
            count = 0
        _n = n
    combinations = 1
    for key, value in cc_count.items():
        combinations *= cc_factor[key] ** value
    return combinations

# Read program
numbers = []
with open('in.txt', 'r') as fd:
    for line in fd:
        num = int(line[:-1])
        numbers.append(num)

combinations = count_combinations(numbers)
print(combinations)
