WIDTH, HEIGHT = 25, 6

with open('input.txt', 'r', encoding='utf-8') as file:
    image_data = file.read()


def chunks(sequence, size):
    for index in range(0, len(sequence), size):
        yield sequence[index:index + size]


layers = [layer for layer in chunks(image_data, WIDTH * HEIGHT)]

# this blows
final_image = [next((pix for pix in position if pix != '2'), '2')  # I think you could do this better with a takewhile
               for position in zip(*layers)]                       # or something but I'm not smart enough

LUT = ' # '
for row in chunks(final_image, WIDTH):
    print(''.join(LUT[int(c)] for c in row))
