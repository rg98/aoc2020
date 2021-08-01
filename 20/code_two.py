#!/usr/bin/env python3.9

def flip_tile(key, tiles, edges):
    new_tile = []
    tile = tiles[key]
    for row in tile:
        rrow = ""
        for c in row:
            rrow = c + rrow
        new_tile.append(rrow)
    tiles[key] = new_tile
    edges[key] = get_tile_edges(new_tile)

def get_tile_edges(tile):
    """get_tile_edges returns an array containing the four edges 
       encoded as integer where '#' -> 1 and '.' -> 0 encode
       the edges in clockwise fasion starting in top left corner
       having least/most significant bit. Every edge encodes 
       therefore two 10bit integers"""
    edges = {'self':[], 'cmp':[]}
    # Encode top edge
    bits = "" 
    for c in tile[0]:
        if c == '#':
            bits += '1'
        elif c == '.':
            bits += '0'
        else:
            raise RuntimeError(f"unknown tile content {c}")
    edges['self'].append(int(bits, base=2))
    edges['cmp'].append(int(bits[::-1], base=2))
    # Encode right edge
    bits = "" 
    for l in tile:
        c = l[-1]
        if c == '#':
            bits += '1'
        elif c == '.':
            bits += '0'
        else:
            raise RuntimeError(f"unknown tile content {c}")
    edges['self'].append(int(bits, base=2))
    edges['cmp'].append(int(bits[::-1], base=2))
    # Encode bottom edge 
    bits = "" 
    for c in reversed(tile[-1]):
        if c == '#':
            bits += '1'
        elif c == '.':
            bits += '0'
        else:
            raise RuntimeError(f"unknown tile content {c}")
    edges['self'].append(int(bits, base=2))
    edges['cmp'].append(int(bits[::-1], base=2))
    # Encode left edge
    bits = "" 
    for l in reversed(tile):
        c = l[0]
        if c == '#':
            bits += '1'
        elif c == '.':
            bits += '0'
        else:
            raise RuntimeError(f"unknown tile content {c}")
    edges['self'].append(int(bits, base=2))
    edges['cmp'].append(int(bits[::-1], base=2))
    return edges

def rotate_tile(tile):
    new_tile = []
    for y in range(len(tile[0])):
        row = ""
        for x in range(len(tile[0])):
            row += tile[len(tile[0])-x-1][y]
        new_tile.append(row)
    return new_tile

tiles = {}
# Read tiles
tile_nr = None
tile = []
with open('in.txt', 'r') as fd:
    for line in fd:
        if line.startswith('Tile '):
            tile_nr = int(line[5:9])
            continue
        if len(line) == 1:
            tiles[tile_nr] = tile
            tile = []
            tile_nr = None
            continue
        tile.append(line[:-1])
if len(tile) > 0:
    tiles[tile_nr] = tile

#print(tiles)

tile_edges = {}
for key, tile in tiles.items():
    tile_edges[key] = get_tile_edges(tile)

#for key, edge in tile_edges.items():
#    print(key, edge)

# Find four tiles where two edges does not fit any other
corners = []
tile_keys = list(tiles.keys())
#print(tile_keys)
for i in range(len(tile_keys)):
    matches = 0
    for j in range(len(tile_keys)):
        if i == j:
            continue
        for k in range(4):
            if tile_edges[tile_keys[i]]['self'][k] in tile_edges[tile_keys[j]]['cmp']:
                matches += 1
            elif tile_edges[tile_keys[i]]['self'][k] in tile_edges[tile_keys[j]]['self']:
                # Flip tile
                flip_tile(tile_keys[i], tiles, tile_edges)
                matches += 1
    if matches == 2:
        #print(f"key: {tile_keys[i]}: {matches} matches")
        corners.append(tile_keys[i])
    #else:
    #    print(f"key: {tile_keys[i]}: {matches} matches")

#print(corners)

for r in tiles[corners[0]]:
    print(r)
print()
for r in rotate_tile(tiles[corners[0]]):
    print(r)
print(corners[0]*corners[1]*corners[2]*corners[3])

