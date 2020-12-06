import functools
import re


def part1(input_data):
    data = functools.reduce(aggregate_group, input_data, [set()])
    return sum(map(len, data))


def part2(input_data):
    pass


def aggregate_group(a, b):
    if len(b) == 0:
        a.append(set())
    else:
        a[-1].update(b)
    return a


if __name__ == "__main__":
    with open("input", "r") as input_file:
        input_data = list(map(lambda x: x.strip(), input_file.readlines()))
        print(part1(input_data))
        print(part2(input_data))
