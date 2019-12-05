import enum
import functools
import inspect
import operator
import sys

with open('input.txt', 'r', encoding='utf-8') as file:
    tape = [int(instruction) for instruction in file.read().split(',')]


class Mode(enum.IntEnum):
    POSITION = 0
    IMMEDIATE = 1


def writing(operation):
    def caller(*args):
        return operation(*args)

    caller.output = True
    caller.__signature__ = inspect.signature(operation)

    return caller


handlers = {
    1: writing(operator.add),
    2: writing(operator.mul),
    3: writing(functools.partial(input, 'Input: ')),
    4: lambda value_at_index: print(value_at_index),
    99: lambda: sys.exit()  # need to wrap in a lambda because sys.exit doesn't have a signature
}


def nth_bit(number, n):
    return (number >> n) & 1


cursor = 0

while True:
    instruction = tape[cursor]
    cursor += 1

    modes, opcode = instruction // 100, instruction % 100

    handler = handlers[opcode]
    n_params = len(inspect.signature(handler).parameters)

    parameters = []
    for n in range(n_params):
        value = tape[cursor]
        mode = nth_bit(modes, n)

        cursor += 1

        if mode == Mode.IMMEDIATE:
            parameters.append(value)
        elif mode == Mode.POSITION:
            parameters.append(tape[value])

    ret = handler(*parameters)

    if ret is not None:
        ret = int(ret)

    if getattr(handler, 'output', False):
        output_index = tape[cursor]
        cursor += 1

        tape[output_index] = ret
