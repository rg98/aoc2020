#!/usr/bin/env python3.9
import numpy as np

def is_active(x, y, z, w, space):
    if space[w, z,y,x] == 1:
        return True
    return False

def count_neighbours(x, y, z, w, space):
    mask = np.full(space.shape, False)
    mask[w-1 if w > 0 else 0:w+2,z-1 if z > 0 else 0:z+2,y-1 if y > 0 else 0:y+2,x-1 if x > 0 else 0:x+2] = True
    neighbours = sum(space[mask])
    if is_active(x, y, z, w, space):
        neighbours -= 1
    return neighbours

# Read config
space = []
with open('in.txt', 'r') as fd:
    for row in fd:
        space.append([])
        for x, c in enumerate(row[:-1]):
            if c == '#':
                space[-1].append(1)
            else:
                space[-1].append(0)

np_space = np.array(space)
np_space = np_space.reshape((1, 1, np_space.shape[0], np_space.shape[1]))
dimension = np_space.shape
print("space:")
print(f"dimension: {dimension}")
print("content:")
print(np_space)

for iteration in range(6):
    new_space = np.zeros((dimension[0]+2, dimension[1]+2, dimension[2]+2, dimension[3]+2), dtype=int)
    ext_space = np.zeros(new_space.shape, dtype=int)
    ext_space[1:-1,1:-1,1:-1,1:-1] = np_space
    # Expand dimension by one and count 
    for w in range(dimension[0] + 2):
        for z in range(dimension[1] + 2):
            for y in range(dimension[2] + 2):
                for x in range(dimension[3] + 2):
                    neighbours = count_neighbours(x, y, z, w, ext_space)
                    if is_active(x, y, z,  w,ext_space):
                        if neighbours == 2 or neighbours == 3:
                            new_space[w,z,y,x] = 1
                    else:
                        if neighbours == 3:
                            new_space[w,z,y,x] = 1
    np_space = new_space.copy()
    dimension = np_space.shape

print(sum(sum(sum(sum(np_space)))))
