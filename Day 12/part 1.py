import itertools
import re
from dataclasses import dataclass

POSITION_PATTERN = re.compile('<x=(-?\d+), y=(-?\d+), z=(-?\d+)>')


@dataclass(frozen=True)
class Vector3:
    x: int = 0
    y: int = 0
    z: int = 0

    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __iter__(self):
        parts = (self.x, self.y, self.z)
        return iter(parts)


@dataclass
class Moon:
    position: Vector3
    velocity: Vector3 = Vector3(0, 0, 0)  # fine because Vector3 is frozen

    @property
    def energy(self):
        potential = sum(abs(part) for part in self.position)
        kinetic = sum(abs(part) for part in self.velocity)

        return potential * kinetic


moons = []

with open('input.txt', 'r', encoding='utf-8') as file:
    for line in file:
        match = POSITION_PATTERN.match(line)

        x, y, z = [int(match[n]) for n in (1, 2, 3)]
        position = Vector3(x, y, z)

        moons.append(Moon(position))


def cmp(a, b):
    """
    Hello three-way equality, my old arch enemy.
    """

    return (a > b) - (a < b)


for step in range(1000):
    for moon1, moon2 in itertools.product(moons, repeat=2):
        differences = [cmp(b, a) for a, b in zip(moon1.position, moon2.position)]
        moon1.velocity += Vector3(*differences)

    for moon in moons:
        moon.position += moon.velocity

print(sum(moon.energy for moon in moons))
