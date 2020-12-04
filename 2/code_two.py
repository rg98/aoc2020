#!/usr/bin/env python3.9

def check_password(first, second, char, password):
    check_one = 0
    check_two = 0
    if password[int(first)-1] == char:
        check_one = 1
    if password[int(second)-1] == char:
        check_two = 1
    if (check_one ^ check_two) != 0:
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
