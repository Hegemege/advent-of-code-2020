import functools
import re
from itertools import combinations
import collections
import math


def part1(input_data):
    mask = "X" * 36
    memory = {}

    for command in input_data:
        if "mask" in command:
            mask = command.split(" = ")[1]
            continue
        address, value = command.split(" = ")
        address = int(address[4:-1])
        value = int(value)
        memory[address] = apply_mask(value, mask)

    return sum(memory.values())


def apply_mask(value, mask):
    value_bits = list("{0:036b}".format(value))
    for i in range(36):
        if mask[i] != "X":
            value_bits[i] = mask[i]
    return int("".join(value_bits), 2)


def part2(input_data):
    pass


if __name__ == "__main__":
    with open("input", "r") as input_file:
        input_data = list(map(lambda x: x.strip(), input_file.readlines()))
        print(part1(input_data))
        print(part2(input_data))
