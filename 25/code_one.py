#!/usr/bin/env python3.9
##############################################################################
# door key
# ---------------------------------------------------------------------------
##############################################################################

def encrypt(key, n):
    value = 1
    const_divisor = 20201227
    for _ in range(n):
        value = (value * key) % const_divisor
    return value

def determine_loop_size(n, key):
    value = 1
    loops = 0
    const_divisor = 20201227
    while value != key:
        value = (value * n) % const_divisor
        loops += 1
    return loops

# Read public keys
door_pk = None
card_pk = None

with open('in.txt', 'r') as fd:
    door_pk = int(fd.readline()[:-1])
    card_pk = int(fd.readline()[:-1])

print(encrypt(card_pk, determine_loop_size(7, door_pk)))
