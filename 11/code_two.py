#!/usr/bin/env python3.9
import copy

def count_neighbours(r, c, seats):
    occupied = 0
    # high left diagonal
    dist = 1
    while r - dist >= 0 and c - dist >= 0 and seats[r-dist][c-dist] == '.':
        dist += 1
    if r - dist >= 0 and c - dist >= 0 and seats[r-dist][c-dist] == '#':
        occupied += 1
            
    # high 
    dist = 1
    while r - dist >= 0 and seats[r-dist][c] == '.':
        dist += 1
    if r - dist >= 0 and seats[r-dist][c] == '#':
        occupied += 1

    # high right diagonal
    dist = 1
    while r - dist >= 0 and c + dist < len(seats[r]) and seats[r-dist][c+dist] == '.':
        dist += 1
    if r - dist >= 0 and c + dist < len(seats[r]) and seats[r-dist][c+dist] == '#':
        occupied += 1

    # left
    dist = 1
    while c - dist >= 0 and seats[r][c-dist] == '.':
        dist += 1
    if c - dist >= 0 and seats[r][c-dist] == '#':
        occupied += 1

    # right
    dist = 1
    while c + dist < len(seats[r]) and seats[r][c+dist] == '.':
        dist += 1
    if c + dist < len(seats[r]) and seats[r][c+dist] == '#':
        occupied += 1

    # low left diagonal
    dist = 1
    while r + dist < len(seats) and c - dist >= 0 and seats[r+dist][c-dist] == '.':
        dist += 1
    if r + dist < len(seats) and c - dist >= 0 and seats[r+dist][c-dist] == '#':
        occupied += 1

    # low
    dist = 1
    while r + dist < len(seats) and seats[r+dist][c] == '.':
        dist += 1
    if r + dist < len(seats) and seats[r+dist][c] == '#':
        occupied += 1

    # low right diagonal
    dist = 1
    while r + dist < len(seats) and c + dist < len(seats[r]) and seats[r+dist][c+dist] == '.':
        dist += 1
    if r + dist < len(seats) and c + dist < len(seats[r]) and seats[r+dist][c+dist] == '#':
        occupied += 1
    return occupied

def iterate_seats(seats):
    new_seats = copy.deepcopy(seats)
    for r, row in enumerate(seats):
        for c, col in enumerate(row):
            if col in '#L':
                cnt = count_neighbours(r, c, seats)
                if col == 'L' and cnt == 0:
                    new_seats[r][c] = '#'
                elif col == '#' and cnt >= 5:
                    new_seats[r][c] = 'L'
    return new_seats

# Read layout
seats = []
with open('in.txt', 'r') as fd:
    for line in fd:
        seats.append([])
        for c in line[:-1]:
            seats[-1].append(c)

old_seats = []
while seats != old_seats:
    old_seats = copy.deepcopy(seats)
    seats = iterate_seats(old_seats)
    #for row in seats:
    #    print(row)
    #print()

cnt = 0
for row in seats:
    for col in row:
        if col == '#':
            cnt += 1
print(f"{cnt} seats are occupied")
