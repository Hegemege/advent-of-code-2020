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
    # The bus intervals are pairwise coprime, use chinese remainder theorem
    input_data = input_data[1].split(",")
    bus_ids = [int(x) for x in input_data if x != "x"]
    bus_arrival_offsets = {bus_id: input_data.index(str(bus_id)) for bus_id in bus_ids}
    a = list(map(lambda x: x - bus_arrival_offsets[x] % x, bus_ids))
    return int(chinese_remainder(bus_ids, a))


# From https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
def chinese_remainder(n, a):
    sum = 0
    prod = functools.reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


if __name__ == "__main__":
    with open("input", "r") as input_file:
        input_data = list(map(lambda x: x.strip(), input_file.readlines()))
        print(part1(input_data))
        print(part2(input_data))
