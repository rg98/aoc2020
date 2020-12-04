#!/usr/bin/env python3.9

def walk_maze(algorithm, maze):
    trees = 0
    right, down = algorithm
    pos = (0, 0)
    for _ in range(len(maze) - 1):
        pos = (pos[0] + right, pos[1] + down)
        if maze[pos[1]][pos[0] % len(maze[0])] == '#':
            trees += 1
    return trees

maze = []
with open('in.txt', 'r') as fd:
    for line in fd:
        maze.append(line[:-1])

algorithm = [3, 1]
print(f'Found {walk_maze(algorithm, maze)} trees')
