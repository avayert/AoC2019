import enum
from itertools import cycle, permutations


class Mode(enum.IntEnum):
    POSITION = 0
    IMMEDIATE = 1


def nth_bit(number, n):
    return (number >> n) & 1


class Program:
    PARAMETER_COUNT = {
        1: 3,
        2: 3,
        3: 1,
        4: 1,
        5: 2,
        6: 2,
        7: 3,
        8: 3,
    }

    def __init__(self, tape):
        self.tape = tape
        self.cursor = 0

    def read_parameter(self, position, mode):
        value = self.tape[position + 1]

        if mode == Mode.POSITION:
            return self.tape[value]

        return value

    def run(self, *inputs):
        inputs = iter(inputs)

        while True:
            instruction = self.tape[self.cursor]

            if instruction == 99:
                return

            modes, opcode = instruction // 100, instruction % 100
            modes = [nth_bit(modes, n) for n in range(3)]

            # this is meh compared to my other implementation, but it
            # avoids the hacks dealing with immediate and position modes.
            n_params = self.PARAMETER_COUNT[opcode]

            parameters = [self.read_parameter(self.cursor + n, mode)
                          for n, mode in zip(range(n_params), modes)]

            output = self.tape[self.cursor + n_params]

            self.cursor += n_params + 1

            # bleh...
            # I really want to refactor this but I also want it to be debuggable
            # I'll do it later.
            if opcode == 1:
                a, b, _, = parameters
                self.tape[output] = a + b

            elif opcode == 2:
                a, b, _, = parameters
                self.tape[output] = a * b

            elif opcode == 3:
                self.tape[output] = next(inputs)

            elif opcode == 4:
                return parameters[0]

            elif opcode == 5:
                value, location = parameters
                if value:
                    self.cursor = location

            elif opcode == 6:
                value, location = parameters
                if not value:
                    self.cursor = location

            elif opcode == 7:
                a, b, _ = instruction
                self.tape[output] = a < b

            elif opcode == 8:
                a, b, _ = instruction
                self.tape[output] = a == b


with open('input.txt', 'r', encoding='utf-8') as file:
    tape = [int(instruction) for instruction in file.read().split(',')]


def run_loops(permutation):
    amplifiers = [Program(tape.copy()) for _ in permutation]
    previous = 0

    for digit, amp in zip(permutation, amplifiers):
        output = amp.run(digit, previous)

        if output is None:
            break

        previous = output

    for amp in cycle(amplifiers):
        output = amp.run(previous)

        if output is None:
            break

        previous = output

    return previous


print(max(run_loops(permutation) for permutation in permutations(range(5, 10))))
