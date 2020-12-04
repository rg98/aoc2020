#!/usr/bin/env python3.9

def check_password(low, high, char, password):
    count = password.count(char)
    # print(f'{int(low)} <= {count} <= {int(high)} for {char} in {password}?')
    if int(low) <= count and count <= int(high):
        return 1
    return 0

valid_passwords = 0
with open('in.txt', 'r') as fd:
    for line in fd:
        line = line[:-1]
        n_range, char, password = line.split(' ')
        low, high = n_range.split('-')
        char = char[:-1]
        valid_passwords += check_password(low, high, char, password)

print(f'valid_passwords: {valid_passwords}')
