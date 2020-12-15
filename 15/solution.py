import functools
import re
from itertools import combinations
import collections
import math


def part1(input_data):
    starting_numbers = list(map(int, input_data[0].split(",")))
    numbers = {starting_numbers[x]: x + 1 for x in range(len(starting_numbers) - 1)}
    t = len(starting_numbers)
    previous = starting_numbers[-1]
    while t < 2020:
        if previous not in numbers:
            numbers[previous] = t
            previous = 0
        else:
            previous_time = numbers[previous]
            numbers[previous] = t
            diff = t - previous_time
            previous = diff
        t += 1
    return previous


def part2(input_data):
    pass


if __name__ == "__main__":
    with open("input", "r") as input_file:
        input_data = list(map(lambda x: x.strip(), input_file.readlines()))
        print(part1(input_data))
        print(part2(input_data))
