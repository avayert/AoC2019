import collections
import enum


class Mode(enum.IntEnum):
    POSITION = 0
    IMMEDIATE = 1
    RELATIVE = 2


def nth_digit(number, n):
    return number // 10 ** n % 10


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
        9: 1,
    }

    def __init__(self, tape):
        self.tape = collections.defaultdict(int)
        self.tape.update({index: value for index, value in enumerate(tape)})

        self.cursor = 0
        self.offset = 0

    def read_parameter(self, position, mode):
        value = self.tape[position + 1]

        if mode == Mode.POSITION:
            return self.tape[value]

        if mode == Mode.RELATIVE:
            return self.tape[value + self.offset]

        return value

    def run(self, *inputs):
        inputs = iter(inputs)

        while True:
            instruction = self.tape[self.cursor]

            if instruction == 99:
                return

            modes, opcode = instruction // 100, instruction % 100
            modes = [nth_digit(modes, n) for n in range(3)]

            # this is meh compared to my other implementation, but it
            # avoids the hacks dealing with immediate and position modes.
            n_params = self.PARAMETER_COUNT[opcode]

            parameters = [self.read_parameter(self.cursor + n, mode)
                          for n, mode in zip(range(n_params), modes)]

            parameters = [int(x) for x in parameters]

            output = self.tape[self.cursor + n_params]

            if modes[n_params - 1] == Mode.RELATIVE:
                output += self.offset

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
                a, b, _ = parameters
                self.tape[output] = a < b

            elif opcode == 8:
                a, b, _ = parameters
                self.tape[output] = a == b

            elif opcode == 9:
                self.offset += parameters[0]


with open('input.txt', 'r', encoding='utf-8') as file:
    tape = [int(instruction) for instruction in file.read().split(',')]

computer = Program(tape)

while True:
    ret = computer.run(1)

    if ret is None:
        break

    output = ret

print(output)
