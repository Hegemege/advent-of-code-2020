import functools
import re
from itertools import combinations


def part1(input_data):
    preamble_size = 25
    for i in range(preamble_size, len(input_data)):
        preamble = input_data[i - preamble_size : i]
        if not sum_in_preamble(preamble, input_data[i]):
            return input_data[i]


def part2(input_data):
    pass


def sum_in_preamble(preamble, item):
    return item in map(sum, combinations(set(preamble), 2))


if __name__ == "__main__":
    with open("input", "r") as input_file:
        input_data = list(map(lambda x: int(x.strip()), input_file.readlines()))
        print(part1(input_data))
        print(part2(input_data))
