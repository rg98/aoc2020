#!/usr/bin/env python3.9

# Read numbers
numbers = []
with open('in.txt', 'r') as fd:
    for num in fd:
        num = num[:-1]
        if len(num) > 0:
            numbers.append(int(num))

# Search pair adding to 2020
found = False
for i in range(0, len(numbers)-2):
    for j in range(i+1, len(numbers)-1):
        for k in range(j+1, len(numbers)):
            if numbers[i] + numbers[j] + numbers[k] == 2020:
                found = True
                print(f'result: {numbers[i]} * {numbers[j]} * {numbers[k]} = {numbers[i] * numbers[j] * numbers[k]}')
                break

if not found:
    print('nothing found')
