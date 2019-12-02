import itertools

with open('input.txt', 'r', encoding='utf-8') as file:
    original_instructions = [int(val) for val in file.read().split(',')]


def chunks(sequence, size):
    for index in range(0, len(sequence), size):
        yield sequence[index:index + size]


for noun, verb in itertools.product(range(100), range(100)):
    instructions = original_instructions.copy()

    instructions[1] = noun
    instructions[2] = verb

    for op_code, i1, i2, output in chunks(instructions, 4):
        if op_code == 99:
            break

        operand1, operand2 = instructions[i1], instructions[i2]

        instructions[output] = (operand1 + operand2) if op_code == 1 else (operand1 * operand2)

    if instructions[0] == 19690720:
        print(100 * noun + verb)
        break
