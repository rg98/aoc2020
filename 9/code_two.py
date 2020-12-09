#!/usr/bin/env python3.9
import copy
  
def search_n(num, numbers):
    begin = 0
    end = 2
    while sum(numbers[begin:end]) != num:
        if sum(numbers[begin:end]) < num:
            end += 1
        else:
            begin += 1
    return begin, end

# Read program
numbers = []
sum_of_nums = 144381670
with open('in.txt', 'r') as fd:
    for line in fd:
        num = int(line[:-1])
        if num >= sum_of_nums:
            break
        numbers.append(num)

l, r = search_n(sum_of_nums, numbers)
num_range = numbers[l:r]
num_range.sort()
print(num_range[0] + num_range[-1])
