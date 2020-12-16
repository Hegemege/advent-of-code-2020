import functools
import re
from itertools import combinations
import collections
import math


def part1(input_data):
    rules, your_ticket, tickets = parse_input(input_data)
    invalid_sum = 0
    for ticket in tickets:
        for value in ticket:
            valid = False
            for _, v in rules.items():
                if (value >= v[0][0] and value <= v[0][1]) or (
                    value >= v[1][0] and value <= v[1][1]
                ):
                    valid = True
                    break
            if not valid:
                invalid_sum += value
    return invalid_sum


def part2(input_data):
    pass


def parse_input(input_data):
    rules = {}
    your_ticket = []
    tickets = []

    data = list(map(lambda x: x.split("\n"), "\n".join(input_data).split("\n\n")))
    for rule in data[0]:
        rule_class, rule_ranges = rule.split(": ")
        rule_ranges = rule_ranges.split(" or ")
        rule_ranges = list(map(lambda x: list(map(int, x.split("-"))), rule_ranges))
        rules[rule_class] = rule_ranges

    your_ticket = list(map(int, data[1][1].split(",")))

    for ticket in data[2][1:]:
        tickets.append(list(map(int, ticket.split(","))))

    return rules, your_ticket, tickets


if __name__ == "__main__":
    with open("input", "r") as input_file:
        input_data = list(map(lambda x: x.strip(), input_file.readlines()))
        print(part1(input_data))
        print(part2(input_data))
