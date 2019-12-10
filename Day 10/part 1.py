import collections
from itertools import product
from math import gcd

coords = collections.defaultdict(int)

with open('input.txt', 'r', encoding='utf-8') as file:
    for y, line in enumerate(file):
        for x, char in enumerate(line):
            if char != '#':
                continue

            coords[(x, y)] = 1

distance = max(x, y)

coprimes = [(a, b) for a, b in product(range(1, distance), repeat=2) if gcd(a, b) == 1]


def seen_at_gradient(x, y, a, b):
    while True:
        x += a
        y += b

        if abs(x) > distance or abs(y) > distance:
            break

        if coords[(x, y)]:
            return True

    return False


results = {}

for x, y in product(range(distance), repeat=2):
    total = 0
    for m1, m2 in product((-1, 1), repeat=2):
        for n1, n2 in coprimes:
            total += seen_at_gradient(x, y, n1 * m1, n2 * m2)

    # can't put these in the coprimes list because 0 * n = 0
    total += seen_at_gradient(x, y,  0,  1)
    total += seen_at_gradient(x, y,  0, -1)
    total += seen_at_gradient(x, y,  1,  0)
    total += seen_at_gradient(x, y, -1,  0)

    results[(x, y)] = total

print(max(results.values()))
