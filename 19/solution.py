import functools
import re
from itertools import combinations
import collections
import math


def part1(input_data):
    rules, data = parse_input(input_data)
    data = data.split("\n")
    return sum(map(lambda x: matches_rule(x, rules), data))


def part2(input_data):
    # Replace the rules 8 and 11
    # for i in range(len(input_data)):
    #    if input_data[i].startswith("8:"):
    #        input_data[i] = "8: 42 | 42 8"
    #    if input_data[i].startswith("11:"):
    #        input_data[i] = "11: 42 31 | 42 11 31"
    # The rules essentially turn into (42 = A, 31 = B):
    # A AB
    # AA AABB
    # AAA AAABBB
    # AAAA AAAABBBB etc.
    # We could use a reasonable expectation to go through 10*10 combinations
    # because the input size per line is rather small
    rules, data = parse_input(input_data)
    data = data.split("\n")

    # print(subtree_as_regexp(42, rules))
    # print(subtree_as_regexp(31, rules))

    return sum(map(lambda x: matches_rule_part2(x, rules), data))


def matches_rule_part2(entry, rules):
    A = subtree_as_regexp(42, rules)
    B = subtree_as_regexp(31, rules)

    N = 10
    # This could be deduced by figuring out the minimum pattern
    # match length of A and B

    for j in range(1, N):
        for i in range(1, N):
            pattern = f"^{A*i}{A*j}{B*j}$"
            if re.match(pattern, entry) != None:
                return True

    return False


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
            lambda y: "".join(
                map(lambda x: subtree_as_regexp(int(x["key"]), rules), y)
            ),
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
        print(part1(input_data))
        print(part2(input_data))
