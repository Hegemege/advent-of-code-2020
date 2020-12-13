import functools
import re
from itertools import combinations
import collections
import math


def part1(input_data):
    arrival = int(input_data[0])
    bus_ids = [int(x) for x in input_data[1].split(",") if x != "x"]
    first_bus_id = max(bus_ids, key=lambda x: arrival / x - arrival // x)
    wait = math.ceil(arrival / first_bus_id) * first_bus_id - arrival
    return wait * first_bus_id


def part2(input_data):
    pass


if __name__ == "__main__":
    with open("input", "r") as input_file:
        input_data = list(map(lambda x: x.strip(), input_file.readlines()))
        print(part1(input_data))
        print(part2(input_data))
