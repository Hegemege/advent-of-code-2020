import functools
import re
from itertools import combinations
import collections


def part1(input_data):
    instructions = [(x[0], int(x[1:])) for x in input_data]
    facing = 0
    position = (0, 0)
    directions = collections.OrderedDict(
        [("E", (1, 0)), ("S", (0, -1)), ("W", (-1, 0)), ("N", (0, 1))]
    )
    facings = {"L": -1, "R": 1}
    for instruction in instructions:
        symbol, units = instruction
        if symbol in directions:
            direction = directions[symbol]
            position = move(position, direction, units)
        elif symbol in facings:
            facing = (facing + facings[symbol] * (units // 90)) % 4
        else:
            direction = directions[list(directions)[facing]]
            position = move(position, direction, units)
    return abs(position[0]) + abs(position[1])


def move(position, direction, units):
    return (
        position[0] + direction[0] * units,
        position[1] + direction[1] * units,
    )


def part2(input_data):
    instructions = [(x[0], int(x[1:])) for x in input_data]
    waypoint = 10 + 1j
    position = 0 + 0j
    directions = collections.OrderedDict(
        [("E", 1 + 0j), ("S", 0 - 1j), ("W", -1 + 0j), ("N", 0 + 1j)]
    )
    facings = {"L": 1j, "R": -1j}
    for instruction in instructions:
        symbol, units = instruction
        if symbol in directions:
            direction = directions[symbol]
            waypoint += direction * units
        elif symbol in facings:
            for i in range((units // 90)):
                waypoint *= facings[symbol]
        else:
            position += waypoint * units
    return int(abs(position.real) + abs(position.imag))


if __name__ == "__main__":
    with open("input", "r") as input_file:
        input_data = list(map(lambda x: x.strip(), input_file.readlines()))
        print(part1(input_data))
        print(part2(input_data))
