#!/usr/bin/env python3

occupied = []

def decode(seat):
    if len(seat) != 10:
        raise RuntimeError('Seat always should have 10 bits')
    seat_id = 0
    for c in seat:
        seat_id = (~ord(c) & 4) >> 2 | (seat_id << 1)
    return seat_id

with open('in.txt') as fd:
    for seat in fd:
        occupied.append(decode(seat[:-1]))

print(f'highest ID: {max(occupied)}')
