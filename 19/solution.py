import functools
import re
from itertools import combinations
import collections
import math


def part1(input_data):
    rules, data = input_data
    data = data.split("\n")
    return sum(map(lambda x: matches_rule(x, rules), data))


def part2(input_data):
    pass


def matches_rule(entry, rules):
    # Depth first search through the tree, when reaching a leaf check if it matches
    # the current index
    # If not, go back up and check all other first-level children
    expression = f"^{subtree_as_regexp(0, rules)}$"
    matches = re.match(expression, entry) != None
    return matches


def subtree_as_regexp(key, rules):
    item = rules[key]
    if item["children"] is None:
        return item["raw"]

    children = "|".join(
        map(
            lambda y: "("
            + "".join(map(lambda x: subtree_as_regexp(int(x["key"]), rules), y))
            + ")",
            item["children"],
        )
    )
    return f"({children})"


def parse_input(input_data):
    rule_rows, data_rows = "\n".join(input_data).split("\n\n")
    rule_lookup = {
        int(x.split(": ")[0]): {"raw": x.split(": ")[1].replace('"', "")}
        for x in rule_rows.split("\n")
    }

    for k, v in rule_lookup.items():
        v["key"] = k
        if v["raw"] == "a" or v["raw"] == "b":
            v["children"] = None
            continue

        if "|" in v["raw"]:
            children = v["raw"].split(" | ")
            children = list(map(lambda x: x.split(" "), children))
        else:
            children = [v["raw"].split(" ")]

        v["children"] = []
        for item in children:
            v["children"].append([rule_lookup[int(x)] for x in item])

    return rule_lookup, data_rows


if __name__ == "__main__":
    with open("input", "r") as input_file:
        input_data = list(map(lambda x: x.strip(), input_file.readlines()))
        print(part1(parse_input(input_data)))
        print(part2(parse_input(input_data)))
