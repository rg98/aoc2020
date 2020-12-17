#!/usr/bin/env python3.9

def get_dimension(space):
    xmin = 1_000_000
    xmax = -1_000_000
    ymin = 1_000_000
    ymax = -1_000_000
    zmin = 1_000_000
    zmax = -1_000_000
    for cube in space:
        xmin = min(xmin, cube[0])
        xmax = max(xmax, cube[0])
        ymin = min(ymin, cube[1])
        ymax = max(ymax, cube[1])
        zmin = min(zmin, cube[2])
        zmax = max(zmax, cube[2])
    return [[xmin, xmax], [ymin, ymax], [zmin, zmax]]

def is_active(x, y, z, space):
    if [x, y, z] in space:
        return True
    return False

def count_neighbours(x, y, z, space):
    neighbours = 0
    for d_z in range(z - 1, z + 2):
        for d_y in range(y - 1, y + 2):
            for d_x in range(x - 1, x + 2):
                if not (d_x == x and d_y == y and d_z == z):
                    if is_active(d_x, d_y, d_z, space):
                        neighbours += 1
    return neighbours

# Read config
space = []
dimension = [[0, 0], [0, 0], [0, 0]]
with open('in.txt', 'r') as fd:
    y = 0
    for row in fd:
        for x, c in enumerate(row[:-1]):
            if c == '#':
                space.append([x, y, 0])
        y += 1

dimension = get_dimension(space)
print("space:")
print(f"dimension: {dimension}")
print("content:")
for cube in space:
    print(cube)

for iteration in range(6):
    new_space = []
    # Expand dimension by one and count 
    for z in range(dimension[2][0] - 1, dimension[2][1] + 2):
        for y in range(dimension[1][0] - 1, dimension[1][1] + 2):
            for x in range(dimension[0][0] - 1, dimension[0][1] + 2):
                neighbours = count_neighbours(x, y, z, space)
                if is_active(x, y, z, space):
                    if neighbours == 2 or neighbours == 3:
                        new_space.append([x, y, z])
                else:
                    if neighbours == 3:
                        new_space.append([x, y, z])
    space = new_space
    dimension = get_dimension(space)

print(len(space))
