import functools
import re


def part1(input_data):
    rows = create_partition("F", "B", 0, 128)
    columns = create_partition("L", "R", 0, 8)

    return max(
        map(
            lambda line: get_seat_id(get_id(rows, line[:7]), get_id(columns, line[7:])),
            input_data,
        )
    )


def part2(input_data):
    pass


def get_id(partition, key):
    current = partition
    for symbol in key:
        current = current[symbol]
    return current["id"]


def get_seat_id(row_id, column_id):
    return row_id * 8 + column_id


def create_partition(low_symbol, high_symbol, low, high):
    partition = {}
    if high - low == 1:
        partition["id"] = low
    else:
        mid = low + ((high - low) >> 1)
        partition[low_symbol] = create_partition(low_symbol, high_symbol, low, mid)
        partition[high_symbol] = create_partition(low_symbol, high_symbol, mid, high)

    return partition


if __name__ == "__main__":
    with open("input", "r") as input_file:
        input_data = list(map(lambda x: x.strip(), input_file.readlines()))
        print(part1(input_data))
        print(part2(input_data))
