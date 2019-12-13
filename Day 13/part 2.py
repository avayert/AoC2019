import enum

from program import Program

with open('input.txt', 'r', encoding='utf-8') as file:
    tape = [int(instruction) for instruction in file.read().split(',')]
    tape[0] = 2
    program = Program(tape)


class Tile(enum.IntEnum):
    EMPTY = 0
    WALL = 1
    BLOCK = 2
    PADDLE = 3
    BALL = 4


score = None
paddle_position = None

items = []
score = 0
position = 0

inputs = [0]

while True:
    output = program.run(*inputs)
    inputs = [0]

    if output is None:
        break

    items.append(output)

    # maybe I should implement this "chunk" reading into the Program class...
    if len(items) != 3:
        continue

    x, y, value = items
    items = []

    if (x, y) == (-1, 0):
        score = value
        continue

    if value == Tile.PADDLE:
        position = x

    if value == Tile.BALL:
        diff = x - position
        diff = max(min(diff, 1), -1)

        inputs = [diff]

    items = []

print(score)
