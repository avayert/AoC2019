from collections import Counter

WIDTH, HEIGHT = 25, 6

with open('input.txt', 'r', encoding='utf-8') as file:
    image_data = file.read()


def chunks(sequence, size):
    for index in range(0, len(sequence), size):
        yield sequence[index:index + size]


layers = [Counter(layer) for layer in chunks(image_data, WIDTH * HEIGHT)]
layer = min(layers, key=lambda layer: layer['0'])

print(layer['1'] * layer['2'])
