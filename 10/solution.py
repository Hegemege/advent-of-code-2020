import functools
import re
from itertools import combinations


def part1(input_data):
    joltage_diff_counts = {}
    input_data = [0] + input_data + [max(input_data) + 3]
    input_data = sorted(list(input_data))
    for i in range(1, len(input_data)):
        diff = input_data[i] - input_data[i - 1]
        if diff not in joltage_diff_counts:
            joltage_diff_counts[diff] = 0
        joltage_diff_counts[diff] += 1
    return joltage_diff_counts[1] * joltage_diff_counts[3]


def part2(input_data):
    pass


if __name__ == "__main__":
    with open("input", "r") as input_file:
        input_data = list(map(lambda x: int(x.strip()), input_file.readlines()))
        print(part1(input_data))
        print(part2(input_data))
