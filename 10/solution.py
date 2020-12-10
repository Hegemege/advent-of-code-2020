import functools
import re
from itertools import combinations


def part1(input_data):
    joltage_diff_counts = {}
    input_data = [0] + input_data + [max(input_data) + 3]
    input_data = sorted(input_data)
    for i in range(1, len(input_data)):
        diff = input_data[i] - input_data[i - 1]
        if diff not in joltage_diff_counts:
            joltage_diff_counts[diff] = 0
        joltage_diff_counts[diff] += 1
    return joltage_diff_counts[1] * joltage_diff_counts[3]


def part2(input_data):
    input_data = [0] + input_data + [max(input_data) + 3]
    input_data = sorted(input_data)

    # Build a directed graph and aggregate parent sums
    nodes = {}
    for adapter in input_data:
        nodes[adapter] = {"key": adapter, "sum": 0, "parents": []}

    # Only at most 4 consecutive items in the list can be linked
    for i in range(0, len(input_data)):
        potential_children = input_data[i + 1 : i + 4]
        for child in potential_children:
            if child - input_data[i] > 3:
                continue

            nodes[child]["parents"].append(nodes[input_data[i]])

    nodes[0]["sum"] = 1
    for adapter in input_data:
        for parent in nodes[adapter]["parents"]:
            nodes[adapter]["sum"] += nodes[parent["key"]]["sum"]

    return nodes[input_data[-1]]["sum"]


if __name__ == "__main__":
    with open("input", "r") as input_file:
        input_data = list(map(lambda x: int(x.strip()), input_file.readlines()))
        print(part1(input_data))
        print(part2(input_data))
