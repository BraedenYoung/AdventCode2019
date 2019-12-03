from input_decorator import has_input


SAMPLE = '''
1969
'''


@has_input
def part_one(input):
    fuel = []
    for mass in input.strip().splitlines():
        fuel.append((int(mass)/3)-2)
    print sum(fuel)


@has_input
def part_two(input):
    fuel = []
    for mass in input.strip().splitlines():
        fuel.append(calc_fuel(mass))
    print sum(fuel)


def calc_fuel(mass):
    fuel = (int(mass)/3)-2
    return fuel + calc_fuel(fuel) if fuel > 0 else 0
