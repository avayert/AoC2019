# I was initially going to use line segments to do this but it was a hassle compared to using just a set
# of (x, y) coordinates. If the input was larger to the point where I would OOM I would definitely go back
# to the segment idea as it would require a lot less memory.

with open('input.txt', 'r', encoding='utf-8') as file:
    line1, line2 = [line.strip().split(',') for line in file]

# initially I had a dict of (x|y).__iadd__ but I remembered ints are immutable
# these represent (index, to_add) for position. I also thought of making position
# a dict with keys x and y but that just begged a dotdict so I decided to just
# go with this slightly more unreadable version
operations = {
    'R': (0,  1),
    'L': (0, -1),
    'U': (1,  1),
    'D': (1, -1)
}


def visit_line(line):
    position = [0, 0]

    for instruction in line:
        # I wish you could do instruction, *number without making number a tuple
        direction, number = instruction[0], int(instruction[1:])
        index, to_add = operations[direction]

        for _ in range(number):
            position[index] += to_add
            yield tuple(position)  # lists aren't hashable


seen = set(visit_line(line1))
intersections = ((x, y) for x, y in visit_line(line2) if (x, y) in seen)

print(min(abs(x) + abs(y) for x, y in intersections))
