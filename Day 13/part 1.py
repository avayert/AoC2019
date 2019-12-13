import collections
import enum

from program import Program

with open('input.txt', 'r', encoding='utf-8') as file:
    program = Program([int(instruction) for instruction in file.read().split(',')])


class Tile(enum.IntEnum):
    EMPTY = 0
    WALL = 1
    BLOCK = 2
    PADDLE = 3
    BALL = 4


coordinates = collections.defaultdict(int)
items = []

while True:
    if len(items) == 3:
        x, y, tile = items
        coordinates[x, y] = tile

        items = []

    output = program.run()

    if output is None:
        break

    items.append(output)

print(sum(tile == Tile.BLOCK for tile in coordinates.values()))
