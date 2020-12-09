#!/usr/bin/env python3.9
import copy
  
def check_sum(num, numbers):
    nums = copy.deepcopy(numbers)
    nums.sort()
    left = 0
    right = len(nums) - 1
    while left != right and nums[left] + nums[right] != num:
        if nums[left] + nums[right] > num:
            right -= 1
        else:
            left += 1
    return left != right

# Read program
numbers = []
with open('in.txt', 'r') as fd:
    for line in fd:
        num = int(line[:-1])
        if len(numbers) == 25:
            if not check_sum(num, numbers):
                print(num)
                break
            numbers.pop(0)
        numbers.append(num)

