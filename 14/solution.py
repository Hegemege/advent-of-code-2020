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
    mask = "0" * 36
    memory = {}

    for command in input_data:
        if "mask" in command:
            mask = command.split(" = ")[1]
            continue
        address, value = command.split(" = ")
        address = int(address[4:-1])
        address = apply_mask_part2(address, mask)
        value = int(value)
        for fixed_address in resolve_floating_address(address):
            memory[fixed_address] = value

    return sum(memory.values())


def apply_mask_part2(value, mask):
    value_bits = list("{0:036b}".format(value))
    for i in range(36):
        if mask[i] != "0":
            value_bits[i] = mask[i]
    return "".join(value_bits)


def resolve_floating_address(address):
    if "X" not in address:
        yield int(address, 2)
        return

    yield from resolve_floating_address(address.replace("X", "0", 1))
    yield from resolve_floating_address(address.replace("X", "1", 1))


if __name__ == "__main__":
    with open("input", "r") as input_file:
        input_data = list(map(lambda x: x.strip(), input_file.readlines()))
        print(part1(input_data))
        print(part2(input_data))
