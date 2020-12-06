import functools
import re


def part1(input_data):
    data = functools.reduce(aggregate_group, input_data, [set()])
    return sum(map(len, data))


def part2(input_data):
    data = functools.reduce(aggregate_group_part2, input_data, [{"size": 0}])
    return sum(
        map(
            lambda x: sum(
                [1 if v == x["size"] and k != "size" else 0 for k, v in x.items()]
            ),
            data,
        )
    )


def aggregate_group(a, b):
    if len(b) == 0:
        a.append(set())
    else:
        a[-1].update(b)
    return a


def aggregate_group_part2(a, b):
    if len(b) == 0:
        a.append({"size": 0})
    else:
        for symbol in b:
            if symbol not in a[-1]:
                a[-1][symbol] = 0
            a[-1][symbol] += 1
        a[-1]["size"] += 1
    return a


if __name__ == "__main__":
    with open("input", "r") as input_file:
        input_data = list(map(lambda x: x.strip(), input_file.readlines()))
        print(part1(input_data))
        print(part2(input_data))
