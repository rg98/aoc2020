#!/usr/bin/env python3.9
##############################################################################
# tiles
# ---------------------------------------------------------------------------
##############################################################################

class Tile:
    def __init__(self):
        self._x = 0
        self._y = 0
        self._id = 0
        self._state = 0

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
with open('in2.txt', 'r') as fd:
    for s_tile in fd:
        flip_tile(s_tile[:-1], tiles)

print(len(list(filter(lambda x: x.state() == 1, tiles.values()))))
