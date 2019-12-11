import collections

from program import Program

directions = collections.deque([
    (0, 1),  # up
    (1, 0),  # right
    (0, -1),  # down
    (-1, 0),  # left
])

coordinates = collections.defaultdict(int)

with open('input.txt', 'r', encoding='utf-8') as file:
    program = Program([int(instruction) for instruction in file.read().split(',')])

x, y = 0, 0

while True:
    current_colour = coordinates[(x, y)]

    paint = program.run(current_colour)
    direction = program.run(current_colour)

    if None in (paint, direction):
        break

    if direction == 0:
        directions.rotate(1)
    else:
        directions.rotate(-1)

    coordinates[(x, y)] = paint

    a, b = directions[0]
    x += a
    y += b

print(len(coordinates))
