import functools
import re
from itertools import combinations
import collections


def part1(input_data):
    instructions = [(x[0], int(x[1:])) for x in input_data]
    facing = 1 + 0j
    position = 0 + 0j
    directions = {"E": 1 + 0j, "S": 0 - 1j, "W": -1 + 0j, "N": 0 + 1j}
    facings = {"L": 1j, "R": -1j}
    for instruction in instructions:
        symbol, units = instruction
        if symbol in facings:
            facing *= facings[symbol] ** (units // 90)
        else:
            if symbol in directions:
                direction = directions[symbol]
            else:
                direction = facing
            position += direction * units
    return int(abs(position.real) + abs(position.imag))


def part2(input_data):
    instructions = [(x[0], int(x[1:])) for x in input_data]
    waypoint = 10 + 1j
    position = 0 + 0j
    directions = {"E": 1 + 0j, "S": 0 - 1j, "W": -1 + 0j, "N": 0 + 1j}
    facings = {"L": 1j, "R": -1j}
    for instruction in instructions:
        symbol, units = instruction
        if symbol in directions:
            direction = directions[symbol]
            waypoint += direction * units
        elif symbol in facings:
            waypoint *= facings[symbol] ** (units // 90)
        else:
            position += waypoint * units
    return int(abs(position.real) + abs(position.imag))


if __name__ == "__main__":
    with open("input", "r") as input_file:
        input_data = list(map(lambda x: x.strip(), input_file.readlines()))
        print(part1(input_data))
        print(part2(input_data))
