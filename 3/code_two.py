#!/usr/bin/env python3.9

def walk_maze(algorithm, maze):
    trees = 0
    right, down = algorithm
    pos = (0, 0)
    for _ in range(int(len(maze) / down) - 1):
        pos = (pos[0] + right, pos[1] + down)
        if maze[pos[1]][pos[0] % len(maze[0])] == '#':
            trees += 1
    return trees

maze = []
with open('in.txt', 'r') as fd:
    for line in fd:
        maze.append(line[:-1])

algorithms = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
trees = []
for algorithm in algorithms:
    trees.append(walk_maze(algorithm, maze))
    print(f'Found {trees[-1]} trees for {algorithm}.')

result = 1
for t in trees:
    result *= t
print(f'result: {result}')
