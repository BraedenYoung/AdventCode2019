from enum import Enum

from input_decorator import has_input


SAMPLE = '''
1,9,10,3,2,3,11,0,99,30,40,50
'''

REQUIRED = 19690720


class OpCodes(Enum):
    ADD = 1
    MULTI = 2
    TERM = 99


FUNC = {
    OpCodes.ADD: lambda (x, y): x + y,
    OpCodes.MULTI: lambda (x, y): x * y,
    OpCodes.TERM: lambda _: terminate()
}


def terminate():
    raise Terminate()


class Terminate(Exception):
    pass


@has_input
def part_one(input):
    program = map(int, input.split(','))
    pointer = 0

    program[1] = 12
    program[2] = 2

    while pointer < len(program)-4:
        try:
            op, p1, p2, r = program[pointer:pointer+4]
            program[r] = FUNC[OpCodes(op)](
                (program[p1], program[p2]))
            pointer += 4
        except Terminate:
            break

    print program


@has_input
def part_two(input):
    INITIAL = map(int, input.split(','))
    for noun in range(99):
        for verb in range(99):
            result = run_program(list(INITIAL), noun, verb)
            if result == REQUIRED:
                print 100 * noun + verb
                break


def run_program(program, noun, verb):
    program[1] = noun
    program[2] = verb

    pointer = 0

    while pointer < len(program)-4:
        try:
            op, p1, p2, r = program[pointer:pointer+4]
            program[r] = FUNC[OpCodes(op)]((program[p1], program[p2]))
            pointer += 4
        except Terminate:
            break

    return program[0]
