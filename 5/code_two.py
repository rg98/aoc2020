#!/usr/bin/env python3

occupied = []

def decode(seat):
    if len(seat) != 10:
        raise RuntimeError('Seat always should have 10 bits')
    seat = seat.replace('F', '0').replace('B','1').replace('R', '1').replace('L', '0')
    return int(seat, base=2)

with open('in.txt') as fd:
    for seat in fd:
        occupied.append(decode(seat[:-1]))

occupied = sorted(occupied)
last_seat = occupied[0]
for seat in occupied[1:]:
    if seat > last_seat + 1:
        print(f'My Seat ID: {last_seat+1}')
        break
    last_seat = seat

