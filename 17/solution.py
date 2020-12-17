import functools
import re
from itertools import combinations
import collections
import math


def part1(input_data):
    grid = {}
    for j in range(len(input_data)):
        for i in range(len(input_data[j])):
            if input_data[j][i] == "#":
                grid[(j, i, 0)] = 1

    for i in range(6):
        grid = iterate_grid(grid, neighbour_generator_part1)

    return sum(grid.values())


def part2(input_data):
    grid = {}
    for j in range(len(input_data)):
        for i in range(len(input_data[j])):
            if input_data[j][i] == "#":
                grid[(j, i, 0, 0)] = 1

    for i in range(6):
        grid = iterate_grid(grid, neighbour_generator_part2)

    return sum(grid.values())


def iterate_grid(grid, neighbour_generator):
    new_grid = dict(grid)
    boundary = set()
    for k, v in grid.items():
        # Check only existing neighbors in the first pass and accumulate the boundary set
        active_neighbors = sum(
            [
                grid[neighbor] if neighbor in grid else 0
                for neighbor in neighbour_generator(k, grid, boundary)
            ]
        )
        new_grid[k] = 0
        if v == 1:
            if active_neighbors == 2 or active_neighbors == 3:
                new_grid[k] = 1
        else:
            if active_neighbors == 3:
                new_grid[k] = 1

    for inactive_cell in boundary:
        active_neighbors = sum(
            [
                grid[neighbor] if neighbor in grid else 0
                for neighbor in neighbour_generator(inactive_cell, None, None)
            ]
        )
        if active_neighbors == 3:
            new_grid[inactive_cell] = 1

    return new_grid


def neighbour_generator_part1(cell, grid, boundary):
    for k in range(-1, 2):
        for j in range(-1, 2):
            for i in range(-1, 2):
                if i == j == k == 0:
                    continue
                neighbor = (cell[0] + i, cell[1] + j, cell[2] + k)
                if grid is not None and (neighbor not in grid or grid[neighbor] == 0):
                    boundary.add(neighbor)
                yield neighbor


def neighbour_generator_part2(cell, grid, boundary):
    for l in range(-1, 2):
        for k in range(-1, 2):
            for j in range(-1, 2):
                for i in range(-1, 2):
                    if i == j == k == l == 0:
                        continue
                    neighbor = (cell[0] + i, cell[1] + j, cell[2] + k, cell[3] + l)
                    if grid is not None and (
                        neighbor not in grid or grid[neighbor] == 0
                    ):
                        boundary.add(neighbor)
                    yield neighbor


if __name__ == "__main__":
    with open("input", "r") as input_file:
        input_data = list(map(lambda x: x.strip(), input_file.readlines()))
        print(part1(input_data))
        print(part2(input_data))
