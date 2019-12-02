with open('input.txt', 'r', encoding='utf-8') as file:
    instructions = [int(val) for val in file.read().split(',')]

instructions[1] = 12
instructions[2] = 2


def chunks(sequence, size):
    for index in range(0, len(sequence), size):
        yield sequence[index:index + size]


for op_code, i1, i2, output in chunks(instructions, 4):
    if op_code == 99:
        break

    operand1, operand2 = instructions[i1], instructions[i2]

    instructions[output] = (operand1 + operand2) if op_code == 1 else (operand1 * operand2)

print(instructions[0])
