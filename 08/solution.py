import functools
import re


def part1(input_data):
    bootcode = list(map(lambda x: x.split(" "), input_data))
    bootcode = list(map(lambda x: (x[0], int(x[1])), bootcode))
    cursor = 0
    accumulator = 0
    visited = set()

    while True:
        if cursor in visited:
            return accumulator
        visited.add(cursor)

        code = bootcode[cursor]
        if code[0] == "nop":
            cursor += 1
        elif code[0] == "acc":
            accumulator += code[1]
            cursor += 1
        elif code[0] == "jmp":
            cursor += code[1]


def part2(input_data):
    pass


if __name__ == "__main__":
    with open("input", "r") as input_file:
        input_data = list(map(lambda x: x.strip(), input_file.readlines()))
        print(part1(input_data))
        print(part2(input_data))
