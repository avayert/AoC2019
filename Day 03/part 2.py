# This is basically a slightly modified version of the previous one. I guess I could have put them into one
# file that prints both solutions. Oh well! Read the comments in the other file for better explanations.

with open('input.txt', 'r', encoding='utf-8') as file:
    line1, line2 = [line.strip().split(',') for line in file]

operations = {
    'R': (0, 1),
    'L': (0, -1),
    'U': (1, 1),
    'D': (1, -1)
}


def visit_line(line):
    position = [0, 0]
    steps = 0

    for instruction in line:
        # I wish you could do instruction, *number without making number a tuple
        direction, number = instruction[0], int(instruction[1:])
        index, to_add = operations[direction]

        for _ in range(number):
            position[index] += to_add
            steps += 1
            yield tuple(position), steps  # lists aren't hashable


# this is awful
seen = {(x, y): steps for (x, y), steps in visit_line(line1)}

intersections = {(x, y): steps for (x, y), steps in visit_line(line2) if (x, y) in seen}

print(min(steps + seen[intersection] for intersection, steps in intersections.items()))
