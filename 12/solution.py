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
    pass


if __name__ == "__main__":
    with open("input", "r") as input_file:
        input_data = list(map(lambda x: x.strip(), input_file.readlines()))
        print(part1(input_data))
        print(part2(input_data))
