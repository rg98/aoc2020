#!/usr/bin/env python3.9
##############################################################################
# tiles
# ---------------------------------------------------------------------------
#           . . . . . . . . .   x_min,x_max: -8,8
#            . . . . . . . .    y_min,y_max: -4,4
#           . . . . . . . . .
#            . . . . . . . .
#           . . . . 0 . . . .
#            . . . . . . . .
#           . . . . . . . . .
#            . . . . . . . .
#           . . . . . . . . .
#
# reference tile: 0
# 
##############################################################################

import copy

def gen_id(x, y):
    return f"{x},{y}"

class Tile:
    def __init__(self, x = 0, y = 0, state = 0):
        self._x = x
        self._y = y
        self._id = gen_id(x, y)
        self._state = state

    def east(self):
        self._x += 2
            
    def north_east(self):
        self._x += 1
        self._y += 1
            
    def south_east(self):
        self._x += 1
        self._y -= 1
            
    def west(self):
        self._x -= 2
            
    def north_west(self):
        self._x -= 1
        self._y += 1
            
    def south_west(self):
        self._x -= 1
        self._y -= 1
            
    def flip_state(self):
        self._state = (self._state + 1) % 2
        return self._state

    def get_id(self):
        return f"{self._x},{self._y}"

    def pos(self):
        return self._x, self._y

    def state(self):
        return self._state

def count_adjacents(tile, tiles):
    n = 0
    x, y = tile.pos()
    adj_pos = [(x-2, y), (x-1, y+1), (x+1, y+1), (x+2, y), (x+1, y-1), (x-1, y-1)]
    for x, y in adj_pos:
        a_id = gen_id(x, y)
        if a_id in tiles.keys() and tiles[a_id].state() == 1:
            n += 1
    return n

def flip_tile(tile, tiles):
    t = Tile()
    while len(tile) > 0:
        if tile.startswith('e'):
            tile = tile[1:]
            t.east()
        elif tile.startswith('se'):
            tile = tile[2:]
            t.south_east()
        elif tile.startswith('sw'):
            tile = tile[2:]
            t.south_west()
        elif tile.startswith('w'):
            tile = tile[1:]
            t.west()
        elif tile.startswith('nw'):
            tile = tile[2:]
            t.north_west()
        elif tile.startswith('ne'):
            tile = tile[2:]
            t.north_east()
        else:
            raise RuntimeError(f"Unknown direction: '{tile[0:2]}'")
    if t.get_id() in tiles.keys():
        tiles[t.get_id()].flip_state()
    else:
        t.flip_state()
        tiles[t.get_id()] = t
                

# Read tiles
tiles = {}
with open('in.txt', 'r') as fd:
    for s_tile in fd:
        flip_tile(s_tile[:-1], tiles)

print(f"0: {len(list(filter(lambda x: x.state() == 1, tiles.values())))}")
for i in range(1, 101):
    x_pos = list(map(lambda x: x.pos()[0], filter(lambda x: x.state() == 1, tiles.values())))
    x_min = min(x_pos) - min(x_pos) % 2
    x_max = max(x_pos) + max(x_pos) % 2
    y_pos = list(map(lambda y: y.pos()[1], filter(lambda y: y.state() == 1, tiles.values())))
    y_min = min(y_pos)
    y_max = max(y_pos)
    # print(f"{i}: ({x_min},{y_min} - {x_max},{y_max}) {len(list(filter(lambda x: x.state() == 1, tiles.values())))}")
    new_tiles = {}
    # for x,y in list(map(lambda x: x.pos(), filter(lambda x: x.state() == 1, tiles.values()))):
    #     print(x,y)
    for x in range(x_min-2, x_max+4, 2):
        for y in range(y_min-1, y_max+2):
            dx = 1 if (y % 2) == 1 else 0
            t_id = gen_id(x+dx, y)
            if t_id not in tiles.keys():
                tiles[t_id] = Tile(x+dx, y)
            n = count_adjacents(tiles[t_id], tiles)
            # print(f"{t_id}: {n} - {tiles[t_id].state()}")
            if tiles[t_id].state() == 1:
                if (n == 0 or n > 2):
                    new_tiles[t_id] = Tile(x+dx, y, 0)
                else:
                    new_tiles[t_id] = Tile(x+dx, y, 1)
            elif tiles[t_id].state() == 0:
                if n == 2:
                    new_tiles[t_id] = Tile(x+dx, y, 1)
                else:
                    new_tiles[t_id] = Tile(x+dx, y, 0)
    tiles = new_tiles.copy()
    print(f"{i}: ({x_min},{y_min} - {x_max},{y_max}) {len(list(filter(lambda x: x.state() == 1, tiles.values())))}")
        
print(len(tiles))
print(len(list(filter(lambda x: x.state() == 1, tiles.values()))))

