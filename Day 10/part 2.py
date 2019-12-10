import math

coords = []

with open('input.txt', 'r', encoding='utf-8') as file:
    for y, line in enumerate(file):
        for x, char in enumerate(line):
            if char != '#':
                continue

            coords.append((x, y))

LASER_X, LASER_Y = LASER_POSITION = 13, 17  # got from day 1

coords.remove(LASER_POSITION)


# I tried to use the coprime solution for part 2 too but I couldn't get it working
# so instead I will use the unit circle!
#
# We can all remember from trigonometry class that on an unit circle the angle theta
# had a distance on the x-axis defined by the cosine of the angle, and on the y-axis
# defined by the sine of the angle. But since we already have these distances, and want
# the angle instead, we can use the fact that tan(x) = sin(x) / cos(x)
# (this is also the reason for the famous TOA in the SOHCAHTOA rule, since the adjacent
#  side is the distance on the x-axis [sine] and the opposite side is the distance on
#  the y-axis [cosine])
#
# I had some issues with doing tan(x / y) but as it turns out there's the function atan2
# which does basically that but is better. I don't know why I'm not smart enough :)

def distance(point):
    # we don't actually need the real distance so the sqrt is irrelevant
    return sum((b - a) ** 2 for a, b in zip(point, LASER_POSITION))


def angle(point):
    x, y = point
    return math.atan2(LASER_Y - y, LASER_X - x) + math.pi


zapped = sorted(coords, key=lambda point: (angle(point), distance(point)), reverse=True)
print(zapped[200])
