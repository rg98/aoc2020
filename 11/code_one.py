#!/usr/bin/env python3.9
import copy

def count_neighbours(r, c, seats):
    occupied = 0
    if r > 0 and c > 0 and seats[r-1][c-1] == '#':
        occupied += 1
    if r > 0 and seats[r-1][c] == '#':
        occupied += 1
    if r > 0 and c < len(seats[r]) - 1 and seats[r-1][c+1] == '#':
        occupied += 1
    if c > 0 and seats[r][c-1] == '#':
        occupied += 1
    if c < len(seats[r]) - 1 and seats[r][c+1] == '#':
        occupied += 1
    if r < len(seats) - 1 and c > 0 and seats[r+1][c-1] == '#':
        occupied += 1
    if r < len(seats) - 1 and seats[r+1][c] == '#':
        occupied += 1
    if r < len(seats) - 1 and c < len(seats[r]) - 1 and seats[r+1][c+1] == '#':
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
                elif col == '#' and cnt >= 4:
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
