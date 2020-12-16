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
            if not validate_value(value, rules):
                invalid_sum += value
    return invalid_sum


def part2(input_data):
    rules, your_ticket, tickets = parse_input(input_data)
    rule_index = {x: [] for x in rules.keys()}
    field_count = len(your_ticket)
    tickets = list(filter(lambda x: validate_ticket(x, rules), tickets))
    # For each rule, go through all tickets index-by-index
    # and find an index that fits the rule for all tickets
    for rule_class, rule_ranges in rules.items():
        for field in range(field_count):
            valid_index = True
            for ticket in tickets:
                if not (
                    (
                        ticket[field] >= rule_ranges[0][0]
                        and ticket[field] <= rule_ranges[0][1]
                    )
                    or (
                        ticket[field] >= rule_ranges[1][0]
                        and ticket[field] <= rule_ranges[1][1]
                    )
                ):
                    valid_index = False
                    break

            rule_index[rule_class].append(valid_index)

    # Reduce the validity of all rules such that only one index is True
    items = sorted(list(rule_index.items()), key=lambda x: sum(x[1]))
    for item in items:
        index = item[1].index(True)
        # Remove it from all items
        for other_item in items:
            other_item[1][index] = False
        item[1][index] = True

    ticket_value = 1
    for rule_class, rule_indices in rule_index.items():
        for rule_index in range(len(rule_indices)):
            valid = rule_indices[rule_index]
            if "departure" in rule_class and valid:
                ticket_value *= your_ticket[rule_index]

    return ticket_value


def validate_value(value, rules):
    for _, v in rules.items():
        if (value >= v[0][0] and value <= v[0][1]) or (
            value >= v[1][0] and value <= v[1][1]
        ):
            return True
    return False


def validate_ticket(ticket, rules):
    for value in ticket:
        if not validate_value(value, rules):
            return False
    return True


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
