import functools
import re
from itertools import combinations


def part1(input_data):
    width = len(input_data[0])
    height = len(input_data)
    grid = [symbol for row in input_data for symbol in row]
    while True:
        new_grid = iterate_part1(grid, width, height)
        if grid == new_grid:
            return len(list(filter(lambda x: x == "#", grid)))
        grid = new_grid


def part2(input_data):
    pass


def print_grid(grid, width, height):
    for j in range(height):
        row = ""
        for i in range(width):
            row += grid[j * width + i]
        print(row)
    print()


def iterate_part1(grid, width, height):
    new_grid = grid[:]
    for i in range(len(grid)):
        if grid[i] == ".":
            continue

        occupied_neighbors = sum(
            [
                grid[neighbor] == "#"
                for neighbor in neighbour_generator(i, width, height)
            ]
        )
        if grid[i] == "L" and occupied_neighbors == 0:
            new_grid[i] = "#"
        elif grid[i] == "#" and occupied_neighbors >= 4:
            new_grid[i] = "L"

    return new_grid


def neighbour_generator(index, width, height):
    x = index % width
    y = index // width
    if y > 0:
        if x > 0:
            yield (y - 1) * width + x - 1
        yield (y - 1) * width + x
        if x < width - 1:
            yield (y - 1) * width + x + 1

    if x > 0:
        yield y * width + x - 1
    if x < width - 1:
        yield y * width + x + 1
    if y < height - 1:
        if x > 0:
            yield (y + 1) * width + x - 1
        yield (y + 1) * width + x
        if x < width - 1:
            yield (y + 1) * width + x + 1


if __name__ == "__main__":
    with open("input", "r") as input_file:
        input_data = list(map(lambda x: x.strip(), input_file.readlines()))
        print(part1(input_data))
        print(part2(input_data))
