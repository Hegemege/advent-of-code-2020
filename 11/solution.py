import functools
import re
from itertools import combinations


def part1(input_data):
    width = len(input_data[0])
    height = len(input_data)
    grid = [symbol for row in input_data for symbol in row]
    while True:
        new_grid = iterate_grid(grid, width, height, neighbour_generator, 4)
        if grid == new_grid:
            return len(list(filter(lambda x: x == "#", grid)))
        grid = new_grid


def part2(input_data):
    global neighbor_lookup
    neighbor_lookup = {}
    width = len(input_data[0])
    height = len(input_data)
    grid = [symbol for row in input_data for symbol in row]
    while True:
        new_grid = iterate_grid(grid, width, height, neighbour_generator_part2, 5)
        if grid == new_grid:
            return len(list(filter(lambda x: x == "#", grid)))
        grid = new_grid


def print_grid(grid, width, height):
    for j in range(height):
        row = ""
        for i in range(width):
            row += grid[j * width + i]
        print(row)
    print()


def iterate_grid(grid, width, height, neighbor_gen, limit):
    new_grid = grid[:]
    for i in range(len(grid)):
        if grid[i] == ".":
            continue

        occupied_neighbors = sum(
            [grid[neighbor] == "#" for neighbor in neighbor_gen(grid, i, width, height)]
        )
        if grid[i] == "L" and occupied_neighbors == 0:
            new_grid[i] = "#"
        elif grid[i] == "#" and occupied_neighbors >= limit:
            new_grid[i] = "L"

    return new_grid


def neighbour_generator(grid, index, width, height):
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


def neighbour_generator_part2(grid, index, width, height):
    global neighbor_lookup
    if index in neighbor_lookup:
        for neighbor in neighbor_lookup[index]:
            yield neighbor
        return

    neighbor_lookup[index] = []
    for neighbor_index in neighbour_generator(grid, index, width, height):
        # Convert the neighbor index to a direction
        # and step towards that direction until we reach a non-floor or the edge
        neighbor_x = neighbor_index % width
        neighbor_y = neighbor_index // width
        x = index % width
        y = index // width
        direction = (neighbor_x - x, neighbor_y - y)
        while True:
            x += direction[0]
            y += direction[1]
            if x < 0 or y < 0 or x > width - 1 or y > height - 1:
                break

            step_index = y * width + x
            if grid[step_index] != ".":
                neighbor_lookup[index].append(step_index)
                yield step_index
                break


if __name__ == "__main__":
    with open("input", "r") as input_file:
        input_data = list(map(lambda x: x.strip(), input_file.readlines()))
        print(part1(input_data))
        print(part2(input_data))
